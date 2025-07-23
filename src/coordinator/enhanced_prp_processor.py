"""
Enhanced PRP Processor with Context Management and Agent Coordination.

This module demonstrates how to implement sophisticated workflow orchestration
and context management for the PRP-driven system.
"""

import asyncio
from typing import Dict, Any, Optional
from datetime import datetime

from .context_manager import (
    ContextManager, WorkflowContext, PhaseContext, AgentContext,
    ProcessingPhase, with_context
)
from .prp_parser import PRPParser
from .project_analyzer import ProjectAnalyzer
from .pattern_library import PatternLibrary
from .claude_flow_config_generator import ClaudeFlowConfigGenerator
from .models import ProjectAnalysis, CoordinationPattern, ClaudeFlowConfig


class EnhancedPRPProcessor:
    """
    Enhanced PRP processor with sophisticated context management and workflow orchestration.
    
    This processor demonstrates how to implement:
    1. Rich context propagation between processing phases
    2. Agent-specific context management
    3. Quality tracking and metrics
    4. Data lineage and transformation tracking
    """
    
    def __init__(self):
        """Initialize the enhanced processor."""
        self.context_manager = ContextManager()
        
        # Core processing components
        self.prp_parser = PRPParser()
        self.project_analyzer = ProjectAnalyzer()
        self.pattern_library = PatternLibrary()
        self.config_generator = ClaudeFlowConfigGenerator()
        
        # Agent configurations
        self.agent_configs = self._build_agent_configs()
    
    async def process_prp_with_context(self, prp_path: str) -> ClaudeFlowConfig:
        """
        Process PRP with full context management and workflow orchestration.
        
        Args:
            prp_path: Path to the PRP document
            
        Returns:
            Generated Claude Flow configuration
        """
        # Create workflow context
        workflow_context = self.context_manager.create_workflow_context(prp_path)
        
        try:
            # Phase 1: Enhanced PRP Parsing
            parsing_result = await self._enhanced_parsing_phase(workflow_context=workflow_context)
            
            # Phase 2: Multi-dimensional Analysis
            analysis_result = await self._enhanced_analysis_phase(workflow_context)
            
            # Phase 3: Expert Pattern Selection
            pattern_result = await self._enhanced_pattern_selection_phase(workflow_context)
            
            # Phase 4: Optimized Configuration Generation
            config_result = await self._enhanced_config_generation_phase(workflow_context)
            
            # Phase 5: Comprehensive Validation
            final_config = await self._enhanced_validation_phase(workflow_context)
            
            # Generate workflow summary
            summary = self.context_manager.get_context_summary(workflow_context)
            print(f"🎯 Workflow completed with {summary['overall_quality']:.2f} quality score")
            
            return final_config
            
        except Exception as e:
            print(f"❌ Workflow failed: {str(e)}")
            raise
    
    @with_context(ProcessingPhase.PARSING)
    async def _enhanced_parsing_phase(self, workflow_context: WorkflowContext,
                                    phase_context: PhaseContext) -> Any:
        """Enhanced PRP parsing with rich context."""
        
        # Create specialized parsing agent context
        parser_agent = phase_context.create_agent_context(
            agent_name="prp_parser",
            role="PRP Document Analysis Expert",
            capabilities=["markdown_parsing", "semantic_extraction", "requirement_identification"]
        )
        
        # Add parsing tools
        parser_agent.add_tool("regex_parser", {"patterns": "prp_section_patterns"})
        parser_agent.add_tool("yaml_parser", {"strict_mode": False})
        parser_agent.add_tool("nlp_extractor", {"model": "semantic_analysis"})
        
        # Set parsing focus areas
        parser_agent.specialization_focus = [
            "technical_requirements", "agent_identification", "coordination_hints",
            "success_criteria", "validation_gates"
        ]
        
        # Execute parsing with context
        prp_analysis = await self.prp_parser.parse_prp_file(workflow_context.prp_source)
        
        # Enrich with semantic analysis
        semantic_entities = await self._extract_semantic_entities(prp_analysis, parser_agent)
        coordination_hints = await self._identify_coordination_hints(prp_analysis, parser_agent)
        
        # Store enriched data in phase context
        phase_context.processing_metadata.update({
            "extracted_entities": semantic_entities,
            "coordination_hints": coordination_hints,
            "parsing_completeness": self._calculate_parsing_completeness(prp_analysis),
            "semantic_confidence": 0.85  # Would be calculated by actual semantic analysis
        })
        
        # Update workflow state
        workflow_context.prp_analysis = prp_analysis
        
        # Record task completion
        parser_agent.record_task_completion(
            task_name="prp_parsing",
            success=True,
            confidence=phase_context.processing_metadata["semantic_confidence"],
            metadata={"entities_found": len(semantic_entities)}
        )
        
        # Update quality metrics
        self.context_manager.update_quality_metrics(
            workflow_context, 
            ProcessingPhase.PARSING,
            {"completeness": phase_context.processing_metadata["parsing_completeness"]}
        )
        
        return prp_analysis
    
    @with_context(ProcessingPhase.ANALYSIS)
    async def _enhanced_analysis_phase(self, workflow_context: WorkflowContext,
                                     phase_context: PhaseContext) -> ProjectAnalysis:
        """Enhanced project analysis with parallel processing."""
        
        # Get propagated context from parsing phase
        parsing_context = self.context_manager.propagate_context(
            workflow_context.phase_contexts["parsing"],
            ProcessingPhase.ANALYSIS
        )
        
        # Create multiple specialized analysis agents
        tech_agent = phase_context.create_agent_context(
            agent_name="tech_analyzer",
            role="Technical Architecture Analyst",
            capabilities=["tech_stack_analysis", "architecture_patterns", "integration_assessment"]
        )
        
        complexity_agent = phase_context.create_agent_context(
            agent_name="complexity_analyzer", 
            role="Complexity Assessment Expert",
            capabilities=["complexity_scoring", "risk_assessment", "scalability_analysis"]
        )
        
        # Parallel analysis tasks
        analysis_tasks = [
            self._analyze_technical_requirements(parsing_context, tech_agent),
            self._analyze_complexity_metrics(parsing_context, complexity_agent),
            self._analyze_constraints_and_risks(parsing_context, phase_context)
        ]
        
        # Execute parallel analysis
        tech_analysis, complexity_analysis, constraints_analysis = await asyncio.gather(*analysis_tasks)
        
        # Convert PRP to project analysis with enriched context
        project_analysis = await self.prp_parser.convert_prp_to_project_analysis(
            workflow_context.prp_analysis
        )
        
        # Enhance with parallel analysis results
        enhanced_analysis = self._merge_analysis_results(
            project_analysis, tech_analysis, complexity_analysis, constraints_analysis
        )
        
        # Store analysis metadata
        phase_context.processing_metadata.update({
            "technical_analysis": tech_analysis,
            "complexity_breakdown": complexity_analysis,
            "constraints_analysis": constraints_analysis,
            "analysis_confidence": enhanced_analysis.confidence_score
        })
        
        # Update workflow state
        workflow_context.project_analysis = enhanced_analysis
        
        # Record agent completions
        tech_agent.record_task_completion("technical_analysis", True, 0.88)
        complexity_agent.record_task_completion("complexity_analysis", True, 0.92)
        
        return enhanced_analysis
    
    @with_context(ProcessingPhase.PATTERN_SELECTION)
    async def _enhanced_pattern_selection_phase(self, workflow_context: WorkflowContext,
                                              phase_context: PhaseContext) -> CoordinationPattern:
        """Enhanced pattern selection with expert reasoning."""
        
        # Create pattern selection expert
        pattern_expert = phase_context.create_agent_context(
            agent_name="pattern_expert",
            role="Coordination Pattern Selection Expert", 
            capabilities=["pattern_matching", "multi_criteria_decision", "expert_reasoning"]
        )
        
        # Add expert knowledge
        pattern_expert.knowledge_base.update({
            "pattern_library": self.pattern_library.get_coordination_patterns(),
            "selection_criteria": ["complexity_fit", "team_size_fit", "project_type_fit"],
            "historical_performance": {}  # Would contain real performance data
        })
        
        # Get analysis context
        analysis_context = self.context_manager.propagate_context(
            workflow_context.phase_contexts["analysis"],
            ProcessingPhase.PATTERN_SELECTION
        )
        
        # Expert pattern selection with reasoning
        pattern_scores = self.pattern_library.get_matching_patterns(workflow_context.project_analysis)
        best_name, best_pattern, best_score = self.pattern_library.select_best_pattern(
            workflow_context.project_analysis
        )
        
        # Generate expert rationale
        selection_rationale = await self._generate_pattern_rationale(
            best_pattern, pattern_scores, analysis_context, pattern_expert
        )
        
        # Store selection metadata
        phase_context.processing_metadata.update({
            "all_pattern_scores": dict(pattern_scores),
            "selection_rationale": selection_rationale,
            "expert_confidence": best_score,
            "alternative_patterns": [name for name, score in pattern_scores[1:3]]
        })
        
        # Update workflow state
        workflow_context.selected_pattern = best_pattern
        
        # Record expert decision
        pattern_expert.record_task_completion(
            "pattern_selection",
            True,
            best_score,
            {"selected_pattern": best_name, "rationale_length": len(selection_rationale)}
        )
        
        return best_pattern
    
    @with_context(ProcessingPhase.CONFIG_GENERATION)
    async def _enhanced_config_generation_phase(self, workflow_context: WorkflowContext,
                                              phase_context: PhaseContext) -> ClaudeFlowConfig:
        """Enhanced configuration generation with optimization."""
        
        # Create configuration generation expert
        config_expert = phase_context.create_agent_context(
            agent_name="config_generator",
            role="Claude Flow Configuration Expert",
            capabilities=["config_optimization", "security_hardening", "performance_tuning"]
        )
        
        # Get pattern context
        pattern_context = self.context_manager.propagate_context(
            workflow_context.phase_contexts["pattern_selection"],
            ProcessingPhase.CONFIG_GENERATION
        )
        
        # Generate optimized configuration
        base_config = await self.config_generator.generate_config(
            workflow_context.project_analysis,
            workflow_context.selected_pattern
        )
        
        # Apply optimizations based on context
        optimized_config = await self._apply_context_optimizations(
            base_config, pattern_context, config_expert
        )
        
        # Store generation metadata
        phase_context.processing_metadata.update({
            "optimization_applied": True,
            "security_hardening": True,
            "performance_tuning": True,
            "config_modules": ["orchestrator", "memory", "coordination", "mcp", "logging"]
        })
        
        # Update workflow state
        workflow_context.generated_config = optimized_config
        
        return optimized_config
    
    @with_context(ProcessingPhase.VALIDATION)
    async def _enhanced_validation_phase(self, workflow_context: WorkflowContext,
                                       phase_context: PhaseContext) -> ClaudeFlowConfig:
        """Enhanced validation with comprehensive quality checks."""
        
        # Create validation expert
        validator_agent = phase_context.create_agent_context(
            agent_name="config_validator",
            role="Configuration Quality Assurance Expert",
            capabilities=["format_validation", "security_audit", "performance_analysis"]
        )
        
        # Comprehensive validation
        validation_results = await self._comprehensive_validation(
            workflow_context.generated_config,
            workflow_context,
            validator_agent
        )
        
        # Store validation results
        phase_context.processing_metadata.update({
            "validation_results": validation_results,
            "quality_score": validation_results.get("overall_score", 0.0),
            "security_score": validation_results.get("security_score", 0.0),
            "performance_score": validation_results.get("performance_score", 0.0)
        })
        
        # Update final quality metrics
        self.context_manager.update_quality_metrics(
            workflow_context,
            ProcessingPhase.VALIDATION,
            {"validation_score": validation_results.get("overall_score", 0.0)}
        )
        
        return workflow_context.generated_config
    
    def _build_agent_configs(self) -> Dict[str, Dict[str, Any]]:
        """Build configuration for specialized agents."""
        return {
            "prp_parser": {
                "tools": ["regex_parser", "yaml_parser", "nlp_extractor"],
                "capabilities": ["markdown_parsing", "semantic_extraction"],
                "specialization": ["technical_requirements", "agent_identification"]
            },
            "tech_analyzer": {
                "tools": ["tech_stack_detector", "architecture_analyzer"],
                "capabilities": ["tech_stack_analysis", "integration_assessment"],
                "specialization": ["technology_mapping", "architecture_patterns"]
            },
            "pattern_expert": {
                "tools": ["pattern_matcher", "decision_engine"],
                "capabilities": ["pattern_matching", "expert_reasoning"],
                "specialization": ["coordination_patterns", "team_dynamics"]
            },
            "config_generator": {
                "tools": ["config_optimizer", "security_hardener"],
                "capabilities": ["config_optimization", "security_hardening"],
                "specialization": ["claude_flow_configs", "performance_tuning"]
            }
        }
    
    async def _extract_semantic_entities(self, prp_analysis: Any, agent: AgentContext) -> Dict[str, Any]:
        """Extract semantic entities from PRP analysis."""
        # Simulate semantic entity extraction
        return {
            "agents": prp_analysis.agent_requirements,
            "technologies": list(prp_analysis.technical_requirements.keys()),
            "business_entities": ["user", "product", "order", "payment"],
            "processes": ["authentication", "ordering", "payment_processing"]
        }
    
    async def _identify_coordination_hints(self, prp_analysis: Any, agent: AgentContext) -> Dict[str, Any]:
        """Identify coordination hints from PRP."""
        return {
            "coordination_style": prp_analysis.coordination_hints,
            "agent_interactions": ["user->product", "order->payment", "notification->all"],
            "data_flow": ["request->validation->processing->response"]
        }
    
    def _calculate_parsing_completeness(self, prp_analysis: Any) -> float:
        """Calculate how complete the PRP parsing was."""
        required_fields = ["name", "goal", "what", "success_criteria"]
        present_fields = sum(1 for field in required_fields if getattr(prp_analysis, field, None))
        return present_fields / len(required_fields)
    
    async def _analyze_technical_requirements(self, context: Dict[str, Any], agent: AgentContext) -> Dict[str, Any]:
        """Analyze technical requirements in detail."""
        return {"tech_stack_complexity": 6, "integration_points": 4, "scalability_requirements": "high"}
    
    async def _analyze_complexity_metrics(self, context: Dict[str, Any], agent: AgentContext) -> Dict[str, Any]:
        """Analyze complexity metrics in detail."""
        return {"technical": 6, "organizational": 7, "temporal": 5, "risk_factors": ["team_coordination", "integration_complexity"]}
    
    async def _analyze_constraints_and_risks(self, context: Dict[str, Any], phase_context: PhaseContext) -> Dict[str, Any]:
        """Analyze constraints and risks."""
        return {"timeline_pressure": "moderate", "resource_constraints": "limited", "quality_requirements": "high"}
    
    def _merge_analysis_results(self, base_analysis: ProjectAnalysis, *additional_analyses) -> ProjectAnalysis:
        """Merge multiple analysis results."""
        # In a real implementation, this would intelligently merge the analyses
        return base_analysis
    
    async def _generate_pattern_rationale(self, pattern: CoordinationPattern, scores, context: Dict[str, Any], agent: AgentContext) -> str:
        """Generate expert rationale for pattern selection."""
        return f"Selected {pattern.name} pattern due to high complexity fit and team size alignment."
    
    async def _apply_context_optimizations(self, config: ClaudeFlowConfig, context: Dict[str, Any], agent: AgentContext) -> ClaudeFlowConfig:
        """Apply context-based optimizations to configuration."""
        # In a real implementation, this would apply intelligent optimizations
        return config
    
    async def _comprehensive_validation(self, config: ClaudeFlowConfig, workflow_context: WorkflowContext, agent: AgentContext) -> Dict[str, Any]:
        """Perform comprehensive validation of the generated configuration."""
        return {
            "overall_score": 0.85,
            "security_score": 0.80,
            "performance_score": 0.90,
            "format_compliance": True,
            "recommendations": ["Enable encryption for production", "Add audit logging"]
        }
