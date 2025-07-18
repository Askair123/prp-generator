# Linear MCP 使用指南 - LLM Agent 版本

## 🎯 核心概念

Linear MCP 是一个用于与 Linear 项目管理工具交互的 MCP 工具。它允许 LLM Agent 执行工单管理、状态更新、评论添加等操作。

## 🔧 工具调用格式

```javascript
// 基本调用结构
{
  "name": "linear",
  "parameters": {
    "summary": "简短的操作描述",
    "query": "详细的操作指令",
    "is_read_only": true/false  // true=只读，false=可写
  }
}
```

## 📋 常用操作模式

### 1. 查询操作 (is_read_only: true)

#### 获取用户信息和团队
```javascript
{
  "summary": "Get user and team information",
  "query": "Get my user information and list all teams I have access to",
  "is_read_only": true
}
```

#### 查询工单列表
```javascript
{
  "summary": "Get recent issues assigned to me",
  "query": "Show me the most recent 10 issues assigned to me with their titles, states, and descriptions",
  "is_read_only": true
}
```

#### 搜索特定工单
```javascript
{
  "summary": "Search for issues by keyword",
  "query": "Find all issues containing 'API' in title or description",
  "is_read_only": true
}
```

#### 获取特定工单详情
```javascript
{
  "summary": "Get issue details",
  "query": "Get full details for issue CLA-17 including comments and history",
  "is_read_only": true
}
```

### 2. 创建操作 (is_read_only: false)

#### 创建新工单
```javascript
{
  "summary": "Create new issue",
  "query": "Create a new issue with title 'Fix API bug' and description 'The API endpoint returns 500 error when processing large requests'",
  "is_read_only": false
}
```

#### 创建带标签的工单
```javascript
{
  "summary": "Create issue with labels",
  "query": "Create issue titled 'Database optimization' with description 'Improve query performance' and add labels 'backend' and 'performance'",
  "is_read_only": false
}
```

### 3. 更新操作 (is_read_only: false)

#### 更新工单状态
```javascript
{
  "summary": "Update issue status",
  "query": "Update issue CLA-22 to 'In Progress' state",
  "is_read_only": false
}
```

#### 分配工单
```javascript
{
  "summary": "Assign issue to user",
  "query": "Assign issue CLA-15 to user with email 'developer@company.com'",
  "is_read_only": false
}
```

#### 更新工单内容
```javascript
{
  "summary": "Update issue details",
  "query": "Update issue CLA-10 title to 'Updated Task Title' and add description 'New detailed description'",
  "is_read_only": false
}
```

### 4. 评论操作 (is_read_only: false)

#### 添加评论
```javascript
{
  "summary": "Add comment to issue",
  "query": "Add comment 'Work completed, ready for review' to issue CLA-18",
  "is_read_only": false
}
```

#### 添加进度更新
```javascript
{
  "summary": "Add progress update",
  "query": "Add comment to issue CLA-12: 'Progress update: 70% complete. API integration done, testing remaining.'",
  "is_read_only": false
}
```

## 🏷️ 重要的状态和ID

### 常见工单状态
- `Todo` / `Backlog` - 待办
- `In Progress` - 进行中  
- `In Review` - 审核中
- `Done` - 完成
- `Canceled` - 已取消

### 状态UUID映射 (示例)
```
Todo: 957c7243-06ca-4bb6-b01a-01915befa780
In Progress: c56134bd-4224-4a72-81ad-17de9690aacb  
In Review: 7a8fde25-b7d2-468b-8861-5440bea9baf8
Done: a71d3752-37df-4ad2-9dc6-a4b67a748eed
Backlog: ec59da7d-8ec3-409e-b679-dbdc61719cc5
```

## 💡 LLM Agent 最佳实践

### 1. 查询前先了解上下文
```javascript
// 总是先获取基本信息
{
  "summary": "Get context information",
  "query": "Get my user info, available teams, and recent issues to understand current context",
  "is_read_only": true
}
```

