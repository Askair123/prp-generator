# 🚀 新项目中的Initial.md到PRP生成系统设置指南

## 📋 **快速设置（推荐）**

### **方法1：使用自动化脚本（最简单）**

```bash
# 在你的新项目目录中
cd /path/to/your/new/project

# 下载并运行设置脚本
curl -O https://raw.githubusercontent.com/Askair123/Context-Engineering-Intro/main/setup_new_project.py
python setup_new_project.py

# 或者如果你已经有Context-Engineering-Intro源码
python /path/to/Context-Engineering-Intro/setup_new_project.py
```

### **方法2：手动复制核心文件**

```bash
# 在你的新项目目录中
cd /path/to/your/new/project

# 从Context-Engineering-Intro复制核心文件（如果你有本地副本）
SOURCE_PATH="/path/to/Context-Engineering-Intro"

# 或者直接从GitHub克隆
git clone https://github.com/Askair123/Context-Engineering-Intro.git temp_source
SOURCE_PATH="temp_source"

# 创建目录结构
mkdir -p coordinator PRPs/templates

# 复制核心模块
cp -r "$SOURCE_PATH/coordinator"/* ./coordinator/

# 复制PRP模板
cp "$SOURCE_PATH/PRPs/templates/prp_base.md" ./PRPs/templates/

# 复制示例文件
cp "$SOURCE_PATH/INITIAL_EXAMPLE.md" ./INITIAL.md
cp "$SOURCE_PATH/QUICK_REFERENCE.md" ./
```

### **方法3：最小化设置**

如果你只需要核心功能：

```bash
# 创建基本目录
mkdir -p coordinator PRPs/templates

# 只复制必要文件
cp "$SOURCE_PATH/coordinator/initial_parser.py" ./coordinator/
cp "$SOURCE_PATH/coordinator/initial_to_prp_generator.py" ./coordinator/
cp "$SOURCE_PATH/coordinator/initial_to_prp_cli.py" ./coordinator/
cp "$SOURCE_PATH/coordinator/__init__.py" ./coordinator/
cp "$SOURCE_PATH/PRPs/templates/prp_base.md" ./PRPs/templates/

# 创建基本INITIAL.md
cat > INITIAL.md << 'EOF'
## FEATURE:
[Insert your feature here]

## EXAMPLES:
[Provide and explain examples]

## DOCUMENTATION:
[List documentation references]

## OTHER CONSIDERATIONS:
[Any other considerations]
EOF
```

## ✅ **验证设置**

### **测试CLI工具**

```bash
# 设置Python路径（如果需要）
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# 测试CLI工具
python -m coordinator.initial_to_prp_cli --help

# 验证INITIAL.md
python -m coordinator.initial_to_prp_cli validate INITIAL.md
```

### **生成第一个PRP**

```bash
# 编辑INITIAL.md文件，然后生成PRP
python -m coordinator.initial_to_prp_cli generate INITIAL.md

# 检查生成的文件
ls PRPs/
```

## 📝 **项目目录结构**

设置完成后，你的项目应该有以下结构：

```
your-new-project/
├── coordinator/                    # 核心系统模块
│   ├── __init__.py
│   ├── initial_parser.py          # INITIAL.md解析器
│   ├── initial_to_prp_generator.py # PRP生成器
│   └── initial_to_prp_cli.py       # CLI工具
├── PRPs/                           # PRP输出目录
│   └── templates/
│       └── prp_base.md            # PRP模板
├── INITIAL.md                      # 功能需求文件
├── QUICK_REFERENCE.md              # 快速参考（可选）
└── USAGE_GUIDE.md                  # 使用指南（自动生成）
```

## 🎯 **立即开始使用**

### **第1步：编辑INITIAL.md**

```markdown
## FEATURE:
Build a simple todo list API using FastAPI with SQLite database, supporting CRUD operations for todo items.

## EXAMPLES:
- `examples/fastapi_basic.py` - basic FastAPI application structure
- `examples/sqlite_models.py` - SQLite database models

## DOCUMENTATION:
- FastAPI: https://fastapi.tiangolo.com/
- SQLite: https://docs.python.org/3/library/sqlite3.html

## OTHER CONSIDERATIONS:
- Use Pydantic for request/response validation
- Include proper error handling for database operations
- Add basic tests for all endpoints
- Support pagination for listing todos
```

### **第2步：生成PRP**

```bash
python -m coordinator.initial_to_prp_cli generate INITIAL.md
```

### **第3步：使用PRP**

1. 查看生成的PRP文件（在`PRPs/`目录下）
2. 将PRP内容复制给AI编程助手（Claude、ChatGPT、Cursor等）
3. AI会根据PRP实现你的功能
4. 按照PRP中的验证步骤测试实现

## 🔧 **常见问题解决**

### **问题1：模块导入错误**

```bash
# 症状
ModuleNotFoundError: No module named 'coordinator'

# 解决方案
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Windows用户
set PYTHONPATH=%PYTHONPATH%;%CD%
```

### **问题2：找不到源文件**

```bash
# 确保源路径正确
ls /path/to/Context-Engineering-Intro/coordinator/

# 或者下载最新版本
git clone https://github.com/coleam00/Context-Engineering-Intro.git
```

### **问题3：权限问题**

```bash
# 确保有写入权限
chmod +w .
mkdir -p coordinator PRPs/templates
```

### **问题4：Python版本兼容性**

```bash
# 确保使用Python 3.7+
python --version

# 如果需要，使用特定版本
python3 -m coordinator.initial_to_prp_cli --help
```

## 🚀 **高级设置选项**

### **自定义配置**

```python
# 创建自定义配置文件 config.py
from coordinator.initial_to_prp_generator import PRPGenerationConfig

custom_config = PRPGenerationConfig(
    output_directory="custom_prps",
    include_research=True,
    confidence_threshold=8
)
```

### **批量项目设置**

```bash
# 为多个项目设置
for project in project1 project2 project3; do
    mkdir -p "$project"
    cd "$project"
    python /path/to/setup_new_project.py . minimal
    cd ..
done
```

### **团队模板**

```bash
# 创建团队标准模板
mkdir -p team-template
cd team-template
python /path/to/setup_new_project.py . full

# 自定义INITIAL.md模板
cat > INITIAL_TEMPLATE.md << 'EOF'
## FEATURE:
[团队标准：详细描述功能，包括技术栈要求]

## EXAMPLES:
[团队标准：引用团队代码库中的相关示例]

## DOCUMENTATION:
[团队标准：列出团队认可的文档和资源]

## OTHER CONSIDERATIONS:
[团队标准：包含团队特定的最佳实践和注意事项]
EOF
```

## 📚 **下一步**

1. **📖 阅读文档**: 查看`QUICK_REFERENCE.md`了解详细使用方法
2. **🎯 实践使用**: 创建你的第一个INITIAL.md并生成PRP
3. **🔄 迭代改进**: 根据使用效果调整INITIAL.md的写法
4. **🤝 团队分享**: 将最佳实践分享给团队成员

## 💡 **最佳实践提醒**

- **详细描述功能**: 包含技术栈、性能要求、安全考虑
- **提供相关示例**: 引用项目中的相似代码或模式
- **列出重要文档**: 包含官方文档和关键参考资料
- **考虑周全**: 列出可能的陷阱、边界情况、错误处理

**现在你可以在任何新项目中快速设置和使用Initial.md到PRP生成系统了！** 🎯
