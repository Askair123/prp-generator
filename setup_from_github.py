#!/usr/bin/env python3
"""
Initial.md到PRP生成系统 - GitHub设置脚本

从GitHub仓库设置Initial.md到PRP生成系统到新项目中。

使用方法:
    python setup_from_github.py [设置方式] [项目路径]
    
设置方式:
    submodule  - Git子模块方式（推荐，保持同步）
    clone      - 克隆后复制（独立副本）
    sparse     - 稀疏检出（只下载需要的文件）
    
示例:
    python setup_from_github.py submodule        # 在当前目录使用子模块
    python setup_from_github.py clone .          # 在当前目录克隆复制
    python setup_from_github.py sparse /path/to/project  # 在指定目录稀疏检出
"""

import os
import sys
import subprocess
import shutil
import argparse
from pathlib import Path
from typing import Optional


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
    print("🚀 Initial.md到PRP生成系统 - GitHub设置")
    print("=" * 50)
    print(f"{Colors.NC}")


class GitHubSetup:
    """GitHub设置类"""

    REPO_URL = "https://github.com/Askair123/prp-generator.git"
    
    def __init__(self, setup_method: str, project_path: str):
        self.setup_method = setup_method
        self.project_path = Path(project_path).resolve()
        
    def check_git_available(self) -> bool:
        """检查Git是否可用"""
        try:
            subprocess.run(["git", "--version"], capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print_error("Git未安装或不可用。请先安装Git。")
            return False
    
    def check_project_is_git_repo(self) -> bool:
        """检查项目是否是Git仓库"""
        git_dir = self.project_path / ".git"
        return git_dir.exists()
    
    def init_git_repo_if_needed(self):
        """如果需要，初始化Git仓库"""
        if not self.check_project_is_git_repo():
            print_info("项目不是Git仓库，正在初始化...")
            try:
                subprocess.run(
                    ["git", "init"],
                    cwd=self.project_path,
                    check=True,
                    capture_output=True
                )
                print_success("Git仓库初始化完成")
            except subprocess.CalledProcessError as e:
                print_error(f"Git仓库初始化失败: {e}")
                raise
    
    def setup_submodule(self):
        """使用Git子模块设置"""
        print_info("使用Git子模块方式设置...")
        
        # 确保是Git仓库
        self.init_git_repo_if_needed()
        
        try:
            # 检查子模块是否已存在
            submodule_path = self.project_path / "context-engineering"
            if submodule_path.exists():
                print_warning("子模块已存在，正在更新...")
                subprocess.run(
                    ["git", "submodule", "update", "--remote"],
                    cwd=self.project_path,
                    check=True
                )
            else:
                # 添加子模块
                subprocess.run(
                    ["git", "submodule", "add", self.REPO_URL, "context-engineering"],
                    cwd=self.project_path,
                    check=True
                )
            
            # 初始化和更新子模块
            subprocess.run(
                ["git", "submodule", "update", "--init", "--recursive"],
                cwd=self.project_path,
                check=True
            )
            
            # 创建符号链接
            self.create_symlinks()
            
            # 复制可编辑文件
            self.copy_editable_files("context-engineering")
            
            print_success("Git子模块设置完成")
            
        except subprocess.CalledProcessError as e:
            print_error(f"Git子模块设置失败: {e}")
            raise
    
    def setup_clone(self):
        """使用克隆方式设置"""
        print_info("使用克隆复制方式设置...")
        
        temp_dir = self.project_path / "temp_context_engineering"
        
        try:
            # 克隆到临时目录
            if temp_dir.exists():
                shutil.rmtree(temp_dir)
            
            subprocess.run(
                ["git", "clone", self.REPO_URL, str(temp_dir)],
                check=True
            )
            
            # 复制需要的文件
            self.copy_files_from_temp(temp_dir)
            
            # 清理临时目录
            shutil.rmtree(temp_dir)
            
            print_success("克隆复制设置完成")
            
        except subprocess.CalledProcessError as e:
            print_error(f"克隆设置失败: {e}")
            if temp_dir.exists():
                shutil.rmtree(temp_dir)
            raise
    
    def setup_sparse(self):
        """使用稀疏检出设置"""
        print_info("使用稀疏检出方式设置...")
        
        context_dir = self.project_path / "context-engineering"
        
        try:
            # 稀疏克隆
            if context_dir.exists():
                shutil.rmtree(context_dir)
            
            subprocess.run([
                "git", "clone", "--filter=blob:none", "--sparse", 
                self.REPO_URL, str(context_dir)
            ], check=True)
            
            # 设置稀疏检出
            subprocess.run([
                "git", "sparse-checkout", "set", 
                "coordinator", "PRPs", "INITIAL_EXAMPLE.md", "QUICK_REFERENCE.md"
            ], cwd=context_dir, check=True)
            
            # 创建符号链接
            self.create_symlinks()
            
            # 复制可编辑文件
            self.copy_editable_files("context-engineering")
            
            print_success("稀疏检出设置完成")
            
        except subprocess.CalledProcessError as e:
            print_error(f"稀疏检出设置失败: {e}")
            if context_dir.exists():
                shutil.rmtree(context_dir)
            raise
    
    def create_symlinks(self):
        """创建符号链接"""
        print_info("创建符号链接...")
        
        links = [
            ("context-engineering/coordinator", "coordinator"),
            ("context-engineering/PRPs", "PRPs")
        ]
        
        for source, target in links:
            source_path = self.project_path / source
            target_path = self.project_path / target
            
            if target_path.exists():
                if target_path.is_symlink():
                    target_path.unlink()
                else:
                    print_warning(f"目标已存在，跳过: {target}")
                    continue
            
            try:
                # 在Windows上可能需要管理员权限
                target_path.symlink_to(source_path)
                print_success(f"创建符号链接: {target} -> {source}")
            except OSError as e:
                print_warning(f"符号链接创建失败，使用复制: {e}")
                if source_path.is_dir():
                    shutil.copytree(source_path, target_path)
                else:
                    shutil.copy2(source_path, target_path)
    
    def copy_editable_files(self, source_dir: str):
        """复制可编辑的文件"""
        print_info("复制可编辑文件...")
        
        files_to_copy = [
            ("INITIAL_EXAMPLE.md", "INITIAL.md"),
            ("QUICK_REFERENCE.md", "QUICK_REFERENCE.md")
        ]
        
        source_base = self.project_path / source_dir
        
        for source_file, target_file in files_to_copy:
            source_path = source_base / source_file
            target_path = self.project_path / target_file
            
            if source_path.exists() and not target_path.exists():
                shutil.copy2(source_path, target_path)
                print_success(f"复制文件: {target_file}")
    
    def copy_files_from_temp(self, temp_dir: Path):
        """从临时目录复制文件"""
        print_info("复制核心文件...")
        
        # 复制目录
        dirs_to_copy = ["coordinator", "PRPs"]
        for dir_name in dirs_to_copy:
            source_dir = temp_dir / dir_name
            target_dir = self.project_path / dir_name
            
            if source_dir.exists():
                if target_dir.exists():
                    shutil.rmtree(target_dir)
                shutil.copytree(source_dir, target_dir)
                print_success(f"复制目录: {dir_name}")
        
        # 复制文件
        files_to_copy = [
            ("INITIAL_EXAMPLE.md", "INITIAL.md"),
            ("QUICK_REFERENCE.md", "QUICK_REFERENCE.md")
        ]
        
        for source_file, target_file in files_to_copy:
            source_path = temp_dir / source_file
            target_path = self.project_path / target_file
            
            if source_path.exists() and not target_path.exists():
                shutil.copy2(source_path, target_path)
                print_success(f"复制文件: {target_file}")
    
    def create_usage_guide(self):
        """创建使用指南"""
        print_info("创建使用指南...")
        
        usage_content = f"""# 🚀 项目中的Initial.md到PRP生成系统使用指南

## 设置方式
本项目使用 **{self.setup_method}** 方式设置了Initial.md到PRP生成系统。

## 快速开始

### 1. 编辑INITIAL.md文件
```markdown
## FEATURE:
Build a REST API using FastAPI...

## EXAMPLES:
- `examples/api.py` - API structure example

## DOCUMENTATION:
- FastAPI: https://fastapi.tiangolo.com/

## OTHER CONSIDERATIONS:
- Use proper error handling
- Add input validation
```

### 2. 生成PRP文档
```bash
# 基本生成
python -m coordinator.initial_to_prp_cli generate INITIAL.md

# 验证INITIAL.md质量
python -m coordinator.initial_to_prp_cli validate INITIAL.md

# 列出生成的PRP文件
python -m coordinator.initial_to_prp_cli list
```

### 3. 使用生成的PRP
1. 查看生成的PRP文件（在PRPs/目录下）
2. 将PRP内容提供给AI编程助手
3. AI会根据PRP实现你的功能

## 更新系统

### Git子模块方式
```bash
git submodule update --remote context-engineering
```

### 克隆方式
```bash
# 重新运行设置脚本
python setup_from_github.py clone
```

### 稀疏检出方式
```bash
cd context-engineering
git pull origin main
```

## 故障排除

### 设置Python路径
```bash
export PYTHONPATH="${{PYTHONPATH}}:$(pwd)"
```

### 验证系统功能
```bash
python -m coordinator.initial_to_prp_cli validate INITIAL.md
```

查看 QUICK_REFERENCE.md 获取更多详细信息。
"""
        
        usage_guide = self.project_path / "USAGE_GUIDE.md"
        usage_guide.write_text(usage_content, encoding='utf-8')
        print_success("使用指南创建完成")
    
    def verify_setup(self) -> bool:
        """验证设置"""
        print_info("验证设置...")
        
        # 检查核心文件
        required_paths = [
            "coordinator/initial_to_prp_cli.py",
            "PRPs/templates/prp_base.md",
            "INITIAL.md"
        ]
        
        for path in required_paths:
            full_path = self.project_path / path
            if not full_path.exists():
                print_error(f"必需文件缺失: {path}")
                return False
        
        # 测试CLI工具
        try:
            env = os.environ.copy()
            env['PYTHONPATH'] = str(self.project_path)
            
            result = subprocess.run(
                [sys.executable, "-m", "coordinator.initial_to_prp_cli", "--help"],
                cwd=self.project_path,
                capture_output=True,
                text=True,
                env=env
            )
            
            if result.returncode == 0:
                print_success("CLI工具验证通过")
            else:
                print_warning("CLI工具验证失败")
                
        except Exception as e:
            print_warning(f"CLI工具验证失败: {e}")
        
        print_success("设置验证完成")
        return True
    
    def run(self):
        """运行设置流程"""
        print_header()
        
        print_info(f"设置方式: {self.setup_method}")
        print_info(f"项目路径: {self.project_path}")
        print_info(f"仓库地址: {self.REPO_URL}")
        print()
        
        # 检查Git可用性
        if not self.check_git_available():
            return False
        
        # 确保项目目录存在
        self.project_path.mkdir(parents=True, exist_ok=True)
        
        try:
            # 根据设置方式执行相应操作
            if self.setup_method == "submodule":
                self.setup_submodule()
            elif self.setup_method == "clone":
                self.setup_clone()
            elif self.setup_method == "sparse":
                self.setup_sparse()
            else:
                print_error(f"未知的设置方式: {self.setup_method}")
                return False
            
            # 验证设置
            if not self.verify_setup():
                return False
            
            # 创建使用指南
            self.create_usage_guide()
            
            print()
            print_success("🎉 GitHub设置完成！")
            print()
            print_info("下一步：")
            print_info("1. 编辑 INITIAL.md 文件描述你的功能需求")
            print_info("2. 运行: python -m coordinator.initial_to_prp_cli generate INITIAL.md")
            print_info("3. 查看生成的PRP文件并提供给AI助手实现")
            print()
            print_info("查看 USAGE_GUIDE.md 获取详细使用指南")
            
            return True
            
        except Exception as e:
            print_error(f"设置失败: {e}")
            return False


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="Initial.md到PRP生成系统 - GitHub设置脚本",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
设置方式说明:
  submodule   Git子模块方式（推荐，保持同步）
  clone       克隆后复制（独立副本）
  sparse      稀疏检出（只下载需要的文件）

示例:
  python setup_from_github.py submodule        # 在当前目录使用子模块
  python setup_from_github.py clone .          # 在当前目录克隆复制
  python setup_from_github.py sparse /path/to/project  # 稀疏检出到指定目录
        """
    )
    
    parser.add_argument(
        'setup_method',
        choices=['submodule', 'clone', 'sparse'],
        help='设置方式'
    )
    
    parser.add_argument(
        'project_path',
        nargs='?',
        default='.',
        help='目标项目目录 (默认: 当前目录)'
    )
    
    args = parser.parse_args()
    
    # 创建设置实例并运行
    setup = GitHubSetup(args.setup_method, args.project_path)
    success = setup.run()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
