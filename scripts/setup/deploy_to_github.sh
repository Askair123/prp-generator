#!/bin/bash

# Initial.md到PRP生成系统 - GitHub部署脚本
# 使用方法: ./deploy_to_github.sh [GitHub用户名] [仓库名]

set -e

# 默认参数
GITHUB_USERNAME=${1:-"Askair123"}
REPO_NAME=${2:-"Context-Engineering-Intro"}
REPO_URL="https://github.com/${GITHUB_USERNAME}/${REPO_NAME}.git"

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
    echo "🚀 Initial.md到PRP生成系统 - GitHub部署"
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

# 检查是否在正确的目录
check_directory() {
    if [ ! -d "coordinator" ] || [ ! -f "README.md" ]; then
        print_error "请在Context-Engineering-Intro项目根目录中运行此脚本。"
        print_info "当前目录: $(pwd)"
        print_info "应该包含: coordinator/ 目录和 README.md 文件"
        exit 1
    fi
}

# 初始化Git仓库（如果需要）
init_git_if_needed() {
    if [ ! -d ".git" ]; then
        print_info "初始化Git仓库..."
        git init
        print_success "Git仓库初始化完成"
    else
        print_info "Git仓库已存在"
    fi
}

# 设置远程仓库
setup_remote() {
    print_info "设置远程仓库..."
    
    # 检查是否已有origin
    if git remote | grep -q "^origin$"; then
        print_info "更新现有的origin远程仓库..."
        git remote set-url origin "$REPO_URL"
    else
        print_info "添加新的origin远程仓库..."
        git remote add origin "$REPO_URL"
    fi
    
    print_success "远程仓库设置完成: $REPO_URL"
}

# 添加和提交文件
commit_files() {
    print_info "添加和提交文件..."
    
    # 检查是否有未提交的更改
    if git diff --quiet && git diff --cached --quiet; then
        print_info "没有需要提交的更改"
        return
    fi
    
    # 添加所有文件
    git add .
    
    # 创建详细的提交信息
    commit_message="Complete Initial.md to PRP generation system implementation

Features:
- Full coordinator pattern system with Claude Flow integration
- Initial.md parser and PRP generator with intelligent content generation
- CLI tools for generate/validate/list operations with comprehensive options
- Git-based setup scripts for easy deployment to new projects
- Comprehensive documentation and usage guides
- Complete test suite and validation scripts
- Support for team collaboration and version control

Components:
- coordinator/ - Core system modules (parser, generator, CLI)
- PRPs/ - PRP templates and output directory
- setup scripts - GitHub-based deployment tools
- documentation - Complete usage guides and references
- examples and demos - Working examples and demonstrations

Ready for production use in any development environment.
Deployed to: $REPO_URL"
    
    git commit -m "$commit_message"
    print_success "文件提交完成"
}

# 推送到GitHub
push_to_github() {
    print_info "推送到GitHub仓库..."
    
    # 获取当前分支名
    current_branch=$(git branch --show-current)
    if [ -z "$current_branch" ]; then
        current_branch="main"
        git checkout -b main
    fi
    
    print_info "推送分支: $current_branch"
    
    # 推送到远程仓库
    if git push -u origin "$current_branch"; then
        print_success "推送成功！"
    else
        print_warning "推送失败，可能需要强制推送或解决冲突"
        print_info "如果这是首次推送到空仓库，可能需要："
        print_info "git push -u origin $current_branch --force"
        
        read -p "是否尝试强制推送？(y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            git push -u origin "$current_branch" --force
            print_success "强制推送成功！"
        else
            print_error "推送取消"
            exit 1
        fi
    fi
}

# 验证部署
verify_deployment() {
    print_info "验证部署..."
    
    # 检查远程仓库状态
    if git ls-remote origin &> /dev/null; then
        print_success "远程仓库连接正常"
    else
        print_error "无法连接到远程仓库"
        return 1
    fi
    
    # 显示仓库信息
    print_info "仓库信息:"
    git remote show origin | head -10
    
    print_success "部署验证完成"
}

# 显示后续步骤
show_next_steps() {
    print_success "🎉 部署完成！"
    echo
    print_info "你的GitHub仓库: https://github.com/${GITHUB_USERNAME}/${REPO_NAME}"
    echo
    print_info "现在你可以在新项目中使用以下命令："
    echo
    echo "# 一键设置"
    echo "curl -sSL https://raw.githubusercontent.com/${GITHUB_USERNAME}/${REPO_NAME}/main/quick_setup.sh | bash"
    echo
    echo "# Git子模块"
    echo "git submodule add https://github.com/${GITHUB_USERNAME}/${REPO_NAME}.git context-engineering"
    echo
    echo "# 下载设置脚本"
    echo "curl -O https://raw.githubusercontent.com/${GITHUB_USERNAME}/${REPO_NAME}/main/setup_from_github.py"
    echo "python setup_from_github.py submodule"
    echo
    print_info "查看完整指南: DEPLOY_TO_YOUR_GITHUB.md"
}

# 主函数
main() {
    print_header
    
    print_info "GitHub用户名: $GITHUB_USERNAME"
    print_info "仓库名称: $REPO_NAME"
    print_info "仓库URL: $REPO_URL"
    echo
    
    # 检查依赖
    check_git
    check_directory
    
    # 确认部署
    print_warning "即将部署到GitHub仓库: $REPO_URL"
    read -p "确认继续？(y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        print_info "部署取消"
        exit 0
    fi
    
    # 执行部署步骤
    init_git_if_needed
    setup_remote
    commit_files
    push_to_github
    verify_deployment
    show_next_steps
}

# 显示帮助
show_help() {
    echo "Initial.md到PRP生成系统 - GitHub部署脚本"
    echo
    echo "使用方法:"
    echo "  $0 [GitHub用户名] [仓库名]"
    echo
    echo "参数:"
    echo "  GitHub用户名    你的GitHub用户名 (默认: Askair123)"
    echo "  仓库名          仓库名称 (默认: Context-Engineering-Intro)"
    echo
    echo "示例:"
    echo "  $0                                    # 使用默认参数"
    echo "  $0 myusername                         # 指定用户名"
    echo "  $0 myusername my-context-engineering  # 指定用户名和仓库名"
    echo
    echo "注意:"
    echo "  - 请在Context-Engineering-Intro项目根目录中运行"
    echo "  - 确保GitHub仓库已创建（可以是空仓库）"
    echo "  - 需要有推送权限到指定仓库"
}

# 检查参数
if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    show_help
    exit 0
fi

# 运行主函数
main
