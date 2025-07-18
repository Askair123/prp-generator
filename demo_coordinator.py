#!/usr/bin/env python3
"""
Demo script for Coordinator Pattern system.

This script demonstrates the complete workflow from project analysis
to Claude Flow configuration generation.
"""

import asyncio
import sys
from pathlib import Path

# Add coordinator to path
sys.path.insert(0, str(Path(__file__).parent))

from coordinator import (
    ProjectAnalyzer,
    PatternLibrary, 
    ClaudeFlowAdapter,
)


async def demo_ecommerce_backend():
    """Demo: E-commerce backend API project."""
    
    print("🎯 Demo: E-commerce Backend API")
    print("=" * 50)
    
    # Initialize components
    analyzer = ProjectAnalyzer()
    pattern_library = PatternLibrary()
    adapter = ClaudeFlowAdapter()
    
    # Project description
    description = """
    Build a comprehensive e-commerce backend API using Python FastAPI.
    The system needs to handle:
    - User authentication and authorization
    - Product catalog management with search and filtering
    - Shopping cart functionality
    - Order processing and payment integration
    - Inventory management
    - Admin dashboard APIs
    
    Technical requirements:
    - Python with FastAPI framework
    - PostgreSQL database with Redis for caching
    - JWT authentication
    - RESTful API design
    - Docker deployment on AWS
    - CI/CD pipeline with automated testing
    
    Team: 4 developers, 3-month timeline, production quality required.
    """
    
    try:
        # Step 1: Analyze project
        print("\n🔍 Step 1: Analyzing project requirements...")
        analysis = await analyzer.analyze_project(description)
        
        print(f"✅ Analysis Results:")
        print(f"   - Project Type: {analysis.project_type}")
        print(f"   - Complexity Level: {analysis.complexity_metrics.complexity_level}")
        print(f"   - Technical Complexity: {analysis.complexity_metrics.technical_complexity}/10")
        print(f"   - Organizational Complexity: {analysis.complexity_metrics.organizational_complexity}/10")
        print(f"   - Overall Score: {analysis.complexity_metrics.overall_score}/10")
        print(f"   - Confidence: {analysis.confidence_score:.2f}")
        print(f"   - Team Size: {analysis.constraints.team_size}")
        print(f"   - Quality Level: {analysis.constraints.quality_requirements}")
        
        print(f"\n📚 Technical Stack Identified:")
        print(f"   - Languages: {', '.join(analysis.technical_requirements.languages)}")
        print(f"   - Frameworks: {', '.join(analysis.technical_requirements.frameworks)}")
        print(f"   - Databases: {', '.join(analysis.technical_requirements.databases)}")
        print(f"   - Infrastructure: {', '.join(analysis.technical_requirements.infrastructure)}")
        
        # Step 2: Pattern selection
        print(f"\n🎯 Step 2: Selecting coordination pattern...")
        
        # Show all pattern scores
        scored_patterns = pattern_library.get_matching_patterns(analysis)
        print(f"   Pattern Scores:")
        for pattern_name, score in scored_patterns:
            print(f"   - {pattern_name}: {score:.3f}")
        
        # Select best pattern
        best_name, best_pattern, best_score = pattern_library.select_best_pattern(analysis)
        
        print(f"\n✅ Selected Pattern: {best_name} (score: {best_score:.3f})")
        print(f"   - Description: {best_pattern.description}")
        print(f"   - Coordination: {best_pattern.coordination_rules}")
        print(f"   - Agents: {', '.join(best_pattern.agents)}")
        print(f"   - Quality Gates: {', '.join(best_pattern.quality_gates)}")
        
        # Step 3: Generate configuration
        print(f"\n⚙️ Step 3: Generating Claude Flow configuration...")
        config = await adapter.generate_config(analysis, best_pattern)
        
        print(f"✅ Configuration Generated:")
        print(f"   - Hive Structure: {config.hive_structure}")
        print(f"   - Memory Strategy: {config.memory_strategy}")
        print(f"   - Agents Count: {len(config.agents)}")
        print(f"   - Quality Gates: {len(config.quality_gates)}")
        
        print(f"\n🤖 Agent Configurations:")
        for agent in config.agents:
            print(f"   - {agent.type.title()}")
            print(f"     * Specialization: {agent.specialization}")
            print(f"     * Capabilities: {', '.join(agent.capabilities[:3])}...")
            print(f"     * Tools: {', '.join(agent.tools[:3])}...")
            if agent.dependencies:
                print(f"     * Dependencies: {', '.join(agent.dependencies)}")
        
        # Step 4: Validate configuration
        print(f"\n🔍 Step 4: Validating configuration...")
        validation = await adapter.validate_config(config)
        
        print(f"✅ Validation Results:")
        print(f"   - Valid: {validation.is_valid}")
        print(f"   - Score: {validation.score:.3f}")
        
        if validation.errors:
            print(f"   - Errors: {len(validation.errors)}")
            for error in validation.errors:
                print(f"     * {error}")
        
        if validation.warnings:
            print(f"   - Warnings: {len(validation.warnings)}")
            for warning in validation.warnings[:3]:  # Show first 3
                print(f"     * {warning}")
        
        # Step 5: Execute handoff
        print(f"\n🚀 Step 5: Executing handoff to Claude Flow...")
        handoff = await adapter.handoff_to_claude_flow(config, "demo_output")
        
        if handoff.success:
            print(f"✅ Handoff Successful!")
            print(f"   - Config Path: {handoff.config_path}")
            print(f"   - Claude Flow Ready: {handoff.claude_flow_ready}")
            print(f"   - Timestamp: {handoff.handoff_timestamp}")
            
            print(f"\n📋 Next Steps:")
            for i, step in enumerate(handoff.next_steps, 1):
                print(f"   {i}. {step}")
            
            # Show a preview of the generated config
            print(f"\n📄 Configuration Preview:")
            print(f"   File: {handoff.config_path}")
            
            try:
                with open(handoff.config_path, 'r') as f:
                    config_content = f.read()
                    # Show first few lines
                    lines = config_content.split('\n')[:15]
                    for line in lines:
                        print(f"   {line}")
                    if len(config_content.split('\n')) > 15:
                        print(f"   ... (truncated, see full file)")
            except Exception as e:
                print(f"   Could not preview file: {e}")
                
        else:
            print(f"❌ Handoff Failed!")
            for step in handoff.next_steps:
                print(f"   - {step}")
        
        return handoff.success
        
    except Exception as e:
        print(f"❌ Demo failed with error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


async def demo_data_pipeline():
    """Demo: Data processing pipeline project."""
    
    print("\n\n🎯 Demo: Data Processing Pipeline")
    print("=" * 50)
    
    analyzer = ProjectAnalyzer()
    pattern_library = PatternLibrary()
    adapter = ClaudeFlowAdapter()
    
    description = """
    Create a data processing pipeline for financial analytics.
    Extract data from multiple APIs (stock prices, news, economic indicators),
    transform and clean the data using Python pandas and numpy,
    perform statistical analysis and machine learning predictions,
    and load results into a data warehouse for reporting.
    
    The pipeline should run daily, handle failures gracefully,
    and provide monitoring and alerting capabilities.
    
    Tech stack: Python, pandas, scikit-learn, Apache Airflow, PostgreSQL, Docker.
    Team: 2 data engineers, 6-week timeline.
    """
    
    try:
        # Quick analysis and generation
        analysis = await analyzer.analyze_project(description)
        pattern_name, pattern, score = pattern_library.select_best_pattern(analysis)
        config = await adapter.generate_config(analysis, pattern)
        
        print(f"✅ Quick Analysis:")
        print(f"   - Type: {analysis.project_type}")
        print(f"   - Complexity: {analysis.complexity_metrics.complexity_level}")
        print(f"   - Best Pattern: {pattern_name} (score: {score:.3f})")
        print(f"   - Agents: {', '.join([agent.type for agent in config.agents])}")
        
        return True
        
    except Exception as e:
        print(f"❌ Demo failed: {str(e)}")
        return False


async def main():
    """Run all demos."""
    
    print("🎯 Coordinator Pattern System - Demo")
    print("=" * 60)
    print("This demo shows the complete workflow from project analysis")
    print("to Claude Flow configuration generation.")
    print("=" * 60)
    
    # Run demos
    success1 = await demo_ecommerce_backend()
    success2 = await demo_data_pipeline()
    
    print(f"\n🎉 Demo Summary:")
    print(f"   - E-commerce Backend: {'✅ Success' if success1 else '❌ Failed'}")
    print(f"   - Data Pipeline: {'✅ Success' if success2 else '❌ Failed'}")
    
    if success1 and success2:
        print(f"\n🎊 All demos completed successfully!")
        print(f"   Check the 'demo_output' directory for generated configurations.")
    else:
        print(f"\n⚠️ Some demos failed. Check the error messages above.")


if __name__ == "__main__":
    asyncio.run(main())
