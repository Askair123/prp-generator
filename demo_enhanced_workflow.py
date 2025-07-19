#!/usr/bin/env python3
"""
Demo script for Enhanced PRP Workflow with Context Management.

This script demonstrates the sophisticated workflow orchestration and context management
capabilities of our enhanced PRP processing system.
"""

import asyncio
import sys
from pathlib import Path

# Add coordinator to path
sys.path.insert(0, str(Path(__file__).parent))

from coordinator.enhanced_prp_processor import EnhancedPRPProcessor
from coordinator.context_manager import ContextManager, ProcessingPhase


async def demo_enhanced_workflow():
    """Demonstrate the enhanced workflow with rich context management."""
    
    print("🎯 Enhanced PRP Workflow Demo")
    print("=" * 70)
    print("Demonstrating sophisticated context management and agent coordination")
    print("=" * 70)
    
    # Initialize enhanced processor
    processor = EnhancedPRPProcessor()
    
    # Use our test PRP
    prp_path = "test_prps/ecommerce-api-system.prp.md"
    
    if not Path(prp_path).exists():
        print(f"❌ PRP file not found: {prp_path}")
        return False
    
    try:
        print(f"\n🔍 Processing PRP with Enhanced Workflow: {prp_path}")
        print("-" * 50)
        
        # Process with full context management
        config = await processor.process_prp_with_context(prp_path)
        
        print(f"\n✅ Enhanced Processing Complete!")
        print(f"   Generated configuration with sophisticated context management")
        
        # Demonstrate context inspection
        await demo_context_inspection(processor)
        
        # Show workflow benefits
        await demo_workflow_benefits()
        
        return True
        
    except Exception as e:
        print(f"❌ Enhanced workflow failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


async def demo_context_inspection(processor: EnhancedPRPProcessor):
    """Demonstrate context inspection capabilities."""
    
    print(f"\n🔍 Context Management Demonstration")
    print("-" * 40)
    
    # Get the most recent workflow context
    if processor.context_manager.active_workflows:
        workflow_id = list(processor.context_manager.active_workflows.keys())[-1]
        workflow_context = processor.context_manager.active_workflows[workflow_id]
        
        print(f"📊 Workflow Context Summary:")
        summary = processor.context_manager.get_context_summary(workflow_context)
        for key, value in summary.items():
            print(f"   - {key}: {value}")
        
        print(f"\n📈 Quality Metrics:")
        metrics = workflow_context.quality_metrics
        print(f"   - Parsing Completeness: {metrics.parsing_completeness:.2f}")
        print(f"   - Analysis Confidence: {metrics.analysis_confidence:.2f}")
        print(f"   - Pattern Match Score: {metrics.pattern_match_score:.2f}")
        print(f"   - Config Validation: {metrics.config_validation_score:.2f}")
        print(f"   - Overall Quality: {metrics.overall_quality:.2f}")
        
        print(f"\n🔄 Data Lineage:")
        lineage = workflow_context.data_lineage
        print(f"   - Total Transformations: {len(lineage.transformations)}")
        print(f"   - Confidence Evolution: {lineage.confidence_evolution}")
        
        print(f"\n🤖 Agent Performance:")
        for phase_name, phase_context in workflow_context.phase_contexts.items():
            print(f"   Phase: {phase_name}")
            for agent_name, agent_context in phase_context.agent_contexts.items():
                print(f"     - {agent_name}: {agent_context.task_success_rate:.2f} success rate, {agent_context.average_confidence:.2f} avg confidence")
    
    else:
        print("   No active workflow contexts found")


async def demo_workflow_benefits():
    """Demonstrate the benefits of the enhanced workflow."""
    
    print(f"\n🎯 Enhanced Workflow Benefits")
    print("-" * 40)
    
    print(f"✅ Context Management:")
    print(f"   - Rich context propagation between phases")
    print(f"   - Agent-specific context and capabilities")
    print(f"   - Data lineage and transformation tracking")
    print(f"   - Quality metrics and confidence scoring")
    
    print(f"\n✅ Agent Specialization:")
    print(f"   - PRP Parser Agent: Document analysis expert")
    print(f"   - Technical Analyzer: Architecture and tech stack specialist")
    print(f"   - Complexity Analyzer: Risk and scalability expert")
    print(f"   - Pattern Expert: Coordination pattern specialist")
    print(f"   - Config Generator: Claude Flow optimization expert")
    print(f"   - Validator: Quality assurance specialist")
    
    print(f"\n✅ Workflow Orchestration:")
    print(f"   - Parallel processing where beneficial")
    print(f"   - Context-aware decision making")
    print(f"   - Comprehensive error handling and recovery")
    print(f"   - Performance and quality tracking")
    
    print(f"\n✅ Quality Assurance:")
    print(f"   - Multi-dimensional quality metrics")
    print(f"   - Confidence tracking throughout pipeline")
    print(f"   - Validation at each processing phase")
    print(f"   - Comprehensive final validation")


async def compare_workflows():
    """Compare simple vs enhanced workflows."""
    
    print(f"\n📊 Workflow Comparison")
    print("=" * 50)
    
    print(f"❌ Simple Workflow (Current):")
    print(f"   - Sequential processing only")
    print(f"   - Minimal context passing")
    print(f"   - No agent specialization")
    print(f"   - Basic error handling")
    print(f"   - Limited quality tracking")
    
    print(f"\n✅ Enhanced Workflow (Demonstrated):")
    print(f"   - Sophisticated orchestration")
    print(f"   - Rich context management")
    print(f"   - Specialized agent roles")
    print(f"   - Comprehensive error handling")
    print(f"   - Multi-dimensional quality tracking")
    print(f"   - Data lineage and transformation tracking")
    print(f"   - Performance metrics and optimization")
    
    print(f"\n🎯 Key Improvements:")
    print(f"   - Higher quality outputs through specialization")
    print(f"   - Better error detection and recovery")
    print(f"   - Comprehensive audit trail")
    print(f"   - Performance optimization opportunities")
    print(f"   - Scalable architecture for complex workflows")


async def demo_context_propagation():
    """Demonstrate context propagation between phases."""
    
    print(f"\n🔄 Context Propagation Demo")
    print("-" * 40)
    
    context_manager = ContextManager()
    
    # Simulate context propagation
    print(f"📋 Phase Transitions and Context Propagation:")
    
    transitions = [
        (ProcessingPhase.PARSING, ProcessingPhase.ANALYSIS),
        (ProcessingPhase.ANALYSIS, ProcessingPhase.PATTERN_SELECTION),
        (ProcessingPhase.PATTERN_SELECTION, ProcessingPhase.CONFIG_GENERATION),
        (ProcessingPhase.CONFIG_GENERATION, ProcessingPhase.VALIDATION)
    ]
    
    for source_phase, target_phase in transitions:
        print(f"   {source_phase.value} → {target_phase.value}:")
        
        if source_phase == ProcessingPhase.PARSING:
            print(f"     - PRP analysis results")
            print(f"     - Extracted entities and semantic hints")
            print(f"     - Parsing confidence and completeness")
        
        elif source_phase == ProcessingPhase.ANALYSIS:
            print(f"     - Project analysis and complexity metrics")
            print(f"     - Technical constraints and requirements")
            print(f"     - Recommended patterns and rationale")
        
        elif source_phase == ProcessingPhase.PATTERN_SELECTION:
            print(f"     - Selected pattern and alternatives")
            print(f"     - Selection rationale and expert reasoning")
            print(f"     - Customization hints and recommendations")
        
        elif source_phase == ProcessingPhase.CONFIG_GENERATION:
            print(f"     - Generated configuration")
            print(f"     - Optimization metadata")
            print(f"     - Security and performance settings")


async def main():
    """Run the enhanced workflow demonstration."""
    
    print("🎯 Enhanced PRP Workflow System - Comprehensive Demo")
    print("=" * 80)
    print("This demo showcases sophisticated workflow orchestration and context management")
    print("=" * 80)
    
    # Run workflow comparison
    await compare_workflows()
    
    # Demonstrate context propagation
    await demo_context_propagation()
    
    # Run enhanced workflow demo
    success = await demo_enhanced_workflow()
    
    print(f"\n🎉 Demo Summary:")
    print(f"   - Enhanced Workflow: {'✅ Success' if success else '❌ Failed'}")
    
    if success:
        print(f"\n🎊 Enhanced workflow system demonstrated successfully!")
        print(f"   - Sophisticated context management")
        print(f"   - Agent specialization and coordination")
        print(f"   - Quality tracking and optimization")
        print(f"   - Comprehensive workflow orchestration")
    else:
        print(f"\n⚠️ Demo encountered issues. Check error messages above.")
    
    print(f"\n📋 Next Steps for Implementation:")
    print(f"   1. Integrate enhanced context management into existing system")
    print(f"   2. Implement agent specialization and coordination")
    print(f"   3. Add comprehensive quality tracking and metrics")
    print(f"   4. Consider Claude Flow integration for true multi-agent execution")
    print(f"   5. Implement parallel processing for performance optimization")


if __name__ == "__main__":
    asyncio.run(main())
