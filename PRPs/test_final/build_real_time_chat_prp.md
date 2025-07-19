name: "Generated PRP - Context-Rich with Validation Loops"
description: |

## Purpose
Generated PRP optimized for AI agents to implement features with sufficient context
and self-validation capabilities to achieve working code through iterative refinement.

## Core Principles
1. **Context is King**: Include ALL necessary documentation, examples, and caveats
2. **Validation Loops**: Provide executable tests/lints the AI can run and fix
3. **Information Dense**: Use keywords and patterns from the codebase
4. **Progressive Success**: Start simple, validate, then enhance
5. **Global rules**: Be sure to follow all rules in CLAUDE.md

---

## Goal
Implement Build a real-time chat application using FastAPI and WebSockets that supports multiple chat rooms, user authentication with JWT tokens, message persistence in PostgreSQL, and real-time notifications. The application should handle user presence (online/offline status), message history, and support file uploads for images.

## Why
- Addresses specific user requirements outlined in INITIAL.md
- Integrates with existing codebase patterns and conventions
- Provides value through automated implementation
- Addresses specific considerations and requirements

## What
Implementation of: Build a real-time chat application using FastAPI and WebSockets that supports multiple chat rooms, user authentication with JWT tokens, message persistence in PostgreSQL, and real-time notifications. The application should handle user presence (online/offline status), message history, and support file uploads for images.

Following patterns from:
- `examples/websocket_chat.py` - demonstrates WebSocket connection handling and message broadcasting
- `examples/jwt_auth.py` - shows JWT token generation and validation patterns
- `examples/database/chat_models.py` - SQLAlchemy models for chat rooms, messages, and users


### Success Criteria
- [ ] Feature implementation matches requirements
- [ ] All tests pass successfully
- [ ] Code follows existing patterns and conventions
- [ ] Documentation is complete and accurate
- [ ] All specific considerations are addressed

## All Needed Context

### Documentation & References
```yaml
- url: https://fastapi.tiangolo.com/advanced/websockets/
  why: FastAPI WebSockets:

- url: https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
  why: SQLAlchemy Async:

- url: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
  why: JWT with FastAPI:

- url: https://magicstack.github.io/asyncpg/current/
  why: PostgreSQL asyncpg:

- url: https://fastapi.tiangolo.com/advanced/testing-websockets/
  why: WebSocket client testing:

- file: `examples/websocket_chat.py` - demonstrates WebSocket connection handling and message broadcasting
  why: Pattern to follow from INITIAL.md

- file: `examples/jwt_auth.py` - shows JWT token generation and validation patterns
  why: Pattern to follow from INITIAL.md

- file: `examples/database/chat_models.py` - SQLAlchemy models for chat rooms, messages, and users
  why: Pattern to follow from INITIAL.md

- file: `examples/file_upload.py` - file upload handling with validation and storage
  why: Pattern to follow from INITIAL.md

- file: `examples/async_postgres.py` - async PostgreSQL connection and query patterns
  why: Pattern to follow from INITIAL.md

```

