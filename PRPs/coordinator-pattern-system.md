name: "Coordinator Pattern System - Project Analysis & Claude Flow Config Generator"
description: |

## Purpose
Build a production-ready Coordinator Pattern system that analyzes software development project requirements and generates optimized Claude Flow configurations. This system embodies the "one-shot advisor" pattern - analyze, configure, handoff, and exit cleanly.

## Core Principles
1. **Context is King**: Include ALL necessary project analysis, patterns, and technical context
2. **Research-Driven**: Base decisions on thorough research of project requirements and best practices
3. **One-Pass Success**: Generate Claude Flow configs that work on first try
4. **Validation Gates**: Include executable tests for config validation
5. **Clean Handoff**: Generate config and exit cleanly, letting Claude Flow take over

---

## Goal
Create a comprehensive Coordinator Pattern system that can:
- Accept natural language project descriptions
- Perform deep technical analysis (stack, complexity, constraints)
- Select optimal coordination patterns from a curated library
- Generate complete Claude Flow configurations
- Execute seamless one-time handoff to Claude Flow
- Provide rich validation and quality assurance

## Why
- **Business Value**: Automates the complex process of multi-agent system configuration
- **Technical Need**: Bridges the gap between project requirements and Claude Flow execution
- **Problems Solved**: Eliminates manual configuration errors and reduces setup time from hours to minutes

## What
A CLI-based system where users describe projects like "Build an e-commerce backend API" and receive:
- Detailed project analysis report
- Recommended coordination pattern with justification
- Complete Claude Flow configuration file
- Validation results and quality metrics
- Handoff documentation for Claude Flow initialization

### Success Criteria
- [ ] Accurately analyzes diverse project types (web, mobile, research, automation)
- [ ] Selects appropriate coordination patterns with >90% accuracy
- [ ] Generates valid Claude Flow configurations that pass all validation gates
- [ ] Completes full analysis-to-handoff cycle in <2 minutes
- [ ] Provides comprehensive documentation and error handling

## All Needed Context

### Documentation & References
```yaml
# MUST READ - Core technical documentation
- url: https://ai.pydantic.dev/
  why: Core agent patterns and multi-agent architectures
  
- file: docs/architecture/refactored-architecture-implementation.md
  why: Our specific Coordinator Pattern architecture and design principles
  
- file: docs/guides/linear-mcp-guide-for-llm.md
  why: Integration patterns and tool usage examples
  
- file: PRPs/EXAMPLE_multi_agent_prp.md
  why: Multi-agent system implementation patterns
  
- file: examples/agent/
  why: Agent creation, tool registration, and dependency injection patterns
  
- file: examples/cli.py
  why: CLI interface patterns with streaming and user interaction
  
- file: PRPs/templates/coordinator/coordinator_prp_base.md
  why: Our specialized PRP template and validation patterns
```

### Project Analysis Requirements
```
Supported Project Types:
- Web Applications (frontend, backend, full-stack)
- Mobile Applications (native, cross-platform)
- API Services (REST, GraphQL, microservices)
- Data Processing (ETL, analytics, ML pipelines)
- Automation Systems (CI/CD, monitoring, deployment)
- Research Projects (analysis, experimentation, reporting)

Technical Stack Analysis:
- Languages: Python, JavaScript/TypeScript, Java, Go, Rust, etc.
- Frameworks: React, Vue, Django, FastAPI, Spring, Express, etc.
- Databases: PostgreSQL, MongoDB, Redis, Elasticsearch, etc.
- Infrastructure: AWS, GCP, Azure, Docker, Kubernetes, etc.

Complexity Assessment Dimensions:
- Technical Complexity: Simple (1-3 components), Moderate (4-8), Complex (9-15), Enterprise (15+)
- Team Size: Solo (1), Small (2-5), Medium (6-15), Large (15+)
- Timeline: Sprint (1-2 weeks), Project (1-3 months), Program (3-12 months)
- Quality Requirements: Prototype, Production, Enterprise, Mission-Critical
```

### Coordination Patterns Library
```python
# Pattern definitions based on our research
COORDINATION_PATTERNS = {
    "hierarchical": {
        "description": "Central coordinator with specialized sub-agents",
        "best_for": ["complex projects", "large teams", "enterprise requirements"],
        "agents": ["architect", "backend_dev", "frontend_dev", "database_designer", "tester", "devops"],
        "coordination_rules": "central_decision_making",
        "quality_gates": ["code_review", "integration_testing", "security_scan"]
    },
    "peer_to_peer": {
        "description": "Distributed coordination with consensus",
        "best_for": ["research projects", "small teams", "experimental work"],
        "agents": ["researcher", "analyst", "writer", "reviewer"],
        "coordination_rules": "consensus_based",
        "quality_gates": ["peer_review", "validation_testing"]
    },
    "pipeline": {
        "description": "Sequential processing with handoffs",
        "best_for": ["data processing", "content creation", "linear workflows"],
        "agents": ["collector", "processor", "transformer", "publisher"],
        "coordination_rules": "sequential_handoff",
        "quality_gates": ["stage_validation", "output_verification"]
    },
    "event_driven": {
        "description": "Reactive coordination based on events",
        "best_for": ["monitoring systems", "real-time processing", "reactive workflows"],
        "agents": ["monitor", "analyzer", "responder", "notifier"],
        "coordination_rules": "event_triggered",
        "quality_gates": ["event_validation", "response_testing"]
    }
}
```

