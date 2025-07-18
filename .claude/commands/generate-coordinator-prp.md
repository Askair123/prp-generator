# Generate Coordinator Pattern PRP

## Project Description: $ARGUMENTS

Generate a comprehensive PRP for Coordinator Pattern implementation that analyzes project requirements and generates Claude Flow configurations. This follows Context Engineering principles with thorough research and rich context.

## Research Process

### 1. Project Analysis Deep Dive
- **Requirements Extraction**: Parse project description for technical and business requirements
- **Technology Stack Identification**: Identify languages, frameworks, tools, and platforms
- **Complexity Assessment**: Evaluate project complexity across multiple dimensions
- **Constraint Analysis**: Identify timeline, resource, quality, and technical constraints
- **Success Criteria Definition**: Define measurable success metrics

### 2. Coordination Pattern Research
- **Pattern Library Analysis**: Research applicable coordination patterns from our library
- **Similar Project Study**: Find and analyze similar projects and their coordination approaches
- **Best Practices Research**: Identify industry best practices for the project type
- **Anti-Pattern Identification**: Document common pitfalls and how to avoid them
- **Performance Considerations**: Research scalability and performance implications

### 3. Claude Flow Integration Research
- **Configuration Requirements**: Research Claude Flow config format and requirements
- **Agent Architecture**: Determine optimal agent types and roles for the project
- **Coordination Rules**: Define decision-making and conflict resolution strategies
- **Memory Strategy**: Choose appropriate memory and state management approach
- **Quality Gates**: Design validation and testing strategies

### 4. Context Engineering Application
- **Rich Context Building**: Gather all necessary documentation, examples, and references
- **Validation Gate Design**: Create executable tests and quality checks
- **Implementation Blueprint**: Design step-by-step implementation approach
- **Gotcha Documentation**: Identify and document potential issues and solutions

## PRP Generation Strategy

### Use Template: `PRPs/templates/coordinator/coordinator_prp_base.md`

### Critical Context to Include:
- **Project Analysis Results**: Complete technical and business analysis
- **Pattern Selection Rationale**: Detailed reasoning for chosen coordination approach
- **Claude Flow Config Specification**: Exact configuration format and parameters
- **Validation Strategy**: Comprehensive testing and quality assurance approach
- **Reference Implementations**: Links to similar projects and code examples

### Implementation Blueprint Structure:
1. **Project Analysis Phase**: Structured approach to requirement analysis
2. **Pattern Selection Phase**: Decision-making process for coordination pattern
3. **Config Generation Phase**: Claude Flow configuration creation process
4. **Validation Phase**: Testing and quality assurance procedures
5. **Handoff Phase**: Clean transition to Claude Flow execution

### Validation Gates (Must be Executable):
```bash
# Configuration validation
python -m coordinator.validators.config_validator --config generated_config.json

# Pattern compatibility check
python -m coordinator.validators.pattern_validator --pattern selected_pattern.json

# Integration testing
python -m coordinator.tests.integration.test_claude_flow_handoff

# Code quality checks
ruff check coordinator/ && mypy coordinator/ && pytest coordinator/tests/ -v
```

## Research Areas to Explore

### Technical Research:
- Coordination pattern literature and implementations
- Claude Flow architecture and configuration options
- Multi-agent system design principles
- Context Engineering best practices

### Project-Specific Research:
- Domain-specific coordination challenges
- Technology stack coordination requirements
- Performance and scalability considerations
- Integration and deployment strategies

### Quality Assurance Research:
- Testing strategies for coordination systems
- Validation approaches for generated configurations
- Monitoring and observability patterns
- Error handling and recovery mechanisms

## Output Requirements

### Save as: `PRPs/coordinator-{project-name}.md`

### Quality Checklist:
- [ ] Complete project analysis with all dimensions covered
- [ ] Thorough research of coordination patterns and best practices
- [ ] Rich context with documentation links and code examples
- [ ] Executable validation gates for all deliverables
- [ ] Clear implementation blueprint with step-by-step approach
- [ ] Comprehensive gotcha documentation and mitigation strategies
- [ ] Claude Flow integration requirements fully specified
- [ ] Success criteria clearly defined and measurable

### Confidence Scoring:
Rate the PRP on a scale of 1-10 for:
- **Analysis Completeness**: How thoroughly the project is analyzed
- **Pattern Appropriateness**: How well the selected pattern fits the project
- **Implementation Clarity**: How clear and actionable the implementation plan is
- **Validation Coverage**: How comprehensive the testing and validation approach is
- **Context Richness**: How much useful context is provided for implementation

**Target Score**: 8+ across all dimensions for production readiness

## Success Criteria

The generated PRP should enable:
1. **One-Pass Implementation**: Complete coordinator implementation without iteration
2. **Clean Claude Flow Integration**: Seamless handoff to Claude Flow execution
3. **Comprehensive Validation**: All aspects tested and validated
4. **Production Readiness**: Ready for real-world deployment and use

Remember: The goal is to create a PRP that enables flawless implementation of a Coordinator Pattern system that generates perfect Claude Flow configurations on the first try.