### 2. 使用描述性的 summary
- ✅ 好: "Create bug report for API timeout issue"
- ❌ 差: "Create issue"

### 3. 详细的 query 指令
- ✅ 好: "Create issue titled 'Fix login timeout' with description 'Users report 30-second timeout on login page' and assign to backend team"
- ❌ 差: "Create login issue"

### 4. 错误处理模式
```javascript
// 如果操作失败，先查询当前状态
{
  "summary": "Check current issue state before retry",
  "query": "Get current state and details for issue CLA-15 to understand why update failed",
  "is_read_only": true
}
```

## 🔍 响应数据结构理解

### 用户信息响应
```json
{
  "viewer": {
    "id": "user-uuid",
    "name": "User Name", 
    "email": "user@email.com",
    "teams": {
      "nodes": [
        {
          "id": "team-uuid",
          "name": "Team Name",
          "key": "TEAM",
          "states": {
            "nodes": [
              {"id": "state-uuid", "name": "Todo", "type": "unstarted"}
            ]
          }
        }
      ]
    }
  }
}
```

### 工单列表响应
```json
{
  "issues": {
    "nodes": [
      {
        "id": "issue-uuid",
        "identifier": "CLA-17",
        "title": "Issue Title",
        "description": "Issue Description",
        "state": {"name": "In Progress"},
        "url": "https://linear.app/team/issue/CLA-17/..."
      }
    ]
  }
}
```

## ⚠️ 注意事项

1. **UUID 要求**: 更新状态时必须使用正确的状态UUID，不能使用状态名称
2. **权限检查**: 确保有足够权限执行写操作
3. **团队上下文**: 操作前确认在正确的团队上下文中
4. **错误重试**: 如果操作失败，检查参数格式和权限

## 🚀 高级用法示例

### 批量操作工作流
```javascript
// 1. 查询待处理工单
{
  "summary": "Get pending issues",
  "query": "Get all issues in 'Todo' state assigned to me",
  "is_read_only": true
}

// 2. 批量更新状态
{
  "summary": "Start working on multiple issues", 
  "query": "Update issues CLA-10, CLA-11, CLA-12 to 'In Progress' state",
  "is_read_only": false
}

// 3. 添加批量进度报告
{
  "summary": "Add progress comments",
  "query": "Add comment 'Started working on this task' to issues CLA-10, CLA-11, CLA-12",
  "is_read_only": false
}
```

## 🎭 Agent 协作模式

### Multi-Agent 工作流示例
```javascript
// Coordinator Agent 创建主任务
{
  "summary": "Create main coordination task",
  "query": "Create issue 'Multi-Agent Market Analysis Project' with description including agent assignments and workflow steps",
  "is_read_only": false
}

// Research Agent 报告完成
{
  "summary": "Research agent reports completion",
  "query": "Add comment to issue CLA-20: '[Research Agent] Market data collection completed. Key findings: Market size $2.5B, Growth rate 15% YoY. Data uploaded to shared workspace.'",
  "is_read_only": false
}

// Analysis Agent 开始工作
{
  "summary": "Analysis agent starts work",
  "query": "Add comment to issue CLA-20: '[Analysis Agent] Starting competitive analysis based on research data. ETA: 2 hours.'",
  "is_read_only": false
}
```

## 📊 状态管理策略

### Agent 状态报告模板
```javascript
{
  "summary": "Agent status update",
  "query": "Add comment to issue CLA-15: '[Agent Type: Research] Status: IN_PROGRESS | Progress: 60% | Current Task: Data validation | Next: Report generation | ETA: 30min'",
  "is_read_only": false
}
```

### 依赖关系管理
```javascript
{
  "summary": "Update dependency status",
  "query": "Add comment to issue CLA-18: '[Dependency Update] Waiting for CLA-17 completion. Research Agent output required before proceeding with analysis phase.'",
  "is_read_only": false
}
```

## 🔄 工作流自动化模式

