"""
Claude Flow Adapter for Coordinator Pattern system.

This module converts coordination patterns and project analysis into
Claude Flow compatible configurations for seamless handoff.
"""

import json
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path

from .models import (
    ProjectAnalysis,
    CoordinationPattern,
    AgentConfig,
    ClaudeFlowConfig,
    ValidationResult,
    HandoffResult,
    ProjectType,
)


class ClaudeFlowAdapter:
    """
    Adapter for converting coordination patterns to Claude Flow configurations.

    This class implements the "one-shot advisor" handoff mechanism by generating
    complete, validated Claude Flow configurations that can be used immediately.
    """

    def __init__(self):
        """Initialize the Claude Flow adapter."""
        self._agent_type_mappings = self._build_agent_type_mappings()
        self._tool_mappings = self._build_tool_mappings()

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
            Complete Claude Flow configuration
        """
        # Map pattern to hive structure
        hive_structure = self._map_pattern_to_hive(pattern)

        # Create agent configurations
        agent_configs = self._create_agent_configs(analysis, pattern)

        # Define coordination rules
        coordination_rules = self._define_coordination_rules(pattern, analysis)

        # Setup quality gates
        quality_gates = self._setup_quality_gates(analysis, pattern)

        # Select memory strategy
        memory_strategy = self._select_memory_strategy(analysis)

        # Setup integration points
        integration_points = self._setup_integrations(analysis)

        # Create metadata
        metadata = self._create_metadata(analysis, pattern)

        return ClaudeFlowConfig(
            hive_structure=hive_structure,
            agents=agent_configs,
            coordination_rules=coordination_rules,
            quality_gates=quality_gates,
            memory_strategy=memory_strategy,
            integration_points=integration_points,
            metadata=metadata,
        )

    def _map_pattern_to_hive(self, pattern: CoordinationPattern) -> str:
        """Map coordination pattern to Claude Flow hive structure."""
        pattern_to_hive = {
            "hierarchical": "hierarchical",
            "peer_to_peer": "flat",
            "pipeline": "sequential",
            "event_driven": "reactive",
            "hybrid": "adaptive",
        }

        return pattern_to_hive.get(pattern.name, "hierarchical")

    def _create_agent_configs(
        self, analysis: ProjectAnalysis, pattern: CoordinationPattern
    ) -> List[AgentConfig]:
        """Create agent configurations based on pattern and analysis."""
        agent_configs = []

        for agent_type in pattern.agents:
            # Get specialization based on project type and tech stack
            specialization = self._get_agent_specialization(
                agent_type, analysis.project_type, analysis.technical_requirements
            )

            # Get capabilities for this agent type
            capabilities = self._get_agent_capabilities(agent_type, analysis)

            # Get tools for this agent type
            tools = self._get_agent_tools(agent_type, analysis)

            # Determine dependencies
            dependencies = self._get_agent_dependencies(agent_type, pattern.agents)

            agent_config = AgentConfig(
                type=agent_type,
                specialization=specialization,
                capabilities=capabilities,
                tools=tools,
                dependencies=dependencies,
            )

            agent_configs.append(agent_config)

        return agent_configs

    def _get_agent_specialization(
        self, agent_type: str, project_type: ProjectType, tech_requirements
    ) -> str:
        """Get agent specialization based on project context."""

        specializations = {
            "architect": {
                ProjectType.WEB_BACKEND: "api_architecture",
                ProjectType.WEB_FRONTEND: "frontend_architecture",
                ProjectType.MICROSERVICES: "microservices_architecture",
                ProjectType.DATA_PROCESSING: "data_architecture",
                ProjectType.ML_PIPELINE: "ml_architecture",
            },
            "backend_dev": {
                ProjectType.WEB_BACKEND: f"{tech_requirements.languages[0] if tech_requirements.languages else 'python'}_backend",
                ProjectType.API_REST: "rest_api_development",
                ProjectType.MICROSERVICES: "microservices_development",
            },
            "frontend_dev": {
                ProjectType.WEB_FRONTEND: f"{tech_requirements.frameworks[0] if tech_requirements.frameworks else 'react'}_frontend",
                ProjectType.WEB_FULLSTACK: "fullstack_frontend",
            },
            "database_designer": {
                ProjectType.WEB_BACKEND: f"{tech_requirements.databases[0] if tech_requirements.databases else 'postgresql'}_design",
                ProjectType.DATA_PROCESSING: "data_modeling",
            },
            "tester": {
                ProjectType.WEB_BACKEND: "api_testing",
                ProjectType.WEB_FRONTEND: "ui_testing",
                ProjectType.DATA_PROCESSING: "data_validation_testing",
            },
            "devops": {
                ProjectType.WEB_BACKEND: f"{tech_requirements.infrastructure[0] if tech_requirements.infrastructure else 'docker'}_deployment",
                ProjectType.MICROSERVICES: "container_orchestration",
            },
        }

        agent_specializations = specializations.get(agent_type, {})
        return agent_specializations.get(project_type, f"{agent_type}_general")

    def _get_agent_capabilities(self, agent_type: str, analysis: ProjectAnalysis) -> List[str]:
        """Get capabilities for an agent type."""

        base_capabilities = {
            "architect": [
                "system_design", "architecture_planning", "technology_selection",
                "scalability_analysis", "performance_optimization"
            ],
            "backend_dev": [
                "api_development", "database_integration", "business_logic",
                "error_handling", "performance_optimization"
            ],
            "frontend_dev": [
                "ui_development", "user_experience", "responsive_design",
                "state_management", "component_architecture"
            ],
            "database_designer": [
                "schema_design", "query_optimization", "data_modeling",
                "indexing_strategy", "migration_planning"
            ],
            "tester": [
                "test_planning", "automated_testing", "manual_testing",
                "bug_reporting", "quality_assurance"
            ],
            "devops": [
                "deployment_automation", "infrastructure_management",
                "monitoring_setup", "ci_cd_pipeline", "security_configuration"
            ],
            "security": [
                "security_analysis", "vulnerability_assessment",
                "secure_coding", "compliance_checking", "threat_modeling"
            ],
        }

        return base_capabilities.get(agent_type, ["general_development"])

    def _get_agent_tools(self, agent_type: str, analysis: ProjectAnalysis) -> List[str]:
        """Get tools for an agent type based on project requirements."""

        base_tools = {
            "architect": [
                "system_design_tool", "architecture_validator", "tech_stack_analyzer"
            ],
            "backend_dev": [
                "code_generator", "api_tester", "database_connector", "error_handler"
            ],
            "frontend_dev": [
                "ui_generator", "component_builder", "style_manager", "asset_optimizer"
            ],
            "database_designer": [
                "schema_generator", "query_optimizer", "migration_tool", "data_validator"
            ],
            "tester": [
                "test_generator", "test_runner", "bug_tracker", "coverage_analyzer"
            ],
            "devops": [
                "deployment_tool", "container_manager", "monitoring_setup", "ci_cd_manager"
            ],
            "security": [
                "security_scanner", "vulnerability_checker", "compliance_validator"
            ],
        }

        # Add tech-specific tools
        tools = base_tools.get(agent_type, ["general_tool"]).copy()

        # Add language-specific tools
        for lang in analysis.technical_requirements.languages:
            if lang == "python":
                tools.extend(["python_linter", "pytest_runner"])
            elif lang == "javascript":
                tools.extend(["eslint", "jest_runner"])
            elif lang == "java":
                tools.extend(["maven_tool", "junit_runner"])

        return list(set(tools))  # Remove duplicates

    def _get_agent_dependencies(self, agent_type: str, all_agents: List[str]) -> List[str]:
        """Get dependencies for an agent type."""

        dependency_map = {
            "backend_dev": ["architect", "database_designer"],
            "frontend_dev": ["architect", "backend_dev"],
            "tester": ["backend_dev", "frontend_dev"],
            "devops": ["backend_dev", "frontend_dev", "tester"],
            "security": ["architect"],
        }

        dependencies = dependency_map.get(agent_type, [])
        # Only return dependencies that exist in the agent list
        return [dep for dep in dependencies if dep in all_agents]

    def _define_coordination_rules(
        self, pattern: CoordinationPattern, analysis: ProjectAnalysis
    ) -> Dict[str, Any]:
        """Define coordination rules based on pattern and analysis."""

        base_rules = {
            "hierarchical": {
                "decision_making": "central",
                "communication_flow": "hub_and_spoke",
                "conflict_resolution": "coordinator_decides",
                "task_assignment": "top_down",
            },
            "peer_to_peer": {
                "decision_making": "consensus",
                "communication_flow": "mesh",
                "conflict_resolution": "voting",
                "task_assignment": "self_organizing",
            },
            "pipeline": {
                "decision_making": "sequential",
                "communication_flow": "linear",
                "conflict_resolution": "upstream_decides",
                "task_assignment": "stage_based",
            },
            "event_driven": {
                "decision_making": "reactive",
                "communication_flow": "publish_subscribe",
                "conflict_resolution": "event_priority",
                "task_assignment": "event_triggered",
            },
            "hybrid": {
                "decision_making": "adaptive",
                "communication_flow": "mixed",
                "conflict_resolution": "context_dependent",
                "task_assignment": "flexible",
            },
        }

        rules = base_rules.get(pattern.name, base_rules["hierarchical"]).copy()

        # Add project-specific rules
        rules["project_type"] = str(analysis.project_type)
        rules["complexity_level"] = str(analysis.complexity_metrics.complexity_level)
        rules["team_size"] = str(analysis.constraints.team_size)

        return rules

    def _setup_quality_gates(
        self, analysis: ProjectAnalysis, pattern: CoordinationPattern
    ) -> List[Dict[str, Any]]:
        """Setup quality gates based on analysis and pattern."""

        quality_gates = []

        for gate_name in pattern.quality_gates:
            gate_config = {
                "name": gate_name,
                "type": self._get_gate_type(gate_name),
                "trigger": self._get_gate_trigger(gate_name),
                "criteria": self._get_gate_criteria(gate_name, analysis),
                "actions": self._get_gate_actions(gate_name),
            }
            quality_gates.append(gate_config)

        return quality_gates

    def _get_gate_type(self, gate_name: str) -> str:
        """Get quality gate type."""
        gate_types = {
            "code_review": "manual",
            "unit_testing": "automated",
            "integration_testing": "automated",
            "security_scan": "automated",
            "performance_testing": "automated",
            "peer_review": "manual",
            "validation_testing": "automated",
        }
        return gate_types.get(gate_name, "automated")

    def _get_gate_trigger(self, gate_name: str) -> str:
        """Get quality gate trigger condition."""
        triggers = {
            "code_review": "on_pull_request",
            "unit_testing": "on_code_change",
            "integration_testing": "on_merge",
            "security_scan": "on_deployment",
            "performance_testing": "on_release",
            "peer_review": "on_completion",
            "validation_testing": "on_output",
        }
        return triggers.get(gate_name, "on_completion")

    def _get_gate_criteria(self, gate_name: str, analysis: ProjectAnalysis) -> Dict[str, Any]:
        """Get quality gate criteria."""
        base_criteria = {
            "code_review": {"approvals_required": 1, "blocking_issues": 0},
            "unit_testing": {"coverage_threshold": 80, "passing_tests": "100%"},
            "integration_testing": {"passing_tests": "100%", "response_time": "<2s"},
            "security_scan": {"critical_vulnerabilities": 0, "high_vulnerabilities": 0},
            "performance_testing": {"response_time": "<1s", "throughput": ">100rps"},
        }

        criteria = base_criteria.get(gate_name, {}).copy()

        # Adjust criteria based on quality requirements
        if str(analysis.constraints.quality_requirements) == "enterprise":
            if gate_name == "unit_testing":
                criteria["coverage_threshold"] = 90
            elif gate_name == "code_review":
                criteria["approvals_required"] = 2

        return criteria

    def _get_gate_actions(self, gate_name: str) -> List[str]:
        """Get quality gate actions."""
        actions = {
            "code_review": ["block_merge", "request_changes"],
            "unit_testing": ["block_deployment", "generate_report"],
            "integration_testing": ["block_release", "notify_team"],
            "security_scan": ["block_deployment", "create_ticket"],
            "performance_testing": ["block_release", "optimize_code"],
        }
        return actions.get(gate_name, ["notify_team"])

    def _select_memory_strategy(self, analysis: ProjectAnalysis) -> str:
        """Select memory strategy based on project characteristics."""

        if str(analysis.complexity_metrics.complexity_level) in ["complex", "enterprise"]:
            return "persistent_hierarchical"
        elif str(analysis.constraints.team_size) in ["medium", "large"]:
            return "shared_context"
        elif str(analysis.project_type) in ["data_processing", "ml_pipeline"]:
            return "pipeline_memory"
        else:
            return "session_based"

    def _setup_integrations(self, analysis: ProjectAnalysis) -> Dict[str, Any]:
        """Setup integration points based on project requirements."""

        integrations = {
            "version_control": {
                "type": "git",
                "provider": "github",  # Default, can be configured
                "hooks": ["pre_commit", "post_merge"],
            },
            "project_management": {
                "type": "linear",
                "sync_frequency": "real_time",
                "sync_fields": ["status", "assignee", "progress"],
            },
        }

        # Add database integration if needed
        if analysis.technical_requirements.databases:
            integrations["database"] = {
                "type": analysis.technical_requirements.databases[0],
                "connection_pool": True,
                "migration_support": True,
            }

        # Add deployment integration if infrastructure is specified
        if analysis.technical_requirements.infrastructure:
            integrations["deployment"] = {
                "type": analysis.technical_requirements.infrastructure[0],
                "auto_deploy": str(analysis.constraints.quality_requirements) != "mission_critical",
                "rollback_support": True,
            }

        return integrations

    def _create_metadata(self, analysis: ProjectAnalysis, pattern: CoordinationPattern) -> Dict[str, Any]:
        """Create metadata for the configuration."""

        return {
            "generated_at": datetime.now().isoformat(),
            "coordinator_version": "1.0.0",
            "project_analysis": {
                "type": str(analysis.project_type),
                "complexity": str(analysis.complexity_metrics.complexity_level),
                "confidence": analysis.confidence_score,
            },
            "pattern_selection": {
                "name": pattern.name,
                "description": pattern.description,
                "agents_count": len(pattern.agents),
            },
            "technical_stack": {
                "languages": analysis.technical_requirements.languages,
                "frameworks": analysis.technical_requirements.frameworks,
                "databases": analysis.technical_requirements.databases,
            },
        }

    async def validate_config(self, config: ClaudeFlowConfig) -> ValidationResult:
        """Validate the generated Claude Flow configuration."""

        errors = []
        warnings = []

        # Validate required fields
        if not config.hive_structure:
            errors.append("Missing hive_structure")

        if not config.agents:
            errors.append("No agents configured")

        # Validate agent configurations
        for agent in config.agents:
            if not agent.type:
                errors.append(f"Agent missing type: {agent}")
            if not agent.capabilities:
                warnings.append(f"Agent {agent.type} has no capabilities defined")

        # Validate coordination rules
        if not config.coordination_rules:
            warnings.append("No coordination rules defined")

        # Validate quality gates
        if not config.quality_gates:
            warnings.append("No quality gates configured")

        # Calculate validation score
        total_checks = 10
        failed_checks = len(errors)
        warning_checks = len(warnings)

        score = max(0.0, (total_checks - failed_checks - warning_checks * 0.5) / total_checks)

        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            score=score,
        )

    async def handoff_to_claude_flow(
        self, config: ClaudeFlowConfig, output_path: str = "output"
    ) -> HandoffResult:
        """Execute handoff to Claude Flow by saving configuration."""

        try:
            # Create output directory
            output_dir = Path(output_path)
            output_dir.mkdir(exist_ok=True)

            # Generate config filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            config_filename = f"claude_flow_config_{timestamp}.json"
            config_path = output_dir / config_filename

            # Save configuration
            config.save_to_file(str(config_path))

            # Create handoff documentation
            handoff_doc = self._create_handoff_documentation(config, str(config_path))
            doc_path = output_dir / f"handoff_instructions_{timestamp}.md"

            with open(doc_path, 'w') as f:
                f.write(handoff_doc)

            return HandoffResult(
                success=True,
                config_path=str(config_path),
                claude_flow_ready=True,
                handoff_timestamp=datetime.now().isoformat(),
                next_steps=[
                    f"Review configuration at {config_path}",
                    f"Read handoff instructions at {doc_path}",
                    "Initialize Claude Flow with the generated configuration",
                    "Monitor initial execution and adjust if needed",
                ],
            )

        except Exception as e:
            return HandoffResult(
                success=False,
                config_path="",
                claude_flow_ready=False,
                handoff_timestamp=datetime.now().isoformat(),
                next_steps=[f"Fix error: {str(e)}", "Retry handoff process"],
            )

    def _create_handoff_documentation(self, config: ClaudeFlowConfig, config_path: str) -> str:
        """Create handoff documentation for Claude Flow."""

        doc = f"""# Claude Flow Configuration Handoff

