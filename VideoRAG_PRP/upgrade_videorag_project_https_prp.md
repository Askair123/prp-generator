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
Implement Upgrade the VideoRAG project (https://github.com/HKUDS/VideoRAG) to support dynamic video segmentation based on scene detection instead of fixed 30-second intervals, adapt the system for RTX 5090ti (16GB VRAM) instead of RTX 3090 (24GB VRAM), replace faster-whisper with OpenAI Whisper API, and set up the environment using conda virtual environment with fixed dependency versions.
The core modifications include:
1. Replace fixed 30-second video segmentation with intelligent scene-based segmentation using PySceneDetect
2. Adapt video processing pipeline to handle variable-length segments (from 0.1 seconds to any length)
3. Modify memory management and batch processing to work within 16GB VRAM constraints
4. Replace faster-whisper implementation with OpenAI Whisper API calls for audio transcription
5. Create conda environment setup with pinned dependency versions for stability

## Why
- Addresses specific user requirements outlined in INITIAL.md
- Integrates with existing codebase patterns and conventions
- Provides value through automated implementation
- Addresses specific considerations and requirements

## What
Implementation of: Upgrade the VideoRAG project (https://github.com/HKUDS/VideoRAG) to support dynamic video segmentation based on scene detection instead of fixed 30-second intervals, adapt the system for RTX 5090ti (16GB VRAM) instead of RTX 3090 (24GB VRAM), replace faster-whisper with OpenAI Whisper API, and set up the environment using conda virtual environment with fixed dependency versions.
The core modifications include:
1. Replace fixed 30-second video segmentation with intelligent scene-based segmentation using PySceneDetect
2. Adapt video processing pipeline to handle variable-length segments (from 0.1 seconds to any length)
3. Modify memory management and batch processing to work within 16GB VRAM constraints
4. Replace faster-whisper implementation with OpenAI Whisper API calls for audio transcription
5. Create conda environment setup with pinned dependency versions for stability

Following patterns from:
- `examples/video_segmentation.py` - PySceneDetect integration for scene-based video cutting
- `examples/openai_whisper_api.py` - OpenAI Whisper API implementation replacing faster-whisper
- `examples/memory_optimization.py` - GPU memory management for 16GB VRAM constraints


### Success Criteria
- [ ] Feature implementation matches requirements
- [ ] All tests pass successfully
- [ ] Code follows existing patterns and conventions
- [ ] Documentation is complete and accurate
- [ ] All specific considerations are addressed

## All Needed Context

### Documentation & References
```yaml
- url: https://github.com/HKUDS/VideoRAG
  why: VideoRAG Original Project:

- url: https://arxiv.org/abs/2502.01549
  why: VideoRAG Paper:

- url: https://scenedetect.com/
  why: PySceneDetect Documentation:

- url: https://platform.openai.com/docs/guides/speech-to-text
  why: OpenAI Whisper API Documentation:

- url: https://huggingface.co/openbmb/MiniCPM-V-2_6-int4
  why: MiniCPM-V Model Documentation:

- url: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
  why: Conda Environment Management:

- url: https://pytorch.org/docs/stable/notes/cuda.html#memory-management
  why: PyTorch Memory Management:

- file: `examples/video_segmentation.py` - PySceneDetect integration for scene-based video cutting
  why: Pattern to follow from INITIAL.md

- file: `examples/openai_whisper_api.py` - OpenAI Whisper API implementation replacing faster-whisper
  why: Pattern to follow from INITIAL.md

- file: `examples/memory_optimization.py` - GPU memory management for 16GB VRAM constraints
  why: Pattern to follow from INITIAL.md

- file: `examples/variable_segment_processing.py` - Processing pipeline adaptation for variable-length segments
  why: Pattern to follow from INITIAL.md

- file: `examples/conda_environment.yml` - Complete conda environment specification with pinned versions
  why: Pattern to follow from INITIAL.md

```

### Current Codebase tree
```bash
.
├── CLAUDE_FLOW_ALIGNMENT_ANALYSIS.md
├── CLAUDE.md
├── COORDINATOR_PROJECT_SETUP.md
├── COORDINATOR_README.md
├── dev
│   ├── benchmarks
│   ├── demo_output
│   │   ├── claude_flow_config_20250718_151702.json
│   │   └── handoff_instructions_20250718_151702.md
│   ├── demos
│   │   ├── demo_complete_documentation_sync.py
│   │   ├── demo_context_engineering_comparison.py
│   │   ├── demo_coordinator.py
│   │   ├── demo_deep_documentation_system.py
│   │   ├── demo_enhanced_workflow.py
│   │   ├── demo_initial_to_prp_system.py
│   │   ├── demo_knowledge_embedding_process.py
│   │   ├── demo_knowledge_enhanced_system.py
│   │   ├── demo_prp_driven_system.py
│   │   └── demo_standard_config.py
│   ├── knowledge_enhanced_output
│   │   └── claude-flow-knowledge-enhanced.config.json
│   ├── prp_coordinator_output
│   │   └── claude-flow-coordinator-pattern-system.config.json
│   ├── prp_multi_agent_output
│   │   └── claude-flow-EXAMPLE_multi_agent_prp.config.json
│   ├── reports
│   │   ├── CLAUDE_FLOW_KNOWLEDGE_INTEGRATION_REPORT.md
│   │   ├── COMPLETE_DOCUMENTATION_SYNC_REPORT.md
│   │   ├── COMPLETE_SYSTEM_TEST_REPORT.md
│   │   ├── CONTEXT_ENGINEERING_ANALYSIS_REPORT.md
│   │   ├── COORDINATOR_IMPLEMENTATION_REPORT.md
│   │   ├── CORRECTED_ARCHITECTURE_REPORT.md
│   │   ├── DEEP_DOCUMENTATION_SYSTEM_REPORT.md
│   │   ├── FINAL_CLAUDE_FLOW_ALIGNMENT_REPORT.md
│   │   ├── INITIAL_TO_PRP_IMPLEMENTATION_REPORT.md
│   │   └── PRP_TEST_REPORT.md
│   ├── standard_config_output
│   │   └── claude-flow.config.json
│   ├── test_output
│   │   └── claude-flow-ecommerce-test.config.json
│   └── tools
│       ├── test_github_deployment.py
│       ├── test_initial_files
│       │   └── web_scraper_initial.md
│       ├── test_prps
│       │   └── ecommerce-api-system.prp.md
│       └── test_prp_system.py
├── docs
│   ├── architecture
│   │   └── refactored-architecture-implementation.md
│   ├── deployment
│   │   ├── github-deployment.md
│   │   └── github-setup.md
│   ├── developer-guide
│   ├── DOCUMENT_CLEANUP_ANALYSIS.md
│   ├── DOCUMENT_COMPARISON_ANALYSIS.md
│   ├── guides
│   │   └── linear-mcp-guide-for-llm.md
│   ├── QUICK_NAVIGATION.md
│   ├── README.md
│   └── user-guide
│       ├── installation.md
│       └── QUICK_REFERENCE.md
├── DOCUMENTATION_SYNC_COMPLETION.md
├── examples
│   ├── coordinator
│   ├── generated_prps
│   │   ├── custom_feature_prp.md
│   │   └── EXAMPLE_multi_agent_prp.md
│   ├── INITIAL_EXAMPLE.md
│   └── use-cases
│       └── mcp-server
│           ├── CLAUDE.md
│           ├── examples
│           │   ├── database-tools-sentry.ts
│           │   └── database-tools.ts
│           ├── package.json
│           ├── package-lock.json
│           ├── PRPs
│           │   ├── ai_docs
│           │   │   ├── claude_api_usage.md
│           │   │   └── mcp_patterns.md
│           │   ├── INITIAL.md
│           │   ├── README.md
│           │   └── templates
│           │       └── prp_mcp_base.md
│           ├── README.md
│           ├── src
│           │   ├── auth
│           │   │   ├── github-handler.ts
│           │   │   └── oauth-utils.ts
│           │   ├── database
│           │   │   ├── connection.ts
│           │   │   ├── security.ts
│           │   │   └── utils.ts
│           │   ├── index_sentry.ts
│           │   ├── index.ts
│           │   ├── tools
│           │   │   └── register-tools.ts
│           │   └── types.ts
│           ├── tests
│           │   ├── fixtures
│           │   │   ├── auth.fixtures.ts
│           │   │   ├── database.fixtures.ts
│           │   │   └── mcp.fixtures.ts
│           │   ├── mocks
│           │   │   ├── crypto.mock.ts
│           │   │   ├── database.mock.ts
│           │   │   ├── github.mock.ts
│           │   │   └── oauth.mock.ts
│           │   ├── setup.ts
│           │   └── unit
│           │       ├── database
│           │       │   ├── security.test.ts
│           │       │   └── utils.test.ts
│           │       ├── tools
│           │       │   └── database-tools.test.ts
│           │       └── utils
│           │           └── response-helpers.test.ts
│           ├── tsconfig.json
│           ├── vitest.config.js
│           ├── worker-configuration.d.ts
│           └── wrangler.jsonc
├── FILE_REORGANIZATION_COMPLETED.md
├── FILE_REORGANIZATION_PLAN.md
├── GITHUB_DEPLOYMENT_SUCCESS.md
├── -home-thomas-dev-Context-Engineering-.txt
├── INITIAL_COORDINATOR_EXAMPLE.md
├── INITIAL_EXAMPLE.md
├── INITIAL.md
├── KNOWLEDGE_EMBEDDING_DETAILED_ANALYSIS.md
├── LICENSE
├── README.md
├── README_UPDATE_SUMMARY.md
├── scripts
│   ├── setup
│   │   ├── deploy_to_github.sh
│   │   ├── quick_setup.sh
│   │   ├── setup_from_github.py
│   │   ├── setup_new_project.py
│   │   └── setup_new_project.sh
│   └── utils
│       └── verify_setup.py
├── setup_from_github.py
├── src
│   └── coordinator
│       ├── benchmarks
│       ├── claude_flow_adapter.py
│       ├── claude_flow_config_generator.py
│       ├── claude_flow_knowledge_base.py
│       ├── claude_flow_llm_docs.py
│       ├── cli.py
│       ├── context_manager.py
│       ├── contextual_knowledge_index.py
│       ├── docs
│       ├── enhanced_prp_processor.py
│       ├── initial_parser.py
│       ├── initial_to_prp_cli.py
│       ├── initial_to_prp_generator.py
│       ├── __init__.py
│       ├── models.py
│       ├── pattern_library.py
│       ├── project_analyzer.py
│       ├── prp_generator.py
│       ├── prp_parser.py
│       ├── README.md
│       ├── tests
│       │   └── test_integration.py
│       └── validators
├── SYSTEM_OVERVIEW.md
├── templates
│   ├── coordinator
│   │   └── coordinator_prp_base.md
│   └── prp_base.md
├── TESTING_COMPLETED_REPORT.md
├── tests
│   ├── fixtures
│   ├── integration
│   └── unit
├── UPDATED_SYSTEM_OVERVIEW.md
├── VERIFICATION_FIX_COMPLETED.md
├── VideoRAG_UPGRADE_INITIAL.md
└── WORKFLOW_ORCHESTRATION_ANALYSIS.md

55 directories, 130 files

```

### Desired Codebase tree with files to be added
```bash
.
├── upgrade_videorag_project_https/
│   ├── __init__.py
│   ├── main.py              # Main implementation
│   ├── models.py            # Data models
│   └── utils.py             # Utility functions
├── tests/
│   ├── __init__.py
│   └── test_upgrade_videorag_project_https.py  # Test suite
├── docs/
│   └── upgrade_videorag_project_https.md    # Documentation
└── requirements.txt         # Updated dependencies
```

### Known Gotchas & Library Quirks
```python
# CRITICAL: Python async functions must be awaited in async context
# CRITICAL: Mutable default arguments can cause unexpected behavior
# CRITICAL: Import order matters for circular dependency issues
# GOTCHA: Forgetting to handle edge cases and error conditions
# GOTCHA: Not implementing proper logging for debugging
# GOTCHA: Hardcoding configuration values instead of using environment variables
```

## Implementation Blueprint

### Data models and structure
Create the core data models for Upgrade the VideoRAG project (https://github.com/HKUDS/VideoRAG) to support dynamic video segmentation based on scene detection instead of fixed 30-second intervals, adapt the system for RTX 5090ti (16GB VRAM) instead of RTX 3090 (24GB VRAM), replace faster-whisper with OpenAI Whisper API, and set up the environment using conda virtual environment with fixed dependency versions.
The core modifications include:
1. Replace fixed 30-second video segmentation with intelligent scene-based segmentation using PySceneDetect
2. Adapt video processing pipeline to handle variable-length segments (from 0.1 seconds to any length)
3. Modify memory management and batch processing to work within 16GB VRAM constraints
4. Replace faster-whisper implementation with OpenAI Whisper API calls for audio transcription
5. Create conda environment setup with pinned dependency versions for stability:

```python
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class FeatureRequest(BaseModel):
    """Request model for the feature."""
    input_data: str = Field(..., description="Input data for processing")
    options: Optional[dict] = Field(None, description="Optional configuration")

class FeatureResponse(BaseModel):
    """Response model for the feature."""
    result: str = Field(..., description="Processing result")
    status: str = Field("success", description="Operation status")
    timestamp: datetime = Field(default_factory=datetime.now)
```

### List of tasks to be completed
```yaml
Task 1: Setup Project Structure
CREATE upgrade_videorag_project_https/__init__.py:
  - Basic package initialization
  - Export main classes and functions

Task 2: Implement Data Models
CREATE upgrade_videorag_project_https/models.py:
  - PATTERN: Use Pydantic models for validation
  - Define request/response models
  - Add proper type hints and validation

Task 3: Core Implementation
CREATE upgrade_videorag_project_https/main.py:
  - PATTERN: Follow existing async patterns
  - Implement main feature logic
  - Add proper error handling

Task 4: Add Utilities
CREATE upgrade_videorag_project_https/utils.py:
  - Helper functions and utilities
  - Common validation and formatting

Task 5: Implement Tests
CREATE tests/test_upgrade_videorag_project_https.py:
  - PATTERN: Follow existing test patterns
  - Test happy path and edge cases
  - Mock external dependencies

Task 6: Add Documentation
CREATE docs/upgrade_videorag_project_https.md:
  - Usage examples and API reference
  - Installation and setup instructions
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
# test_upgrade_videorag_project_https.py
import pytest
from upgrade_videorag_project_https.main import main_feature_function
from upgrade_videorag_project_https.models import FeatureRequest, FeatureResponse

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
python -m upgrade_videorag_project_https.main --test

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