### Current Codebase tree
```bash
.
├── CLAUDE_FLOW_ALIGNMENT_ANALYSIS.md
├── CLAUDE_FLOW_KNOWLEDGE_INTEGRATION_REPORT.md
├── CLAUDE.md
├── COMPLETE_DOCUMENTATION_SYNC_REPORT.md
├── CONTEXT_ENGINEERING_ANALYSIS_REPORT.md
├── coordinator
│   ├── benchmarks
│   ├── claude_flow_adapter.py
│   ├── claude_flow_config_generator.py
│   ├── claude_flow_knowledge_base.py
│   ├── claude_flow_llm_docs.py
│   ├── cli.py
│   ├── context_manager.py
│   ├── contextual_knowledge_index.py
│   ├── docs
│   ├── enhanced_prp_processor.py
│   ├── initial_parser.py
│   ├── initial_to_prp_cli.py
│   ├── initial_to_prp_generator.py
│   ├── __init__.py
│   ├── models.py
│   ├── pattern_library.py
│   ├── project_analyzer.py
│   ├── prp_generator.py
│   ├── prp_parser.py
│   ├── README.md
│   ├── tests
│   │   └── test_integration.py
│   └── validators
├── COORDINATOR_IMPLEMENTATION_REPORT.md
├── COORDINATOR_PROJECT_SETUP.md
├── COORDINATOR_README.md
├── CORRECTED_ARCHITECTURE_REPORT.md
├── DEEP_DOCUMENTATION_SYSTEM_REPORT.md
├── demo_complete_documentation_sync.py
├── demo_context_engineering_comparison.py
├── demo_coordinator.py
├── demo_deep_documentation_system.py
├── demo_enhanced_workflow.py
├── demo_initial_to_prp_system.py
├── demo_knowledge_embedding_process.py
├── demo_knowledge_enhanced_system.py
├── demo_output
│   ├── claude_flow_config_20250718_151702.json
│   └── handoff_instructions_20250718_151702.md
├── demo_prp_driven_system.py
├── demo_standard_config.py
├── docs
│   ├── architecture
│   │   └── refactored-architecture-implementation.md
│   ├── DOCUMENT_CLEANUP_ANALYSIS.md
│   ├── DOCUMENT_COMPARISON_ANALYSIS.md
│   ├── guides
│   │   └── linear-mcp-guide-for-llm.md
│   ├── QUICK_NAVIGATION.md
│   └── README.md
├── DOCUMENTATION_SYNC_COMPLETION.md
├── examples
│   └── coordinator
├── FINAL_CLAUDE_FLOW_ALIGNMENT_REPORT.md
├── -home-thomas-dev-Context-Engineering-.txt
├── INITIAL_COORDINATOR_EXAMPLE.md
├── INITIAL_EXAMPLE.md
├── INITIAL.md
├── INITIAL_TO_PRP_IMPLEMENTATION_REPORT.md
├── KNOWLEDGE_EMBEDDING_DETAILED_ANALYSIS.md
├── knowledge_enhanced_output
│   └── claude-flow-knowledge-enhanced.config.json
├── LICENSE
├── prp_coordinator_output
│   └── claude-flow-coordinator-pattern-system.config.json
├── prp_multi_agent_output
│   └── claude-flow-EXAMPLE_multi_agent_prp.config.json
├── PRPs
│   ├── coordinator-pattern-system.md
│   ├── create_simple_rest_api_prp.md
│   ├── EXAMPLE_multi_agent_prp.md
│   ├── examples
│   ├── pydantic_agent_another_pydantic_prp.md
│   ├── templates
│   │   ├── coordinator
│   │   │   └── coordinator_prp_base.md
│   │   └── prp_base.md
│   ├── test
│   │   └── create_simple_rest_api_prp.md
│   ├── test_complete
│   │   └── build_real_time_chat_prp.md
│   └── test_improved
│       └── build_real_time_chat_prp.md
├── PRP_TEST_REPORT.md
├── README.md
├── standard_config_output
│   └── claude-flow.config.json
├── SYSTEM_OVERVIEW.md
├── test_initial_files
│   └── web_scraper_initial.md
├── TEST_INITIAL.md
├── test_output
│   └── claude-flow-ecommerce-test.config.json
├── test_prps
│   └── ecommerce-api-system.prp.md
├── test_prp_system.py
├── test_simple_initial.md
├── UPDATED_SYSTEM_OVERVIEW.md
├── use-cases
│   └── mcp-server
│       ├── CLAUDE.md
│       ├── examples
│       │   ├── database-tools-sentry.ts
│       │   └── database-tools.ts
│       ├── package.json
│       ├── package-lock.json
│       ├── PRPs
│       │   ├── ai_docs
│       │   │   ├── claude_api_usage.md
│       │   │   └── mcp_patterns.md
│       │   ├── INITIAL.md
│       │   ├── README.md
│       │   └── templates
│       │       └── prp_mcp_base.md
│       ├── README.md
│       ├── src
│       │   ├── auth
│       │   │   ├── github-handler.ts
│       │   │   └── oauth-utils.ts
│       │   ├── database
│       │   │   ├── connection.ts
│       │   │   ├── security.ts
│       │   │   └── utils.ts
│       │   ├── index_sentry.ts
│       │   ├── index.ts
│       │   ├── tools
│       │   │   └── register-tools.ts
│       │   └── types.ts
│       ├── tests
│       │   ├── fixtures
│       │   │   ├── auth.fixtures.ts
│       │   │   ├── database.fixtures.ts
│       │   │   └── mcp.fixtures.ts
│       │   ├── mocks
│       │   │   ├── crypto.mock.ts
│       │   │   ├── database.mock.ts
│       │   │   ├── github.mock.ts
│       │   │   └── oauth.mock.ts
│       │   ├── setup.ts
│       │   └── unit
│       │       ├── database
│       │       │   ├── security.test.ts
│       │       │   └── utils.test.ts
│       │       ├── tools
│       │       │   └── database-tools.test.ts
│       │       └── utils
│       │           └── response-helpers.test.ts
│       ├── tsconfig.json
│       ├── vitest.config.js
│       ├── worker-configuration.d.ts
│       └── wrangler.jsonc
└── WORKFLOW_ORCHESTRATION_ANALYSIS.md

43 directories, 116 files

```

