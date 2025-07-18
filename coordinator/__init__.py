"""
Coordinator Pattern System for Claude Flow Configuration Generation.

This package implements a "one-shot advisor" system that analyzes project requirements
and generates optimized Claude Flow configurations for multi-agent coordination.

Core Components:
- ProjectAnalyzer: Analyzes project descriptions and extracts requirements
- PatternLibrary: Manages coordination patterns and best practices
- PRPGenerator: Generates Claude Flow configuration PRPs
- ClaudeFlowAdapter: Converts patterns to Claude Flow configurations
- CLI: Command-line interface for user interaction

Usage:
    from coordinator import ProjectAnalyzer, PatternLibrary, PRPGenerator, ClaudeFlowAdapter
    from coordinator.models import ProjectAnalysis, CoordinationPattern, ClaudeFlowConfig
"""

from .models import (
    ProjectAnalysis,
    TechnicalRequirements,
    ComplexityMetrics,
    ProjectConstraints,
    CoordinationPattern,
    AgentConfig,
    ClaudeFlowConfig,
    LegacyClaudeFlowConfig,
    OrchestratorConfig,
    TerminalConfig,
    MemoryConfig,
    CoordinationConfig,
    MCPConfig,
    LoggingConfig,
    ValidationResult,
    HandoffResult,
    ProjectType,
    ComplexityLevel,
    TeamSize,
    QualityLevel,
)

from .project_analyzer import ProjectAnalyzer
from .pattern_library import PatternLibrary
from .prp_generator import PRPGenerator
from .claude_flow_adapter import ClaudeFlowAdapter

__version__ = "1.0.0"
__author__ = "Coordinator Pattern Team"
__description__ = "One-shot advisor for Claude Flow configuration generation"

__all__ = [
    # Models
    "ProjectAnalysis",
    "TechnicalRequirements",
    "ComplexityMetrics",
    "ProjectConstraints",
    "CoordinationPattern",
    "AgentConfig",
    "ClaudeFlowConfig",
    "ValidationResult",
    "HandoffResult",
    "ProjectType",
    "ComplexityLevel",
    "TeamSize",
    "QualityLevel",
    # Core Components
    "ProjectAnalyzer",
    "PatternLibrary",
    "PRPGenerator",
    "ClaudeFlowAdapter",
]