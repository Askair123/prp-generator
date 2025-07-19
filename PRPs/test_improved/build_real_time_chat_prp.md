name: "Base PRP Template v2 - Context-Rich with Validation Loops"
description: |

## Purpose
Template optimized for AI agents to implement features with sufficient context and self-validation capabilities to achieve working code through iterative refinement.

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

### Documentation & References (list all context needed to implement the feature)
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

### Current Codebase tree (run `tree` in the root of the project) to get an overview of the codebase
```bash

```

### Desired Codebase tree with files to be added and responsibility of file
```bash

```

### Known Gotchas of our codebase & Library Quirks
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

Create the core data models, we ensure type safety and consistency.
```python
Examples: 
 - orm models
 - pydantic models
 - pydantic schemas
 - pydantic validators

```

### list of tasks to be completed to fullfill the PRP in the order they should be completed

```yaml
Task 1:
MODIFY src/existing_module.py:
  - FIND pattern: "class OldImplementation"
  - INJECT after line containing "def __init__"
  - PRESERVE existing method signatures

CREATE src/new_feature.py:
  - MIRROR pattern from: src/similar_feature.py
  - MODIFY class name and core logic
  - KEEP error handling pattern identical

...(...)

Task N:
...

```


### Per task pseudocode as needed added to each task
```python

# Task 1
# Pseudocode with CRITICAL details dont write entire code
async def new_feature(param: str) -> Result:
    # PATTERN: Always validate input first (see src/validators.py)
    validated = validate_input(param)  # raises ValidationError
    
    # GOTCHA: This library requires connection pooling
    async with get_connection() as conn:  # see src/db/pool.py
        # PATTERN: Use existing retry decorator
        @retry(attempts=3, backoff=exponential)
        async def _inner():
            # CRITICAL: API returns 429 if >10 req/sec
            await rate_limiter.acquire()
            return await external_api.call(validated)
        
        result = await _inner()
    
    # PATTERN: Standardized response format
    return format_response(result)  # see src/utils/responses.py
```

### Integration Points
```yaml
DATABASE:
  - migration: "Add column 'feature_enabled' to users table"
  - index: "CREATE INDEX idx_feature_lookup ON users(feature_id)"
  
CONFIG:
  - add to: config/settings.py
  - pattern: "FEATURE_TIMEOUT = int(os.getenv('FEATURE_TIMEOUT', '30'))"
  
ROUTES:
  - add to: src/api/routes.py  
  - pattern: "router.include_router(feature_router, prefix='/feature')"
```

## Validation Loop

### Level 1: Syntax & Style
```bash
# Run these FIRST - fix any errors before proceeding
ruff check src/new_feature.py --fix  # Auto-fix what's possible
mypy src/new_feature.py              # Type checking

# Expected: No errors. If errors, READ the error and fix.
```

### Level 2: Unit Tests each new feature/file/function use existing test patterns
```python
# CREATE test_new_feature.py with these test cases:
def test_happy_path():
    """Basic functionality works"""
    result = new_feature("valid_input")
    assert result.status == "success"

def test_validation_error():
    """Invalid input raises ValidationError"""
    with pytest.raises(ValidationError):
        new_feature("")

def test_external_api_timeout():
    """Handles timeouts gracefully"""
    with mock.patch('external_api.call', side_effect=TimeoutError):
        result = new_feature("valid")
        assert result.status == "error"
        assert "timeout" in result.message
```

```bash
# Run and iterate until passing:
uv run pytest test_new_feature.py -v
# If failing: Read error, understand root cause, fix code, re-run (never mock to pass)
```

### Level 3: Integration Test
```bash
# Start the service
uv run python -m src.main --dev

# Test the endpoint
curl -X POST http://localhost:8000/feature \
  -H "Content-Type: application/json" \
  -d '{"param": "test_value"}'

# Expected: {"status": "success", "data": {...}}
# If error: Check logs at logs/app.log for stack trace
```

## Final validation Checklist
- [ ] All tests pass: `uv run pytest tests/ -v`
- [ ] No linting errors: `uv run ruff check src/`
- [ ] No type errors: `uv run mypy src/`
- [ ] Manual test successful: [specific curl/command]
- [ ] Error cases handled gracefully
- [ ] Logs are informative but not verbose
- [ ] Documentation updated if needed

---

## Anti-Patterns to Avoid
- ❌ Don't create new patterns when existing ones work
- ❌ Don't skip validation because "it should work"  
- ❌ Don't ignore failing tests - fix them
- ❌ Don't use sync functions in async context
- ❌ Don't hardcode values that should be config
- ❌ Don't catch all exceptions - be specific