### Desired Codebase tree with files to be added
```bash
.
├── build_real_time_chat/
│   ├── __init__.py
│   ├── main.py              # Main implementation
│   ├── models.py            # Data models
│   └── utils.py             # Utility functions
├── tests/
│   ├── __init__.py
│   └── test_build_real_time_chat.py  # Test suite
├── docs/
│   └── build_real_time_chat.md    # Documentation
└── requirements.txt         # Updated dependencies
```

### Known Gotchas & Library Quirks
```python
# CRITICAL: FastAPI requires async functions for endpoints that use await
# CRITICAL: SQLAlchemy async sessions require explicit commit/rollback
# GOTCHA: Forgetting to handle edge cases and error conditions
# GOTCHA: Not implementing proper logging for debugging
# GOTCHA: Hardcoding configuration values instead of using environment variables
# PATTERN: Uses asyncio for async operations
```

## Implementation Blueprint

### Data models and structure
Create the core data models for the chat application:

```python
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from typing import List, Optional
from datetime import datetime
from enum import Enum

Base = declarative_base()

# SQLAlchemy Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_online = Column(Boolean, default=False)
    last_seen = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)

class ChatRoom(Base):
    __tablename__ = "chat_rooms"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    room_id = Column(Integer, ForeignKey("chat_rooms.id"))
    message_type = Column(String(20), default="text")  # text, image, file
    file_url = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)

# Pydantic Models
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., regex=r'^[^@]+@[^@]+\.[^@]+$')
    password: str = Field(..., min_length=8)

class MessageCreate(BaseModel):
    content: str = Field(..., max_length=1000)
    room_id: int
    message_type: str = Field(default="text")

class WebSocketMessage(BaseModel):
    type: str  # "message", "join", "leave", "typing"
    room_id: int
    content: Optional[str] = None
    user_id: int
    timestamp: datetime = Field(default_factory=datetime.utcnow)
```

### List of tasks to be completed
```yaml
Task 1: Setup Project Structure
CREATE build_real_time_chat/__init__.py:
  - Basic package initialization
  - Export main classes and functions

Task 2: Database Models and Setup
CREATE build_real_time_chat/models.py:
  - PATTERN: Use SQLAlchemy async models
  - Define User, ChatRoom, Message models
  - Add proper relationships and constraints

CREATE build_real_time_chat/database.py:
  - PATTERN: Async database connection setup
  - Connection pooling configuration
  - Database session management

Task 3: Authentication System
CREATE build_real_time_chat/auth.py:
  - PATTERN: JWT token generation and validation
  - Password hashing with bcrypt
  - User registration and login endpoints

Task 4: WebSocket Connection Manager
CREATE build_real_time_chat/websocket_manager.py:
  - PATTERN: WebSocket connection management
  - Room-based message broadcasting
  - User presence tracking (online/offline)

Task 5: Chat API Endpoints
CREATE build_real_time_chat/chat_routes.py:
  - PATTERN: FastAPI router with dependency injection
  - CRUD operations for rooms and messages
  - Message history retrieval with pagination

Task 6: File Upload Handler
CREATE build_real_time_chat/file_handler.py:
  - PATTERN: Async file upload with validation
  - Image processing and storage
  - File type and size validation

Task 7: Real-time Features
CREATE build_real_time_chat/realtime.py:
  - PATTERN: WebSocket message handling
  - Typing indicators implementation
  - Message delivery status tracking

Task 8: Main Application
CREATE build_real_time_chat/main.py:
  - PATTERN: FastAPI application setup
  - WebSocket and HTTP route registration
  - Middleware configuration (CORS, auth)

Task 9: Comprehensive Tests
CREATE tests/test_build_real_time_chat.py:
  - PATTERN: Async test patterns with pytest-asyncio
  - WebSocket connection testing
  - Authentication flow testing
  - Database operations testing

Task 10: Documentation and Deployment
CREATE docs/build_real_time_chat.md:
  - API documentation with examples
  - WebSocket protocol documentation
  - Deployment and configuration guide
```

