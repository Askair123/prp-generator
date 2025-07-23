#!/usr/bin/env python3
"""
Initial.md到PRP生成系统 - 新项目设置脚本 (Python版本)

使用方法:
    python setup_new_project.py [项目路径] [设置类型]
    
设置类型:
    full     - 完整设置，包含所有文件和演示
    minimal  - 最小设置，只包含核心功能
    
示例:
    python setup_new_project.py                    # 在当前目录完整设置
    python setup_new_project.py /path/to/project   # 在指定目录完整设置
    python setup_new_project.py . minimal          # 在当前目录最小设置
"""

import os
import sys
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
    NC = '\033[0m'  # No Color


def print_info(message: str):
    """打印信息"""
    print(f"{Colors.BLUE}ℹ️  {message}{Colors.NC}")


def print_success(message: str):
    """打印成功信息"""
    print(f"{Colors.GREEN}✅ {message}{Colors.NC}")


def print_warning(message: str):
    """打印警告信息"""
    print(f"{Colors.YELLOW}⚠️  {message}{Colors.NC}")


def print_error(message: str):
    """打印错误信息"""
    print(f"{Colors.RED}❌ {message}{Colors.NC}")


def print_header():
    """打印标题"""
    print(f"{Colors.BLUE}")
    print("🚀 Initial.md到PRP生成系统 - 新项目设置")
    print("=" * 50)
    print(f"{Colors.NC}")


