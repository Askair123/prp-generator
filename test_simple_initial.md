## FEATURE:

Create a simple REST API using FastAPI that manages a todo list. The API should support CRUD operations (Create, Read, Update, Delete) for todo items with fields: id, title, description, completed status, and created_at timestamp.

## EXAMPLES:

- `examples/fastapi_basic.py` - shows basic FastAPI application structure
- `examples/pydantic_models.py` - demonstrates Pydantic model patterns for data validation

## DOCUMENTATION:

- FastAPI documentation: https://fastapi.tiangolo.com/
- Pydantic documentation: https://docs.pydantic.dev/

## OTHER CONSIDERATIONS:

- Use SQLite database for simplicity
- Include proper error handling and HTTP status codes
- Add input validation using Pydantic models
- Include basic tests for all endpoints
