name: "E-commerce API Multi-Agent System"
description: |
  ## Purpose
  Build a comprehensive e-commerce backend API system using a multi-agent architecture
  to handle complex business workflows with high reliability and scalability.
  
  ## Core Principles
  - Multi-agent coordination for complex business logic
  - Microservices-ready architecture
  - Production-grade security and monitoring
  - Event-driven communication between agents
  - Automated testing and quality assurance

# E-commerce API Multi-Agent System

## Goal
Create a production-ready e-commerce backend API system that uses multiple specialized agents to handle different aspects of the business logic including user management, product catalog, inventory, orders, payments, and notifications. The system should be scalable, secure, and maintainable with comprehensive testing and monitoring.

## Why
- **Business value**: Enables rapid development of complex e-commerce features through agent specialization
- **Technical need**: Handles complex business workflows that require coordination between multiple domains
- **Scalability**: Agent-based architecture allows independent scaling of different business functions
- **Maintainability**: Clear separation of concerns through specialized agents
- **Problems solved**: 
  - Complex order processing workflows
  - Real-time inventory management
  - Payment processing coordination
  - Multi-channel notification delivery
  - User authentication and authorization

## What
A CLI-based multi-agent system where:

### Core Agents
1. **User Agent**: Handles authentication, authorization, user profiles, and preferences
2. **Product Agent**: Manages product catalog, categories, search, and recommendations
3. **Inventory Agent**: Tracks stock levels, reservations, and warehouse management
4. **Order Agent**: Processes orders, manages order lifecycle, and coordinates with other agents
5. **Payment Agent**: Handles payment processing, refunds, and financial transactions
6. **Notification Agent**: Sends emails, SMS, push notifications across multiple channels
7. **Analytics Agent**: Collects metrics, generates reports, and provides business insights

### Agent Interactions
- Order Agent coordinates with Inventory Agent for stock checks
- Payment Agent communicates with Order Agent for payment confirmation
- Notification Agent receives events from all other agents
- Analytics Agent monitors all agent activities
- User Agent provides authentication context to all agents

### Key Features
- RESTful API endpoints for each business domain
- Real-time inventory updates and stock reservations
- Multi-step order processing with rollback capabilities
- Integrated payment gateway support (Stripe, PayPal)
- Multi-channel notification system (email, SMS, push)
- Comprehensive audit logging and analytics
- Rate limiting and security controls
- Automated testing and CI/CD pipeline

## Success Criteria
- [ ] All 7 agents are implemented and functional
- [ ] User Agent successfully handles JWT authentication and authorization
- [ ] Product Agent provides fast search and recommendation capabilities
- [ ] Inventory Agent maintains accurate stock levels with real-time updates
- [ ] Order Agent processes complete order workflows with proper error handling
- [ ] Payment Agent integrates with at least 2 payment providers
- [ ] Notification Agent delivers messages via email, SMS, and push notifications
- [ ] Analytics Agent generates real-time dashboards and reports
- [ ] System handles 1000+ concurrent users with <200ms response time
- [ ] All agents communicate via event-driven architecture
- [ ] Comprehensive test coverage >90% for all agents
- [ ] Production deployment with monitoring and alerting
- [ ] Security audit passes with no critical vulnerabilities
- [ ] API documentation is complete and up-to-date

## All Needed Context

### Documentation & References
```yaml
- url: https://docs.pydantic.dev/latest/concepts/agents/
  why: Primary framework for building the multi-agent system
- url: https://fastapi.tiangolo.com/
  why: REST API framework for exposing agent capabilities
- url: https://docs.celery.dev/
  why: Task queue for handling asynchronous agent communications
- url: https://redis.io/docs/
  why: Message broker and caching layer for agent coordination
- url: https://www.postgresql.org/docs/
  why: Primary database for persistent data storage
- url: https://stripe.com/docs/api
  why: Payment processing integration
- url: https://docs.aws.amazon.com/ses/
  why: Email notification service
```

### Technical Requirements

#### Programming Languages & Frameworks
- **Python 3.11+**: Primary development language
- **Pydantic AI**: Multi-agent framework and coordination
- **FastAPI**: REST API framework with automatic OpenAPI documentation
- **SQLAlchemy**: ORM for database operations
- **Alembic**: Database migration management

#### Databases & Storage
- **PostgreSQL 15+**: Primary relational database
- **Redis 7+**: Caching, session storage, and message broker
- **Elasticsearch**: Product search and analytics
- **AWS S3**: File storage for product images and documents

