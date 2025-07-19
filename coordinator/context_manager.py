"""
Context Management System for PRP-driven Coordinator Pattern.

This module implements a sophisticated context management system that tracks
data flow, maintains state, and provides rich context for each processing step.
"""

import asyncio
from datetime import datetime
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
import uuid

from .models import ProjectAnalysis, CoordinationPattern, ClaudeFlowConfig


class ContextLevel(Enum):
    """Context hierarchy levels."""
    WORKFLOW = "workflow"
    PHASE = "phase"
    AGENT = "agent"
    TASK = "task"


class ProcessingPhase(Enum):
    """Processing phases in the PRP workflow."""
    PARSING = "parsing"
    ANALYSIS = "analysis"
    PATTERN_SELECTION = "pattern_selection"
    CONFIG_GENERATION = "config_generation"
    VALIDATION = "validation"


@dataclass
class DataLineage:
    """Tracks data transformation through the workflow."""
    transformations: List[Dict[str, Any]] = field(default_factory=list)
    confidence_evolution: List[float] = field(default_factory=list)
    quality_metrics: Dict[str, float] = field(default_factory=dict)
    
    def add_transformation(self, phase: ProcessingPhase, input_data: Any, output_data: Any, confidence: float):
        """Record a data transformation."""
        self.transformations.append({
            "phase": phase.value,
            "timestamp": datetime.now().isoformat(),
            "input_type": type(input_data).__name__,
            "output_type": type(output_data).__name__,
            "confidence": confidence
        })
        self.confidence_evolution.append(confidence)


@dataclass
class QualityMetrics:
    """Quality metrics for the processing workflow."""
    parsing_completeness: float = 0.0
    analysis_confidence: float = 0.0
    pattern_match_score: float = 0.0
    config_validation_score: float = 0.0
    overall_quality: float = 0.0
    
    def calculate_overall_quality(self):
        """Calculate overall quality score."""
        scores = [
            self.parsing_completeness,
            self.analysis_confidence,
            self.pattern_match_score,
            self.config_validation_score
        ]
        self.overall_quality = sum(scores) / len(scores) if scores else 0.0


@dataclass
class WorkflowContext:
    """Top-level workflow context."""
    workflow_id: str
    prp_source: str
    timestamp: datetime
    current_phase: ProcessingPhase
    
    # Shared state across all phases
    prp_analysis: Optional[Any] = None
    project_analysis: Optional[ProjectAnalysis] = None
    selected_pattern: Optional[CoordinationPattern] = None
    generated_config: Optional[ClaudeFlowConfig] = None
    
    # Context hierarchy
    phase_contexts: Dict[str, 'PhaseContext'] = field(default_factory=dict)
    
    # Tracking and metrics
    data_lineage: DataLineage = field(default_factory=DataLineage)
    quality_metrics: QualityMetrics = field(default_factory=QualityMetrics)
    
    # Intermediate results and hints
    intermediate_results: Dict[str, Any] = field(default_factory=dict)
    downstream_hints: Dict[str, Any] = field(default_factory=dict)


@dataclass
class PhaseContext:
    """Phase-specific context."""
    phase: ProcessingPhase
    workflow_context: WorkflowContext
    
    # Phase-specific data
    input_data: Any = None
    output_data: Any = None
    processing_metadata: Dict[str, Any] = field(default_factory=dict)
    
    # Agent contexts within this phase
    agent_contexts: Dict[str, 'AgentContext'] = field(default_factory=dict)
    
    # Phase metrics
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    confidence_score: float = 0.0
    
    def create_agent_context(self, agent_name: str, role: str, capabilities: List[str]) -> 'AgentContext':
        """Create an agent context within this phase."""
        agent_context = AgentContext(
            agent_name=agent_name,
            role=role,
            capabilities=capabilities,
            phase_context=self
        )
        self.agent_contexts[agent_name] = agent_context
        return agent_context