## Implementation Strategy

### Phase 1: Core Infrastructure
```python
# coordinator/__init__.py - Package initialization
from .project_analyzer import ProjectAnalyzer
from .pattern_library import PatternLibrary
from .prp_generator import PRPGenerator
from .claude_flow_adapter import ClaudeFlowAdapter
from .models import ProjectAnalysis, CoordinationPattern, ClaudeFlowConfig

__all__ = [
    "ProjectAnalyzer", "PatternLibrary", "PRPGenerator", 
    "ClaudeFlowAdapter", "ProjectAnalysis", "CoordinationPattern", "ClaudeFlowConfig"
]
```

### Phase 2: Project Analysis Engine
```python
# coordinator/project_analyzer.py
from pydantic import BaseModel
from typing import List, Dict, Optional
import asyncio
import re

class ProjectAnalyzer:
    """Analyzes project descriptions and extracts structured requirements"""
    
    async def analyze_project(self, description: str) -> ProjectAnalysis:
        # PATTERN: Multi-stage analysis pipeline
        tech_analysis = await self._extract_technical_requirements(description)
        complexity_analysis = await self._assess_complexity(description, tech_analysis)
        constraint_analysis = await self._identify_constraints(description)
        
        return ProjectAnalysis(
            description=description,
            technical_requirements=tech_analysis,
            complexity_metrics=complexity_analysis,
            constraints=constraint_analysis,
            recommended_patterns=await self._suggest_patterns(tech_analysis, complexity_analysis)
        )
    
    async def _extract_technical_requirements(self, description: str) -> TechnicalRequirements:
        # CRITICAL: Use NLP and pattern matching to identify tech stack
        # PATTERN: Keyword extraction with context analysis
        # GOTCHA: Handle ambiguous terms and synonyms
        pass
    
    async def _assess_complexity(self, description: str, tech_req: TechnicalRequirements) -> ComplexityMetrics:
        # PATTERN: Multi-dimensional complexity scoring
        # CRITICAL: Consider technical, organizational, and temporal complexity
        pass
```

### Phase 3: Pattern Selection & Config Generation
```python
# coordinator/claude_flow_adapter.py
class ClaudeFlowAdapter:
    """Converts coordination patterns to Claude Flow configurations"""
    
    async def generate_config(
        self, 
        analysis: ProjectAnalysis, 
        pattern: CoordinationPattern
    ) -> ClaudeFlowConfig:
        # PATTERN: Template-based config generation with validation
        config = {
            "hive_structure": self._map_pattern_to_hive(pattern),
            "agents": self._create_agent_configs(analysis, pattern),
            "coordination_rules": self._define_coordination_rules(pattern),
            "quality_gates": self._setup_quality_gates(analysis.quality_requirements),
            "memory_strategy": self._select_memory_strategy(analysis.complexity_metrics),
            "integration_points": self._setup_integrations(analysis.technical_requirements)
        }
        
        # CRITICAL: Validate config before returning
        await self._validate_config(config)
        return ClaudeFlowConfig(**config)
```

## Validation Gates

### Level 1: Unit Testing
```bash
# Test individual components
pytest coordinator/tests/test_project_analyzer.py -v
pytest coordinator/tests/test_pattern_library.py -v
pytest coordinator/tests/test_claude_flow_adapter.py -v

# Test data models and validation
pytest coordinator/tests/test_models.py -v
```

### Level 2: Integration Testing
```bash
# Test end-to-end workflow
pytest coordinator/tests/integration/test_full_workflow.py -v

# Test Claude Flow config generation
pytest coordinator/tests/integration/test_config_generation.py -v

# Test pattern selection accuracy
pytest coordinator/tests/integration/test_pattern_selection.py -v
```

### Level 3: System Validation
```bash
# Test CLI interface
python -m coordinator.cli --test-mode

# Validate generated configs
python -m coordinator.validators.config_validator --config output/test_config.json

# Performance benchmarks
python -m coordinator.benchmarks.performance_test
```

### Level 4: Quality Assurance
```bash
# Code quality checks
ruff check coordinator/ && mypy coordinator/

# Security scanning
bandit -r coordinator/

# Documentation validation
python -m coordinator.docs.validate_examples
```

## Task Breakdown

### Task 1: Setup Project Structure
```bash
# Create core package structure
mkdir -p coordinator/{tests,validators,benchmarks,docs}
touch coordinator/__init__.py coordinator/models.py
touch coordinator/{project_analyzer,pattern_library,prp_generator,claude_flow_adapter,cli}.py
```