#### Infrastructure & Deployment
- **Docker**: Containerization for all services
- **Kubernetes**: Container orchestration and scaling
- **AWS EKS**: Managed Kubernetes service
- **AWS RDS**: Managed PostgreSQL database
- **AWS ElastiCache**: Managed Redis service
- **AWS Application Load Balancer**: Traffic distribution

#### External Integrations
- **Stripe API**: Primary payment processor
- **PayPal API**: Secondary payment processor
- **AWS SES**: Email notifications
- **Twilio**: SMS notifications
- **Firebase**: Push notifications
- **Brave Search API**: Product recommendation enhancement

#### Development Tools
- **pytest**: Testing framework with fixtures and mocking
- **black**: Code formatting
- **ruff**: Linting and code quality
- **mypy**: Static type checking
- **pre-commit**: Git hooks for code quality
- **GitHub Actions**: CI/CD pipeline

### Implementation Details

#### Agent Architecture
```python
# Each agent follows this pattern
class BaseAgent:
    def __init__(self, dependencies: AgentDependencies):
        self.db = dependencies.db
        self.cache = dependencies.cache
        self.event_bus = dependencies.event_bus
    
    async def handle_request(self, request: RequestModel) -> ResponseModel:
        # Agent-specific business logic
        pass
    
    async def handle_event(self, event: EventModel) -> None:
        # React to events from other agents
        pass
```

#### Event-Driven Communication
- All agents communicate via Redis-based event bus
- Events are typed using Pydantic models
- Automatic retry and dead letter queue handling
- Event sourcing for audit trails

#### Security Implementation
- JWT-based authentication with refresh tokens
- Role-based access control (RBAC)
- API rate limiting per user and endpoint
- Input validation and sanitization
- SQL injection prevention via ORM
- HTTPS enforcement and security headers

#### Performance Requirements
- API response time: <200ms for 95% of requests
- Database query optimization with proper indexing
- Redis caching for frequently accessed data
- Connection pooling for database and external APIs
- Horizontal scaling capability via Kubernetes

### Validation Gates

#### Development Phase
- [ ] Code review approval from 2+ team members
- [ ] All unit tests pass with >90% coverage
- [ ] Integration tests pass for agent interactions
- [ ] Static analysis (mypy, ruff) passes with no errors
- [ ] Security scan passes with no critical issues

#### Testing Phase
- [ ] Load testing handles 1000+ concurrent users
- [ ] End-to-end testing covers all user workflows
- [ ] Payment processing tested with test transactions
- [ ] Notification delivery tested across all channels
- [ ] Database migration testing in staging environment

#### Deployment Phase
- [ ] Staging deployment successful with full feature testing
- [ ] Production deployment with zero-downtime strategy
- [ ] Monitoring and alerting configured and tested
- [ ] Backup and disaster recovery procedures verified
- [ ] Performance monitoring shows acceptable metrics

#### Post-Deployment
- [ ] 24-hour monitoring shows stable performance
- [ ] User acceptance testing completed successfully
- [ ] Documentation updated and published
- [ ] Team training completed for maintenance procedures

### Constraints & Considerations

#### Timeline
- **Development**: 12 weeks
- **Testing**: 3 weeks  
- **Deployment**: 1 week
- **Total**: 16 weeks

#### Team Structure
- **Team size**: 6 developers (2 senior, 4 mid-level)
- **Roles**: Tech lead, backend developers, DevOps engineer, QA engineer
- **Methodology**: Agile with 2-week sprints

#### Quality Requirements
- **Level**: Production-grade enterprise system
- **Availability**: 99.9% uptime SLA
- **Security**: SOC 2 compliance required
- **Performance**: Sub-200ms response time for 95% of requests
- **Scalability**: Handle 10x traffic growth without architecture changes

#### Budget & Resources
- **Infrastructure**: AWS cloud services with auto-scaling
- **External services**: Stripe, Twilio, AWS SES subscriptions
- **Development tools**: GitHub Enterprise, monitoring tools
- **Compliance**: Security audit and penetration testing

#### Risk Mitigation
- **Technical risks**: Comprehensive testing and staging environment
- **Integration risks**: Mock services for external API testing
- **Performance risks**: Load testing and performance monitoring
- **Security risks**: Regular security audits and vulnerability scanning