### 任务完成检查点
```javascript
// 检查前置条件
{
  "summary": "Check prerequisites",
  "query": "Get status of issues CLA-15, CLA-16, CLA-17 to verify all dependencies are completed before starting CLA-18",
  "is_read_only": true
}

// 自动状态转换
{
  "summary": "Auto-transition based on dependencies",
  "query": "If all dependency issues (CLA-15, CLA-16, CLA-17) are in 'Done' state, update CLA-18 to 'In Progress' and add comment 'All dependencies satisfied, starting execution'",
  "is_read_only": false
}
```

## 🏗️ 项目结构化管理

### 创建项目层次结构
```javascript
// 主项目工单
{
  "summary": "Create main project issue",
  "query": "Create issue '[PROJECT] AI Agent Documentation System' with comprehensive description including scope, timeline, and deliverables",
  "is_read_only": false
}

// 子任务创建
{
  "summary": "Create subtasks",
  "query": "Create issues for subtasks: '[RESEARCH] Technology Stack Analysis', '[DESIGN] Architecture Planning', '[IMPLEMENT] Core Features', '[TEST] Quality Assurance'",
  "is_read_only": false
}
```

## 🎯 查询优化技巧

### 高效数据获取
```javascript
// 获取完整上下文
{
  "summary": "Get comprehensive project status",
  "query": "Get all issues with prefix '[PROJECT]' including their current states, assignees, recent comments, and completion percentage",
  "is_read_only": true
}

// 过滤特定信息
{
  "summary": "Get issues by criteria",
  "query": "Find all issues assigned to me that are in 'In Progress' state and were updated in the last 24 hours",
  "is_read_only": true
}
```

## 🚨 错误处理和调试

### 常见错误及解决方案

#### 1. UUID 错误
```
错误: "stateId must be a UUID"
解决: 使用完整的UUID而不是状态名称
```

#### 2. 权限错误
```javascript
// 检查权限
{
  "summary": "Check user permissions",
  "query": "Get my user permissions and team access levels to understand what operations I can perform",
  "is_read_only": true
}
```

#### 3. 工单不存在
```javascript
// 验证工单存在
{
  "summary": "Verify issue exists",
  "query": "Check if issue CLA-25 exists and get its current status before attempting updates",
  "is_read_only": true
}
```

## 📈 性能优化建议

### 1. 批量操作
- 尽可能在单个查询中处理多个相关操作
- 避免频繁的单个工单查询

### 2. 缓存策略
- 缓存团队信息和状态UUID映射
- 避免重复查询相同的基础数据

### 3. 查询优化
- 使用具体的过滤条件减少返回数据量
- 只请求需要的字段信息

## 🔐 安全最佳实践

### 1. 数据验证
```javascript
// 验证输入数据
{
  "summary": "Validate before update",
  "query": "Before updating issue CLA-20, verify it exists and I have write permissions",
  "is_read_only": true
}
```

### 2. 操作确认
```javascript
// 重要操作前确认
{
  "summary": "Confirm before deletion",
  "query": "Get full details of issue CLA-19 to confirm it's safe to delete/cancel",
  "is_read_only": true
}
```

---

## 📚 快速参考卡片

### 必记命令模板
```javascript
// 查询我的工单
{"summary": "Get my issues", "query": "Get all issues assigned to me", "is_read_only": true}

// 创建工单
{"summary": "Create issue", "query": "Create issue 'Title' with description 'Description'", "is_read_only": false}

// 更新状态
{"summary": "Update status", "query": "Update issue CLA-X to 'In Progress' state", "is_read_only": false}

// 添加评论
{"summary": "Add comment", "query": "Add comment 'Message' to issue CLA-X", "is_read_only": false}
```

### 状态转换流程
```
Todo → In Progress → In Review → Done
  ↓         ↓           ↓
Backlog   Canceled   Canceled
```

---

**记住**: Linear MCP 是一个强大的项目管理工具，合理使用可以大大提高工作效率！

**提示**: 始终先用 `is_read_only: true` 查询了解当前状态，再执行写操作。

