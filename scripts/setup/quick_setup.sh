#!/bin/bash

# Initial.md到PRP生成系统 - 一键快速设置脚本
# 使用方法: curl -sSL https://raw.githubusercontent.com/Askair123/prp-generator/main/quick_setup.sh | bash

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# 打印函数
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_header() {
    echo -e "${BLUE}"
    echo "🚀 Initial.md到PRP生成系统 - 一键设置"
    echo "=" * 50
    echo -e "${NC}"
}

# 检查Git是否可用
check_git() {
    if ! command -v git &> /dev/null; then
        print_error "Git未安装。请先安装Git。"
        exit 1
    fi
}

# 检查Python是否可用
check_python() {
    if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
        print_error "Python未安装。请先安装Python 3.7+。"
        exit 1
    fi
    
    # 确定Python命令
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    else
        PYTHON_CMD="python"
    fi
}

# 主设置函数
main_setup() {
    print_header
    
    print_info "正在设置Initial.md到PRP生成系统..."
    print_info "当前目录: $(pwd)"
    echo
    
    # 检查依赖
    check_git
    check_python
    
    # 选择设置方式
    if [ -d ".git" ]; then
        print_info "检测到Git仓库，使用子模块方式..."
        SETUP_METHOD="submodule"
    else
        print_info "非Git仓库，使用克隆复制方式..."
        SETUP_METHOD="clone"
    fi
    
    # 下载设置脚本
    print_info "下载设置脚本..."
    curl -sSL https://raw.githubusercontent.com/Askair123/prp-generator/main/scripts/setup/setup_from_github.py -o setup_from_github.py
    
    # 运行设置
    print_info "运行设置脚本..."
    $PYTHON_CMD setup_from_github.py $SETUP_METHOD .
    
    # 清理设置脚本
    rm -f setup_from_github.py
    
    print_success "设置完成！"
    echo
    print_info "下一步："
    print_info "1. 编辑 INITIAL.md 文件"
    print_info "2. 运行: $PYTHON_CMD src/coordinator/initial_to_prp_cli.py generate INITIAL.md"
    print_info "3. 使用生成的PRP文件"
    echo
    print_info "查看 USAGE_GUIDE.md 获取详细指南"
}

# 错误处理
trap 'print_error "设置过程中出现错误"; exit 1' ERR

# 运行主函数
main_setup
