"""
Initial to PRP Generator for Coordinator Pattern System.

This module generates comprehensive PRPs from INITIAL.md files, following the
context-engineering-intro project patterns for one-pass implementation success.
"""

import re
import json
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path
import asyncio
from datetime import datetime

from .initial_parser import InitialParser, InitialAnalysis, CodebaseContext


@dataclass
class PRPGenerationConfig:
    """Configuration for PRP generation."""
    template_path: str = "PRPs/templates/prp_base.md"
    output_directory: str = "PRPs"
    include_research: bool = True
    include_validation: bool = True
    confidence_threshold: int = 7
    max_context_items: int = 10


@dataclass
class ResearchContext:
    """Research context for PRP generation."""
    external_documentation: List[Dict[str, str]]
    similar_implementations: List[str]
    best_practices: List[str]
    common_pitfalls: List[str]
    library_quirks: List[str]


@dataclass
class GeneratedPRP:
    """Generated PRP document with metadata."""
    content: str
    file_path: str
    confidence_score: int
    feature_name: str
    generation_timestamp: str
    research_context: ResearchContext
    validation_commands: List[str]


class InitialToPRPGenerator:
    """
    Generator for comprehensive PRPs from INITIAL.md files.
    
    This generator creates detailed implementation blueprints that enable
    AI agents to achieve one-pass implementation success through comprehensive
    context and validation loops, following context-engineering-intro patterns.
    """
    
    def __init__(self, config: Optional[PRPGenerationConfig] = None):
        """Initialize the PRP generator."""
        self.config = config or PRPGenerationConfig()
        self.initial_parser = InitialParser()
        # Always use embedded template for consistency
        self.prp_template = self._get_embedded_template()
    
    def _load_prp_template(self) -> str:
        """Load the PRP base template."""
        try:
            template_path = Path(self.config.template_path)
            if template_path.exists():
                print(f"📄 Loading template from: {template_path}")
                return template_path.read_text(encoding='utf-8')
            else:
                print(f"📄 Template not found at {template_path}, using embedded template")
                # Use embedded template if file not found
                return self._get_embedded_template()
        except Exception as e:
            print(f"📄 Error loading template: {e}, using embedded template")
            return self._get_embedded_template()
    
    def _get_embedded_template(self) -> str:
        """Get embedded PRP template based on context-engineering-intro patterns."""
        return '''name: "Generated PRP - Context-Rich with Validation Loops"
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
{goal}

## Why
{why}

## What
{what}

### Success Criteria
{success_criteria}

## All Needed Context

### Documentation & References
```yaml
{documentation_references}
```

### Current Codebase tree
```bash
{current_codebase_tree}
```

### Desired Codebase tree with files to be added
```bash
{desired_codebase_tree}
```

### Known Gotchas & Library Quirks
```python
{known_gotchas}
```

## Implementation Blueprint

### Data models and structure
{data_models}

### List of tasks to be completed
```yaml
{task_list}
```

### Per task pseudocode
```python
{pseudocode}
```

### Integration Points
```yaml
{integration_points}
```

## Validation Loop

### Level 1: Syntax & Style
```bash
{syntax_validation}
```

### Level 2: Unit Tests
```python
{unit_tests}
```

```bash
{test_commands}
```

### Level 3: Integration Test
```bash
{integration_tests}
```

## Final Validation Checklist
{final_checklist}

---

## Anti-Patterns to Avoid
{anti_patterns}

## Confidence Score: {confidence_score}/10

{confidence_explanation}
'''
    
    async def generate_prp_from_initial(
        self, 
        initial_file_path: str,
        project_root: str = "."
    ) -> GeneratedPRP:
        """
        Generate a comprehensive PRP from an INITIAL.md file.
        
        Args:
            initial_file_path: Path to the INITIAL.md file
            project_root: Root directory of the project
            
        Returns:
            GeneratedPRP with complete implementation blueprint
        """
        try:
            # Step 1: Parse the INITIAL.md file
            print("📋 Parsing INITIAL.md file...")
            initial_analysis = await self.initial_parser.parse_initial_file(initial_file_path)
            
            # Step 2: Analyze codebase context
            print("🔍 Analyzing codebase context...")
            codebase_context = await self.initial_parser.analyze_codebase_context(project_root)
            
            # Step 3: Conduct research (if enabled)
            research_context = ResearchContext(
                external_documentation=[],
                similar_implementations=[],
                best_practices=[],
                common_pitfalls=[],
                library_quirks=[]
            )
            
            if self.config.include_research:
                print("🔬 Conducting research...")
                research_context = await self._conduct_research(initial_analysis)
            
            # Step 4: Generate feature name
            feature_name = self._generate_feature_name(initial_analysis.feature)
            
            # Step 5: Generate PRP content
            print("📝 Generating PRP content...")
            prp_content = await self._generate_prp_content(
                initial_analysis,
                codebase_context,
                research_context,
                feature_name
            )
            
            # Step 6: Calculate confidence score
            confidence_score = self._calculate_confidence_score(
                initial_analysis,
                codebase_context,
                research_context
            )
            
            # Step 7: Save PRP file
            output_path = await self._save_prp_file(prp_content, feature_name)
            
            # Step 8: Generate validation commands
            validation_commands = self._generate_validation_commands(feature_name)
            
            print(f"✅ PRP generated successfully: {output_path}")
            print(f"🎯 Confidence Score: {confidence_score}/10")
            
            return GeneratedPRP(
                content=prp_content,
                file_path=output_path,
                confidence_score=confidence_score,
                feature_name=feature_name,
                generation_timestamp=datetime.now().isoformat(),
                research_context=research_context,
                validation_commands=validation_commands
            )
            
        except Exception as e:
            raise Exception(f"Failed to generate PRP: {str(e)}")
    
    async def _conduct_research(self, initial_analysis: InitialAnalysis) -> ResearchContext:
        """Conduct research for PRP generation."""
        # Extract documentation URLs from the initial analysis
        external_docs = []
        for doc in initial_analysis.documentation:
            if 'http' in doc:
                # Extract URL and description
                url_match = re.search(r'https?://[^\s]+', doc)
                if url_match:
                    url = url_match.group()
                    description = doc.replace(url, '').strip()
                    external_docs.append({
                        'url': url,
                        'why': description or 'Referenced in INITIAL.md',
                        'section': 'Main documentation'
                    })
        
        # Generate best practices based on feature type
        best_practices = self._generate_best_practices(initial_analysis.feature)
        
        # Generate common pitfalls
        common_pitfalls = self._generate_common_pitfalls(initial_analysis.feature)
        
        # Generate library quirks
        library_quirks = self._generate_library_quirks(initial_analysis)
        
        return ResearchContext(
            external_documentation=external_docs,
            similar_implementations=[],
            best_practices=best_practices,
            common_pitfalls=common_pitfalls,
            library_quirks=library_quirks
        )
    
    def _generate_best_practices(self, feature_description: str) -> List[str]:
        """Generate best practices based on feature type."""
        practices = [
            "Always validate input parameters before processing",
            "Use type hints for better code clarity and IDE support",
            "Implement proper error handling with specific exceptions",
            "Follow async/await patterns consistently",
            "Use dependency injection for better testability"
        ]
        
        # Add specific practices based on feature keywords
        feature_lower = feature_description.lower()
        
        if 'api' in feature_lower:
            practices.extend([
                "Implement rate limiting for API endpoints",
                "Use proper HTTP status codes",
                "Validate request payloads with Pydantic models"
            ])
        
        if 'database' in feature_lower or 'db' in feature_lower:
            practices.extend([
                "Use connection pooling for database operations",
                "Implement proper transaction handling",
                "Use migrations for schema changes"
            ])
        
        if 'async' in feature_lower:
            practices.extend([
                "Avoid blocking operations in async functions",
                "Use asyncio.gather for concurrent operations",
                "Implement proper timeout handling"
            ])
        
        return practices[:8]  # Limit to 8 practices
    
    def _generate_common_pitfalls(self, feature_description: str) -> List[str]:
        """Generate common pitfalls based on feature type."""
        pitfalls = [
            "Forgetting to handle edge cases and error conditions",
            "Not implementing proper logging for debugging",
            "Hardcoding configuration values instead of using environment variables",
            "Mixing sync and async code patterns"
        ]
        
        feature_lower = feature_description.lower()
        
        if 'api' in feature_lower:
            pitfalls.extend([
                "Not implementing proper authentication/authorization",
                "Exposing sensitive information in error messages",
                "Not handling request timeouts properly"
            ])
        
        if 'test' in feature_lower:
            pitfalls.extend([
                "Writing tests that depend on external services",
                "Not mocking external dependencies properly",
                "Testing implementation details instead of behavior"
            ])
        
        return pitfalls[:6]  # Limit to 6 pitfalls
    
    def _generate_library_quirks(self, initial_analysis: InitialAnalysis) -> List[str]:
        """Generate library-specific quirks and gotchas."""
        quirks = []
        
        # Analyze documentation and examples for library mentions
        all_text = f"{initial_analysis.feature} {' '.join(initial_analysis.documentation)} {' '.join(initial_analysis.examples)}"
        text_lower = all_text.lower()
        
        # Common library quirks
        if 'fastapi' in text_lower:
            quirks.append("FastAPI requires async functions for endpoints that use await")
        
        if 'pydantic' in text_lower:
            quirks.append("Pydantic v2 has different validation syntax than v1")
        
        if 'sqlalchemy' in text_lower:
            quirks.append("SQLAlchemy async sessions require explicit commit/rollback")
        
        if 'pytest' in text_lower:
            quirks.append("Pytest async tests require pytest-asyncio plugin")
        
        if 'requests' in text_lower:
            quirks.append("Requests library is synchronous - use httpx for async HTTP calls")
        
        # Add general Python quirks if no specific libraries detected
        if not quirks:
            quirks.extend([
                "Python async functions must be awaited in async context",
                "Mutable default arguments can cause unexpected behavior",
                "Import order matters for circular dependency issues"
            ])
        
        return quirks[:5]  # Limit to 5 quirks
    
    def _generate_feature_name(self, feature_description: str) -> str:
        """Generate a clean feature name from description."""
        # Extract key words and create a clean name
        words = re.findall(r'\b[a-zA-Z]+\b', feature_description.lower())
        
        # Filter out common words
        stop_words = {'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can', 'that', 'this', 'these', 'those'}
        
        meaningful_words = [word for word in words if word not in stop_words and len(word) > 2]
        
        # Take first 3-4 meaningful words
        feature_words = meaningful_words[:4]
        
        if not feature_words:
            feature_words = ['custom', 'feature']
        
        return '_'.join(feature_words)

    async def _generate_prp_content(
        self,
        initial_analysis: InitialAnalysis,
        codebase_context: CodebaseContext,
        research_context: ResearchContext,
        feature_name: str
    ) -> str:
        """Generate the complete PRP content."""

        # Prepare template variables
        template_vars = {
            'goal': self._format_goal(initial_analysis.feature),
            'why': self._format_why(initial_analysis),
            'what': self._format_what(initial_analysis),
            'success_criteria': self._format_success_criteria(initial_analysis),
            'documentation_references': self._format_documentation_references(initial_analysis, research_context),
            'current_codebase_tree': codebase_context.current_tree,
            'desired_codebase_tree': self._generate_desired_tree(feature_name, initial_analysis),
            'known_gotchas': self._format_known_gotchas(research_context, codebase_context),
            'data_models': self._generate_data_models(initial_analysis),
            'task_list': self._generate_task_list(initial_analysis, feature_name),
            'pseudocode': self._generate_pseudocode(initial_analysis),
            'integration_points': self._format_integration_points(codebase_context),
            'syntax_validation': self._generate_syntax_validation(),
            'unit_tests': self._generate_unit_tests(feature_name),
            'test_commands': self._generate_test_commands(),
            'integration_tests': self._generate_integration_tests(feature_name),
            'final_checklist': self._generate_final_checklist(),
            'anti_patterns': self._generate_anti_patterns(),
            'confidence_score': 8,  # Will be calculated later
            'confidence_explanation': 'High confidence due to comprehensive context and validation loops.'
        }

        # Fill the template - handle both {key} and [key] formats
        prp_content = self.prp_template

        # First try curly brace format
        for key, value in template_vars.items():
            placeholder = f'{{{key}}}'
            prp_content = prp_content.replace(placeholder, str(value))

        # Then handle specific template placeholders from the original template
        template_replacements = {
            '[What needs to be built - be specific about the end state and desires]': template_vars['goal'],
            '- [Business value and user impact]\n- [Integration with existing features]\n- [Problems this solves and for whom]': template_vars['why'],
            '[User-visible behavior and technical requirements]': template_vars['what'],
            '- [ ] [Specific measurable outcomes]': template_vars['success_criteria'],
            '# MUST READ - Include these in your context window\n- url: [Official API docs URL]\n  why: [Specific sections/methods you\'ll need]\n  \n- file: [path/to/example.py]\n  why: [Pattern to follow, gotchas to avoid]\n  \n- doc: [Library documentation URL] \n  section: [Specific section about common pitfalls]\n  critical: [Key insight that prevents common errors]\n\n- docfile: [PRPs/ai_docs/file.md]\n  why: [docs that the user has pasted in to the project]': template_vars['documentation_references'],
            '# CRITICAL: [Library name] requires [specific setup]\n# Example: FastAPI requires async functions for endpoints\n# Example: This ORM doesn\'t support batch inserts over 1000 records\n# Example: We use pydantic v2 and': template_vars['known_gotchas']
        }

        for placeholder, replacement in template_replacements.items():
            prp_content = prp_content.replace(placeholder, str(replacement))

        return prp_content

    def _format_goal(self, feature_description: str) -> str:
        """Format the goal section."""
        return f"Implement {feature_description.strip()}"

    def _format_why(self, initial_analysis: InitialAnalysis) -> str:
        """Format the why section."""
        why_items = [
            "- Addresses specific user requirements outlined in INITIAL.md",
            "- Integrates with existing codebase patterns and conventions",
            "- Provides value through automated implementation"
        ]

        if initial_analysis.other_considerations:
            why_items.append("- Addresses specific considerations and requirements")

        return '\n'.join(why_items)

    def _format_what(self, initial_analysis: InitialAnalysis) -> str:
        """Format the what section."""
        what_text = f"Implementation of: {initial_analysis.feature}"

        if initial_analysis.examples:
            what_text += f"\n\nFollowing patterns from:\n"
            for example in initial_analysis.examples[:3]:
                what_text += f"- {example}\n"

        return what_text

    def _format_success_criteria(self, initial_analysis: InitialAnalysis) -> str:
        """Format success criteria."""
        criteria = [
            "- [ ] Feature implementation matches requirements",
            "- [ ] All tests pass successfully",
            "- [ ] Code follows existing patterns and conventions",
            "- [ ] Documentation is complete and accurate"
        ]

        if initial_analysis.other_considerations:
            criteria.append("- [ ] All specific considerations are addressed")

        return '\n'.join(criteria)

    def _format_documentation_references(
        self,
        initial_analysis: InitialAnalysis,
        research_context: ResearchContext
    ) -> str:
        """Format documentation references."""
        refs = []

        # Add external documentation
        for doc in research_context.external_documentation:
            refs.append(f"- url: {doc['url']}")
            refs.append(f"  why: {doc['why']}")
            refs.append("")

        # Add example files
        for example in initial_analysis.examples[:5]:
            if 'examples/' in example or '.py' in example:
                refs.append(f"- file: {example}")
                refs.append(f"  why: Pattern to follow from INITIAL.md")
                refs.append("")

        return '\n'.join(refs) if refs else "# No specific documentation references found"

    def _generate_desired_tree(self, feature_name: str, initial_analysis: InitialAnalysis) -> str:
        """Generate desired codebase tree structure."""
        tree_lines = [
            ".",
            f"├── {feature_name}/",
            f"│   ├── __init__.py",
            f"│   ├── main.py              # Main implementation",
            f"│   ├── models.py            # Data models",
            f"│   └── utils.py             # Utility functions",
            f"├── tests/",
            f"│   ├── __init__.py",
            f"│   └── test_{feature_name}.py  # Test suite",
            f"├── docs/",
            f"│   └── {feature_name}.md    # Documentation",
            f"└── requirements.txt         # Updated dependencies"
        ]

        return '\n'.join(tree_lines)

    def _format_known_gotchas(
        self,
        research_context: ResearchContext,
        codebase_context: CodebaseContext
    ) -> str:
        """Format known gotchas and library quirks."""
        gotchas = []

        # Add library quirks
        for quirk in research_context.library_quirks:
            gotchas.append(f"# CRITICAL: {quirk}")

        # Add common pitfalls
        for pitfall in research_context.common_pitfalls[:3]:
            gotchas.append(f"# GOTCHA: {pitfall}")

        # Add codebase-specific conventions
        for convention in codebase_context.existing_conventions[:3]:
            gotchas.append(f"# PATTERN: {convention}")

        return '\n'.join(gotchas) if gotchas else "# No specific gotchas identified"

    def _generate_data_models(self, initial_analysis: InitialAnalysis) -> str:
        """Generate data models section."""
        feature_lower = initial_analysis.feature.lower()

        # Generate specific models based on feature type
        if 'chat' in feature_lower and 'websocket' in feature_lower:
            models_text = """
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
"""
        elif 'api' in feature_lower and 'rest' in feature_lower:
            models_text = """
Create the core data models for the REST API:

```python
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional
from datetime import datetime

Base = declarative_base()

# SQLAlchemy Model
class TodoItem(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Pydantic Models
class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)

class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    completed: Optional[bool] = None

class TodoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
```
"""
        else:
            # Generic models
            models_text = f"""
Create the core data models for {initial_analysis.feature}:

```python
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class FeatureRequest(BaseModel):
    \"\"\"Request model for the feature.\"\"\"
    input_data: str = Field(..., description="Input data for processing")
    options: Optional[dict] = Field(None, description="Optional configuration")

class FeatureResponse(BaseModel):
    \"\"\"Response model for the feature.\"\"\"
    result: str = Field(..., description="Processing result")
    status: str = Field("success", description="Operation status")
    timestamp: datetime = Field(default_factory=datetime.now)
```
"""

        return models_text.strip()

    def _generate_task_list(self, initial_analysis: InitialAnalysis, feature_name: str) -> str:
        """Generate task list for implementation."""
        feature_lower = initial_analysis.feature.lower()

        if 'chat' in feature_lower and 'websocket' in feature_lower:
            tasks = [
                f"Task 1: Setup Project Structure",
                f"CREATE {feature_name}/__init__.py:",
                f"  - Basic package initialization",
                f"  - Export main classes and functions",
                f"",
                f"Task 2: Database Models and Setup",
                f"CREATE {feature_name}/models.py:",
                f"  - PATTERN: Use SQLAlchemy async models",
                f"  - Define User, ChatRoom, Message models",
                f"  - Add proper relationships and constraints",
                f"",
                f"CREATE {feature_name}/database.py:",
                f"  - PATTERN: Async database connection setup",
                f"  - Connection pooling configuration",
                f"  - Database session management",
                f"",
                f"Task 3: Authentication System",
                f"CREATE {feature_name}/auth.py:",
                f"  - PATTERN: JWT token generation and validation",
                f"  - Password hashing with bcrypt",
                f"  - User registration and login endpoints",
                f"",
                f"Task 4: WebSocket Connection Manager",
                f"CREATE {feature_name}/websocket_manager.py:",
                f"  - PATTERN: WebSocket connection management",
                f"  - Room-based message broadcasting",
                f"  - User presence tracking (online/offline)",
                f"",
                f"Task 5: Chat API Endpoints",
                f"CREATE {feature_name}/chat_routes.py:",
                f"  - PATTERN: FastAPI router with dependency injection",
                f"  - CRUD operations for rooms and messages",
                f"  - Message history retrieval with pagination",
                f"",
                f"Task 6: File Upload Handler",
                f"CREATE {feature_name}/file_handler.py:",
                f"  - PATTERN: Async file upload with validation",
                f"  - Image processing and storage",
                f"  - File type and size validation",
                f"",
                f"Task 7: Real-time Features",
                f"CREATE {feature_name}/realtime.py:",
                f"  - PATTERN: WebSocket message handling",
                f"  - Typing indicators implementation",
                f"  - Message delivery status tracking",
                f"",
                f"Task 8: Main Application",
                f"CREATE {feature_name}/main.py:",
                f"  - PATTERN: FastAPI application setup",
                f"  - WebSocket and HTTP route registration",
                f"  - Middleware configuration (CORS, auth)",
                f"",
                f"Task 9: Comprehensive Tests",
                f"CREATE tests/test_{feature_name}.py:",
                f"  - PATTERN: Async test patterns with pytest-asyncio",
                f"  - WebSocket connection testing",
                f"  - Authentication flow testing",
                f"  - Database operations testing",
                f"",
                f"Task 10: Documentation and Deployment",
                f"CREATE docs/{feature_name}.md:",
                f"  - API documentation with examples",
                f"  - WebSocket protocol documentation",
                f"  - Deployment and configuration guide"
            ]
        elif 'api' in feature_lower and 'rest' in feature_lower:
            tasks = [
                f"Task 1: Setup Project Structure",
                f"CREATE {feature_name}/__init__.py:",
                f"  - Basic package initialization",
                f"  - Export main classes and functions",
                f"",
                f"Task 2: Database Models",
                f"CREATE {feature_name}/models.py:",
                f"  - PATTERN: SQLAlchemy models with Pydantic schemas",
                f"  - TodoItem model with proper constraints",
                f"  - Request/response Pydantic models",
                f"",
                f"Task 3: Database Setup",
                f"CREATE {feature_name}/database.py:",
                f"  - PATTERN: SQLite database connection",
                f"  - Database initialization and table creation",
                f"  - Session management",
                f"",
                f"Task 4: CRUD Operations",
                f"CREATE {feature_name}/crud.py:",
                f"  - PATTERN: Async CRUD operations",
                f"  - Create, read, update, delete functions",
                f"  - Proper error handling and validation",
                f"",
                f"Task 5: API Routes",
                f"CREATE {feature_name}/routes.py:",
                f"  - PATTERN: FastAPI router with proper HTTP methods",
                f"  - GET /todos - list all todos",
                f"  - POST /todos - create new todo",
                f"  - PUT /todos/{{id}} - update todo",
                f"  - DELETE /todos/{{id}} - delete todo",
                f"",
                f"Task 6: Main Application",
                f"CREATE {feature_name}/main.py:",
                f"  - PATTERN: FastAPI application setup",
                f"  - Route registration and middleware",
                f"  - Error handling and validation",
                f"",
                f"Task 7: Tests",
                f"CREATE tests/test_{feature_name}.py:",
                f"  - PATTERN: FastAPI test client",
                f"  - Test all CRUD endpoints",
                f"  - Test error cases and validation",
                f"",
                f"Task 8: Documentation",
                f"CREATE docs/{feature_name}.md:",
                f"  - API usage examples",
                f"  - Setup and installation guide"
            ]
        else:
            # Generic task list
            tasks = [
                f"Task 1: Setup Project Structure",
                f"CREATE {feature_name}/__init__.py:",
                f"  - Basic package initialization",
                f"  - Export main classes and functions",
                f"",
                f"Task 2: Implement Data Models",
                f"CREATE {feature_name}/models.py:",
                f"  - PATTERN: Use Pydantic models for validation",
                f"  - Define request/response models",
                f"  - Add proper type hints and validation",
                f"",
                f"Task 3: Core Implementation",
                f"CREATE {feature_name}/main.py:",
                f"  - PATTERN: Follow existing async patterns",
                f"  - Implement main feature logic",
                f"  - Add proper error handling",
                f"",
                f"Task 4: Add Utilities",
                f"CREATE {feature_name}/utils.py:",
                f"  - Helper functions and utilities",
                f"  - Common validation and formatting",
                f"",
                f"Task 5: Implement Tests",
                f"CREATE tests/test_{feature_name}.py:",
                f"  - PATTERN: Follow existing test patterns",
                f"  - Test happy path and edge cases",
                f"  - Mock external dependencies",
                f"",
                f"Task 6: Add Documentation",
                f"CREATE docs/{feature_name}.md:",
                f"  - Usage examples and API reference",
                f"  - Installation and setup instructions"
            ]

        return '\n'.join(tasks)

    def _generate_pseudocode(self, initial_analysis: InitialAnalysis) -> str:
        """Generate pseudocode for implementation."""
        pseudocode = f"""
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
        logger.error(f"Feature processing failed: {{e}}")
        return FeatureResponse(
            result="",
            status="error",
            error="Internal processing error"
        )
"""
        return pseudocode.strip()

    def _format_integration_points(self, codebase_context: CodebaseContext) -> str:
        """Format integration points."""
        points = []

        for integration in codebase_context.integration_points:
            if 'config' in integration.lower():
                points.append(f"CONFIG:")
                points.append(f"  - add to: {integration}")
                points.append(f"  - pattern: Environment variable configuration")
            elif 'api' in integration.lower():
                points.append(f"API:")
                points.append(f"  - add to: {integration}")
                points.append(f"  - pattern: RESTful endpoint registration")
            elif 'database' in integration.lower():
                points.append(f"DATABASE:")
                points.append(f"  - add to: {integration}")
                points.append(f"  - pattern: Model registration and migrations")

        if not points:
            points = [
                "CONFIG:",
                "  - add to: config/settings.py",
                "  - pattern: Feature-specific configuration variables",
                "",
                "DEPENDENCIES:",
                "  - update: requirements.txt",
                "  - pattern: Add new dependencies if needed"
            ]

        return '\n'.join(points)

    def _generate_syntax_validation(self) -> str:
        """Generate syntax validation commands."""
        return """# Run these FIRST - fix any errors before proceeding
ruff check . --fix              # Auto-fix style issues
mypy .                          # Type checking

# Expected: No errors. If errors, READ and fix."""

    def _generate_unit_tests(self, feature_name: str) -> str:
        """Generate unit test examples."""
        tests = f"""
# test_{feature_name}.py
import pytest
from {feature_name}.main import main_feature_function
from {feature_name}.models import FeatureRequest, FeatureResponse

async def test_happy_path():
    \"\"\"Test basic functionality works.\"\"\"
    request = FeatureRequest(input_data="test_input")
    result = await main_feature_function(request)
    assert result.status == "success"
    assert result.result is not None

async def test_validation_error():
    \"\"\"Test invalid input handling.\"\"\"
    request = FeatureRequest(input_data="")
    result = await main_feature_function(request)
    assert result.status == "validation_error"

async def test_error_handling():
    \"\"\"Test error handling.\"\"\"
    # Test with mock that raises exception
    with pytest.raises(Exception):
        # Test error scenarios
        pass
"""
        return tests.strip()

    def _generate_test_commands(self) -> str:
        """Generate test execution commands."""
        return """# Run tests iteratively until passing:
pytest tests/ -v --cov=. --cov-report=term-missing

# If failing: Debug specific test, fix code, re-run"""

    def _generate_integration_tests(self, feature_name: str) -> str:
        """Generate integration test commands."""
        return f"""# Test the implementation end-to-end
python -m {feature_name}.main --test

# Expected: Feature works as intended
# If error: Check logs and debug step by step"""

    def _generate_final_checklist(self) -> str:
        """Generate final validation checklist."""
        checklist = [
            "- [ ] All tests pass: `pytest tests/ -v`",
            "- [ ] No linting errors: `ruff check .`",
            "- [ ] No type errors: `mypy .`",
            "- [ ] Feature works as specified in INITIAL.md",
            "- [ ] Error cases handled gracefully",
            "- [ ] Documentation is complete and accurate",
            "- [ ] Code follows existing patterns and conventions"
        ]
        return '\n'.join(checklist)

    def _generate_anti_patterns(self) -> str:
        """Generate anti-patterns to avoid."""
        patterns = [
            "- ❌ Don't create new patterns when existing ones work",
            "- ❌ Don't skip validation because \"it should work\"",
            "- ❌ Don't ignore failing tests - fix them",
            "- ❌ Don't use sync functions in async context",
            "- ❌ Don't hardcode values that should be config",
            "- ❌ Don't catch all exceptions - be specific"
        ]
        return '\n'.join(patterns)

    def _calculate_confidence_score(
        self,
        initial_analysis: InitialAnalysis,
        codebase_context: CodebaseContext,
        research_context: ResearchContext
    ) -> int:
        """Calculate confidence score for PRP success."""
        score = 5  # Base score

        # Add points for clear feature description
        if len(initial_analysis.feature) > 20:
            score += 1

        # Add points for examples provided
        if initial_analysis.examples:
            score += 1

        # Add points for documentation references
        if initial_analysis.documentation:
            score += 1

        # Add points for codebase context
        if codebase_context.similar_patterns:
            score += 1

        # Add points for research context
        if research_context.external_documentation:
            score += 1

        return min(score, 10)  # Cap at 10

    async def _save_prp_file(self, prp_content: str, feature_name: str) -> str:
        """Save PRP content to file."""
        # Ensure output directory exists
        output_dir = Path(self.config.output_directory)
        output_dir.mkdir(exist_ok=True)

        # Generate filename
        filename = f"{feature_name}_prp.md"
        file_path = output_dir / filename

        # Save content
        file_path.write_text(prp_content, encoding='utf-8')

        return str(file_path)

    def _generate_validation_commands(self, feature_name: str) -> List[str]:
        """Generate validation commands for the feature."""
        return [
            "ruff check . --fix",
            "mypy .",
            "pytest tests/ -v",
            f"python -m {feature_name}.main --test"
        ]
