#!/usr/bin/env python3
"""
Initial.md到PRP生成系统 - GitHub设置脚本
支持多种设置方式：submodule, clone, sparse
"""

import os
import sys
import subprocess
import shutil
import argparse
from pathlib import Path

def run_command(cmd, cwd=None, check=True):
    """运行命令并返回结果"""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, check=check)
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return False, e.stdout, e.stderr
    except Exception as e:
        return False, "", str(e)

def print_info(msg):
    print(f"ℹ️  {msg}")

def print_success(msg):
    print(f"✅ {msg}")

def print_error(msg):
    print(f"❌ {msg}")

def setup_clone(target_dir):
    """克隆复制方式设置"""
    print_info("使用克隆复制方式设置...")

    # 克隆仓库（指定main分支）
    print_info("克隆PRP生成工具仓库...")
    success, stdout, stderr = run_command("git clone -b main https://github.com/Askair123/prp-generator.git prp-temp")

    if not success:
        print_error(f"克隆失败: {stderr}")
        return False

    # 复制核心文件
    print_info("复制核心文件...")
    try:
        # 复制src目录
        if os.path.exists("src"):
            shutil.rmtree("src")
        shutil.copytree("prp-temp/src", "src")

        # 复制templates目录
        if os.path.exists("templates"):
            shutil.rmtree("templates")
        shutil.copytree("prp-temp/templates", "templates")

        # 复制INITIAL.md
        if os.path.exists("prp-temp/INITIAL.md"):
            shutil.copy2("prp-temp/INITIAL.md", "INITIAL.md")

        print_success("文件复制完成")

    except Exception as e:
        print_error(f"文件复制失败: {e}")
        return False

    # 清理临时文件
    try:
        shutil.rmtree("prp-temp")
        print_success("临时文件清理完成")
    except Exception as e:
        print_error(f"清理失败: {e}")

    return True

def setup_submodule(target_dir):
    """子模块方式设置"""
    print_info("使用Git子模块方式设置...")

    # 添加子模块
    success, stdout, stderr = run_command("git submodule add https://github.com/Askair123/prp-generator.git prp-tools")

    if not success:
        print_error(f"子模块添加失败: {stderr}")
        return False

    # 创建符号链接
    try:
        if not os.path.exists("src"):
            os.symlink("prp-tools/src", "src")
        if not os.path.exists("templates"):
            os.symlink("prp-tools/templates", "templates")
        if not os.path.exists("INITIAL.md"):
            os.symlink("prp-tools/INITIAL.md", "INITIAL.md")

        print_success("符号链接创建完成")

    except Exception as e:
        print_error(f"符号链接创建失败: {e}")
        return False

    return True

def setup_sparse(target_dir):
    """稀疏检出方式设置"""
    print_info("使用稀疏检出方式设置...")

    # 初始化Git仓库
    success, stdout, stderr = run_command("git init")
    if not success:
        print_error(f"Git初始化失败: {stderr}")
        return False

    # 添加远程仓库
    success, stdout, stderr = run_command("git remote add origin https://github.com/Askair123/prp-generator.git")
    if not success:
        print_error(f"添加远程仓库失败: {stderr}")
        return False

    # 配置稀疏检出
    success, stdout, stderr = run_command("git config core.sparseCheckout true")
    if not success:
        print_error(f"配置稀疏检出失败: {stderr}")
        return False

    # 设置稀疏检出路径
    sparse_paths = ["src/*", "templates/*", "INITIAL.md"]
    with open(".git/info/sparse-checkout", "w") as f:
        f.write("\n".join(sparse_paths))

    # 拉取文件
    success, stdout, stderr = run_command("git pull origin main")
    if not success:
        print_error(f"拉取文件失败: {stderr}")
        return False

    print_success("稀疏检出完成")
    return True

def main():
    parser = argparse.ArgumentParser(description="Initial.md到PRP生成系统设置脚本")
    parser.add_argument("method", choices=["clone", "submodule", "sparse"],
                       help="设置方式: clone(克隆复制), submodule(Git子模块), sparse(稀疏检出)")
    parser.add_argument("target", nargs="?", default=".", help="目标目录 (默认: 当前目录)")

    args = parser.parse_args()

    # 切换到目标目录
    target_dir = Path(args.target).resolve()
    os.chdir(target_dir)

    print_info(f"设置目录: {target_dir}")
    print_info(f"设置方式: {args.method}")

    # 根据方式执行设置
    if args.method == "clone":
        success = setup_clone(target_dir)
    elif args.method == "submodule":
        success = setup_submodule(target_dir)
    elif args.method == "sparse":
        success = setup_sparse(target_dir)
    else:
        print_error(f"不支持的设置方式: {args.method}")
        return 1

    if success:
        print_success("PRP生成工具设置完成！")
        print_info("下一步:")
        print_info("1. 编辑 INITIAL.md 文件")
        print_info("2. 运行: python src/coordinator/initial_to_prp_cli.py validate INITIAL.md")
        print_info("3. 运行: python src/coordinator/initial_to_prp_cli.py generate INITIAL.md")
        return 0
    else:
        print_error("设置失败")
        return 1

if __name__ == "__main__":
    sys.exit(main())