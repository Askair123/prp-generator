# 🚀 Initial.md到PRP生成系统 - 快速参考

## 📋 **基本工作流程**

```bash
# 1. 创建INITIAL.md文件（按模板格式）
# 2. 生成PRP文档
python -m coordinator.initial_to_prp_cli generate INITIAL.md
# 3. 将PRP提供给AI助手实现功能
```

## 🛠️ **常用命令**

### **生成PRP**
```bash
# 基本生成
python -m coordinator.initial_to_prp_cli generate INITIAL.md

# 自定义输出目录
python -m coordinator.initial_to_prp_cli generate INITIAL.md --output my_prps

# 跳过研究阶段（更快）
python -m coordinator.initial_to_prp_cli generate INITIAL.md --no-research

# 指定项目根目录
python -m coordinator.initial_to_prp_cli generate INITIAL.md --project-root /path/to/project
```

### **验证和管理**
```bash
# 验证INITIAL.md质量
python -m coordinator.initial_to_prp_cli validate INITIAL.md

# 列出现有PRP文件
python -m coordinator.initial_to_prp_cli list

# 列出指定目录的PRP
python -m coordinator.initial_to_prp_cli list --directory custom_prps

# 查看帮助
python -m coordinator.initial_to_prp_cli --help
```

### **演示脚本**
```bash
# 完整系统演示
python demo_initial_to_prp_system.py

# 其他演示
python demo_complete_documentation_sync.py
python demo_context_engineering_comparison.py
```

## 📝 **INITIAL.md模板**

```markdown
## FEATURE:
[详细描述功能，包括技术栈和主要需求]

## EXAMPLES:
[列出相关示例文件和参考代码]
- `examples/file1.py` - 功能描述
- `examples/file2.py` - 功能描述

## DOCUMENTATION:
[列出需要参考的文档链接]
- 官方文档: https://example.com/docs
- 教程: https://example.com/tutorial

## OTHER CONSIDERATIONS:
[重要考虑事项、性能要求、安全注意点]
- 性能要求
- 安全考虑
- 错误处理
```

## 🎯 **使用场景示例**

### **Web API开发**
```markdown
## FEATURE:
Create a user management API with FastAPI, JWT authentication, and PostgreSQL database.

## EXAMPLES:
- `examples/auth_api.py` - authentication patterns
- `examples/user_models.py` - user data models

## DOCUMENTATION:
- FastAPI Security: https://fastapi.tiangolo.com/tutorial/security/
- JWT: https://pyjwt.readthedocs.io/

## OTHER CONSIDERATIONS:
- Password hashing with bcrypt
- Rate limiting for login attempts
- Email verification for registration
```

### **数据处理**
```markdown
## FEATURE:
Build a data processing pipeline for CSV analysis with pandas and report generation.

## EXAMPLES:
- `examples/data_processor.py` - data cleaning patterns
- `examples/report_generator.py` - report generation

## DOCUMENTATION:
- Pandas: https://pandas.pydata.org/docs/
- Matplotlib: https://matplotlib.org/stable/

## OTHER CONSIDERATIONS:
- Handle large files efficiently
- Support multiple CSV formats
- Generate both PDF and HTML reports
```

## 🔧 **故障排除**

### **常见问题**
```bash
# 问题：验证失败
# 解决：检查INITIAL.md格式，确保所有部分都有内容

# 问题：找不到PRP文件
# 解决：检查输出目录
ls -la PRPs/
python -m coordinator.initial_to_prp_cli list

# 问题：生成质量低
# 解决：添加更多详细信息到INITIAL.md
python -m coordinator.initial_to_prp_cli validate INITIAL.md
```

### **调试技巧**
```bash
# 检查PRP文件大小（应该>200行）
wc -l PRPs/*.md

# 检查PRP结构
grep "## " PRPs/your_prp.md

# 验证生成的内容
head -50 PRPs/your_prp.md
```

## 📊 **质量指标**

### **INITIAL.md质量评分**
- **8/8分**: 优秀，可直接生成PRP
- **6-7分**: 良好，建议小幅改进
- **4-5分**: 一般，需要添加更多信息
- **<4分**: 需要大幅改进

### **PRP置信度评分**
- **9-10分**: 高质量，可直接使用
- **7-8分**: 良好质量，可能需要小调整
- **5-6分**: 中等质量，建议改进INITIAL.md
- **<5分**: 需要重新生成

## 🚀 **高级用法**

### **批量处理**
```bash
# 处理多个INITIAL文件
for file in *.md; do
    python -m coordinator.initial_to_prp_cli generate "$file" --output "prps_$(basename "$file" .md)"
done
```

### **程序化使用**
```python
from coordinator.initial_to_prp_generator import InitialToPRPGenerator
import asyncio

async def generate_prp():
    generator = InitialToPRPGenerator()
    prp = await generator.generate_prp_from_initial("INITIAL.md")
    print(f"Generated: {prp.file_path} (Score: {prp.confidence_score}/10)")

asyncio.run(generate_prp())
```

### **自定义配置**
```python
from coordinator.initial_to_prp_generator import PRPGenerationConfig

config = PRPGenerationConfig(
    output_directory="custom_prps",
    include_research=True,
    confidence_threshold=8
)
```

## 📚 **相关文档**

- **系统概览**: [`SYSTEM_OVERVIEW.md`](./SYSTEM_OVERVIEW.md)
- **实现报告**: [`INITIAL_TO_PRP_IMPLEMENTATION_REPORT.md`](./INITIAL_TO_PRP_IMPLEMENTATION_REPORT.md)
- **测试报告**: [`COMPLETE_SYSTEM_TEST_REPORT.md`](./COMPLETE_SYSTEM_TEST_REPORT.md)
- **完整README**: [`README.md`](./README.md)

## 💡 **最佳实践**

1. **详细描述功能** - 包含技术栈、主要需求、性能要求
2. **提供相关示例** - 引用项目中的相似代码或模式
3. **列出重要文档** - 包含官方文档和关键参考资料
4. **考虑周全** - 列出可能的陷阱、性能考虑、安全要求
5. **验证质量** - 使用validate命令确保INITIAL.md质量
6. **测试PRP** - 将生成的PRP提供给AI助手验证可用性

---

**记住：好的INITIAL.md = 高质量的PRP = 成功的实现！** 🎯
