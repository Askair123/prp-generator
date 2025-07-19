#!/usr/bin/env python3
"""
Initial.md到PRP生成系统 - 设置验证脚本

验证系统是否正确设置并可以正常工作。

使用方法:
    python verify_setup.py
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple


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
    print("🔍 Initial.md到PRP生成系统 - 设置验证")
    print("=" * 50)
    print(f"{Colors.NC}")


class SetupVerifier:
    """设置验证类"""
    
    def __init__(self):
        self.project_path = Path.cwd()
        self.errors = []
        self.warnings = []
        
    def check_file_exists(self, file_path: str, description: str) -> bool:
        """检查文件是否存在"""
        full_path = self.project_path / file_path
        if full_path.exists():
            print_success(f"{description}: {file_path}")
            return True
        else:
            print_error(f"{description}缺失: {file_path}")
            self.errors.append(f"缺失文件: {file_path}")
            return False
    
    def check_directory_exists(self, dir_path: str, description: str) -> bool:
        """检查目录是否存在"""
        full_path = self.project_path / dir_path
        if full_path.exists() and full_path.is_dir():
            print_success(f"{description}: {dir_path}")
            return True
        else:
            print_error(f"{description}缺失: {dir_path}")
            self.errors.append(f"缺失目录: {dir_path}")
            return False
    
    def check_python_module(self, module_name: str) -> bool:
        """检查Python模块是否可导入"""
        try:
            # 设置Python路径
            env = os.environ.copy()
            env['PYTHONPATH'] = str(self.project_path)
            
            result = subprocess.run(
                [sys.executable, "-c", f"import {module_name}"],
                capture_output=True,
                text=True,
                env=env
            )
            
            if result.returncode == 0:
                print_success(f"Python模块可导入: {module_name}")
                return True
            else:
                print_error(f"Python模块导入失败: {module_name}")
                print_error(f"错误信息: {result.stderr.strip()}")
                self.errors.append(f"模块导入失败: {module_name}")
                return False
                
        except Exception as e:
            print_error(f"模块检查失败: {module_name} - {e}")
            self.errors.append(f"模块检查异常: {module_name}")
            return False
    
    def check_cli_command(self, command: List[str], description: str) -> bool:
        """检查CLI命令是否可执行"""
        try:
            # 设置Python路径
            env = os.environ.copy()
            env['PYTHONPATH'] = str(self.project_path)
            
            result = subprocess.run(
                command,
                cwd=self.project_path,
                capture_output=True,
                text=True,
                env=env,
                timeout=30
            )
            
            if result.returncode == 0:
                print_success(f"{description}: 命令执行成功")
                return True
            else:
                print_error(f"{description}: 命令执行失败")
                print_error(f"错误信息: {result.stderr.strip()}")
                self.errors.append(f"CLI命令失败: {' '.join(command)}")
                return False
                
        except subprocess.TimeoutExpired:
            print_error(f"{description}: 命令执行超时")
            self.errors.append(f"CLI命令超时: {' '.join(command)}")
            return False
        except Exception as e:
            print_error(f"{description}: 命令检查失败 - {e}")
            self.errors.append(f"CLI命令异常: {' '.join(command)}")
            return False
    
    def check_initial_md_quality(self) -> bool:
        """检查INITIAL.md文件质量"""
        initial_md = self.project_path / "INITIAL.md"
        if not initial_md.exists():
            return False
        
        try:
            content = initial_md.read_text(encoding='utf-8')
            
            # 检查必要的部分
            required_sections = ["## FEATURE:", "## EXAMPLES:", "## DOCUMENTATION:", "## OTHER CONSIDERATIONS:"]
            missing_sections = []
            
            for section in required_sections:
                if section not in content:
                    missing_sections.append(section)
            
            if missing_sections:
                print_warning(f"INITIAL.md缺少部分: {', '.join(missing_sections)}")
                self.warnings.append(f"INITIAL.md缺少部分: {missing_sections}")
                return False
            else:
                print_success("INITIAL.md格式正确")
                return True
                
        except Exception as e:
            print_error(f"INITIAL.md检查失败: {e}")
            self.errors.append("INITIAL.md检查异常")
            return False
    
    def check_prp_generation(self) -> bool:
        """测试PRP生成功能"""
        print_info("测试PRP生成功能...")
        
        # 检查是否有INITIAL.md
        if not (self.project_path / "INITIAL.md").exists():
            print_error("无法测试PRP生成：INITIAL.md文件不存在")
            return False
        
        try:
            # 设置Python路径
            env = os.environ.copy()
            env['PYTHONPATH'] = str(self.project_path)
            
            # 运行PRP生成命令
            result = subprocess.run(
                [sys.executable, "-m", "coordinator.initial_to_prp_cli", "generate", "INITIAL.md", "--no-research"],
                cwd=self.project_path,
                capture_output=True,
                text=True,
                env=env,
                timeout=60
            )
            
            if result.returncode == 0:
                print_success("PRP生成测试成功")
                
                # 检查是否生成了PRP文件
                prp_dir = self.project_path / "PRPs"
                if prp_dir.exists():
                    prp_files = list(prp_dir.glob("*.md"))
                    if prp_files:
                        print_success(f"生成了 {len(prp_files)} 个PRP文件")
                        
                        # 检查PRP文件大小
                        for prp_file in prp_files:
                            size = prp_file.stat().st_size
                            if size > 1000:  # 至少1KB
                                print_success(f"PRP文件大小正常: {prp_file.name} ({size} bytes)")
                            else:
                                print_warning(f"PRP文件可能太小: {prp_file.name} ({size} bytes)")
                                self.warnings.append(f"PRP文件较小: {prp_file.name}")
                    else:
                        print_warning("未找到生成的PRP文件")
                        self.warnings.append("未生成PRP文件")
                
                return True
            else:
                print_error("PRP生成测试失败")
                print_error(f"错误信息: {result.stderr.strip()}")
                self.errors.append("PRP生成失败")
                return False
                
        except subprocess.TimeoutExpired:
            print_error("PRP生成测试超时")
            self.errors.append("PRP生成超时")
            return False
        except Exception as e:
            print_error(f"PRP生成测试异常: {e}")
            self.errors.append("PRP生成异常")
            return False
    
    def run_verification(self) -> bool:
        """运行完整验证"""
        print_header()
        print_info(f"验证项目: {self.project_path}")
        print()
        
        # 1. 检查核心文件和目录
        print_info("1. 检查核心文件和目录...")
        core_checks = [
            ("coordinator", "核心模块目录", "dir"),
            ("coordinator/__init__.py", "模块初始化文件", "file"),
            ("coordinator/initial_parser.py", "INITIAL.md解析器", "file"),
            ("coordinator/initial_to_prp_generator.py", "PRP生成器", "file"),
            ("coordinator/initial_to_prp_cli.py", "CLI工具", "file"),
            ("PRPs", "PRP输出目录", "dir"),
            ("PRPs/templates", "PRP模板目录", "dir"),
            ("PRPs/templates/prp_base.md", "PRP基础模板", "file"),
            ("INITIAL.md", "功能需求文件", "file"),
        ]
        
        core_success = True
        for path, desc, type_check in core_checks:
            if type_check == "dir":
                if not self.check_directory_exists(path, desc):
                    core_success = False
            else:
                if not self.check_file_exists(path, desc):
                    core_success = False
        
        print()
        
        # 2. 检查Python模块导入
        print_info("2. 检查Python模块导入...")
        module_checks = [
            "coordinator",
            "coordinator.initial_parser",
            "coordinator.initial_to_prp_generator",
            "coordinator.initial_to_prp_cli"
        ]
        
        module_success = True
        for module in module_checks:
            if not self.check_python_module(module):
                module_success = False
        
        print()
        
        # 3. 检查CLI命令
        print_info("3. 检查CLI命令...")
        cli_commands = [
            ([sys.executable, "-m", "coordinator.initial_to_prp_cli", "--help"], "CLI帮助命令"),
            ([sys.executable, "-m", "coordinator.initial_to_prp_cli", "validate", "INITIAL.md"], "INITIAL.md验证命令"),
        ]
        
        cli_success = True
        for command, desc in cli_commands:
            if not self.check_cli_command(command, desc):
                cli_success = False
        
        print()
        
        # 4. 检查INITIAL.md质量
        print_info("4. 检查INITIAL.md质量...")
        initial_success = self.check_initial_md_quality()
        print()
        
        # 5. 测试PRP生成
        print_info("5. 测试PRP生成功能...")
        prp_success = self.check_prp_generation()
        print()
        
        # 总结结果
        print_info("验证结果总结:")
        print(f"  核心文件检查: {'✅ 通过' if core_success else '❌ 失败'}")
        print(f"  模块导入检查: {'✅ 通过' if module_success else '❌ 失败'}")
        print(f"  CLI命令检查: {'✅ 通过' if cli_success else '❌ 失败'}")
        print(f"  INITIAL.md检查: {'✅ 通过' if initial_success else '⚠️ 警告'}")
        print(f"  PRP生成测试: {'✅ 通过' if prp_success else '❌ 失败'}")
        
        overall_success = core_success and module_success and cli_success and prp_success
        
        print()
        if overall_success:
            print_success("🎉 系统设置验证通过！系统已准备就绪。")
        else:
            print_error("❌ 系统设置验证失败。请检查以下问题：")
            for error in self.errors:
                print_error(f"  - {error}")
        
        if self.warnings:
            print()
            print_warning("⚠️ 发现以下警告：")
            for warning in self.warnings:
                print_warning(f"  - {warning}")
        
        print()
        print_info("下一步：")
        if overall_success:
            print_info("1. 编辑 INITIAL.md 文件描述你的功能需求")
            print_info("2. 运行: python -m coordinator.initial_to_prp_cli generate INITIAL.md")
            print_info("3. 查看生成的PRP文件并提供给AI助手实现")
        else:
            print_info("1. 解决上述错误")
            print_info("2. 重新运行验证: python verify_setup.py")
            print_info("3. 查看设置指南: GIT_SETUP_GUIDE.md")
        
        return overall_success


def main():
    """主函数"""
    verifier = SetupVerifier()
    success = verifier.run_verification()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
