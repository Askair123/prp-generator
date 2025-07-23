## FEATURE:

Build an async web scraper using BeautifulSoup that extracts product data from e-commerce sites, handles rate limiting, and stores results in PostgreSQL. The scraper should support multiple sites, respect robots.txt, and provide real-time progress updates.

## EXAMPLES:

- `examples/async_client.py` - shows how to structure async HTTP clients with proper session management
- `examples/database/models.py` - demonstrates SQLAlchemy model patterns and relationships
- `examples/rate_limiter.py` - shows implementation of token bucket rate limiting
- `examples/config/settings.py` - configuration management with environment variables

## DOCUMENTATION:

- BeautifulSoup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- aiohttp client documentation: https://docs.aiohttp.org/en/stable/client.html
- SQLAlchemy async documentation: https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
- robots.txt parser: https://github.com/python/cpython/blob/main/Lib/urllib/robotparser.py

## OTHER CONSIDERATIONS:

- Must respect rate limits (max 1 request per second per domain)
- Handle dynamic content loading with JavaScript (consider playwright for SPA sites)
- Implement retry logic with exponential backoff for failed requests
- Store raw HTML and parsed data separately for debugging
- Add comprehensive logging for monitoring scraping progress
- Include data validation to ensure extracted data quality
- Handle different product page structures across sites
- Implement graceful shutdown to avoid leaving incomplete data
