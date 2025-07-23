"""
Contextual Knowledge Index for Claude Flow Configuration.

This module implements Context Engineering principles by providing precise,
actionable documentation references and implementation guidance for each agent.
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum

from .claude_flow_llm_docs import ClaudeFlowLLMDocs, DocumentType, UsageContext


class KnowledgeType(Enum):
    """Types of knowledge references."""
    CRITICAL_PATTERN = "critical_pattern"
    IMPLEMENTATION_EXAMPLE = "implementation_example"
    REFERENCE_CODE = "reference_code"
    OFFICIAL_DOC = "official_doc"
    BEST_PRACTICE = "best_practice"


class ActionType(Enum):
    """Specific actions to take with the knowledge."""
    READ_FIRST = "READ_FIRST"
    STUDY_PATTERN = "STUDY_PATTERN"
    COPY_PATTERN = "COPY_PATTERN"
    MIRROR_IMPLEMENTATION = "MIRROR_IMPLEMENTATION"
    FOLLOW_EXAMPLE = "FOLLOW_EXAMPLE"
    REFERENCE_WHEN_NEEDED = "REFERENCE_WHEN_NEEDED"


@dataclass
class KnowledgeReference:
    """A specific knowledge reference with context and action."""
    knowledge_type: KnowledgeType
    source_type: str  # "file", "docfile", "url"
    source_path: str
    why: str
    action: ActionType
    priority: int  # 1 = highest priority
    applicable_contexts: List[str]
    prerequisites: List[str] = None


class ContextualKnowledgeIndex:
    """
    Context Engineering approach to knowledge management.
    
    Instead of abstract recommendations, provides specific, actionable
    references to documentation, examples, and implementations.
    """
    
    def __init__(self):
        """Initialize the contextual knowledge index with LLM-optimized docs."""
        self.llm_docs = ClaudeFlowLLMDocs()
        self.knowledge_index = self._build_knowledge_index()
        self.agent_contexts = self._build_agent_contexts()
        self.task_contexts = self._build_task_contexts()
    
    def get_contextual_guidance(self, 
                              agent_role: str, 
                              task_context: str,
                              project_characteristics: Dict[str, Any]) -> Dict[str, List[KnowledgeReference]]:
        """
        Get contextual guidance for a specific agent and task.
        
        Args:
            agent_role: Role of the agent (e.g., "orchestrator_config_generator")
            task_context: Current task context (e.g., "high_performance_setup")
            project_characteristics: Project-specific characteristics
            
        Returns:
            Organized knowledge references by priority and type
        """
        # Get base knowledge for agent role
        base_knowledge = self.agent_contexts.get(agent_role, [])
        
        # Get task-specific knowledge
        task_knowledge = self.task_contexts.get(task_context, [])
        
        # Filter by project characteristics
        filtered_knowledge = self._filter_by_characteristics(
            base_knowledge + task_knowledge, 
            project_characteristics
        )
        
        # Organize by priority and type
        return self._organize_knowledge_references(filtered_knowledge)
    
    def _build_knowledge_index(self) -> Dict[str, List[KnowledgeReference]]:
        """Build the comprehensive knowledge index."""
        return {
            "claude_flow_orchestrator": [
                KnowledgeReference(
                    knowledge_type=KnowledgeType.CRITICAL_PATTERN,
                    source_type="docfile",
                    source_path="claude-flow/docs/orchestrator-patterns.md",
                    why="Core orchestrator patterns for multi-agent coordination - ESSENTIAL for understanding agent pool management",
                    action=ActionType.READ_FIRST,
                    priority=1,
                    applicable_contexts=["orchestrator_config", "multi_agent_setup"]
                ),
                KnowledgeReference(
                    knowledge_type=KnowledgeType.IMPLEMENTATION_EXAMPLE,
                    source_type="file",
                    source_path="claude-flow/examples/production-orchestrator.json",
                    why="Production-tested orchestrator configuration with 50+ agents - PROVEN patterns for enterprise scale",
                    action=ActionType.COPY_PATTERN,
                    priority=2,
                    applicable_contexts=["high_performance", "enterprise_scale"]
                ),
                KnowledgeReference(
                    knowledge_type=KnowledgeType.REFERENCE_CODE,
                    source_type="file", 
                    source_path="claude-flow/src/orchestrator/resource-allocation.ts",
                    why="Resource allocation algorithms - STUDY the balanced vs performance strategies",
                    action=ActionType.STUDY_PATTERN,
                    priority=3,
                    applicable_contexts=["resource_optimization", "performance_tuning"]
                )
            ],
            
            "claude_flow_memory": [
                KnowledgeReference(
                    knowledge_type=KnowledgeType.CRITICAL_PATTERN,
                    source_type="docfile",
                    source_path="claude-flow/docs/memory-backends.md",
                    why="Memory backend selection criteria - CRITICAL for multi-agent systems",
                    action=ActionType.READ_FIRST,
                    priority=1,
                    applicable_contexts=["memory_config", "backend_selection"]
                ),
                KnowledgeReference(
                    knowledge_type=KnowledgeType.IMPLEMENTATION_EXAMPLE,
                    source_type="file",
                    source_path="claude-flow/examples/hybrid-memory-config.json",
                    why="Hybrid backend configuration for 1000+ MB cache - FOLLOW this pattern for performance",
                    action=ActionType.FOLLOW_EXAMPLE,
                    priority=2,
                    applicable_contexts=["high_performance", "large_cache"]
                )
            ],
            
            "claude_flow_coordination": [
                KnowledgeReference(
                    knowledge_type=KnowledgeType.CRITICAL_PATTERN,
                    source_type="docfile",
                    source_path="claude-flow/docs/coordination-strategies.md",
                    why="Load balancing and scheduling algorithms - ESSENTIAL for multi-agent coordination",
                    action=ActionType.READ_FIRST,
                    priority=1,
                    applicable_contexts=["coordination_config", "load_balancing"]
                ),
                KnowledgeReference(
                    knowledge_type=KnowledgeType.REFERENCE_CODE,
                    source_type="file",
                    source_path="claude-flow/src/coordination/weighted-balancer.ts",
                    why="Weighted load balancing implementation - MIRROR this for heterogeneous agents",
                    action=ActionType.MIRROR_IMPLEMENTATION,
                    priority=2,
                    applicable_contexts=["weighted_balancing", "agent_specialization"]
                )
            ],
            
            "claude_flow_security": [
                KnowledgeReference(
                    knowledge_type=KnowledgeType.BEST_PRACTICE,
                    source_type="docfile",
                    source_path="claude-flow/docs/security-guidelines.md",
                    why="Security configuration for production environments",
                    action=ActionType.REFERENCE_WHEN_NEEDED,
                    priority=4,
                    applicable_contexts=["production_deployment", "security_hardening"]
                )
            ],
            
            "claude_flow_terminal": [
                KnowledgeReference(
                    knowledge_type=KnowledgeType.CRITICAL_PATTERN,
                    source_type="docfile",
                    source_path="claude-flow/docs/terminal-management.md",
                    why="Terminal configuration and security patterns - ESSENTIAL for command execution",
                    action=ActionType.READ_FIRST,
                    priority=1,
                    applicable_contexts=["terminal_config", "command_execution", "security"]
                ),
                KnowledgeReference(
                    knowledge_type=KnowledgeType.IMPLEMENTATION_EXAMPLE,
                    source_type="file",
                    source_path="claude-flow/examples/secure-terminal-config.json",
                    why="Production-ready terminal security configuration - COPY for secure setups",
                    action=ActionType.COPY_PATTERN,
                    priority=2,
                    applicable_contexts=["production_deployment", "security_hardening"]
                )
            ],

            "claude_flow_mcp": [
                KnowledgeReference(
                    knowledge_type=KnowledgeType.CRITICAL_PATTERN,
                    source_type="docfile",
                    source_path="claude-flow/docs/mcp-configuration.md",
                    why="MCP transport and security configuration - CRITICAL for tool integration",
                    action=ActionType.READ_FIRST,
                    priority=1,
                    applicable_contexts=["mcp_config", "tool_integration"]
                ),
                KnowledgeReference(
                    knowledge_type=KnowledgeType.IMPLEMENTATION_EXAMPLE,
                    source_type="file",
                    source_path="claude-flow/examples/enterprise-mcp-config.json",
                    why="Enterprise MCP configuration with authentication - FOLLOW for production",
                    action=ActionType.FOLLOW_EXAMPLE,
                    priority=2,
                    applicable_contexts=["enterprise_deployment", "authentication"]
                )
            ],

            "claude_flow_logging": [
                KnowledgeReference(
                    knowledge_type=KnowledgeType.CRITICAL_PATTERN,
                    source_type="docfile",
                    source_path="claude-flow/docs/logging-configuration.md",
                    why="Logging levels and audit configuration - ESSENTIAL for monitoring",
                    action=ActionType.READ_FIRST,
                    priority=1,
                    applicable_contexts=["logging_config", "monitoring", "debugging"]
                ),
                KnowledgeReference(
                    knowledge_type=KnowledgeType.IMPLEMENTATION_EXAMPLE,
                    source_type="file",
                    source_path="claude-flow/examples/production-logging-config.json",
                    why="Production logging with audit trail - COPY for compliance",
                    action=ActionType.COPY_PATTERN,
                    priority=2,
                    applicable_contexts=["production_deployment", "compliance"]
                )
            ],

            "claude_flow_monitoring": [
                KnowledgeReference(
                    knowledge_type=KnowledgeType.BEST_PRACTICE,
                    source_type="docfile",
                    source_path="claude-flow/docs/monitoring-best-practices.md",
                    why="Performance monitoring and alerting strategies",
                    action=ActionType.REFERENCE_WHEN_NEEDED,
                    priority=3,
                    applicable_contexts=["performance_monitoring", "alerting"]
                )
            ],

            "claude_flow_official": [
                KnowledgeReference(
                    knowledge_type=KnowledgeType.OFFICIAL_DOC,
                    source_type="url",
                    source_path="https://claude-flow.dev/docs/configuration",
                    why="Official configuration reference - AUTHORITATIVE source for all parameters",
                    action=ActionType.REFERENCE_WHEN_NEEDED,
                    priority=5,
                    applicable_contexts=["parameter_validation", "official_reference"]
                )
            ]
        }
    
    def _build_agent_contexts(self) -> Dict[str, List[str]]:
        """Map agent roles to relevant knowledge domains."""
        return {
            "orchestrator_config_generator": [
                "claude_flow_orchestrator",
                "claude_flow_coordination",
                "claude_flow_official"
            ],
            "memory_config_generator": [
                "claude_flow_memory",
                "claude_flow_official"
            ],
            "coordination_config_generator": [
                "claude_flow_coordination",
                "claude_flow_orchestrator",
                "claude_flow_official"
            ],
            "terminal_config_generator": [
                "claude_flow_terminal",
                "claude_flow_security",
                "claude_flow_official"
            ],
            "mcp_config_generator": [
                "claude_flow_mcp",
                "claude_flow_security",
                "claude_flow_official"
            ],
            "logging_config_generator": [
                "claude_flow_logging",
                "claude_flow_monitoring",
                "claude_flow_official"
            ],
            "security_config_generator": [
                "claude_flow_security",
                "claude_flow_official"
            ]
        }
    
    def _build_task_contexts(self) -> Dict[str, List[str]]:
        """Map task contexts to relevant knowledge domains."""
        return {
            "high_performance_setup": [
                "claude_flow_orchestrator",
                "claude_flow_memory",
                "claude_flow_coordination",
                "claude_flow_terminal"
            ],
            "enterprise_deployment": [
                "claude_flow_orchestrator",
                "claude_flow_security",
                "claude_flow_coordination",
                "claude_flow_mcp",
                "claude_flow_logging"
            ],
            "multi_agent_coordination": [
                "claude_flow_orchestrator",
                "claude_flow_coordination",
                "claude_flow_terminal"
            ],
            "production_optimization": [
                "claude_flow_orchestrator",
                "claude_flow_memory",
                "claude_flow_coordination",
                "claude_flow_logging",
                "claude_flow_monitoring"
            ],
            "security_hardening": [
                "claude_flow_security",
                "claude_flow_terminal",
                "claude_flow_mcp",
                "claude_flow_logging"
            ],
            "development_setup": [
                "claude_flow_orchestrator",
                "claude_flow_memory",
                "claude_flow_terminal",
                "claude_flow_logging"
            ],
            "monitoring_setup": [
                "claude_flow_logging",
                "claude_flow_monitoring",
                "claude_flow_orchestrator"
            ]
        }
    
    def _filter_by_characteristics(self, 
                                 knowledge_refs: List[str], 
                                 characteristics: Dict[str, Any]) -> List[KnowledgeReference]:
        """Filter knowledge references by project characteristics."""
        filtered_refs = []
        
        for domain in knowledge_refs:
            domain_refs = self.knowledge_index.get(domain, [])
            for ref in domain_refs:
                # Check if reference applies to current characteristics
                if self._is_applicable(ref, characteristics):
                    filtered_refs.append(ref)
        
        return filtered_refs
    
    def _is_applicable(self, ref: KnowledgeReference, characteristics: Dict[str, Any]) -> bool:
        """Check if a knowledge reference applies to current characteristics."""
        # Check complexity level
        if characteristics.get("complexity") == "high" and "high_performance" in ref.applicable_contexts:
            return True
        
        # Check team size
        if characteristics.get("team_size") == "large" and "enterprise_scale" in ref.applicable_contexts:
            return True
        
        # Check quality level
        if characteristics.get("quality") == "production" and "production_deployment" in ref.applicable_contexts:
            return True
        
        # Always include critical patterns
        if ref.knowledge_type == KnowledgeType.CRITICAL_PATTERN:
            return True
        
        return len(ref.applicable_contexts) == 0  # No specific context = always applicable
    
    def _organize_knowledge_references(self, refs: List[KnowledgeReference]) -> Dict[str, List[KnowledgeReference]]:
        """Organize knowledge references by priority and type."""
        # Sort by priority
        sorted_refs = sorted(refs, key=lambda x: x.priority)
        
        # Group by action type for clear guidance
        organized = {
            "must_read_first": [],
            "study_patterns": [],
            "copy_examples": [],
            "mirror_implementations": [],
            "follow_examples": [],
            "reference_docs": []
        }
        
        action_mapping = {
            ActionType.READ_FIRST: "must_read_first",
            ActionType.STUDY_PATTERN: "study_patterns", 
            ActionType.COPY_PATTERN: "copy_examples",
            ActionType.MIRROR_IMPLEMENTATION: "mirror_implementations",
            ActionType.FOLLOW_EXAMPLE: "follow_examples",
            ActionType.REFERENCE_WHEN_NEEDED: "reference_docs"
        }
        
        for ref in sorted_refs:
            category = action_mapping.get(ref.action, "reference_docs")
            organized[category].append(ref)
        
        return organized


def format_contextual_guidance(guidance: Dict[str, List[KnowledgeReference]]) -> str:
    """Format contextual guidance for agent consumption."""
    formatted = "# Contextual Knowledge Guidance\n\n"
    
    for category, refs in guidance.items():
        if not refs:
            continue
            
        formatted += f"## {category.replace('_', ' ').title()}\n\n"
        
        for ref in refs:
            formatted += f"### {ref.source_path}\n"
            formatted += f"**Why**: {ref.why}\n"
            formatted += f"**Action**: {ref.action.value}\n"
            formatted += f"**Type**: {ref.knowledge_type.value}\n"
            if ref.prerequisites:
                formatted += f"**Prerequisites**: {', '.join(ref.prerequisites)}\n"
            formatted += "\n"
    
    return formatted
