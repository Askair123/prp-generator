"""
Standard Claude Flow Configuration Generator.

This module generates Claude Flow configurations that conform to the official
claude-flow.config.json format and best practices.
"""

from typing import Dict, List, Any
from datetime import datetime

from .models import (
    ProjectAnalysis,
    CoordinationPattern,
    ClaudeFlowConfig,
    OrchestratorConfig,
    TerminalConfig,
    MemoryConfig,
    CoordinationConfig,
    MCPConfig,
    LoggingConfig,
    ProjectType,
    ComplexityLevel,
    TeamSize,
    QualityLevel,
)


class ClaudeFlowConfigGenerator:
    """
    Generates standard Claude Flow configurations based on project analysis.
    
    This generator creates configurations that conform to the official Claude Flow
    configuration format and incorporates best practices for different project types.
    """
    
    def __init__(self):
        """Initialize the configuration generator."""
        self._complexity_multipliers = {
            ComplexityLevel.SIMPLE: 1,
            ComplexityLevel.MODERATE: 2,
            ComplexityLevel.COMPLEX: 3,
            ComplexityLevel.ENTERPRISE: 5
        }
        
        self._team_size_multipliers = {
            TeamSize.SOLO: 1,
            TeamSize.SMALL: 2,
            TeamSize.MEDIUM: 4,
            TeamSize.LARGE: 8
        }
    
    async def generate_config(
        self,
        analysis: ProjectAnalysis,
        pattern: CoordinationPattern,
    ) -> ClaudeFlowConfig:
        """
        Generate complete Claude Flow configuration.
        
        Args:
            analysis: Project analysis results
            pattern: Selected coordination pattern
            
        Returns:
            Standard Claude Flow configuration
        """
        return ClaudeFlowConfig(
            orchestrator=self._generate_orchestrator_config(analysis, pattern),
            terminal=self._generate_terminal_config(analysis),
            memory=self._generate_memory_config(analysis),
            coordination=self._generate_coordination_config(pattern),
            mcp=self._generate_mcp_config(analysis),
            logging=self._generate_logging_config(analysis),
        )
    
    def _generate_orchestrator_config(
        self, analysis: ProjectAnalysis, pattern: CoordinationPattern
    ) -> OrchestratorConfig:
        """Generate orchestrator configuration."""
        
        # Calculate optimal agent count based on complexity and team size
        base_agents = len(pattern.agents)
        complexity_factor = self._complexity_multipliers[analysis.complexity_metrics.complexity_level]
        team_factor = self._team_size_multipliers[analysis.constraints.team_size]
        
        max_concurrent = min(base_agents * complexity_factor, 50)  # Cap at 50
        task_queue_size = max_concurrent * 10
        
        # Select resource allocation strategy
        allocation_strategy = self._select_allocation_strategy(analysis)
        
        # Configure agent recycling
        agent_recycling = {
            "enabled": analysis.constraints.quality_requirements != QualityLevel.MISSION_CRITICAL,
            "maxAge": "2h" if analysis.constraints.quality_requirements == QualityLevel.PROTOTYPE else "4h",
            "maxTasks": 50 if analysis.constraints.quality_requirements == QualityLevel.PROTOTYPE else 100
        }
        
        # Configure failover
        failover = {
            "enabled": analysis.constraints.quality_requirements in [QualityLevel.ENTERPRISE, QualityLevel.MISSION_CRITICAL],
            "detectionThreshold": 10000,
            "recoveryStrategy": "restart"
        }
        
        return OrchestratorConfig(
            maxConcurrentAgents=max_concurrent,
            taskQueueSize=task_queue_size,
            healthCheckInterval=30000 if analysis.constraints.quality_requirements != QualityLevel.MISSION_CRITICAL else 15000,
            shutdownTimeout=30000,
            agentTimeoutMs=300000 if analysis.constraints.quality_requirements != QualityLevel.PROTOTYPE else 180000,
            resourceAllocationStrategy=allocation_strategy,
            agentRecycling=agent_recycling,
            failover=failover,
        )
    
    def _generate_terminal_config(self, analysis: ProjectAnalysis) -> TerminalConfig:
        """Generate terminal configuration."""
        
        # Adjust pool size based on team size and complexity
        base_pool_size = 5
        team_factor = self._team_size_multipliers[analysis.constraints.team_size]
        pool_size = min(base_pool_size * team_factor, 20)  # Cap at 20
        
        # Configure security based on quality requirements
        security = {
            "allowedCommands": self._get_allowed_commands(analysis),
            "blockedCommands": self._get_blocked_commands(),
            "sandboxed": analysis.constraints.quality_requirements in [QualityLevel.ENTERPRISE, QualityLevel.MISSION_CRITICAL],
            "maxExecutionTime": 600000 if analysis.constraints.quality_requirements == QualityLevel.MISSION_CRITICAL else 300000
        }
        
        # Set environment variables based on tech stack
        environment = self._get_environment_variables(analysis)
        
        return TerminalConfig(
            type="auto",
            poolSize=pool_size,
            recycleAfter=10,
            healthCheckInterval=60000,
            commandTimeout=300000,
            maxConcurrentCommands=3,
            shellPreference=["bash", "zsh", "sh"],
            environment=environment,
            security=security,
        )
    
    def _generate_memory_config(self, analysis: ProjectAnalysis) -> MemoryConfig:
        """Generate memory configuration."""
        
        # Select backend based on project type
        backend_mapping = {
            ProjectType.RESEARCH: "markdown",
            ProjectType.DATA_PROCESSING: "sqlite",
            ProjectType.DATA_ANALYTICS: "sqlite",
            ProjectType.ML_PIPELINE: "hybrid",
            ProjectType.WEB_BACKEND: "hybrid",
            ProjectType.WEB_FRONTEND: "hybrid",
            ProjectType.WEB_FULLSTACK: "hybrid",
        }
        backend = backend_mapping.get(analysis.project_type, "hybrid")
        
        # Calculate cache size based on team size and complexity
        base_cache = 100
        team_factor = self._team_size_multipliers[analysis.constraints.team_size]
        complexity_factor = self._complexity_multipliers[analysis.complexity_metrics.complexity_level]
        cache_size = min(base_cache * team_factor * complexity_factor, 2000)  # Cap at 2GB
        
        # Configure retention based on quality requirements
        retention_days = {
            QualityLevel.PROTOTYPE: 7,
            QualityLevel.PRODUCTION: 30,
            QualityLevel.ENTERPRISE: 90,
            QualityLevel.MISSION_CRITICAL: 365
        }[analysis.constraints.quality_requirements]
        
        # Configure backup
        backup = {
            "enabled": analysis.constraints.quality_requirements != QualityLevel.PROTOTYPE,
            "interval": "6h" if analysis.constraints.quality_requirements == QualityLevel.MISSION_CRITICAL else "24h",
            "location": "./backups",
            "maxBackups": 10 if analysis.constraints.quality_requirements == QualityLevel.MISSION_CRITICAL else 5
        }
        
        # Configure optimization
        optimization = {
            "autoCleanup": True,
            "cleanupThreshold": "1GB",
            "indexRebuildInterval": "24h" if analysis.constraints.quality_requirements == QualityLevel.MISSION_CRITICAL else "48h"
        }
        
        return MemoryConfig(
            backend=backend,
            cacheSizeMB=cache_size,
            syncInterval=5000,
            conflictResolution="crdt",
            retentionDays=retention_days,
            compressionEnabled=True,
            encryptionEnabled=analysis.constraints.quality_requirements == QualityLevel.MISSION_CRITICAL,
            backup=backup,
            optimization=optimization,
        )
    
    def _generate_coordination_config(self, pattern: CoordinationPattern) -> CoordinationConfig:
        """Generate coordination configuration."""
        
        # Pattern-specific configurations
        pattern_configs = {
            "hierarchical": {
                "loadBalancingStrategy": "weighted",
                "scheduling": {
                    "algorithm": "priority-queue",
                    "fairness": True,
                    "starvationPrevention": True
                },
                "communication": {
                    "protocol": "async",
                    "bufferSize": 1000,
                    "compression": True
                }
            },
            "peer_to_peer": {
                "loadBalancingStrategy": "round-robin",
                "scheduling": {
                    "algorithm": "fifo",
                    "fairness": True,
                    "starvationPrevention": True
                },
                "communication": {
                    "protocol": "async",
                    "bufferSize": 500,
                    "compression": False
                }
            },
            "pipeline": {
                "loadBalancingStrategy": "round-robin",
                "scheduling": {
                    "algorithm": "shortest-job-first",
                    "fairness": False,
                    "starvationPrevention": False
                },
                "communication": {
                    "protocol": "sync",
                    "bufferSize": 100,
                    "compression": True
                }
            },
            "event_driven": {
                "loadBalancingStrategy": "adaptive",
                "scheduling": {
                    "algorithm": "deadline-aware",
                    "fairness": True,
                    "starvationPrevention": True
                },
                "communication": {
                    "protocol": "async",
                    "bufferSize": 2000,
                    "compression": True
                }
            },
            "hybrid": {
                "loadBalancingStrategy": "adaptive",
                "scheduling": {
                    "algorithm": "priority-queue",
                    "fairness": True,
                    "starvationPrevention": True
                },
                "communication": {
                    "protocol": "async",
                    "bufferSize": 1500,
                    "compression": True
                }
            }
        }
        
        pattern_specific = pattern_configs.get(pattern.name, pattern_configs["hierarchical"])
        
        return CoordinationConfig(
            maxRetries=3,
            retryDelay=1000,
            deadlockDetection=True,
            resourceTimeout=60000,
            messageTimeout=30000,
            priorityLevels=5,
            loadBalancingStrategy=pattern_specific["loadBalancingStrategy"],
            scheduling=pattern_specific["scheduling"],
            communication=pattern_specific["communication"],
        )

    def _generate_mcp_config(self, analysis: ProjectAnalysis) -> MCPConfig:
        """Generate MCP configuration."""

        # Generate allowed tools based on tech stack
        allowed_tools = ["*"]  # Default allow all

        if analysis.technical_requirements.languages:
            language_tools = {
                "python": ["python.*", "pip.*", "pytest.*", "black.*", "ruff.*"],
                "javascript": ["npm.*", "node.*", "yarn.*", "eslint.*", "jest.*"],
                "typescript": ["tsc.*", "npm.*", "yarn.*", "eslint.*"],
                "java": ["mvn.*", "gradle.*", "java.*", "junit.*"],
                "go": ["go.*", "gofmt.*", "golint.*"],
                "rust": ["cargo.*", "rustc.*", "rustfmt.*"],
                "php": ["composer.*", "php.*", "phpunit.*"],
                "ruby": ["gem.*", "bundle.*", "rake.*", "rspec.*"],
                "csharp": ["dotnet.*", "nuget.*", "msbuild.*"]
            }

            specific_tools = []
            for lang in analysis.technical_requirements.languages:
                if lang in language_tools:
                    specific_tools.extend(language_tools[lang])

            if specific_tools:
                allowed_tools = specific_tools

        # Configure rate limiting based on team size
        requests_per_minute = {
            TeamSize.SOLO: 50,
            TeamSize.SMALL: 100,
            TeamSize.MEDIUM: 200,
            TeamSize.LARGE: 500
        }[analysis.constraints.team_size]

        # Configure authentication for enterprise/mission-critical
        authentication = {
            "enabled": analysis.constraints.quality_requirements in [QualityLevel.ENTERPRISE, QualityLevel.MISSION_CRITICAL],
            "method": "token",
            "tokenExpiry": "24h"
        }

        rate_limiting = {
            "enabled": True,
            "requestsPerMinute": requests_per_minute,
            "burstSize": min(requests_per_minute // 5, 50)
        }

        return MCPConfig(
            transport="stdio",
            port=3000,
            host="localhost",
            tlsEnabled=analysis.constraints.quality_requirements == QualityLevel.MISSION_CRITICAL,
            allowedTools=allowed_tools,
            maxRequestSize="10MB",
            requestTimeout=30000,
            authentication=authentication,
            rateLimiting=rate_limiting,
        )

    def _generate_logging_config(self, analysis: ProjectAnalysis) -> LoggingConfig:
        """Generate logging configuration."""

        # Set log level based on quality requirements
        log_levels = {
            QualityLevel.PROTOTYPE: "debug",
            QualityLevel.PRODUCTION: "info",
            QualityLevel.ENTERPRISE: "info",
            QualityLevel.MISSION_CRITICAL: "warn"
        }
        level = log_levels[analysis.constraints.quality_requirements]

        # Configure component-specific logging
        components = {
            "orchestrator": "info" if analysis.constraints.quality_requirements != QualityLevel.PROTOTYPE else "debug",
            "memory": "info",
            "terminal": "warn",
            "mcp": "info",
            "coordination": "info" if analysis.constraints.quality_requirements != QualityLevel.PROTOTYPE else "debug"
        }

        # Configure audit for enterprise/mission-critical
        audit = {
            "enabled": analysis.constraints.quality_requirements in [QualityLevel.ENTERPRISE, QualityLevel.MISSION_CRITICAL],
            "includePayloads": analysis.constraints.quality_requirements == QualityLevel.MISSION_CRITICAL,
            "retention": "90d" if analysis.constraints.quality_requirements == QualityLevel.MISSION_CRITICAL else "30d"
        }

        return LoggingConfig(
            level=level,
            format="json",
            destination="console" if analysis.constraints.quality_requirements == QualityLevel.PROTOTYPE else "file",
            fileOutput="logs/claude-flow.log",
            maxFileSize="10MB",
            maxFiles=5 if analysis.constraints.quality_requirements != QualityLevel.MISSION_CRITICAL else 10,
            components=components,
            audit=audit,
        )

    def _select_allocation_strategy(self, analysis: ProjectAnalysis) -> str:
        """Select resource allocation strategy."""
        if analysis.constraints.quality_requirements == QualityLevel.MISSION_CRITICAL:
            return "performance"
        elif analysis.constraints.team_size == TeamSize.LARGE:
            return "balanced"
        elif analysis.complexity_metrics.complexity_level == ComplexityLevel.SIMPLE:
            return "memory-optimized"
        else:
            return "balanced"

    def _get_allowed_commands(self, analysis: ProjectAnalysis) -> List[str]:
        """Get allowed commands based on tech stack."""
        commands = ["git.*", "ls", "pwd", "cd", "mkdir", "touch", "cat", "grep", "find"]

        # Add language-specific commands
        for lang in analysis.technical_requirements.languages:
            if lang == "python":
                commands.extend(["python.*", "pip.*", "pytest.*"])
            elif lang == "javascript":
                commands.extend(["npm.*", "node.*", "yarn.*"])
            elif lang == "java":
                commands.extend(["mvn.*", "gradle.*", "java.*"])

        # Add framework-specific commands
        for framework in analysis.technical_requirements.frameworks:
            if framework == "docker":
                commands.extend(["docker.*"])
            elif framework == "kubernetes":
                commands.extend(["kubectl.*"])

        return commands

    def _get_blocked_commands(self) -> List[str]:
        """Get blocked commands for security."""
        return [
            "rm -rf /",
            "sudo rm",
            "format.*",
            "del /s /q",
            "shutdown.*",
            "reboot.*",
            "halt.*",
            "poweroff.*"
        ]

    def _get_environment_variables(self, analysis: ProjectAnalysis) -> Dict[str, str]:
        """Get environment variables based on tech stack."""
        env = {
            "PATH": "/usr/local/bin:/usr/bin:/bin",
            "LANG": "en_US.UTF-8"
        }

        # Add language-specific environment variables
        if "python" in analysis.technical_requirements.languages:
            env["PYTHONPATH"] = "."
            env["PYTHONUNBUFFERED"] = "1"

        if "node" in analysis.technical_requirements.languages or "javascript" in analysis.technical_requirements.languages:
            env["NODE_ENV"] = "development"

        if "java" in analysis.technical_requirements.languages:
            env["JAVA_HOME"] = "/usr/lib/jvm/default-java"

        return env