## Configuration Details
- **Config File**: {config_path}
- **Generated**: {config.metadata.get('generated_at', 'Unknown')}
- **Hive Structure**: {config.hive_structure}
- **Agents Count**: {len(config.agents)}

## Agent Configuration
"""

        for agent in config.agents:
            doc += f"""
### {agent.type.title()} Agent
- **Specialization**: {agent.specialization}
- **Capabilities**: {', '.join(agent.capabilities)}
- **Tools**: {', '.join(agent.tools)}
- **Dependencies**: {', '.join(agent.dependencies) if agent.dependencies else 'None'}
"""

        doc += f"""
## Coordination Rules
- **Decision Making**: {config.coordination_rules.get('decision_making', 'Not specified')}
- **Communication Flow**: {config.coordination_rules.get('communication_flow', 'Not specified')}
- **Conflict Resolution**: {config.coordination_rules.get('conflict_resolution', 'Not specified')}

## Quality Gates
{len(config.quality_gates)} quality gates configured:
"""

        for gate in config.quality_gates:
            doc += f"- **{gate['name']}**: {gate['type']} gate, triggered {gate['trigger']}\n"

        doc += f"""
## Next Steps
1. Load this configuration into Claude Flow
2. Initialize the hive with the specified structure
3. Deploy agents with their configured tools and capabilities
4. Monitor initial coordination and adjust as needed

## Memory Strategy
**Strategy**: {config.memory_strategy}

## Integration Points
"""

        for integration, details in config.integration_points.items():
            doc += f"- **{integration.title()}**: {details.get('type', 'Not specified')}\n"

        return doc

    def _build_agent_type_mappings(self) -> Dict[str, str]:
        """Build agent type mappings for Claude Flow compatibility."""
        return {
            "architect": "system_architect",
            "backend_dev": "backend_developer",
            "frontend_dev": "frontend_developer",
            "database_designer": "data_architect",
            "tester": "quality_assurance",
            "devops": "deployment_engineer",
            "security": "security_specialist",
        }

    def _build_tool_mappings(self) -> Dict[str, List[str]]:
        """Build tool mappings for different agent types."""
        return {
            "architect": ["system_design", "architecture_validation", "tech_analysis"],
            "developer": ["code_generation", "testing", "debugging"],
            "tester": ["test_automation", "quality_metrics", "bug_tracking"],
            "devops": ["deployment", "monitoring", "infrastructure"],
        }