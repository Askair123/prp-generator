## FEATURE:

创建一个Coordinator Pattern系统，用于分析软件开发项目需求并生成Claude Flow配置。该系统应该能够：

- 接收自然语言的项目描述
- 分析项目的技术栈、复杂度、团队规模等维度
- 从预定义的协调模式库中选择最适合的模式
- 生成完整的Claude Flow配置文件
- 执行一次性交接后优雅退出

具体场景：用户描述一个"构建电商网站后台API"的项目，系统应该分析出这是一个中等复杂度的Web开发项目，推荐层次化协调模式，并生成包含架构师Agent、后端开发Agent、数据库设计Agent、测试Agent等的Claude Flow配置。

## EXAMPLES:

参考 `examples/` 文件夹中的现有示例：
- `examples/cli.py` - CLI交互模式的实现参考
- `examples/agent/` - Agent架构和工具集成的最佳实践
- `PRPs/EXAMPLE_multi_agent_prp.md` - 多Agent系统的PRP示例

同时参考我们已有的文档：
- `docs/architecture/refactored-architecture-implementation.md` - 架构设计指导
- `docs/guides/linear-mcp-guide-for-llm.md` - 工具集成参考

## DOCUMENTATION:

核心技术文档：
- Pydantic AI: https://ai.pydantic.dev/
- Claude Flow架构参考：我们的docs目录中的相关文档
- Context Engineering方法论：当前项目的README.md和相关文档

## OTHER CONSIDERATIONS:

- 使用我们定制化的PRP模板 `PRPs/templates/coordinator/coordinator_prp_base.md`
- 遵循CLAUDE.md中定义的Coordinator Pattern特定规则
- 实现应该包含完整的项目分析引擎、模式库、PRP生成器等核心组件
- 包含丰富的验证门控，确保生成的Claude Flow配置的有效性
- 设计清晰的一次性交接机制
- 提供详细的使用文档和示例
- 考虑扩展性，支持自定义协调模式和最佳实践
- 包含错误处理和边界情况的处理
- 设计合理的配置文件格式和数据模型

项目结构应该遵循我们在COORDINATOR_PROJECT_SETUP.md中定义的架构。
