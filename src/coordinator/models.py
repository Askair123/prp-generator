"""
Data models for Coordinator Pattern system.

This module defines all the Pydantic models used throughout the Coordinator Pattern
system for project analysis, pattern selection, and Claude Flow configuration generation.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field, validator
from enum import Enum
import json


class ProjectType(str, Enum):
    """Supported project types for analysis."""
    WEB_FRONTEND = "web_frontend"
    WEB_BACKEND = "web_backend"
    WEB_FULLSTACK = "web_fullstack"
    MOBILE_NATIVE = "mobile_native"
    MOBILE_CROSSPLATFORM = "mobile_crossplatform"
    API_REST = "api_rest"
    API_GRAPHQL = "api_graphql"
    MICROSERVICES = "microservices"
    DATA_PROCESSING = "data_processing"
    DATA_ANALYTICS = "data_analytics"
    ML_PIPELINE = "ml_pipeline"
    AUTOMATION = "automation"
    CI_CD = "ci_cd"
    MONITORING = "monitoring"
    RESEARCH = "research"


class ComplexityLevel(str, Enum):
    """Project complexity levels."""
    SIMPLE = "simple"      # 1-3 components
    MODERATE = "moderate"  # 4-8 components
    COMPLEX = "complex"    # 9-15 components
    ENTERPRISE = "enterprise"  # 15+ components


class TeamSize(str, Enum):
    """Team size categories."""
    SOLO = "solo"          # 1 person
    SMALL = "small"        # 2-5 people
    MEDIUM = "medium"      # 6-15 people
    LARGE = "large"        # 15+ people


class QualityLevel(str, Enum):
    """Quality requirement levels."""
    PROTOTYPE = "prototype"
    PRODUCTION = "production"
    ENTERPRISE = "enterprise"
    MISSION_CRITICAL = "mission_critical"


class TechnicalRequirements(BaseModel):
    """Technical requirements extracted from project description."""
    languages: List[str] = Field(default_factory=list, description="Programming languages identified")
    frameworks: List[str] = Field(default_factory=list, description="Frameworks and libraries")
    databases: List[str] = Field(default_factory=list, description="Database technologies")
    infrastructure: List[str] = Field(default_factory=list, description="Infrastructure and deployment")
    tools: List[str] = Field(default_factory=list, description="Development and build tools")
    apis: List[str] = Field(default_factory=list, description="External APIs and integrations")

    @validator('languages', 'frameworks', 'databases', 'infrastructure', 'tools', 'apis')
    def normalize_tech_names(cls, v):
        """Normalize technology names to lowercase."""
        return [tech.lower().strip() for tech in v if tech.strip()]


class ComplexityMetrics(BaseModel):
    """Complexity assessment metrics."""
    technical_complexity: int = Field(ge=1, le=10, description="Technical complexity score (1-10)")
    organizational_complexity: int = Field(ge=1, le=10, description="Team/process complexity (1-10)")
    temporal_complexity: int = Field(ge=1, le=10, description="Timeline pressure (1-10)")
    overall_score: float = Field(ge=0.0, le=10.0, description="Weighted overall complexity")
    complexity_level: ComplexityLevel = Field(description="Categorized complexity level")

    @validator('overall_score', always=True)
    def calculate_overall_score(cls, v, values):
        """Calculate weighted overall complexity score."""
        if 'technical_complexity' in values and 'organizational_complexity' in values and 'temporal_complexity' in values:
            # Weighted average: technical=50%, organizational=30%, temporal=20%
            return round(
                (values['technical_complexity'] * 0.5 +
                 values['organizational_complexity'] * 0.3 +
                 values['temporal_complexity'] * 0.2), 1
            )
        return v

    @validator('complexity_level', always=True)
    def determine_complexity_level(cls, v, values):
        """Determine complexity level based on overall score."""
        if 'overall_score' in values:
            score = values['overall_score']
            if score <= 1.0:
                return ComplexityLevel.SIMPLE
            elif score <= 3.0:
                return ComplexityLevel.SIMPLE
            elif score <= 6.0:
                return ComplexityLevel.MODERATE
            elif score <= 8.5:
                return ComplexityLevel.COMPLEX
            else:
                return ComplexityLevel.ENTERPRISE
        return v


class ProjectConstraints(BaseModel):
    """Project constraints and limitations."""
    timeline_days: Optional[int] = Field(None, ge=1, description="Project timeline in days")
    budget_level: Optional[str] = Field(None, description="Budget constraints")
    team_size: TeamSize = Field(description="Team size category")
    quality_requirements: QualityLevel = Field(description="Quality level requirements")
    compliance_requirements: List[str] = Field(default_factory=list, description="Compliance standards")
    performance_requirements: Dict[str, Any] = Field(default_factory=dict, description="Performance criteria")


class ProjectAnalysis(BaseModel):
    """Complete project analysis results."""
    description: str = Field(description="Original project description")
    project_type: ProjectType = Field(description="Identified project type")
    technical_requirements: TechnicalRequirements = Field(description="Technical stack analysis")
    complexity_metrics: ComplexityMetrics = Field(description="Complexity assessment")
    constraints: ProjectConstraints = Field(description="Project constraints")
    recommended_patterns: List[str] = Field(default_factory=list, description="Suggested coordination patterns")
    confidence_score: float = Field(ge=0.0, le=1.0, description="Analysis confidence (0-1)")

    class Config:
        """Pydantic configuration."""
        use_enum_values = True
        validate_assignment = True


class CoordinationPattern(BaseModel):
    """Coordination pattern definition."""
    name: str = Field(description="Pattern name")
    description: str = Field(description="Pattern description")
    best_for: List[str] = Field(description="Ideal use cases")
    agents: List[str] = Field(description="Required agent types")
    coordination_rules: str = Field(description="Coordination strategy")
    quality_gates: List[str] = Field(description="Quality assurance gates")
    complexity_fit: List[ComplexityLevel] = Field(description="Suitable complexity levels")
    team_size_fit: List[TeamSize] = Field(description="Suitable team sizes")

    class Config:
        """Pydantic configuration."""
        use_enum_values = True


class AgentConfig(BaseModel):
    """Individual agent configuration."""
    type: str = Field(description="Agent type/role")
    specialization: str = Field(description="Agent specialization")
    capabilities: List[str] = Field(description="Agent capabilities")
    tools: List[str] = Field(description="Available tools")
    dependencies: List[str] = Field(default_factory=list, description="Agent dependencies")


# New Claude Flow standard configuration models
class OrchestratorConfig(BaseModel):
    """Orchestrator configuration for Claude Flow."""
    maxConcurrentAgents: int = Field(default=10, ge=1, le=100)
    taskQueueSize: int = Field(default=100, ge=10, le=1000)
    healthCheckInterval: int = Field(default=30000, ge=1000)
    shutdownTimeout: int = Field(default=30000, ge=1000)
    agentTimeoutMs: int = Field(default=300000, ge=10000)
    resourceAllocationStrategy: str = Field(default="balanced")
    agentRecycling: Dict[str, Any] = Field(default_factory=dict)
    failover: Dict[str, Any] = Field(default_factory=dict)


class TerminalConfig(BaseModel):
    """Terminal configuration for Claude Flow."""
    type: str = Field(default="auto")
    poolSize: int = Field(default=5, ge=1, le=50)
    recycleAfter: int = Field(default=10, ge=1)
    healthCheckInterval: int = Field(default=60000, ge=1000)
    commandTimeout: int = Field(default=300000, ge=1000)
    maxConcurrentCommands: int = Field(default=3, ge=1, le=10)
    shellPreference: List[str] = Field(default=["bash", "zsh", "sh"])
    environment: Dict[str, str] = Field(default_factory=dict)
    security: Dict[str, Any] = Field(default_factory=dict)


class MemoryConfig(BaseModel):
    """Memory configuration for Claude Flow."""
    backend: str = Field(default="hybrid")
    cacheSizeMB: int = Field(default=100, ge=10, le=10000)
    syncInterval: int = Field(default=5000, ge=1000)
    conflictResolution: str = Field(default="crdt")
    retentionDays: int = Field(default=30, ge=1, le=365)
    compressionEnabled: bool = Field(default=True)
    encryptionEnabled: bool = Field(default=False)
    backup: Dict[str, Any] = Field(default_factory=dict)
    optimization: Dict[str, Any] = Field(default_factory=dict)


class CoordinationConfig(BaseModel):
    """Coordination configuration for Claude Flow."""
    maxRetries: int = Field(default=3, ge=0, le=10)
    retryDelay: int = Field(default=1000, ge=100)
    deadlockDetection: bool = Field(default=True)
    resourceTimeout: int = Field(default=60000, ge=1000)
    messageTimeout: int = Field(default=30000, ge=1000)
    priorityLevels: int = Field(default=5, ge=1, le=10)
    loadBalancingStrategy: str = Field(default="round-robin")
    scheduling: Dict[str, Any] = Field(default_factory=dict)
    communication: Dict[str, Any] = Field(default_factory=dict)


class MCPConfig(BaseModel):
    """MCP configuration for Claude Flow."""
    transport: str = Field(default="stdio")
    port: int = Field(default=3000, ge=1000, le=65535)
    host: str = Field(default="localhost")
    tlsEnabled: bool = Field(default=False)
    allowedTools: List[str] = Field(default=["*"])
    maxRequestSize: str = Field(default="10MB")
    requestTimeout: int = Field(default=30000, ge=1000)
    authentication: Dict[str, Any] = Field(default_factory=dict)
    rateLimiting: Dict[str, Any] = Field(default_factory=dict)


class LoggingConfig(BaseModel):
    """Logging configuration for Claude Flow."""
    level: str = Field(default="info")
    format: str = Field(default="json")
    destination: str = Field(default="console")
    fileOutput: str = Field(default="logs/claude-flow.log")
    maxFileSize: str = Field(default="10MB")
    maxFiles: int = Field(default=5, ge=1, le=100)
    components: Dict[str, str] = Field(default_factory=dict)
    audit: Dict[str, Any] = Field(default_factory=dict)


class ClaudeFlowConfig(BaseModel):
    """Standard Claude Flow configuration."""
    orchestrator: OrchestratorConfig = Field(default_factory=OrchestratorConfig)
    terminal: TerminalConfig = Field(default_factory=TerminalConfig)
    memory: MemoryConfig = Field(default_factory=MemoryConfig)
    coordination: CoordinationConfig = Field(default_factory=CoordinationConfig)
    mcp: MCPConfig = Field(default_factory=MCPConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)

    def to_json(self) -> str:
        """Export configuration as JSON string."""
        return json.dumps(self.dict(), indent=2)

    def save_to_file(self, filepath: str) -> None:
        """Save configuration to JSON file."""
        with open(filepath, 'w') as f:
            f.write(self.to_json())


# Legacy configuration for backward compatibility
class LegacyClaudeFlowConfig(BaseModel):
    """Legacy Claude Flow configuration output."""
    hive_structure: str = Field(description="Hive organization structure")
    agents: List[AgentConfig] = Field(description="Agent configurations")
    coordination_rules: Dict[str, Any] = Field(description="Coordination rules and strategies")
    quality_gates: List[Dict[str, Any]] = Field(description="Quality assurance gates")
    memory_strategy: str = Field(description="Memory management strategy")
    integration_points: Dict[str, Any] = Field(description="External integrations")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")

    def to_json(self) -> str:
        """Export configuration as JSON string."""
        return json.dumps(self.dict(), indent=2)

    def save_to_file(self, filepath: str) -> None:
        """Save configuration to JSON file."""
        with open(filepath, 'w') as f:
            f.write(self.to_json())


class ValidationResult(BaseModel):
    """Validation result for generated configurations."""
    is_valid: bool = Field(description="Whether validation passed")
    errors: List[str] = Field(default_factory=list, description="Validation errors")
    warnings: List[str] = Field(default_factory=list, description="Validation warnings")
    score: float = Field(ge=0.0, le=1.0, description="Validation score (0-1)")

    @property
    def has_errors(self) -> bool:
        """Check if there are validation errors."""
        return len(self.errors) > 0

    @property
    def has_warnings(self) -> bool:
        """Check if there are validation warnings."""
        return len(self.warnings) > 0


class HandoffResult(BaseModel):
    """Result of handoff to Claude Flow."""
    success: bool = Field(description="Whether handoff was successful")
    config_path: str = Field(description="Path to generated configuration")
    claude_flow_ready: bool = Field(description="Whether Claude Flow can use the config")
    handoff_timestamp: str = Field(description="Timestamp of handoff")
    next_steps: List[str] = Field(description="Recommended next steps")

    class Config:
        """Pydantic configuration."""
        validate_assignment = True