@dataclass
class AgentContext:
    """Agent-specific context."""
    agent_name: str
    role: str
    capabilities: List[str]
    phase_context: PhaseContext
    
    # Agent-specific tools and knowledge
    available_tools: List[str] = field(default_factory=list)
    knowledge_base: Dict[str, Any] = field(default_factory=dict)
    specialization_focus: List[str] = field(default_factory=list)
    
    # Task execution context
    current_task: Optional[str] = None
    task_history: List[Dict[str, Any]] = field(default_factory=list)
    
    # Agent performance metrics
    task_success_rate: float = 1.0
    average_confidence: float = 0.0
    
    def add_tool(self, tool_name: str, tool_config: Dict[str, Any] = None):
        """Add a tool to the agent's toolkit."""
        self.available_tools.append(tool_name)
        if tool_config:
            self.knowledge_base[f"tool_{tool_name}"] = tool_config
    
    def record_task_completion(self, task_name: str, success: bool, confidence: float, metadata: Dict[str, Any] = None):
        """Record completion of a task."""
        self.task_history.append({
            "task": task_name,
            "success": success,
            "confidence": confidence,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        })
        
        # Update metrics
        successful_tasks = sum(1 for task in self.task_history if task["success"])
        self.task_success_rate = successful_tasks / len(self.task_history)
        
        confidences = [task["confidence"] for task in self.task_history]
        self.average_confidence = sum(confidences) / len(confidences)


