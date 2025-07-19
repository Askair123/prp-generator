## FEATURE:

Build a real-time chat application using FastAPI and WebSockets that supports multiple chat rooms, user authentication with JWT tokens, message persistence in PostgreSQL, and real-time notifications. The application should handle user presence (online/offline status), message history, and support file uploads for images.

## EXAMPLES:

- `examples/websocket_chat.py` - demonstrates WebSocket connection handling and message broadcasting
- `examples/jwt_auth.py` - shows JWT token generation and validation patterns
- `examples/database/chat_models.py` - SQLAlchemy models for chat rooms, messages, and users
- `examples/file_upload.py` - file upload handling with validation and storage
- `examples/async_postgres.py` - async PostgreSQL connection and query patterns

## DOCUMENTATION:

- FastAPI WebSockets: https://fastapi.tiangolo.com/advanced/websockets/
- SQLAlchemy Async: https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
- JWT with FastAPI: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
- PostgreSQL asyncpg: https://magicstack.github.io/asyncpg/current/
- WebSocket client testing: https://fastapi.tiangolo.com/advanced/testing-websockets/

## OTHER CONSIDERATIONS:

- Implement connection pooling for PostgreSQL to handle concurrent users
- Add rate limiting to prevent spam messages (max 10 messages per minute per user)
- Handle WebSocket disconnections gracefully and clean up user presence
- Implement message encryption for sensitive conversations
- Add comprehensive logging for debugging connection issues
- Support message reactions (like, dislike) and message threading
- Implement user roles (admin, moderator, regular user) with different permissions
- Add message search functionality with full-text search
- Handle file upload size limits (max 10MB) and validate file types
- Implement message delivery status (sent, delivered, read)
- Add typing indicators when users are composing messages
- Support message editing and deletion with audit trail
