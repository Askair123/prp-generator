"""
Claude Flow Knowledge Base for Coordinator Pattern System.

This module embeds comprehensive Claude Flow knowledge into agent contexts,
enabling intelligent configuration generation based on best practices.
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum


class ConfigurationDomain(Enum):
    """Configuration domains in Claude Flow."""
    ORCHESTRATOR = "orchestrator"
    TERMINAL = "terminal"
    MEMORY = "memory"
    COORDINATION = "coordination"
    MCP = "mcp"
    LOGGING = "logging"


class ProjectComplexity(Enum):
    """Project complexity levels."""
    SIMPLE = "simple"
    MODERATE = "moderate"
    COMPLEX = "complex"
    ENTERPRISE = "enterprise"


class QualityLevel(Enum):
    """Quality requirement levels."""
    PROTOTYPE = "prototype"
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    ENTERPRISE = "enterprise"
    MISSION_CRITICAL = "mission_critical"


@dataclass
class ClaudeFlowBestPractice:
    """Represents a Claude Flow best practice."""
    domain: ConfigurationDomain
    practice_name: str
    description: str
    applicable_scenarios: List[str]
    configuration_impact: Dict[str, Any]
    quality_level: QualityLevel
    complexity_level: ProjectComplexity
    rationale: str
    examples: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class ConfigurationPattern:
    """Configuration pattern for specific scenarios."""
    name: str
    description: str
    scenario: str
    configuration: Dict[str, Any]
    benefits: List[str]
    trade_offs: List[str]
    when_to_use: List[str]
    when_not_to_use: List[str]


class ClaudeFlowKnowledgeBase:
    """
    Comprehensive knowledge base of Claude Flow best practices and patterns.
    
    This knowledge base contains:
    1. Configuration best practices for different scenarios
    2. Performance optimization patterns
    3. Security hardening guidelines
    4. Scalability recommendations
    5. Agent coordination patterns
    """
    
    def __init__(self):
        """Initialize the knowledge base with Claude Flow expertise."""
        self.best_practices = self._build_best_practices()
        self.configuration_patterns = self._build_configuration_patterns()
        self.performance_guidelines = self._build_performance_guidelines()
        # 移除复杂的安全策略 - 保持系统简洁
        self.agent_patterns = self._build_agent_patterns()
        self.troubleshooting_guide = self._build_troubleshooting_guide()
    
    def get_recommendations_for_project(self, 
                                      complexity: ProjectComplexity,
                                      quality_level: QualityLevel,
                                      team_size: str,
                                      project_type: str) -> Dict[str, Any]:
        """
        Get comprehensive recommendations for a specific project profile.
        
        Args:
            complexity: Project complexity level
            quality_level: Required quality level
            team_size: Team size (solo, small, medium, large)
            project_type: Type of project (web_backend, data_processing, etc.)
            
        Returns:
            Comprehensive recommendations for Claude Flow configuration
        """
        recommendations = {
            "orchestrator": self._get_orchestrator_recommendations(complexity, team_size),
            "memory": self._get_memory_recommendations(complexity, quality_level),
            "coordination": self._get_coordination_recommendations(team_size, project_type),
            # 简化：移除复杂的安全配置
            "performance": self._get_performance_recommendations(complexity, project_type),
            "monitoring": self._get_monitoring_recommendations(quality_level),
            "best_practices": self._get_applicable_best_practices(complexity, quality_level)
        }
        
        return recommendations
    
    def _build_best_practices(self) -> List[ClaudeFlowBestPractice]:
        """Build comprehensive best practices database."""
        return [
            # Orchestrator Best Practices
            ClaudeFlowBestPractice(
                domain=ConfigurationDomain.ORCHESTRATOR,
                practice_name="Agent Pool Sizing",
                description="Optimize agent pool size based on project complexity and team size",
                applicable_scenarios=["multi-agent coordination", "resource optimization"],
                configuration_impact={
                    "maxConcurrentAgents": "Calculated based on complexity and team size",
                    "resourceAllocationStrategy": "balanced for most cases, performance for high-load"
                },
                quality_level=QualityLevel.PRODUCTION,
                complexity_level=ProjectComplexity.MODERATE,
                rationale="Proper agent pool sizing prevents resource contention and ensures optimal performance",
                examples=[
                    {"scenario": "Small team (2-5)", "maxConcurrentAgents": 8},
                    {"scenario": "Large team (20+)", "maxConcurrentAgents": 50}
                ]
            ),
            
            ClaudeFlowBestPractice(
                domain=ConfigurationDomain.ORCHESTRATOR,
                practice_name="Failover Configuration",
                description="Enable failover for production and enterprise systems",
                applicable_scenarios=["production deployment", "high availability"],
                configuration_impact={
                    "failover.enabled": True,
                    "failover.detectionThreshold": 10000,
                    "failover.recoveryStrategy": "restart"
                },
                quality_level=QualityLevel.PRODUCTION,
                complexity_level=ProjectComplexity.COMPLEX,
                rationale="Failover ensures system resilience and automatic recovery from failures"
            ),
            
            # Memory Best Practices
            ClaudeFlowBestPractice(
                domain=ConfigurationDomain.MEMORY,
                practice_name="Hybrid Backend Selection",
                description="Use hybrid backend for optimal performance and flexibility",
                applicable_scenarios=["multi-agent systems", "complex workflows"],
                configuration_impact={
                    "backend": "hybrid",
                    "cacheSizeMB": "Calculated based on project complexity",
                    "compressionEnabled": True
                },
                quality_level=QualityLevel.PRODUCTION,
                complexity_level=ProjectComplexity.MODERATE,
                rationale="Hybrid backend combines SQLite performance with Markdown readability"
            ),
            
            ClaudeFlowBestPractice(
                domain=ConfigurationDomain.MEMORY,
                practice_name="Encryption for Sensitive Data",
                description="Enable encryption for production and enterprise systems",
                applicable_scenarios=["sensitive data", "compliance requirements"],
                configuration_impact={
                    "encryptionEnabled": True,
                    "encryption.algorithm": "AES-256-GCM",
                    "encryption.keyRotation": "weekly"
                },
                quality_level=QualityLevel.ENTERPRISE,
                complexity_level=ProjectComplexity.COMPLEX,
                rationale="Encryption protects sensitive data and ensures compliance"
            ),
            
            # Coordination Best Practices
            ClaudeFlowBestPractice(
                domain=ConfigurationDomain.COORDINATION,
                practice_name="Weighted Load Balancing",
                description="Use weighted load balancing for heterogeneous agent capabilities",
                applicable_scenarios=["specialized agents", "performance optimization"],
                configuration_impact={
                    "loadBalancingStrategy": "weighted",
                    "scheduling.algorithm": "priority-queue",
                    "deadlockDetection": True
                },
                quality_level=QualityLevel.PRODUCTION,
                complexity_level=ProjectComplexity.MODERATE,
                rationale="Weighted balancing optimizes task distribution based on agent capabilities"
            ),
            
            # Security Best Practices
            ClaudeFlowBestPractice(
                domain=ConfigurationDomain.MCP,
                practice_name="Rate Limiting",
                description="Enable rate limiting to prevent abuse and ensure stability",
                applicable_scenarios=["production deployment", "external API access"],
                configuration_impact={
                    "rateLimiting.enabled": True,
                    "rateLimiting.requestsPerMinute": "Calculated based on expected load",
                    "rateLimiting.burstSize": 20
                },
                quality_level=QualityLevel.PRODUCTION,
                complexity_level=ProjectComplexity.SIMPLE,
                rationale="Rate limiting prevents system overload and ensures fair resource usage"
            ),
            
            # Terminal Best Practices
            ClaudeFlowBestPractice(
                domain=ConfigurationDomain.TERMINAL,
                practice_name="Command Sandboxing",
                description="Enable command sandboxing for security in production",
                applicable_scenarios=["production deployment", "security requirements"],
                configuration_impact={
                    "security.sandboxed": True,
                    "security.allowedCommands": "Whitelist based on project needs",
                    "security.maxExecutionTime": 600000
                },
                quality_level=QualityLevel.PRODUCTION,
                complexity_level=ProjectComplexity.MODERATE,
                rationale="Sandboxing prevents malicious command execution and limits security risks"
            )
        ]
    
    def _build_configuration_patterns(self) -> List[ConfigurationPattern]:
        """Build configuration patterns for common scenarios."""
        return [
            ConfigurationPattern(
                name="High-Performance Multi-Agent",
                description="Optimized for high-throughput multi-agent coordination",
                scenario="Large team with complex workflows requiring high performance",
                configuration={
                    "orchestrator": {
                        "maxConcurrentAgents": 50,
                        "resourceAllocationStrategy": "performance",
                        "agentRecycling": {"enabled": True, "maxTasks": 100}
                    },
                    "memory": {
                        "backend": "hybrid",
                        "cacheSizeMB": 2000,
                        "compressionEnabled": True
                    },
                    "coordination": {
                        "loadBalancingStrategy": "adaptive",
                        "scheduling": {"algorithm": "shortest-job-first"}
                    }
                },
                benefits=["High throughput", "Optimal resource utilization", "Adaptive performance"],
                trade_offs=["Higher memory usage", "Increased complexity"],
                when_to_use=["Large teams", "High-volume workflows", "Performance-critical applications"],
                when_not_to_use=["Small teams", "Simple workflows", "Resource-constrained environments"]
            ),
            
            ConfigurationPattern(
                name="Security-Hardened Enterprise",
                description="Maximum security configuration for enterprise environments",
                scenario="Enterprise deployment with strict security and compliance requirements",
                configuration={
                    "memory": {
                        "encryptionEnabled": True,
                        "backup": {"enabled": True, "encrypted": True}
                    },
                    "mcp": {
                        "authentication": {"enabled": True, "method": "certificate"},
                        "tlsEnabled": True,
                        "rateLimiting": {"enabled": True}
                    },
                    "terminal": {
                        "security": {
                            "sandboxed": True,
                            "allowedCommands": ["git.*", "npm.*", "python.*"],
                            "auditLogging": True
                        }
                    },
                    "logging": {
                        "audit": {"enabled": True, "retention": "7y"}
                    }
                },
                benefits=["Maximum security", "Compliance ready", "Audit trail"],
                trade_offs=["Performance overhead", "Configuration complexity"],
                when_to_use=["Enterprise environments", "Regulated industries", "Sensitive data"],
                when_not_to_use=["Development environments", "Prototype projects"]
            ),
            
            ConfigurationPattern(
                name="Resource-Optimized Development",
                description="Optimized for development environments with limited resources",
                scenario="Development and testing with resource constraints",
                configuration={
                    "orchestrator": {
                        "maxConcurrentAgents": 5,
                        "resourceAllocationStrategy": "memory-optimized"
                    },
                    "terminal": {
                        "poolSize": 3,
                        "commandTimeout": 60000
                    },
                    "memory": {
                        "cacheSizeMB": 100,
                        "retentionDays": 7,
                        "compressionEnabled": True
                    },
                    "logging": {
                        "level": "debug",
                        "destination": "console"
                    }
                },
                benefits=["Low resource usage", "Fast startup", "Development-friendly"],
                trade_offs=["Limited concurrency", "Shorter retention"],
                when_to_use=["Development", "Testing", "Resource-constrained environments"],
                when_not_to_use=["Production", "High-load scenarios"]
            )
        ]
    
    def _build_performance_guidelines(self) -> Dict[str, Any]:
        """Build performance optimization guidelines."""
        return {
            "agent_sizing": {
                "simple_projects": {"max_agents": 5, "rationale": "Minimal overhead for simple tasks"},
                "moderate_projects": {"max_agents": 15, "rationale": "Balanced performance and resource usage"},
                "complex_projects": {"max_agents": 30, "rationale": "High concurrency for complex workflows"},
                "enterprise_projects": {"max_agents": 50, "rationale": "Maximum throughput for enterprise scale"}
            },
            "memory_optimization": {
                "cache_sizing": {
                    "development": 100,  # MB
                    "production": 500,
                    "enterprise": 2000
                },
                "backend_selection": {
                    "simple": "sqlite",
                    "moderate": "hybrid",
                    "complex": "hybrid",
                    "enterprise": "distributed"
                }
            },
            "coordination_optimization": {
                "load_balancing": {
                    "small_team": "round-robin",
                    "medium_team": "weighted",
                    "large_team": "adaptive"
                },
                "scheduling": {
                    "simple_tasks": "fifo",
                    "mixed_tasks": "priority-queue",
                    "deadline_critical": "deadline-aware"
                }
            }
        }
    
    def _build_security_guidelines(self) -> Dict[str, Any]:
        """Build security hardening guidelines."""
        return {
            "encryption": {
                "development": {"enabled": False, "rationale": "Performance over security"},
                "production": {"enabled": True, "algorithm": "AES-256-GCM"},
                "enterprise": {"enabled": True, "algorithm": "AES-256-GCM", "keyRotation": "weekly"}
            },
            "authentication": {
                "development": {"enabled": False},
                "production": {"enabled": True, "method": "token"},
                "enterprise": {"enabled": True, "method": "certificate", "mfa": True}
            },
            "sandboxing": {
                "development": {"enabled": False},
                "production": {"enabled": True, "strict": False},
                "enterprise": {"enabled": True, "strict": True, "whitelist_only": True}
            },
            "audit_logging": {
                "development": {"enabled": False},
                "production": {"enabled": True, "retention": "90d"},
                "enterprise": {"enabled": True, "retention": "7y", "immutable": True}
            }
        }
    
    def _build_agent_patterns(self) -> Dict[str, Any]:
        """Build agent coordination patterns."""
        return {
            "hierarchical": {
                "description": "Central coordinator with specialized sub-agents",
                "best_for": ["Complex projects", "Large teams", "Clear authority structure"],
                "agent_config": {
                    "coordinator": {"count": 1, "capabilities": ["planning", "delegation"]},
                    "specialists": {"count": "variable", "capabilities": ["domain-specific"]}
                },
                "coordination_config": {
                    "loadBalancingStrategy": "weighted",
                    "scheduling": {"algorithm": "priority-queue"}
                }
            },
            "peer_to_peer": {
                "description": "Equal agents collaborating without central authority",
                "best_for": ["Research projects", "Small teams", "Collaborative work"],
                "agent_config": {
                    "peers": {"count": "3-8", "capabilities": ["collaborative", "autonomous"]}
                },
                "coordination_config": {
                    "loadBalancingStrategy": "round-robin",
                    "scheduling": {"algorithm": "consensus-based"}
                }
            },
            "pipeline": {
                "description": "Sequential processing with specialized stages",
                "best_for": ["Data processing", "Linear workflows", "Quality gates"],
                "agent_config": {
                    "stages": {"count": "variable", "capabilities": ["stage-specific"]}
                },
                "coordination_config": {
                    "loadBalancingStrategy": "pipeline",
                    "scheduling": {"algorithm": "fifo"}
                }
            }
        }
    
    def _build_troubleshooting_guide(self) -> Dict[str, Any]:
        """Build troubleshooting guide for common issues."""
        return {
            "performance_issues": {
                "high_memory_usage": {
                    "symptoms": ["Memory usage > 80%", "Slow response times"],
                    "solutions": ["Reduce cache size", "Enable compression", "Increase agent recycling"],
                    "config_changes": {"memory.cacheSizeMB": "reduce by 50%", "memory.compressionEnabled": True}
                },
                "agent_bottlenecks": {
                    "symptoms": ["High queue length", "Long wait times"],
                    "solutions": ["Increase agent pool", "Optimize load balancing"],
                    "config_changes": {"orchestrator.maxConcurrentAgents": "increase by 50%"}
                }
            },
            "security_issues": {
                "unauthorized_access": {
                    "symptoms": ["Unexpected commands", "Security alerts"],
                    "solutions": ["Enable authentication", "Restrict command whitelist"],
                    "config_changes": {"mcp.authentication.enabled": True, "terminal.security.sandboxed": True}
                }
            }
        }
    
    def _get_orchestrator_recommendations(self, complexity: ProjectComplexity, team_size: str) -> Dict[str, Any]:
        """Get orchestrator-specific recommendations."""
        base_agents = {"solo": 3, "small": 8, "medium": 15, "large": 30}
        complexity_multiplier = {
            ProjectComplexity.SIMPLE: 1.0,
            ProjectComplexity.MODERATE: 1.5,
            ProjectComplexity.COMPLEX: 2.0,
            ProjectComplexity.ENTERPRISE: 2.5
        }
        
        max_agents = int(base_agents.get(team_size, 8) * complexity_multiplier[complexity])
        
        return {
            "maxConcurrentAgents": min(max_agents, 50),  # Cap at 50
            "resourceAllocationStrategy": "performance" if complexity in [ProjectComplexity.COMPLEX, ProjectComplexity.ENTERPRISE] else "balanced",
            "failover": {"enabled": complexity in [ProjectComplexity.COMPLEX, ProjectComplexity.ENTERPRISE]},
            "agentRecycling": {"enabled": True, "maxTasks": 50 if complexity == ProjectComplexity.ENTERPRISE else 25}
        }
    
    def _get_memory_recommendations(self, complexity: ProjectComplexity, quality_level: QualityLevel) -> Dict[str, Any]:
        """Get memory-specific recommendations."""
        cache_sizes = {
            ProjectComplexity.SIMPLE: 100,
            ProjectComplexity.MODERATE: 500,
            ProjectComplexity.COMPLEX: 1000,
            ProjectComplexity.ENTERPRISE: 2000
        }
        
        return {
            "backend": "hybrid",
            "cacheSizeMB": cache_sizes[complexity],
            "encryptionEnabled": quality_level in [QualityLevel.ENTERPRISE, QualityLevel.MISSION_CRITICAL],
            "compressionEnabled": True,
            "retentionDays": 90 if quality_level in [QualityLevel.PRODUCTION, QualityLevel.ENTERPRISE] else 30
        }
    
    def _get_coordination_recommendations(self, team_size: str, project_type: str) -> Dict[str, Any]:
        """Get coordination-specific recommendations."""
        load_balancing = {
            "solo": "round-robin",
            "small": "weighted",
            "medium": "weighted",
            "large": "adaptive"
        }
        
        return {
            "loadBalancingStrategy": load_balancing.get(team_size, "weighted"),
            "scheduling": {"algorithm": "priority-queue"},
            "deadlockDetection": True,
            "maxRetries": 3
        }
    
    def _get_security_recommendations(self, quality_level: QualityLevel) -> Dict[str, Any]:
        """Get security-specific recommendations."""
        security_levels = {
            QualityLevel.PROTOTYPE: {"encryption": False, "auth": False, "sandbox": False},
            QualityLevel.DEVELOPMENT: {"encryption": False, "auth": False, "sandbox": False},
            QualityLevel.PRODUCTION: {"encryption": True, "auth": True, "sandbox": True},
            QualityLevel.ENTERPRISE: {"encryption": True, "auth": True, "sandbox": True},
            QualityLevel.MISSION_CRITICAL: {"encryption": True, "auth": True, "sandbox": True}
        }
        
        level = security_levels[quality_level]
        return {
            "encryption_enabled": level["encryption"],
            "authentication_required": level["auth"],
            "command_sandboxing": level["sandbox"],
            "audit_logging": quality_level in [QualityLevel.ENTERPRISE, QualityLevel.MISSION_CRITICAL]
        }
    
    def _get_performance_recommendations(self, complexity: ProjectComplexity, project_type: str) -> Dict[str, Any]:
        """Get performance-specific recommendations."""
        return {
            "terminal_pool_size": 20 if complexity == ProjectComplexity.ENTERPRISE else 10,
            "command_timeout": 600000 if complexity in [ProjectComplexity.COMPLEX, ProjectComplexity.ENTERPRISE] else 300000,
            "health_check_interval": 30000,
            "optimization_strategy": "performance" if complexity == ProjectComplexity.ENTERPRISE else "balanced"
        }
    
    def _get_monitoring_recommendations(self, quality_level: QualityLevel) -> Dict[str, Any]:
        """Get monitoring-specific recommendations."""
        return {
            "logging_level": "debug" if quality_level == QualityLevel.DEVELOPMENT else "info",
            "audit_enabled": quality_level in [QualityLevel.PRODUCTION, QualityLevel.ENTERPRISE, QualityLevel.MISSION_CRITICAL],
            "metrics_collection": quality_level != QualityLevel.PROTOTYPE,
            "health_monitoring": quality_level in [QualityLevel.PRODUCTION, QualityLevel.ENTERPRISE, QualityLevel.MISSION_CRITICAL]
        }
    
    def _get_applicable_best_practices(self, complexity: ProjectComplexity, quality_level: QualityLevel) -> List[str]:
        """Get list of applicable best practices."""
        practices = []
        for practice in self.best_practices:
            if (practice.complexity_level == complexity or 
                practice.quality_level == quality_level):
                practices.append(practice.practice_name)
        return practices
