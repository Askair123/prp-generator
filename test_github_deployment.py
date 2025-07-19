#!/usr/bin/env python3
"""
GitHub部署测试脚本

测试从你的GitHub仓库部署Initial.md到PRP生成系统的完整流程。

使用方法:
    python test_github_deployment.py [GitHub用户名] [仓库名]
"""

import os
import sys
import subprocess
import tempfile
import shutil
import argparse
from pathlib import Path


class Colors:
    """终端颜色定义"""
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    NC = '\033[0m'


def print_info(message: str):
    print(f"{Colors.BLUE}ℹ️  {message}{Colors.NC}")


def print_success(message: str):
    print(f"{Colors.GREEN}✅ {message}{Colors.NC}")


def print_warning(message: str):
    print(f"{Colors.YELLOW}⚠️  {message}{Colors.NC}")


def print_error(message: str):
    print(f"{Colors.RED}❌ {message}{Colors.NC}")


def print_header():
    print(f"{Colors.BLUE}")
    print("🧪 GitHub部署测试")
    print("=" * 50)
    print(f"{Colors.NC}")


class GitHubDeploymentTester:
    """GitHub部署测试类"""
    
    def __init__(self, github_username: str, repo_name: str):
        self.github_username = github_username
        self.repo_name = repo_name
        self.repo_url = f"https://github.com/{github_username}/{repo_name}.git"
        self.raw_base_url = f"https://raw.githubusercontent.com/{github_username}/{repo_name}/main"
        self.test_dir = None
        self.errors = []
        
    def test_repo_accessibility(self) -> bool:
        """测试仓库是否可访问"""
        print_info("测试GitHub仓库可访问性...")
        
        try:
            # 测试仓库URL
            result = subprocess.run(
                ["git", "ls-remote", self.repo_url],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                print_success("GitHub仓库可访问")
                return True
            else:
                print_error(f"无法访问GitHub仓库: {self.repo_url}")
                print_error(f"错误信息: {result.stderr.strip()}")
                self.errors.append("仓库不可访问")
                return False
                
        except subprocess.TimeoutExpired:
            print_error("仓库访问超时")
            self.errors.append("仓库访问超时")
            return False
        except Exception as e:
            print_error(f"仓库访问测试失败: {e}")
            self.errors.append("仓库访问异常")
            return False
    
    def test_raw_files_accessibility(self) -> bool:
        """测试原始文件是否可访问"""
        print_info("测试原始文件可访问性...")
        
        test_files = [
            "quick_setup.sh",
            "setup_from_github.py",
            "README.md",
            "coordinator/__init__.py"
        ]
        
        success = True
        for file_path in test_files:
            try:
                url = f"{self.raw_base_url}/{file_path}"
                result = subprocess.run(
                    ["curl", "-I", "-s", url],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                if "200 OK" in result.stdout:
                    print_success(f"文件可访问: {file_path}")
                else:
                    print_error(f"文件不可访问: {file_path}")
                    success = False
                    
            except Exception as e:
                print_error(f"文件访问测试失败: {file_path} - {e}")
                success = False
        
        if not success:
            self.errors.append("部分原始文件不可访问")
        
        return success
    
    def test_one_click_setup(self) -> bool:
        """测试一键设置脚本"""
        print_info("测试一键设置脚本...")
        
        try:
            # 创建临时测试目录
            self.test_dir = Path(tempfile.mkdtemp(prefix="github_deploy_test_"))
            print_info(f"测试目录: {self.test_dir}")
            
            # 下载并运行一键设置脚本
            setup_url = f"{self.raw_base_url}/quick_setup.sh"
            
            result = subprocess.run(
                ["curl", "-sSL", setup_url],
                cwd=self.test_dir,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0:
                # 保存脚本并执行
                script_path = self.test_dir / "quick_setup.sh"
                script_path.write_text(result.stdout)
                script_path.chmod(0o755)
                
                # 执行设置脚本
                exec_result = subprocess.run(
                    ["bash", str(script_path)],
                    cwd=self.test_dir,
                    capture_output=True,
                    text=True,
                    timeout=120
                )
                
                if exec_result.returncode == 0:
                    print_success("一键设置脚本执行成功")
                    return True
                else:
                    print_error("一键设置脚本执行失败")
                    print_error(f"错误信息: {exec_result.stderr.strip()}")
                    self.errors.append("一键设置脚本执行失败")
                    return False
            else:
                print_error("无法下载一键设置脚本")
                self.errors.append("一键设置脚本下载失败")
                return False
                
        except Exception as e:
            print_error(f"一键设置测试失败: {e}")
            self.errors.append("一键设置测试异常")
            return False
    
    def test_submodule_setup(self) -> bool:
        """测试Git子模块设置"""
        print_info("测试Git子模块设置...")
        
        try:
            # 创建新的测试目录
            submodule_test_dir = Path(tempfile.mkdtemp(prefix="submodule_test_"))
            print_info(f"子模块测试目录: {submodule_test_dir}")
            
            # 初始化Git仓库
            subprocess.run(["git", "init"], cwd=submodule_test_dir, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=submodule_test_dir, check=True)
            subprocess.run(["git", "config", "user.name", "Test User"], cwd=submodule_test_dir, check=True)
            
            # 添加子模块
            subprocess.run([
                "git", "submodule", "add", self.repo_url, "context-engineering"
            ], cwd=submodule_test_dir, check=True, timeout=60)
            
            # 初始化子模块
            subprocess.run([
                "git", "submodule", "update", "--init", "--recursive"
            ], cwd=submodule_test_dir, check=True, timeout=60)
            
            # 检查子模块内容
            context_dir = submodule_test_dir / "context-engineering"
            if (context_dir / "coordinator").exists() and (context_dir / "PRPs").exists():
                print_success("Git子模块设置成功")
                
                # 清理
                shutil.rmtree(submodule_test_dir)
                return True
            else:
                print_error("子模块内容不完整")
                self.errors.append("子模块内容不完整")
                shutil.rmtree(submodule_test_dir)
                return False
                
        except subprocess.CalledProcessError as e:
            print_error(f"Git子模块设置失败: {e}")
            self.errors.append("Git子模块设置失败")
            return False
        except Exception as e:
            print_error(f"子模块测试异常: {e}")
            self.errors.append("子模块测试异常")
            return False
    
    def test_setup_script(self) -> bool:
        """测试设置脚本"""
        print_info("测试专用设置脚本...")
        
        try:
            # 创建测试目录
            script_test_dir = Path(tempfile.mkdtemp(prefix="script_test_"))
            print_info(f"脚本测试目录: {script_test_dir}")
            
            # 下载设置脚本
            script_url = f"{self.raw_base_url}/setup_from_github.py"
            result = subprocess.run(
                ["curl", "-O", script_url],
                cwd=script_test_dir,
                check=True,
                timeout=30
            )
            
            # 运行设置脚本
            result = subprocess.run(
                [sys.executable, "setup_from_github.py", "clone", "."],
                cwd=script_test_dir,
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode == 0:
                # 检查设置结果
                if (script_test_dir / "coordinator").exists() and (script_test_dir / "PRPs").exists():
                    print_success("专用设置脚本执行成功")
                    shutil.rmtree(script_test_dir)
                    return True
                else:
                    print_error("设置脚本执行后文件不完整")
                    self.errors.append("设置脚本文件不完整")
                    shutil.rmtree(script_test_dir)
                    return False
            else:
                print_error("专用设置脚本执行失败")
                print_error(f"错误信息: {result.stderr.strip()}")
                self.errors.append("专用设置脚本执行失败")
                shutil.rmtree(script_test_dir)
                return False
                
        except Exception as e:
            print_error(f"设置脚本测试失败: {e}")
            self.errors.append("设置脚本测试异常")
            return False
    
    def test_functionality(self) -> bool:
        """测试系统功能"""
        print_info("测试系统功能...")
        
        if not self.test_dir or not self.test_dir.exists():
            print_error("没有可用的测试目录")
            return False
        
        try:
            # 设置Python路径
            env = os.environ.copy()
            env['PYTHONPATH'] = str(self.test_dir)
            
            # 测试CLI帮助
            result = subprocess.run(
                [sys.executable, "-m", "coordinator.initial_to_prp_cli", "--help"],
                cwd=self.test_dir,
                capture_output=True,
                text=True,
                env=env,
                timeout=30
            )
            
            if result.returncode == 0:
                print_success("CLI工具功能正常")
                
                # 测试INITIAL.md验证
                if (self.test_dir / "INITIAL.md").exists():
                    result = subprocess.run(
                        [sys.executable, "-m", "coordinator.initial_to_prp_cli", "validate", "INITIAL.md"],
                        cwd=self.test_dir,
                        capture_output=True,
                        text=True,
                        env=env,
                        timeout=30
                    )
                    
                    if result.returncode == 0:
                        print_success("INITIAL.md验证功能正常")
                        return True
                    else:
                        print_warning("INITIAL.md验证失败，但CLI基本功能正常")
                        return True
                else:
                    print_warning("INITIAL.md文件不存在，跳过验证测试")
                    return True
            else:
                print_error("CLI工具功能异常")
                print_error(f"错误信息: {result.stderr.strip()}")
                self.errors.append("CLI工具功能异常")
                return False
                
        except Exception as e:
            print_error(f"功能测试失败: {e}")
            self.errors.append("功能测试异常")
            return False
    
    def cleanup(self):
        """清理测试目录"""
        if self.test_dir and self.test_dir.exists():
            try:
                shutil.rmtree(self.test_dir)
                print_info("测试目录清理完成")
            except Exception as e:
                print_warning(f"测试目录清理失败: {e}")
    
    def run_tests(self) -> bool:
        """运行所有测试"""
        print_header()
        print_info(f"测试GitHub仓库: {self.repo_url}")
        print()
        
        tests = [
            ("仓库可访问性", self.test_repo_accessibility),
            ("原始文件可访问性", self.test_raw_files_accessibility),
            ("一键设置脚本", self.test_one_click_setup),
            ("Git子模块设置", self.test_submodule_setup),
            ("专用设置脚本", self.test_setup_script),
            ("系统功能", self.test_functionality),
        ]
        
        results = {}
        for test_name, test_func in tests:
            print_info(f"运行测试: {test_name}")
            try:
                results[test_name] = test_func()
            except Exception as e:
                print_error(f"测试异常: {test_name} - {e}")
                results[test_name] = False
                self.errors.append(f"{test_name}测试异常")
            print()
        
        # 清理
        self.cleanup()
        
        # 总结结果
        print_info("测试结果总结:")
        all_passed = True
        for test_name, passed in results.items():
            status = "✅ 通过" if passed else "❌ 失败"
            print(f"  {test_name}: {status}")
            if not passed:
                all_passed = False
        
        print()
        if all_passed:
            print_success("🎉 所有测试通过！GitHub部署成功！")
            print()
            print_info("你现在可以在新项目中使用:")
            print(f"curl -sSL {self.raw_base_url}/quick_setup.sh | bash")
        else:
            print_error("❌ 部分测试失败。请检查以下问题:")
            for error in self.errors:
                print_error(f"  - {error}")
        
        return all_passed


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="GitHub部署测试脚本",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'github_username',
        nargs='?',
        default='Askair123',
        help='GitHub用户名 (默认: Askair123)'
    )
    
    parser.add_argument(
        'repo_name',
        nargs='?',
        default='Context-Engineering-Intro',
        help='仓库名称 (默认: Context-Engineering-Intro)'
    )
    
    args = parser.parse_args()
    
    # 创建测试实例并运行
    tester = GitHubDeploymentTester(args.github_username, args.repo_name)
    success = tester.run_tests()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