---

## 🌟 实际应用案例和最佳实践

### 案例1: n8n工作流自动化集成

基于n8n平台的Linear MCP服务器实现，支持完整的工单生命周期管理：

```javascript
// n8n MCP服务器配置示例
{
  "mcpServers": {
    "linear-automation": {
      "command": "npx",
      "args": ["-y", "linear-mcp-server"],
      "env": {
        "LINEAR_API_KEY": "$LINEAR_TOKEN",
        "TEAM_ID": "your-team-id"
      }
    }
  }
}
```

**工作流示例**:
```javascript
// 1. 自动创建工单
{
  "summary": "Auto-create issue from bug report",
  "query": "Create issue 'Bug: Login timeout after 30 seconds' with description 'Users report timeout issues on login page. Priority: High. Assign to backend team.'",
  "is_read_only": false
}

// 2. 批量状态更新
{
  "summary": "Batch update sprint issues",
  "query": "Update all issues with label 'sprint-current' to 'In Progress' state and add comment 'Sprint started - work in progress'",
  "is_read_only": false
}
```

### 案例2: Glue AI团队协作配置

Glue AI平台的Linear MCP集成，展示了企业级团队管理的最佳实践：

**团队规则配置**:
```yaml
# Glue AI Linear MCP 规则示例
- Web (WEB) team ID: ABC-123
- API (API) team ID: DEF-456
- Glue (GLU) team ID: GHI-789

When creating issues:
- Infer the teamId from context:
  - For issues relating to the API, glue-api, or Glue AI, use the API Team ID
  - For issues relating to the native app, client, or glue-web, use the Web Team ID
  - If you do not know, always default to the Glue (GLUE) Team ID
- Add detailed description in the `description` param, using Markdown where helpful
- Issue priority should be 3 (Normal) unless otherwise specified
```

**智能工单分配**:
```javascript
{
  "summary": "Smart issue assignment based on context",
  "query": "Create issue 'API rate limiting implementation' and automatically assign to API team (DEF-456) with priority 2 (High)",
  "is_read_only": false
}
```

### 案例3: Claude Code开发工作流

针对Claude Code用户的Linear MCP集成模式：

**开发任务管理**:
```javascript
// 代码审查工单创建
{
  "summary": "Create code review issue",
  "query": "Create issue 'Code Review: User Authentication Module' with description '## Files Changed\n- auth.py\n- user_model.py\n- tests/test_auth.py\n\n## Review Points\n- Security validation\n- Error handling\n- Test coverage' and assign to senior developer",
  "is_read_only": false
}

// 自动化测试结果报告
{
  "summary": "Report test results to Linear",
  "query": "Add comment to issue CLA-25: '## Test Results ✅\n- Unit tests: 98% coverage\n- Integration tests: All passed\n- Performance tests: Response time < 200ms\n\nReady for production deployment.'",
  "is_read_only": false
}
```

### 案例4: 多Agent协作系统

展示多个AI Agent如何通过Linear MCP协调工作：

**Coordinator Agent模式**:
```javascript
// 主协调器创建项目
{
  "summary": "Coordinator creates main project",
  "query": "Create issue '[PROJECT] Multi-Agent Documentation System' with description '## Agent Assignments\n- Research Agent: Market analysis (CLA-101)\n- Writing Agent: Content creation (CLA-102)\n- Review Agent: Quality assurance (CLA-103)\n- Integration Agent: System integration (CLA-104)\n\n## Timeline: 2 weeks\n## Dependencies: Research → Writing → Review → Integration'",
  "is_read_only": false
}

// Research Agent报告进度
{
  "summary": "Research agent progress update",
  "query": "Add comment to CLA-101: '[Research Agent] 📊 Progress Update\n- Status: 75% Complete\n- Completed: Market size analysis, competitor research\n- Current: Technology trend analysis\n- Next: Final report compilation\n- ETA: 2 hours\n- Blockers: None'",
  "is_read_only": false
}
```