class ContextManager:
    """Central context management system."""
    
    def __init__(self):
        self.active_workflows: Dict[str, WorkflowContext] = {}
        self.context_templates: Dict[ProcessingPhase, Dict[str, Any]] = self._build_context_templates()
    
    def create_workflow_context(self, prp_path: str) -> WorkflowContext:
        """Create a new workflow context."""
        workflow_id = str(uuid.uuid4())
        
        context = WorkflowContext(
            workflow_id=workflow_id,
            prp_source=prp_path,
            timestamp=datetime.now(),
            current_phase=ProcessingPhase.PARSING
        )
        
        self.active_workflows[workflow_id] = context
        return context
    
    def create_phase_context(self, workflow_context: WorkflowContext, phase: ProcessingPhase) -> PhaseContext:
        """Create a phase context within a workflow."""
        phase_context = PhaseContext(
            phase=phase,
            workflow_context=workflow_context,
            start_time=datetime.now()
        )
        
        # Apply phase-specific context template
        if phase in self.context_templates:
            template = self.context_templates[phase]
            phase_context.processing_metadata.update(template)
        
        workflow_context.phase_contexts[phase.value] = phase_context
        workflow_context.current_phase = phase
        
        return phase_context
    
    def propagate_context(self, source_phase: PhaseContext, target_phase: ProcessingPhase) -> Dict[str, Any]:
        """Propagate context from one phase to another."""
        propagated_data = {}
        
        # Extract propagatable data based on phase transition
        if source_phase.phase == ProcessingPhase.PARSING and target_phase == ProcessingPhase.ANALYSIS:
            propagated_data = {
                "prp_analysis": source_phase.workflow_context.prp_analysis,
                "parsing_confidence": source_phase.confidence_score,
                "extracted_entities": source_phase.processing_metadata.get("extracted_entities", []),
                "semantic_hints": source_phase.processing_metadata.get("semantic_hints", {})
            }
        
        elif source_phase.phase == ProcessingPhase.ANALYSIS and target_phase == ProcessingPhase.PATTERN_SELECTION:
            propagated_data = {
                "project_analysis": source_phase.workflow_context.project_analysis,
                "complexity_breakdown": source_phase.processing_metadata.get("complexity_breakdown", {}),
                "technical_constraints": source_phase.processing_metadata.get("technical_constraints", {}),
                "recommended_patterns": source_phase.processing_metadata.get("recommended_patterns", [])
            }
        
        elif source_phase.phase == ProcessingPhase.PATTERN_SELECTION and target_phase == ProcessingPhase.CONFIG_GENERATION:
            propagated_data = {
                "selected_pattern": source_phase.workflow_context.selected_pattern,
                "pattern_rationale": source_phase.processing_metadata.get("selection_rationale", ""),
                "customization_hints": source_phase.processing_metadata.get("customization_hints", {}),
                "alternative_patterns": source_phase.processing_metadata.get("alternatives", [])
            }
        
        return propagated_data
    
    def update_quality_metrics(self, workflow_context: WorkflowContext, phase: ProcessingPhase, metrics: Dict[str, float]):
        """Update quality metrics for a specific phase."""
        if phase == ProcessingPhase.PARSING:
            workflow_context.quality_metrics.parsing_completeness = metrics.get("completeness", 0.0)
        elif phase == ProcessingPhase.ANALYSIS:
            workflow_context.quality_metrics.analysis_confidence = metrics.get("confidence", 0.0)
        elif phase == ProcessingPhase.PATTERN_SELECTION:
            workflow_context.quality_metrics.pattern_match_score = metrics.get("match_score", 0.0)
        elif phase == ProcessingPhase.CONFIG_GENERATION:
            workflow_context.quality_metrics.config_validation_score = metrics.get("validation_score", 0.0)
        
        workflow_context.quality_metrics.calculate_overall_quality()
    
    def record_data_transformation(self, workflow_context: WorkflowContext, phase: ProcessingPhase, 
                                 input_data: Any, output_data: Any, confidence: float):
        """Record a data transformation in the workflow."""
        workflow_context.data_lineage.add_transformation(phase, input_data, output_data, confidence)
    
    def get_context_summary(self, workflow_context: WorkflowContext) -> Dict[str, Any]:
        """Get a summary of the workflow context."""
        return {
            "workflow_id": workflow_context.workflow_id,
            "current_phase": workflow_context.current_phase.value,
            "overall_quality": workflow_context.quality_metrics.overall_quality,
            "confidence_evolution": workflow_context.data_lineage.confidence_evolution,
            "phases_completed": len(workflow_context.phase_contexts),
            "total_transformations": len(workflow_context.data_lineage.transformations)
        }
    
    def _build_context_templates(self) -> Dict[ProcessingPhase, Dict[str, Any]]:
        """Build context templates for each processing phase."""
        return {
            ProcessingPhase.PARSING: {
                "expected_sections": ["name", "goal", "why", "what", "success_criteria"],
                "extraction_tools": ["regex", "yaml_parser", "nlp"],
                "quality_thresholds": {"completeness": 0.8, "confidence": 0.7}
            },
            ProcessingPhase.ANALYSIS: {
                "analysis_dimensions": ["technical", "organizational", "temporal"],
                "complexity_factors": ["tech_stack_size", "team_size", "timeline"],
                "confidence_factors": ["prp_completeness", "requirement_clarity"]
            },
            ProcessingPhase.PATTERN_SELECTION: {
                "scoring_weights": {"complexity": 0.4, "team_size": 0.3, "project_type": 0.2, "quality": 0.1},
                "selection_criteria": ["best_fit", "proven_success", "team_familiarity"],
                "fallback_patterns": ["hierarchical", "hybrid"]
            },
            ProcessingPhase.CONFIG_GENERATION: {
                "config_modules": ["orchestrator", "memory", "coordination", "mcp", "logging"],
                "optimization_goals": ["performance", "security", "maintainability"],
                "validation_rules": ["format_compliance", "parameter_ranges", "security_policies"]
            }
        }


# Context-aware processing decorators
def with_context(phase: ProcessingPhase):
    """Decorator to automatically manage context for processing functions."""
    def decorator(func):
        async def wrapper(self, *args, **kwargs):
            # Get or create workflow context
            workflow_context = kwargs.get('workflow_context') or getattr(self, '_workflow_context', None)
            if not workflow_context:
                raise ValueError("No workflow context available")
            
            # Create phase context
            context_manager = getattr(self, 'context_manager', ContextManager())
            phase_context = context_manager.create_phase_context(workflow_context, phase)
            
            try:
                # Execute the function with phase context
                result = await func(self, *args, phase_context=phase_context, **kwargs)
                
                # Record successful completion
                phase_context.end_time = datetime.now()
                phase_context.output_data = result
                
                return result
            
            except Exception as e:
                # Record failure
                phase_context.end_time = datetime.now()
                phase_context.processing_metadata["error"] = str(e)
                raise
        
        return wrapper
    return decorator
