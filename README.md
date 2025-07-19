# Context Engineering Template

A comprehensive template for getting started with Context Engineering - the discipline of engineering context for AI coding assistants so they have the information necessary to get the job done end to end.

> **Context Engineering is 10x better than prompt engineering and 100x better than vibe coding.**

## 🚀 Quick Start

```bash
# 1. Clone this template
git clone https://github.com/coleam00/Context-Engineering-Intro.git
cd Context-Engineering-Intro

# 2. Set up your project rules (optional - template provided)
# Edit CLAUDE.md to add your project-specific guidelines

# 3. Add examples (highly recommended)
# Place relevant code examples in the examples/ folder

# 4. Create your initial feature request
# Edit INITIAL.md with your feature requirements

# 5. Generate a comprehensive PRP (Product Requirements Prompt)
# In Claude Code, run:
/generate-prp INITIAL.md

# 6. Execute the PRP to implement your feature
# In Claude Code, run:
/execute-prp PRPs/your-feature-name.md
```

## 🎯 **新增内容：Coordinator Pattern System with Claude Flow Integration**

本仓库现已扩展，包含了完整的**Coordinator Pattern System**，展示了通过智能Claude Flow配置生成的高级Context Engineering原理。

### 🧠 **核心系统特性**
- **🤖 多Agent协调**: 智能agent编排和任务分配
- **📚 深度文档系统**: LLM优化的Claude Flow文档，100%组件覆盖
- **🎯 上下文感知配置**: 基于项目分析的智能配置生成
- **✅ 完整验证**: 所有配置的内置验证和故障排除
- **🔍 智能知识检索**: 上下文感知的文档选择和指导生成

### 📊 **系统完成度**
```
✅ 文档覆盖: 6个核心组件 (100%覆盖)
✅ 配置模式: 3个完整模式 (开发/生产/企业)
✅ 验证支持: 18个验证命令 + 15个故障排除方案
✅ 质量评分: 100% (生产就绪级别)
✅ Agent角色: 6个专业化Agent角色
```

### 📚 **完整项目文档**
**详细文档请查看**: [`docs/`](./docs/) 目录和项目根目录

#### **核心系统文档**
- 📖 **深度文档系统**: [`DEEP_DOCUMENTATION_SYSTEM_REPORT.md`](./DEEP_DOCUMENTATION_SYSTEM_REPORT.md)
- 🧠 **知识嵌入分析**: [`CLAUDE_FLOW_KNOWLEDGE_INTEGRATION_REPORT.md`](./CLAUDE_FLOW_KNOWLEDGE_INTEGRATION_REPORT.md)
- 🔄 **Context Engineering对比**: [`CONTEXT_ENGINEERING_ANALYSIS_REPORT.md`](./CONTEXT_ENGINEERING_ANALYSIS_REPORT.md)
- 📚 **完整文档同步**: [`COMPLETE_DOCUMENTATION_SYNC_REPORT.md`](./COMPLETE_DOCUMENTATION_SYNC_REPORT.md)

#### **原有项目文档**
- 📖 **使用指南**: Coordinator Agent模式和Linear MCP使用指南
- 🏗️ **架构设计**: 三层架构分析和重构实现方案
- 📊 **技术分析**: 功能重叠分析和优化建议
- 🔗 **集成方案**: Claude Flow整合架构和实施指导
- 💡 **实现示例**: 完整的代码示例和使用演示

### 🚀 **快速开始（Coordinator Pattern System）**

#### **体验完整系统**
```bash
# 1. 运行完整文档同步演示
python demo_complete_documentation_sync.py

# 2. 体验Context Engineering对比
python demo_context_engineering_comparison.py

# 3. 测试知识增强配置生成
python demo_knowledge_enhanced_system.py

# 4. 查看深度文档检索
python demo_deep_documentation_system.py
```

#### **了解系统架构**
1. **深度文档系统**: 阅读 [`DEEP_DOCUMENTATION_SYSTEM_REPORT.md`](./DEEP_DOCUMENTATION_SYSTEM_REPORT.md)
2. **知识嵌入原理**: 查看 [`CLAUDE_FLOW_KNOWLEDGE_INTEGRATION_REPORT.md`](./CLAUDE_FLOW_KNOWLEDGE_INTEGRATION_REPORT.md)
3. **Context Engineering**: 参考 [`CONTEXT_ENGINEERING_ANALYSIS_REPORT.md`](./CONTEXT_ENGINEERING_ANALYSIS_REPORT.md)