### Task 2: Define Data Models
CREATE coordinator/models.py:
- PATTERN: Use Pydantic BaseModel for all data structures
- Define ProjectAnalysis, TechnicalRequirements, ComplexityMetrics
- Define CoordinationPattern, ClaudeFlowConfig with validation
- CRITICAL: Include proper type hints and validation rules

### Task 3: Implement Project Analyzer
CREATE coordinator/project_analyzer.py:
- PATTERN: Async analysis pipeline with structured extraction
- Use regex and NLP techniques for tech stack identification
- Implement complexity scoring algorithm
- GOTCHA: Handle edge cases and ambiguous descriptions

### Task 4: Build Pattern Library
CREATE coordinator/pattern_library.py:
- PATTERN: Registry pattern for coordination patterns
- Implement pattern matching and scoring algorithms
- Include extensibility for custom patterns
- CRITICAL: Validate pattern definitions and compatibility

### Task 5: Create Claude Flow Adapter
CREATE coordinator/claude_flow_adapter.py:
- PATTERN: Adapter pattern for config generation
- Map coordination patterns to Claude Flow structures
- Implement config validation and optimization
- GOTCHA: Ensure generated configs are Claude Flow compatible

### Task 6: Build CLI Interface
CREATE coordinator/cli.py:
- PATTERN: Follow examples/cli.py for structure and UX
- Implement interactive and batch modes
- Add progress indicators and rich output formatting
- CRITICAL: Handle user input validation and error cases

### Task 7: Add Comprehensive Testing
CREATE coordinator/tests/:
- Unit tests for all components with >80% coverage
- Integration tests for end-to-end workflows
- Performance benchmarks and validation tests
- PATTERN: Mirror existing test structure from examples/

## Expected Deliverables

1. **Core System Components** (Production Ready):
   - Complete project analysis engine with NLP capabilities
   - Curated coordination patterns library with scoring
   - Claude Flow adapter with full config generation
   - Robust data models with comprehensive validation

2. **User Interface** (CLI + API):
   - Interactive CLI with rich formatting and progress indicators
   - Batch processing mode for automation
   - JSON API for programmatic access
   - Comprehensive help and documentation

3. **Quality Assurance** (Enterprise Grade):
   - >80% test coverage with unit and integration tests
   - Performance benchmarks (<2min analysis cycle)
   - Security validation and error handling
   - Documentation with examples and troubleshooting

4. **Integration & Deployment**:
   - Claude Flow configuration templates and validators
   - Docker containerization for easy deployment
   - CI/CD pipeline with automated testing
   - Monitoring and logging capabilities

## Gotchas and Common Issues

### Technical Challenges:
- **NLP Accuracy**: Tech stack extraction may miss domain-specific terms
- **Pattern Ambiguity**: Multiple patterns may score similarly - implement tiebreakers
- **Config Complexity**: Claude Flow configs have many interdependent parameters
- **Performance**: Large project descriptions may slow analysis - implement caching

### Integration Issues:
- **Claude Flow Compatibility**: Ensure configs match expected format and version
- **Validation Coverage**: Test with diverse project types and edge cases
- **Error Recovery**: Provide meaningful error messages and suggested fixes
- **Extensibility**: Design for easy addition of new patterns and project types

### User Experience:
- **Input Ambiguity**: Guide users to provide sufficient detail in descriptions
- **Output Clarity**: Present analysis results in understandable format
- **Workflow Integration**: Ensure smooth handoff to Claude Flow execution
- **Documentation**: Provide clear examples and troubleshooting guides

## Files to Reference During Implementation

```yaml
# Core patterns and examples
- file: examples/agent/agent.py
  why: Agent creation and tool registration patterns

- file: examples/cli.py
  why: CLI structure, streaming, and user interaction

- file: PRPs/EXAMPLE_multi_agent_prp.md
  why: Multi-agent system architecture and validation

# Our specific templates and docs
- file: PRPs/templates/coordinator/coordinator_prp_base.md
  why: Our PRP template structure and validation gates

- file: docs/architecture/refactored-architecture-implementation.md
  why: Coordinator Pattern architecture and design principles

# Configuration and setup
- file: CLAUDE.md
  why: Project-specific rules and conventions

- file: COORDINATOR_PROJECT_SETUP.md
  why: Implementation plan and technical requirements
```

## Confidence Score: 9/10

**High confidence due to**:
- Clear architecture based on proven Context Engineering principles
- Rich examples and patterns from existing codebase
- Well-defined scope with specific deliverables
- Comprehensive validation strategy with multiple test levels
- Detailed implementation plan with task breakdown

**Minor uncertainty on**:
- NLP accuracy for tech stack extraction (mitigated by pattern matching)
- Claude Flow config format compatibility (mitigated by validation testing)

---

**Remember**: This Coordinator Pattern system embodies "analyze once, configure perfectly, handoff cleanly" - the ultimate one-shot advisor for multi-agent system setup.