**Agent间依赖管理**:
```javascript
// 检查依赖状态
{
  "summary": "Check dependency completion",
  "query": "Get status of issues CLA-101, CLA-102 to verify Research and Writing phases are complete before starting Review phase CLA-103",
  "is_read_only": true
}

// 自动触发下一阶段
{
  "summary": "Auto-trigger next phase",
  "query": "If CLA-101 and CLA-102 are both in 'Done' state, update CLA-103 to 'In Progress' and add comment '[Review Agent] Starting quality assurance phase. All dependencies satisfied.'",
  "is_read_only": false
}
```

## 🏢 企业级部署模式

### 远程MCP服务器配置

**官方托管服务器** (推荐):
```javascript
// Linear官方MCP服务器
{
  "mcpServers": {
    "linear-official": {
      "url": "https://mcp.linear.app/sse",
      "transport": "sse",
      "auth": {
        "type": "oauth",
        "scopes": ["read", "write"]
      }
    }
  }
}
```

### 本地MCP服务器部署

**使用mcp-proxy的stdio转换**:
```bash
# 安装依赖
brew install uv
uv tool install git+https://github.com/sparfenyuk/mcp-proxy

# 启动Linear MCP服务器
mcp-proxy --pass-environment --sse-port=9000 \
  npx @ibraheem4/linear-mcp

# 使用ngrok暴露服务
ngrok http 9000 --basic-auth="username:password"
```

**Glue兼容URL格式**:
```
https://username:password@random.ngrok-free.app/sse
```

## 🔒 安全和权限管理

### API密钥管理
```javascript
// 环境变量配置
{
  "env": {
    "LINEAR_API_KEY": "$LINEAR_TOKEN",
    "LINEAR_TEAM_ID": "$TEAM_ID",
    "LINEAR_WORKSPACE_ID": "$WORKSPACE_ID"
  }
}
```

### 权限验证模式
```javascript
// 操作前权限检查
{
  "summary": "Verify permissions before sensitive operation",
  "query": "Check if I have admin permissions for team ABC-123 before creating high-priority issues",
  "is_read_only": true
}
```

## 📊 监控和分析

### 工单分析查询
```javascript
// 团队效率分析
{
  "summary": "Analyze team productivity",
  "query": "Get all issues completed in the last 30 days, group by assignee, and calculate average completion time",
  "is_read_only": true
}

// 项目进度跟踪
{
  "summary": "Track project milestone progress",
  "query": "Find all issues with label 'milestone-v2.0' and show completion percentage by status",
  "is_read_only": true
}
```

### 自动化报告生成
```javascript
// 每周进度报告
{
  "summary": "Generate weekly progress report",
  "query": "Create weekly report comment on project issue CLA-100: '## Week 12 Progress\n- Completed: 15 issues\n- In Progress: 8 issues\n- Blocked: 2 issues\n- Team Velocity: 23 story points\n- Next Week Focus: API integration testing'",
  "is_read_only": false
}
```

## 🚀 高级集成模式

### 与CI/CD集成
```javascript
// 部署成功通知
{
  "summary": "Notify deployment success",
  "query": "Add comment to all issues with label 'deployed-v1.2.3': '🚀 Deployment Successful\n- Version: v1.2.3\n- Environment: Production\n- Deployed at: 2025-01-15 14:30 UTC\n- Status: All systems operational'",
  "is_read_only": false
}
```

### 与监控系统集成
```javascript
// 自动创建故障工单
{
  "summary": "Auto-create incident issue",
  "query": "Create high-priority issue 'INCIDENT: API Response Time > 5s' with description 'Alert triggered at 14:25 UTC. Affected endpoints: /api/users, /api/orders. Investigating root cause.' and assign to on-call engineer",
  "is_read_only": false
}
```

---

**记住**: Linear MCP 是一个强大的项目管理工具，合理使用可以大大提高工作效率！

**提示**: 始终先用 `is_read_only: true` 查询了解当前状态，再执行写操作。