### Per task pseudocode
```python
# Main implementation pseudocode
async def main_feature_function(request: FeatureRequest) -> FeatureResponse:
    # PATTERN: Always validate input first
    validated_input = validate_request(request)

    # PATTERN: Use existing error handling patterns
    try:
        # Core processing logic
        result = await process_feature_request(validated_input)

        # PATTERN: Standardized response format
        return FeatureResponse(
            result=result,
            status="success",
            timestamp=datetime.now()
        )
    except ValidationError as e:
        # GOTCHA: Handle validation errors gracefully
        return FeatureResponse(
            result="",
            status="validation_error",
            error=str(e)
        )
    except Exception as e:
        # PATTERN: Log errors for debugging
        logger.error(f"Feature processing failed: {e}")
        return FeatureResponse(
            result="",
            status="error",
            error="Internal processing error"
        )
```

### Integration Points
```yaml
DATABASE:
  - add to: Database integration: models.py
  - pattern: Model registration and migrations
```

## Validation Loop

### Level 1: Syntax & Style
```bash
# Run these FIRST - fix any errors before proceeding
ruff check . --fix              # Auto-fix style issues
mypy .                          # Type checking

# Expected: No errors. If errors, READ and fix.
```

### Level 2: Unit Tests
```python
# test_build_real_time_chat.py
import pytest
from build_real_time_chat.main import main_feature_function
from build_real_time_chat.models import FeatureRequest, FeatureResponse

async def test_happy_path():
    """Test basic functionality works."""
    request = FeatureRequest(input_data="test_input")
    result = await main_feature_function(request)
    assert result.status == "success"
    assert result.result is not None

async def test_validation_error():
    """Test invalid input handling."""
    request = FeatureRequest(input_data="")
    result = await main_feature_function(request)
    assert result.status == "validation_error"

async def test_error_handling():
    """Test error handling."""
    # Test with mock that raises exception
    with pytest.raises(Exception):
        # Test error scenarios
        pass
```

```bash
# Run tests iteratively until passing:
pytest tests/ -v --cov=. --cov-report=term-missing

# If failing: Debug specific test, fix code, re-run
```

### Level 3: Integration Test
```bash
# Test the implementation end-to-end
python -m build_real_time_chat.main --test

# Expected: Feature works as intended
# If error: Check logs and debug step by step
```

## Final Validation Checklist
- [ ] All tests pass: `pytest tests/ -v`
- [ ] No linting errors: `ruff check .`
- [ ] No type errors: `mypy .`
- [ ] Feature works as specified in INITIAL.md
- [ ] Error cases handled gracefully
- [ ] Documentation is complete and accurate
- [ ] Code follows existing patterns and conventions

---

## Anti-Patterns to Avoid
- ❌ Don't create new patterns when existing ones work
- ❌ Don't skip validation because "it should work"
- ❌ Don't ignore failing tests - fix them
- ❌ Don't use sync functions in async context
- ❌ Don't hardcode values that should be config
- ❌ Don't catch all exceptions - be specific

## Confidence Score: 8/10

High confidence due to comprehensive context and validation loops.
