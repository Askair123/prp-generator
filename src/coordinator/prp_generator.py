"""
PRP Generator for Coordinator Pattern system.

This module generates Product Requirement Prompts (PRPs) for Claude Flow
configurations based on project analysis and coordination patterns.
"""

from typing import Dict, List, Any
from datetime import datetime

from .models import ProjectAnalysis, CoordinationPattern, ClaudeFlowConfig


class PRPGenerator:
    """
    Generator for Product Requirement Prompts (PRPs) for Claude Flow.

    This class creates detailed PRPs that can be used to guide Claude Flow
    in implementing the recommended coordination patterns.
    """

    def __init__(self):
        """Initialize the PRP generator."""
        pass

    async def generate_prp(
        self,
        analysis: ProjectAnalysis,
        pattern: CoordinationPattern,
        config: ClaudeFlowConfig,
    ) -> str:
        """
        Generate a comprehensive PRP for Claude Flow implementation.

        Args:
            analysis: Project analysis results
            pattern: Selected coordination pattern
            config: Generated Claude Flow configuration

        Returns:
            Complete PRP as markdown string
        """

        prp_sections = [
            self._generate_header(analysis, pattern),
            self._generate_overview(analysis, pattern),
            self._generate_technical_requirements(analysis),
            self._generate_coordination_strategy(pattern, config),
            self._generate_agent_specifications(config),
            self._generate_quality_gates(config),
            self._generate_implementation_guidelines(),
            self._generate_success_criteria(analysis),
        ]

        return "\n\n".join(prp_sections)

    def _generate_header(self, analysis: ProjectAnalysis, pattern: CoordinationPattern) -> str:
        """Generate PRP header."""
        return f"""# Claude Flow Configuration PRP

**Generated**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Project Type**: {analysis.project_type.value}
**Coordination Pattern**: {pattern.name}
**Complexity Level**: {analysis.complexity_metrics.complexity_level.value}

---"""

    def _generate_overview(self, analysis: ProjectAnalysis, pattern: CoordinationPattern) -> str:
        """Generate project overview section."""
        return f"""## Project Overview

**Description**: {analysis.description}

**Key Characteristics**:
- **Type**: {analysis.project_type.value}
- **Complexity**: {analysis.complexity_metrics.complexity_level.value} (score: {analysis.complexity_metrics.overall_score}/10)
- **Team Size**: {analysis.constraints.team_size.value}
- **Quality Requirements**: {analysis.constraints.quality_requirements.value}
- **Confidence**: {analysis.confidence_score:.2f}

**Recommended Pattern**: {pattern.name}
- **Description**: {pattern.description}
- **Best For**: {', '.join(pattern.best_for)}"""

    def _generate_technical_requirements(self, analysis: ProjectAnalysis) -> str:
        """Generate technical requirements section."""
        tech = analysis.technical_requirements

        return f"""## Technical Requirements

**Programming Languages**: {', '.join(tech.languages) if tech.languages else 'Not specified'}
**Frameworks**: {', '.join(tech.frameworks) if tech.frameworks else 'Not specified'}
**Databases**: {', '.join(tech.databases) if tech.databases else 'Not specified'}
**Infrastructure**: {', '.join(tech.infrastructure) if tech.infrastructure else 'Not specified'}
**Tools**: {', '.join(tech.tools) if tech.tools else 'Not specified'}
**APIs/Integrations**: {', '.join(tech.apis) if tech.apis else 'Not specified'}"""

    def _generate_coordination_strategy(self, pattern: CoordinationPattern, config: ClaudeFlowConfig) -> str:
        """Generate coordination strategy section."""
        return f"""## Coordination Strategy

**Pattern**: {pattern.name}
**Hive Structure**: {config.hive_structure}
**Memory Strategy**: {config.memory_strategy}

**Coordination Rules**:
- **Decision Making**: {config.coordination_rules.get('decision_making', 'Not specified')}
- **Communication Flow**: {config.coordination_rules.get('communication_flow', 'Not specified')}
- **Conflict Resolution**: {config.coordination_rules.get('conflict_resolution', 'Not specified')}
- **Task Assignment**: {config.coordination_rules.get('task_assignment', 'Not specified')}"""

    def _generate_agent_specifications(self, config: ClaudeFlowConfig) -> str:
        """Generate agent specifications section."""
        agents_section = "## Agent Specifications\n"

        for agent in config.agents:
            agents_section += f"""
### {agent.type.title()} Agent
- **Specialization**: {agent.specialization}
- **Capabilities**: {', '.join(agent.capabilities)}
- **Tools**: {', '.join(agent.tools)}
- **Dependencies**: {', '.join(agent.dependencies) if agent.dependencies else 'None'}"""

        return agents_section

    def _generate_quality_gates(self, config: ClaudeFlowConfig) -> str:
        """Generate quality gates section."""
        gates_section = "## Quality Gates\n"

        for gate in config.quality_gates:
            gates_section += f"""
### {gate['name'].title()}
- **Type**: {gate['type']}
- **Trigger**: {gate['trigger']}
- **Criteria**: {gate.get('criteria', {})}
- **Actions**: {', '.join(gate.get('actions', []))}"""

        return gates_section

    def _generate_implementation_guidelines(self) -> str:
        """Generate implementation guidelines section."""
        return """## Implementation Guidelines

### Setup Phase
1. Initialize Claude Flow with the specified hive structure
2. Deploy agents with their configured tools and capabilities
3. Establish communication channels according to coordination rules
4. Set up quality gates and monitoring

### Execution Phase
1. Follow the coordination pattern for task assignment and communication
2. Ensure all quality gates are properly configured and active
3. Monitor agent performance and coordination effectiveness
4. Adjust configuration as needed based on real-world performance

### Quality Assurance
1. Validate that all agents are functioning correctly
2. Test coordination mechanisms under various scenarios
3. Verify quality gates are triggering appropriately
4. Ensure integration points are working as expected"""

    def _generate_success_criteria(self, analysis: ProjectAnalysis) -> str:
        """Generate success criteria section."""
        return f"""## Success Criteria

### Primary Objectives
- Successful implementation of {analysis.project_type.value} project
- Effective coordination between all agents
- Quality requirements met according to {analysis.constraints.quality_requirements.value} standards
- All technical requirements satisfied

### Performance Metrics
- Agent coordination efficiency > 80%
- Quality gate pass rate > 95%
- Project delivery within timeline constraints
- Technical debt maintained at acceptable levels

### Validation Checkpoints
1. **Initial Setup**: All agents deployed and communicating
2. **Mid-Project**: Coordination patterns working effectively
3. **Pre-Delivery**: All quality gates passing
4. **Post-Delivery**: System performing as expected

### Risk Mitigation
- Monitor for coordination bottlenecks
- Have fallback patterns ready if primary pattern fails
- Ensure quality gates don't become development blockers
- Maintain flexibility for pattern adjustments"""