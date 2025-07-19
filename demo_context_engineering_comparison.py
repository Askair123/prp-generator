#!/usr/bin/env python3
"""
Context Engineering vs Traditional Knowledge Embedding Comparison.

This demo shows the difference between abstract knowledge recommendations
and specific, actionable contextual guidance following Context Engineering principles.
"""

import asyncio
import sys
from pathlib import Path

# Add coordinator to path
sys.path.insert(0, str(Path(__file__).parent))

from coordinator.prp_parser import PRPParser
from coordinator.claude_flow_config_generator import ClaudeFlowConfigGenerator
from coordinator.contextual_knowledge_index import ContextualKnowledgeIndex
from coordinator import PatternLibrary


async def demo_traditional_vs_context_engineering():
    """Compare traditional knowledge embedding vs Context Engineering approach."""
    
    print("🔄 Traditional vs Context Engineering Comparison")
    print("=" * 80)
    print("Comparing abstract recommendations vs specific, actionable guidance")
    print("=" * 80)
    
    # Initialize components
    prp_parser = PRPParser()
    pattern_library = PatternLibrary()
    config_generator = ClaudeFlowConfigGenerator()
    contextual_index = ContextualKnowledgeIndex()
    
    # Use test PRP
    prp_path = "test_prps/ecommerce-api-system.prp.md"
    
    if not Path(prp_path).exists():
        print(f"❌ PRP file not found: {prp_path}")
        return False
    
    try:
        # Parse PRP and get analysis
        print("📋 Processing E-commerce API System PRP...")
        prp_analysis = await prp_parser.parse_prp_file(prp_path)
        project_analysis = await prp_parser.convert_prp_to_project_analysis(prp_analysis)
        pattern_name, pattern, score = pattern_library.select_best_pattern(project_analysis)
        
        print(f"✅ Project: {project_analysis.project_type}")
        print(f"✅ Complexity: {project_analysis.complexity_metrics.complexity_level}")
        print(f"✅ Selected Pattern: {pattern_name}")
        print()
        
        # Traditional Approach Demo
        print("🔴 TRADITIONAL APPROACH: Abstract Knowledge Recommendations")
        print("=" * 70)
        
        traditional_recommendations = {
            "orchestrator": {
                "maxConcurrentAgents": 30,
                "resourceAllocationStrategy": "balanced",
                "rationale": "Based on complexity and team size calculations"
            },
            "memory": {
                "backend": "hybrid",
                "cacheSizeMB": 1000,
                "rationale": "Optimized for multi-agent systems"
            },
            "coordination": {
                "loadBalancingStrategy": "weighted",
                "rationale": "Suitable for large teams"
            }
        }
        
        print("📊 Traditional Recommendations:")
        for component, config in traditional_recommendations.items():
            print(f"   {component.upper()}:")
            for key, value in config.items():
                if key != "rationale":
                    print(f"      - {key}: {value}")
            print(f"      - Rationale: {config['rationale']}")
            print()
        
        print("❌ Problems with Traditional Approach:")
        print("   - Abstract recommendations without implementation guidance")
        print("   - No specific documentation references")
        print("   - Agent doesn't know HOW to implement these recommendations")
        print("   - No validation or verification steps")
        print("   - Missing critical implementation details")
        print()
        
        # Context Engineering Approach Demo
        print("🟢 CONTEXT ENGINEERING APPROACH: Specific, Actionable Guidance")
        print("=" * 70)
        
        # Generate contextual guidance
        contextual_guidance = config_generator.generate_contextual_guidance(project_analysis, pattern)
        
        print("📚 Context Engineering Guidance:")
        print()
        
        # Show orchestrator guidance
        print("🎛️ ORCHESTRATOR CONFIG GENERATOR GUIDANCE:")
        print("-" * 50)
        orchestrator_guidance = contextual_guidance.get("orchestrator_config_generator", "")
        if orchestrator_guidance:
            # Show first few lines of guidance
            lines = orchestrator_guidance.split('\n')[:15]
            for line in lines:
                print(f"   {line}")
            print("   ... (truncated for demo)")
        print()
        
        # Show memory guidance  
        print("💾 MEMORY CONFIG GENERATOR GUIDANCE:")
        print("-" * 50)
        memory_guidance = contextual_guidance.get("memory_config_generator", "")
        if memory_guidance:
            lines = memory_guidance.split('\n')[:15]
            for line in lines:
                print(f"   {line}")
            print("   ... (truncated for demo)")
        print()
        
        # Demonstrate specific contextual guidance
        print("🎯 SPECIFIC CONTEXTUAL GUIDANCE EXAMPLE:")
        print("-" * 50)
        
        project_characteristics = {
            "complexity": "moderate",
            "quality": "production", 
            "team_size": "large",
            "project_type": "web_backend"
        }
        
        specific_guidance = contextual_index.get_contextual_guidance(
            agent_role="orchestrator_config_generator",
            task_context="high_performance_setup",
            project_characteristics=project_characteristics
        )
        
        print("📖 Must Read First:")
        for ref in specific_guidance.get("must_read_first", []):
            print(f"   📄 {ref.source_path}")
            print(f"      WHY: {ref.why}")
            print(f"      ACTION: {ref.action.value}")
            print()
        
        print("🔍 Study Patterns:")
        for ref in specific_guidance.get("study_patterns", []):
            print(f"   📄 {ref.source_path}")
            print(f"      WHY: {ref.why}")
            print(f"      ACTION: {ref.action.value}")
            print()
        
        print("📋 Copy Examples:")
        for ref in specific_guidance.get("copy_examples", []):
            print(f"   📄 {ref.source_path}")
            print(f"      WHY: {ref.why}")
            print(f"      ACTION: {ref.action.value}")
            print()
        
        # Key Differences Analysis
        print("🔍 KEY DIFFERENCES ANALYSIS")
        print("=" * 50)
        
        differences = [
            {
                "aspect": "Knowledge Type",
                "traditional": "Abstract recommendations",
                "context_engineering": "Specific documentation references"
            },
            {
                "aspect": "Actionability", 
                "traditional": "What to configure",
                "context_engineering": "How to implement + where to find examples"
            },
            {
                "aspect": "Validation",
                "traditional": "No validation guidance",
                "context_engineering": "Specific validation steps and patterns"
            },
            {
                "aspect": "Implementation",
                "traditional": "Generic parameter values",
                "context_engineering": "Proven patterns with rationale"
            },
            {
                "aspect": "Context Awareness",
                "traditional": "One-size-fits-all",
                "context_engineering": "Project-specific guidance"
            }
        ]
        
        print(f"{'Aspect':<20} {'Traditional':<30} {'Context Engineering':<40}")
        print("-" * 90)
        for diff in differences:
            print(f"{diff['aspect']:<20} {diff['traditional']:<30} {diff['context_engineering']:<40}")
        
        print()
        
        # Benefits Analysis
        print("✅ CONTEXT ENGINEERING BENEFITS")
        print("=" * 50)
        
        benefits = [
            "🎯 Specific Actions: Agent knows exactly what to read and implement",
            "📚 Documentation Links: Direct references to authoritative sources", 
            "🔍 Implementation Examples: Proven patterns to copy and adapt",
            "⚡ Faster Implementation: No guessing about best practices",
            "🛡️ Reduced Errors: Following proven patterns reduces mistakes",
            "🎓 Learning: Agent builds expertise through guided exploration",
            "🔄 Validation: Built-in validation and verification steps",
            "📈 Quality: Higher quality outcomes through expert guidance"
        ]
        
        for benefit in benefits:
            print(f"   {benefit}")
        
        print()
        
        # Implementation Comparison
        print("🛠️ IMPLEMENTATION COMPARISON")
        print("=" * 50)
        
        print("❌ Traditional Agent Prompt:")
        print('   "Configure Claude Flow orchestrator with 30 agents using balanced strategy"')
        print("   → Agent has to guess implementation details")
        print()
        
        print("✅ Context Engineering Agent Prompt:")
        print('   "Configure Claude Flow orchestrator following these specific patterns:')
        print('    1. READ FIRST: claude-flow/docs/orchestrator-patterns.md')
        print('    2. COPY PATTERN: claude-flow/examples/production-orchestrator.json')
        print('    3. STUDY: claude-flow/src/orchestrator/resource-allocation.ts')
        print('    4. VALIDATE: Run validation steps from patterns doc"')
        print("   → Agent has clear, actionable guidance")
        
        return True
        
    except Exception as e:
        print(f"❌ Demo failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


async def demo_context_engineering_principles():
    """Demonstrate Context Engineering principles."""
    
    print("\n\n📚 Context Engineering Principles")
    print("=" * 60)
    
    principles = [
        {
            "principle": "Context is King",
            "description": "Include ALL necessary patterns, examples, and references",
            "example": "Instead of 'use hybrid backend', provide 'READ: memory-backends.md, COPY: hybrid-memory-config.json'"
        },
        {
            "principle": "Validation Loops", 
            "description": "Provide executable validation steps",
            "example": "Include specific commands: 'claude-flow validate config.json'"
        },
        {
            "principle": "Specific Actions",
            "description": "Tell agents exactly what to do",
            "example": "READ FIRST, STUDY PATTERN, COPY EXAMPLE, MIRROR IMPLEMENTATION"
        },
        {
            "principle": "Proven Patterns",
            "description": "Reference battle-tested implementations",
            "example": "Point to production-tested configurations, not theoretical ones"
        }
    ]
    
    for i, principle in enumerate(principles, 1):
        print(f"{i}. **{principle['principle']}**")
        print(f"   Description: {principle['description']}")
        print(f"   Example: {principle['example']}")
        print()


async def main():
    """Run the Context Engineering comparison demo."""
    
    print("🧠 Context Engineering vs Traditional Knowledge Embedding")
    print("=" * 80)
    print("Demonstrating the difference between abstract recommendations")
    print("and specific, actionable contextual guidance")
    print("=" * 80)
    
    # Run Context Engineering principles demo
    await demo_context_engineering_principles()
    
    # Run comparison demo
    success = await demo_traditional_vs_context_engineering()
    
    print(f"\n🎉 Demo Summary:")
    print(f"   - Context Engineering Comparison: {'✅ Success' if success else '❌ Failed'}")
    
    if success:
        print(f"\n🎊 Context Engineering approach is clearly superior!")
        print(f"   - Provides specific, actionable guidance")
        print(f"   - References proven patterns and examples")
        print(f"   - Includes validation and verification steps")
        print(f"   - Enables agents to build real expertise")
    
    print(f"\n📋 Key Takeaway:")
    print(f"   Context Engineering transforms abstract knowledge into")
    print(f"   specific, actionable guidance that agents can actually use!")


if __name__ == "__main__":
    asyncio.run(main())
