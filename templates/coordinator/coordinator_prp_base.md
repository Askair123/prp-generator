name: "Coordinator Pattern PRP Template - Claude Flow Config Generator"
description: |

## Purpose
Template optimized for Coordinator Pattern systems that analyze project requirements and generate Claude Flow configurations. Follows Context Engineering principles with rich context and validation loops.

## Core Principles
1. **Context is King**: Include ALL necessary project analysis, patterns, and technical context
2. **Research-Driven**: Base decisions on thorough research of project requirements and best practices
3. **One-Pass Success**: Generate Claude Flow configs that work on first try
4. **Validation Gates**: Include executable tests for config validation
5. **Clean Handoff**: Generate config and exit cleanly, letting Claude Flow take over

---

## Goal
[Specific project analysis and Claude Flow configuration generation goal]

## Why
- **Business Value**: [How this coordination pattern adds value]
- **Technical Need**: [Why this specific coordination approach is needed]
- **Problems Solved**: [What coordination challenges this addresses]

## What
[Detailed description of the project requirements and desired coordination pattern]

## Context

### Project Analysis Requirements
```
Project Type: [web app, research, automation, etc.]
Technical Stack: [languages, frameworks, tools]
Complexity Level: [simple, moderate, complex, enterprise]
Team Size: [solo, small team, large team]
Timeline: [days, weeks, months]
Quality Requirements: [basic, production, enterprise]
```

### Research Areas
- **Similar Projects**: [Links to similar project patterns and implementations]
- **Best Practices**: [Industry standards and proven approaches]
- **Technical Constraints**: [Platform limitations, performance requirements]
- **Integration Points**: [External systems, APIs, databases]

### Coordination Patterns to Consider
```
Pattern Options:
1. Hierarchical: Central coordinator with specialized sub-agents
2. Peer-to-Peer: Distributed coordination with consensus
3. Pipeline: Sequential processing with handoffs
4. Event-Driven: Reactive coordination based on events
5. Hybrid: Combination of above patterns
```

### Claude Flow Integration Context
```
Required Claude Flow Configuration:
- Hive Structure: [hierarchical, flat, hybrid]
- Agent Types: [researcher, architect, coder, tester, etc.]
- Coordination Rules: [decision-making, conflict resolution]
- Memory Strategy: [shared, isolated, hybrid]
- Quality Gates: [testing, review, validation]
```

## Implementation Strategy

### Phase 1: Project Analysis
```python
# Pseudocode for project analysis
async def analyze_project(description: str) -> ProjectAnalysis:
    # PATTERN: Use structured analysis approach
    analysis = ProjectAnalyzer()
    
    # CRITICAL: Identify all technical requirements
    tech_requirements = await analysis.extract_technical_requirements(description)
    
    # PATTERN: Assess complexity using proven metrics
    complexity = await analysis.assess_complexity(tech_requirements)
    
    # GOTCHA: Consider non-functional requirements
    constraints = await analysis.identify_constraints(description)
    
    return ProjectAnalysis(
        requirements=tech_requirements,
        complexity=complexity,
        constraints=constraints
    )
```

### Phase 2: Pattern Selection
```python
# Pseudocode for pattern selection
async def select_coordination_pattern(analysis: ProjectAnalysis) -> CoordinationPattern:
    # PATTERN: Use decision matrix for pattern selection
    pattern_library = PatternLibrary()
    
    # CRITICAL: Match patterns to project characteristics
    candidates = pattern_library.get_matching_patterns(analysis)
    
    # PATTERN: Score patterns based on fit
    scored_patterns = await score_patterns(candidates, analysis)
    
    # GOTCHA: Consider team experience and preferences
    return select_best_pattern(scored_patterns, analysis.team_context)
```

### Phase 3: Claude Flow Config Generation
```python
# Pseudocode for config generation
async def generate_claude_flow_config(
    analysis: ProjectAnalysis, 
    pattern: CoordinationPattern
) -> ClaudeFlowConfig:
    # PATTERN: Use template-based config generation
    config_generator = ClaudeFlowConfigGenerator()
    
    # CRITICAL: Map pattern to Claude Flow structures
    hive_config = config_generator.create_hive_config(pattern)
    
    # PATTERN: Define agent roles and responsibilities
    agent_configs = config_generator.create_agent_configs(analysis, pattern)
    
    # GOTCHA: Include validation and quality gates
    quality_gates = config_generator.create_quality_gates(analysis.quality_requirements)
    
    return ClaudeFlowConfig(
        hive=hive_config,
        agents=agent_configs,
        quality_gates=quality_gates,
        coordination_rules=pattern.rules
    )
```

## Validation Gates

### Config Validation
```bash
# Validate generated Claude Flow configuration
python -m coordinator.validators.config_validator --config generated_config.json

# Check pattern compatibility
python -m coordinator.validators.pattern_validator --pattern selected_pattern.json
```

### Integration Testing
```bash
# Test Claude Flow integration
python -m coordinator.tests.integration.test_claude_flow_handoff

# Validate handoff process
python -m coordinator.tests.test_handoff_process
```

### Quality Assurance
```bash
# Run all coordinator tests
pytest coordinator/tests/ -v

# Check code quality
ruff check coordinator/ && mypy coordinator/
```

## Success Criteria
- [ ] Project requirements accurately analyzed and categorized
- [ ] Appropriate coordination pattern selected based on analysis
- [ ] Valid Claude Flow configuration generated
- [ ] Configuration passes all validation gates
- [ ] Clean handoff to Claude Flow completed
- [ ] All tests pass and code quality checks succeed

## Gotchas and Common Issues
- **Incomplete Analysis**: Ensure all project dimensions are considered
- **Pattern Mismatch**: Validate pattern selection against project constraints
- **Config Compatibility**: Verify Claude Flow config format and requirements
- **Handoff Timing**: Ensure clean exit after successful config generation
- **Validation Coverage**: Include comprehensive validation for all config aspects

## Files to Reference
- `coordinator/project_analyzer.py` - Project analysis patterns
- `coordinator/pattern_library.py` - Coordination pattern definitions
- `coordinator/claude_flow_adapter.py` - Claude Flow integration patterns
- `examples/coordinator/` - Reference implementations
- `docs/architecture/refactored-architecture-implementation.md` - Architecture guidance

## Expected Deliverables
1. **Project Analysis Report** - Detailed analysis of requirements and constraints
2. **Pattern Selection Justification** - Reasoning for chosen coordination pattern
3. **Claude Flow Configuration** - Complete, validated configuration file
4. **Handoff Documentation** - Instructions for Claude Flow initialization
5. **Validation Results** - All test results and quality checks

---

**Remember**: The Coordinator Pattern is a "one-shot advisor" - analyze, configure, handoff, and exit cleanly.
