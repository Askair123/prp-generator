#!/bin/bash

# Initial.md到PRP生成系统 - 新项目设置脚本
# 使用方法: ./setup_new_project.sh [项目路径] [设置类型]
# 设置类型: full (完整), minimal (最小), submodule (子模块)

set -e

# 默认参数
PROJECT_PATH=${1:-$(pwd)}
SETUP_TYPE=${2:-"full"}
SOURCE_PATH=${3:-"$(dirname "$0")"}

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

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
    echo "🚀 Initial.md到PRP生成系统 - 新项目设置"
    echo "=" * 50
    echo -e "${NC}"
}

# 检查源路径
check_source_path() {
    if [ ! -d "$SOURCE_PATH/coordinator" ]; then
        print_error "找不到源系统文件。请确保在Context-Engineering-Intro目录中运行此脚本。"
        print_info "或者指定正确的源路径: $0 [项目路径] [设置类型] [源路径]"
        exit 1
    fi
}

# 创建目录结构
create_directories() {
    print_info "创建目录结构..."
    
    cd "$PROJECT_PATH"
    
    mkdir -p coordinator
    mkdir -p PRPs/templates
    mkdir -p test_initial_files
    mkdir -p examples
    
    print_success "目录结构创建完成"
}

# 完整设置
setup_full() {
    print_info "执行完整设置..."
    
    # 复制核心模块
    cp -r "$SOURCE_PATH/coordinator"/* ./coordinator/
    
    # 复制PRP模板
    cp "$SOURCE_PATH/PRPs/templates/prp_base.md" ./PRPs/templates/
    
    # 复制示例和文档
    cp "$SOURCE_PATH/INITIAL_EXAMPLE.md" ./
    cp "$SOURCE_PATH/QUICK_REFERENCE.md" ./
    
    # 复制演示脚本
    cp "$SOURCE_PATH/demo_initial_to_prp_system.py" ./
    
    # 创建基本的INITIAL.md
    if [ ! -f "INITIAL.md" ]; then
        cp "$SOURCE_PATH/INITIAL_EXAMPLE.md" ./INITIAL.md
    fi
    
    print_success "完整设置完成"
}

# 最小设置
setup_minimal() {
    print_info "执行最小设置..."
    
    # 只复制核心文件
    cp "$SOURCE_PATH/coordinator/initial_parser.py" ./coordinator/
    cp "$SOURCE_PATH/coordinator/initial_to_prp_generator.py" ./coordinator/
    cp "$SOURCE_PATH/coordinator/initial_to_prp_cli.py" ./coordinator/
    cp "$SOURCE_PATH/coordinator/__init__.py" ./coordinator/
    
    # 复制PRP模板
    cp "$SOURCE_PATH/PRPs/templates/prp_base.md" ./PRPs/templates/
    
    # 创建基本的INITIAL.md模板
    cat > INITIAL.md << 'EOF'
## FEATURE:
[Insert your feature here]

## EXAMPLES:
[Provide and explain examples that you have in the `examples/` folder]

## DOCUMENTATION:
[List out any documentation (web pages, sources for an MCP server like Crawl4AI RAG, etc.) that will need to be referenced during development]

## OTHER CONSIDERATIONS:
[Any other considerations or specific requirements - great place to include gotchas that you see AI coding assistants miss with your projects a lot]
EOF
    
    print_success "最小设置完成"
}

# 子模块设置
setup_submodule() {
    print_info "执行Git子模块设置..."
    
    # 检查是否是Git仓库
    if [ ! -d ".git" ]; then
        print_warning "当前目录不是Git仓库，初始化Git仓库..."
        git init
    fi
    
    # 添加子模块
    if [ ! -d "context-engineering" ]; then
        git submodule add https://github.com/coleam00/Context-Engineering-Intro.git context-engineering
    fi
    
    # 创建符号链接
    ln -sf context-engineering/coordinator ./coordinator
    ln -sf context-engineering/PRPs ./PRPs
    
    # 复制本地文件
    cp context-engineering/INITIAL_EXAMPLE.md ./INITIAL.md
    cp context-engineering/QUICK_REFERENCE.md ./
    
    print_success "Git子模块设置完成"
}

# 验证设置
verify_setup() {
    print_info "验证设置..."
    
    # 检查核心文件
    if [ ! -f "coordinator/initial_to_prp_cli.py" ]; then
        print_error "核心CLI文件缺失"
        return 1
    fi
    
    if [ ! -f "PRPs/templates/prp_base.md" ]; then
        print_error "PRP模板文件缺失"
        return 1
    fi
    
    if [ ! -f "INITIAL.md" ]; then
        print_error "INITIAL.md文件缺失"
        return 1
    fi
    
    # 测试CLI工具
    if python -m coordinator.initial_to_prp_cli --help > /dev/null 2>&1; then
        print_success "CLI工具验证通过"
    else
        print_warning "CLI工具验证失败，可能需要设置PYTHONPATH"
        print_info "运行: export PYTHONPATH=\"\${PYTHONPATH}:\$(pwd)\""
    fi
    
    print_success "设置验证完成"
}

# 创建使用指南
create_usage_guide() {
    print_info "创建使用指南..."
    
    cat > USAGE_GUIDE.md << 'EOF'
# 🚀 项目中的Initial.md到PRP生成系统使用指南

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

### 模块导入错误
```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### 验证系统功能
```bash
python -m coordinator.initial_to_prp_cli validate INITIAL.md
```

## 更多信息

查看 QUICK_REFERENCE.md 获取详细的使用指南和最佳实践。
EOF
    
    print_success "使用指南创建完成"
}

# 主函数
main() {
    print_header
    
    print_info "项目路径: $PROJECT_PATH"
    print_info "设置类型: $SETUP_TYPE"
    print_info "源路径: $SOURCE_PATH"
    echo
    
    # 检查源路径
    check_source_path
    
    # 创建目录结构
    create_directories
    
    # 根据设置类型执行相应设置
    case $SETUP_TYPE in
        "full")
            setup_full
            ;;
        "minimal")
            setup_minimal
            ;;
        "submodule")
            setup_submodule
            ;;
        *)
            print_error "未知的设置类型: $SETUP_TYPE"
            print_info "支持的类型: full, minimal, submodule"
            exit 1
            ;;
    esac
    
    # 验证设置
    verify_setup
    
    # 创建使用指南
    create_usage_guide
    
    echo
    print_success "🎉 新项目设置完成！"
    echo
    print_info "下一步："
    print_info "1. 编辑 INITIAL.md 文件描述你的功能需求"
    print_info "2. 运行: python -m coordinator.initial_to_prp_cli generate INITIAL.md"
    print_info "3. 查看生成的PRP文件并提供给AI助手实现"
    echo
    print_info "查看 USAGE_GUIDE.md 获取详细使用指南"
    print_info "查看 QUICK_REFERENCE.md 获取快速参考"
}

# 显示帮助
show_help() {
    echo "Initial.md到PRP生成系统 - 新项目设置脚本"
    echo
    echo "使用方法:"
    echo "  $0 [项目路径] [设置类型] [源路径]"
    echo
    echo "参数:"
    echo "  项目路径    目标项目目录 (默认: 当前目录)"
    echo "  设置类型    full|minimal|submodule (默认: full)"
    echo "  源路径      Context-Engineering-Intro源目录 (默认: 脚本所在目录)"
    echo
    echo "设置类型说明:"
    echo "  full        完整设置，包含所有文件和演示"
    echo "  minimal     最小设置，只包含核心功能"
    echo "  submodule   Git子模块方式，保持与源同步"
    echo
    echo "示例:"
    echo "  $0                                    # 在当前目录完整设置"
    echo "  $0 /path/to/project minimal          # 在指定目录最小设置"
    echo "  $0 . submodule                       # 在当前目录使用子模块设置"
}

# 检查参数
if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    show_help
    exit 0
fi

# 运行主函数
main