#### **原有项目快速开始**
1. **了解完整方案**: 阅读 [`docs/architecture/refactored-architecture-implementation.md`](./docs/architecture/refactored-architecture-implementation.md)
2. **掌握工具使用**: 查看 [`docs/guides/linear-mcp-guide-for-llm.md`](./docs/guides/linear-mcp-guide-for-llm.md)
3. **理解技术分析**: 参考 [`docs/analysis/overlap-analysis-and-optimization.md`](./docs/analysis/overlap-analysis-and-optimization.md)

---

## 📚 Table of Contents (原有内容)

- [What is Context Engineering?](#what-is-context-engineering)
- [Template Structure](#template-structure)
- [Step-by-Step Guide](#step-by-step-guide)
- [Writing Effective INITIAL.md Files](#writing-effective-initialmd-files)
- [The PRP Workflow](#the-prp-workflow)
- [Using Examples Effectively](#using-examples-effectively)
- [Best Practices](#best-practices)

## What is Context Engineering?

Context Engineering represents a paradigm shift from traditional prompt engineering:

### Prompt Engineering vs Context Engineering

**Prompt Engineering:**
- Focuses on clever wording and specific phrasing
- Limited to how you phrase a task
- Like giving someone a sticky note

**Context Engineering:**
- A complete system for providing comprehensive context
- Includes documentation, examples, rules, patterns, and validation
- Like writing a full screenplay with all the details

### Why Context Engineering Matters

1. **Reduces AI Failures**: Most agent failures aren't model failures - they're context failures
2. **Ensures Consistency**: AI follows your project patterns and conventions
3. **Enables Complex Features**: AI can handle multi-step implementations with proper context
4. **Self-Correcting**: Validation loops allow AI to fix its own mistakes

## Template Structure

```
context-engineering-intro/
├── .claude/
│   ├── commands/
│   │   ├── generate-prp.md    # Generates comprehensive PRPs
│   │   └── execute-prp.md     # Executes PRPs to implement features
│   └── settings.local.json    # Claude Code permissions
├── PRPs/
│   ├── templates/
│   │   └── prp_base.md       # Base template for PRPs
│   └── EXAMPLE_multi_agent_prp.md  # Example of a complete PRP
├── examples/                  # Your code examples (critical!)
├── CLAUDE.md                 # Global rules for AI assistant
├── INITIAL.md               # Template for feature requests
├── INITIAL_EXAMPLE.md       # Example feature request
└── README.md                # This file
```

This template doesn't focus on RAG and tools with context engineering because I have a LOT more in store for that soon. ;)

## Step-by-Step Guide

### 1. Set Up Global Rules (CLAUDE.md)

The `CLAUDE.md` file contains project-wide rules that the AI assistant will follow in every conversation. The template includes:

- **Project awareness**: Reading planning docs, checking tasks
- **Code structure**: File size limits, module organization
- **Testing requirements**: Unit test patterns, coverage expectations
- **Style conventions**: Language preferences, formatting rules
- **Documentation standards**: Docstring formats, commenting practices

**You can use the provided template as-is or customize it for your project.**

### 2. Create Your Initial Feature Request

Edit `INITIAL.md` to describe what you want to build:

```markdown
## FEATURE:
[Describe what you want to build - be specific about functionality and requirements]

## EXAMPLES:
[List any example files in the examples/ folder and explain how they should be used]

## DOCUMENTATION:
[Include links to relevant documentation, APIs, or MCP server resources]

## OTHER CONSIDERATIONS:
[Mention any gotchas, specific requirements, or things AI assistants commonly miss]
```

**See `INITIAL_EXAMPLE.md` for a complete example.**

### 3. Generate the PRP

PRPs (Product Requirements Prompts) are comprehensive implementation blueprints that include:

- Complete context and documentation
- Implementation steps with validation
- Error handling patterns
- Test requirements

They are similar to PRDs (Product Requirements Documents) but are crafted more specifically to instruct an AI coding assistant.

Run in Claude Code:
```bash
/generate-prp INITIAL.md
```

**Note:** The slash commands are custom commands defined in `.claude/commands/`. You can view their implementation:
- `.claude/commands/generate-prp.md` - See how it researches and creates PRPs
- `.claude/commands/execute-prp.md` - See how it implements features from PRPs

The `$ARGUMENTS` variable in these commands receives whatever you pass after the command name (e.g., `INITIAL.md` or `PRPs/your-feature.md`).

This command will:
1. Read your feature request
2. Research the codebase for patterns
3. Search for relevant documentation
4. Create a comprehensive PRP in `PRPs/your-feature-name.md`

### 4. Execute the PRP

Once generated, execute the PRP to implement your feature:

```bash
/execute-prp PRPs/your-feature-name.md
```

The AI coding assistant will:
1. Read all context from the PRP
2. Create a detailed implementation plan
3. Execute each step with validation
4. Run tests and fix any issues
5. Ensure all success criteria are met

## Writing Effective INITIAL.md Files

### Key Sections Explained

**FEATURE**: Be specific and comprehensive
- ❌ "Build a web scraper"
- ✅ "Build an async web scraper using BeautifulSoup that extracts product data from e-commerce sites, handles rate limiting, and stores results in PostgreSQL"

**EXAMPLES**: Leverage the examples/ folder
- Place relevant code patterns in `examples/`
- Reference specific files and patterns to follow
- Explain what aspects should be mimicked

**DOCUMENTATION**: Include all relevant resources
- API documentation URLs
- Library guides
- MCP server documentation
- Database schemas

**OTHER CONSIDERATIONS**: Capture important details
- Authentication requirements
- Rate limits or quotas
- Common pitfalls
- Performance requirements

## The PRP Workflow

### How /generate-prp Works

The command follows this process:

1. **Research Phase**
   - Analyzes your codebase for patterns
   - Searches for similar implementations
   - Identifies conventions to follow

2. **Documentation Gathering**
   - Fetches relevant API docs
   - Includes library documentation
   - Adds gotchas and quirks

3. **Blueprint Creation**
   - Creates step-by-step implementation plan
   - Includes validation gates
   - Adds test requirements

4. **Quality Check**
   - Scores confidence level (1-10)
   - Ensures all context is included

### How /execute-prp Works

1. **Load Context**: Reads the entire PRP
2. **Plan**: Creates detailed task list using TodoWrite
3. **Execute**: Implements each component
4. **Validate**: Runs tests and linting
5. **Iterate**: Fixes any issues found
6. **Complete**: Ensures all requirements met

See `PRPs/EXAMPLE_multi_agent_prp.md` for a complete example of what gets generated.

## Using Examples Effectively

The `examples/` folder is **critical** for success. AI coding assistants perform much better when they can see patterns to follow.

### What to Include in Examples

1. **Code Structure Patterns**
   - How you organize modules
   - Import conventions
   - Class/function patterns

2. **Testing Patterns**
   - Test file structure
   - Mocking approaches
   - Assertion styles

3. **Integration Patterns**
   - API client implementations
   - Database connections
   - Authentication flows

4. **CLI Patterns**
   - Argument parsing
   - Output formatting
   - Error handling

### Example Structure

```
examples/
├── README.md           # Explains what each example demonstrates
├── cli.py             # CLI implementation pattern
├── agent/             # Agent architecture patterns
│   ├── agent.py      # Agent creation pattern
│   ├── tools.py      # Tool implementation pattern
│   └── providers.py  # Multi-provider pattern
└── tests/            # Testing patterns
    ├── test_agent.py # Unit test patterns
    └── conftest.py   # Pytest configuration
```

## Best Practices

### 1. Be Explicit in INITIAL.md
- Don't assume the AI knows your preferences
- Include specific requirements and constraints
- Reference examples liberally

### 2. Provide Comprehensive Examples
- More examples = better implementations
- Show both what to do AND what not to do
- Include error handling patterns

### 3. Use Validation Gates
- PRPs include test commands that must pass
- AI will iterate until all validations succeed
- This ensures working code on first try

### 4. Leverage Documentation
- Include official API docs
- Add MCP server resources
- Reference specific documentation sections

### 5. Customize CLAUDE.md
- Add your conventions
- Include project-specific rules
- Define coding standards

## Resources

- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Context Engineering Best Practices](https://www.philschmid.de/context-engineering)