class ProjectSetup:
    """项目设置类"""
    
    def __init__(self, project_path: str, setup_type: str, source_path: Optional[str] = None):
        self.project_path = Path(project_path).resolve()
        self.setup_type = setup_type
        self.source_path = Path(source_path or Path(__file__).parent).resolve()
        
    def check_source_path(self) -> bool:
        """检查源路径是否有效"""
        coordinator_path = self.source_path / "coordinator"
        if not coordinator_path.exists():
            print_error("找不到源系统文件。请确保在Context-Engineering-Intro目录中运行此脚本。")
            print_info(f"当前源路径: {self.source_path}")
            print_info("或者指定正确的源路径作为第三个参数")
            return False
        return True
    
    def create_directories(self):
        """创建目录结构"""
        print_info("创建目录结构...")
        
        directories = [
            "coordinator",
            "PRPs/templates", 
            "test_initial_files",
            "examples"
        ]
        
        for directory in directories:
            dir_path = self.project_path / directory
            dir_path.mkdir(parents=True, exist_ok=True)
        
        print_success("目录结构创建完成")
    
    def setup_full(self):
        """完整设置"""
        print_info("执行完整设置...")
        
        try:
            # 复制核心模块
            coordinator_src = self.source_path / "coordinator"
            coordinator_dst = self.project_path / "coordinator"
            
            if coordinator_src.exists():
                shutil.copytree(coordinator_src, coordinator_dst, dirs_exist_ok=True)
            
            # 复制PRP模板
            template_src = self.source_path / "PRPs" / "templates" / "prp_base.md"
            template_dst = self.project_path / "PRPs" / "templates" / "prp_base.md"
            
            if template_src.exists():
                shutil.copy2(template_src, template_dst)
            
            # 复制示例和文档
            files_to_copy = [
                "INITIAL_EXAMPLE.md",
                "QUICK_REFERENCE.md",
                "demo_initial_to_prp_system.py"
            ]
            
            for filename in files_to_copy:
                src_file = self.source_path / filename
                dst_file = self.project_path / filename
                
                if src_file.exists():
                    shutil.copy2(src_file, dst_file)
            
            # 创建基本的INITIAL.md
            initial_md = self.project_path / "INITIAL.md"
            if not initial_md.exists():
                initial_example = self.source_path / "INITIAL_EXAMPLE.md"
                if initial_example.exists():
                    shutil.copy2(initial_example, initial_md)
                else:
                    self.create_basic_initial_md()
            
            print_success("完整设置完成")
            
        except Exception as e:
            print_error(f"完整设置失败: {str(e)}")
            raise
    
    def setup_minimal(self):
        """最小设置"""
        print_info("执行最小设置...")
        
        try:
            # 只复制核心文件
            core_files = [
                "initial_parser.py",
                "initial_to_prp_generator.py", 
                "initial_to_prp_cli.py",
                "__init__.py"
            ]
            
            coordinator_src = self.source_path / "coordinator"
            coordinator_dst = self.project_path / "coordinator"
            
            for filename in core_files:
                src_file = coordinator_src / filename
                dst_file = coordinator_dst / filename
                
                if src_file.exists():
                    shutil.copy2(src_file, dst_file)
            
            # 复制PRP模板
            template_src = self.source_path / "PRPs" / "templates" / "prp_base.md"
            template_dst = self.project_path / "PRPs" / "templates" / "prp_base.md"
            
            if template_src.exists():
                shutil.copy2(template_src, template_dst)
            
            # 创建基本的INITIAL.md模板
            self.create_basic_initial_md()
            
            print_success("最小设置完成")
            
        except Exception as e:
            print_error(f"最小设置失败: {str(e)}")
            raise
    
    def create_basic_initial_md(self):
        """创建基本的INITIAL.md模板"""
        initial_content = """## FEATURE:
[Insert your feature here]

## EXAMPLES:
[Provide and explain examples that you have in the `examples/` folder]

## DOCUMENTATION:
[List out any documentation (web pages, sources for an MCP server like Crawl4AI RAG, etc.) that will need to be referenced during development]

## OTHER CONSIDERATIONS:
[Any other considerations or specific requirements - great place to include gotchas that you see AI coding assistants miss with your projects a lot]
"""
        
        initial_md = self.project_path / "INITIAL.md"
        initial_md.write_text(initial_content, encoding='utf-8')
    
    def verify_setup(self) -> bool:
        """验证设置"""
        print_info("验证设置...")
        
        # 检查核心文件
        required_files = [
            "coordinator/initial_to_prp_cli.py",
            "PRPs/templates/prp_base.md",
            "INITIAL.md"
        ]
        
        for file_path in required_files:
            full_path = self.project_path / file_path
            if not full_path.exists():
                print_error(f"必需文件缺失: {file_path}")
                return False
        
        # 测试CLI工具
        try:
            import subprocess
            import sys
            
            # 切换到项目目录
            original_cwd = os.getcwd()
            os.chdir(self.project_path)
            
            # 设置Python路径
            env = os.environ.copy()
            env['PYTHONPATH'] = str(self.project_path)
            
            # 测试CLI命令
            result = subprocess.run(
                [sys.executable, "-m", "coordinator.initial_to_prp_cli", "--help"],
                capture_output=True,
                text=True,
                env=env
            )
            
            os.chdir(original_cwd)
            
            if result.returncode == 0:
                print_success("CLI工具验证通过")
            else:
                print_warning("CLI工具验证失败，可能需要设置PYTHONPATH")
                print_info(f"在项目目录中运行: export PYTHONPATH=\"${{PYTHONPATH}}:{self.project_path}\"")
                
        except Exception as e:
            print_warning(f"CLI工具验证失败: {str(e)}")
        
        print_success("设置验证完成")
        return True
    
    def create_usage_guide(self):
        """创建使用指南"""
        print_info("创建使用指南...")
        
        usage_content = """# 🚀 项目中的Initial.md到PRP生成系统使用指南

## 快速开始

### 1. 编辑INITIAL.md文件
描述你要实现的功能需求：

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
4. 按照PRP中的验证步骤测试实现

## 常用命令

```bash
# 生成PRP
python -m coordinator.initial_to_prp_cli generate INITIAL.md

# 自定义输出目录
python -m coordinator.initial_to_prp_cli generate INITIAL.md --output my_prps

# 跳过研究阶段（更快）
python -m coordinator.initial_to_prp_cli generate INITIAL.md --no-research

# 验证INITIAL.md
python -m coordinator.initial_to_prp_cli validate INITIAL.md

# 查看帮助
python -m coordinator.initial_to_prp_cli --help
```

## 故障排除

### Windows环境
```cmd
set PYTHONPATH=%PYTHONPATH%;%CD%
```

### Linux/Mac环境
```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### 验证系统功能
```bash
python -m coordinator.initial_to_prp_cli validate INITIAL.md
```

## 更多信息

查看 QUICK_REFERENCE.md 获取详细的使用指南和最佳实践。
"""
        
        usage_guide = self.project_path / "USAGE_GUIDE.md"
        usage_guide.write_text(usage_content, encoding='utf-8')
        
        print_success("使用指南创建完成")
    
    def run(self):
        """运行设置流程"""
        print_header()
        
        print_info(f"项目路径: {self.project_path}")
        print_info(f"设置类型: {self.setup_type}")
        print_info(f"源路径: {self.source_path}")
        print()
        
        # 检查源路径
        if not self.check_source_path():
            return False
        
        # 确保项目目录存在
        self.project_path.mkdir(parents=True, exist_ok=True)
        
        # 创建目录结构
        self.create_directories()
        
        # 根据设置类型执行相应设置
        try:
            if self.setup_type == "full":
                self.setup_full()
            elif self.setup_type == "minimal":
                self.setup_minimal()
            else:
                print_error(f"未知的设置类型: {self.setup_type}")
                print_info("支持的类型: full, minimal")
                return False
        except Exception as e:
            print_error(f"设置失败: {str(e)}")
            return False
        
        # 验证设置
        if not self.verify_setup():
            return False
        
        # 创建使用指南
        self.create_usage_guide()
        
        print()
        print_success("🎉 新项目设置完成！")
        print()
        print_info("下一步：")
        print_info("1. 编辑 INITIAL.md 文件描述你的功能需求")
        print_info("2. 运行: python -m coordinator.initial_to_prp_cli generate INITIAL.md")
        print_info("3. 查看生成的PRP文件并提供给AI助手实现")
        print()
        print_info("查看 USAGE_GUIDE.md 获取详细使用指南")
        if (self.project_path / "QUICK_REFERENCE.md").exists():
            print_info("查看 QUICK_REFERENCE.md 获取快速参考")
        
        return True


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="Initial.md到PRP生成系统 - 新项目设置脚本",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
设置类型说明:
  full        完整设置，包含所有文件和演示
  minimal     最小设置，只包含核心功能

示例:
  python setup_new_project.py                    # 在当前目录完整设置
  python setup_new_project.py /path/to/project   # 在指定目录完整设置
  python setup_new_project.py . minimal          # 在当前目录最小设置
        """
    )
    
    parser.add_argument(
        'project_path',
        nargs='?',
        default='.',
        help='目标项目目录 (默认: 当前目录)'
    )
    
    parser.add_argument(
        'setup_type',
        nargs='?',
        default='full',
        choices=['full', 'minimal'],
        help='设置类型 (默认: full)'
    )
    
    parser.add_argument(
        '--source',
        help='Context-Engineering-Intro源目录 (默认: 脚本所在目录)'
    )
    
    args = parser.parse_args()
    
    # 创建设置实例并运行
    setup = ProjectSetup(args.project_path, args.setup_type, args.source)
    success = setup.run()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
