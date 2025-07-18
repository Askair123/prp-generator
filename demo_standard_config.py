#!/usr/bin/env python3
"""
Demo script for Standard Claude Flow Configuration Generator.

This script demonstrates the new standard configuration generation that
conforms to the official Claude Flow configuration format.
"""

import asyncio
import sys
from pathlib import Path

# Add coordinator to path
sys.path.insert(0, str(Path(__file__).parent))

from coordinator import (
    ProjectAnalyzer,
    PatternLibrary,
)
from coordinator.claude_flow_config_generator import ClaudeFlowConfigGenerator


async def demo_standard_config_generation():
    """Demo: Generate standard Claude Flow configuration."""
    
    print("🎯 Demo: Standard Claude Flow Configuration Generation")
    print("=" * 60)
    
    # Initialize components
    analyzer = ProjectAnalyzer()
    pattern_library = PatternLibrary()
    config_generator = ClaudeFlowConfigGenerator()
    
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
        print(f"   - Team Size: {analysis.constraints.team_size}")
        print(f"   - Quality Level: {analysis.constraints.quality_requirements}")
        print(f"   - Confidence: {analysis.confidence_score:.2f}")
        
        # Step 2: Select pattern
        print(f"\n🎯 Step 2: Selecting coordination pattern...")
        best_name, best_pattern, best_score = pattern_library.select_best_pattern(analysis)
        
        print(f"✅ Selected Pattern: {best_name} (score: {best_score:.3f})")
        print(f"   - Description: {best_pattern.description}")
        print(f"   - Agents: {', '.join(best_pattern.agents)}")
        
        # Step 3: Generate standard Claude Flow configuration
        print(f"\n⚙️ Step 3: Generating standard Claude Flow configuration...")
        config = await config_generator.generate_config(analysis, best_pattern)
        
        print(f"✅ Standard Configuration Generated:")
        print(f"   - Orchestrator: {config.orchestrator.maxConcurrentAgents} max agents")
        print(f"   - Terminal: {config.terminal.poolSize} terminal pool")
        print(f"   - Memory: {config.memory.backend} backend, {config.memory.cacheSizeMB}MB cache")
        print(f"   - Coordination: {config.coordination.loadBalancingStrategy} load balancing")
        print(f"   - MCP: {len(config.mcp.allowedTools)} allowed tools")
        print(f"   - Logging: {config.logging.level} level")
        
        # Step 4: Show detailed configuration sections
        print(f"\n📋 Detailed Configuration Sections:")
        
        print(f"\n🎛️ Orchestrator Configuration:")
        print(f"   - Max Concurrent Agents: {config.orchestrator.maxConcurrentAgents}")
        print(f"   - Task Queue Size: {config.orchestrator.taskQueueSize}")
        print(f"   - Resource Allocation: {config.orchestrator.resourceAllocationStrategy}")
        print(f"   - Agent Recycling: {config.orchestrator.agentRecycling['enabled']}")
        print(f"   - Failover Enabled: {config.orchestrator.failover['enabled']}")
        
        print(f"\n💾 Memory Configuration:")
        print(f"   - Backend: {config.memory.backend}")
        print(f"   - Cache Size: {config.memory.cacheSizeMB}MB")
        print(f"   - Retention: {config.memory.retentionDays} days")
        print(f"   - Compression: {config.memory.compressionEnabled}")
        print(f"   - Encryption: {config.memory.encryptionEnabled}")
        
        print(f"\n🔗 Coordination Configuration:")
        print(f"   - Load Balancing: {config.coordination.loadBalancingStrategy}")
        print(f"   - Scheduling Algorithm: {config.coordination.scheduling.get('algorithm', 'N/A')}")
        print(f"   - Max Retries: {config.coordination.maxRetries}")
        print(f"   - Deadlock Detection: {config.coordination.deadlockDetection}")
        
        print(f"\n🛠️ MCP Configuration:")
        print(f"   - Transport: {config.mcp.transport}")
        print(f"   - Allowed Tools: {len(config.mcp.allowedTools)} tools")
        print(f"   - Rate Limiting: {config.mcp.rateLimiting['enabled']}")
        print(f"   - Authentication: {config.mcp.authentication['enabled']}")
        
        print(f"\n📊 Terminal Configuration:")
        print(f"   - Pool Size: {config.terminal.poolSize}")
        print(f"   - Security Sandboxed: {config.terminal.security.get('sandboxed', False)}")
        print(f"   - Max Concurrent Commands: {config.terminal.maxConcurrentCommands}")
        
        print(f"\n📝 Logging Configuration:")
        print(f"   - Level: {config.logging.level}")
        print(f"   - Format: {config.logging.format}")
        print(f"   - Destination: {config.logging.destination}")
        print(f"   - Audit Enabled: {config.logging.audit.get('enabled', False)}")
        
        # Step 5: Save configuration
        print(f"\n💾 Step 5: Saving configuration...")
        
        # Create output directory
        output_dir = Path("standard_config_output")
        output_dir.mkdir(exist_ok=True)
        
        # Save standard configuration
        config_path = output_dir / "claude-flow.config.json"
        config.save_to_file(str(config_path))
        
        print(f"✅ Configuration saved to: {config_path}")
        
        # Step 6: Show configuration preview
        print(f"\n📄 Configuration File Preview:")
        print(f"   File: {config_path}")
        
        try:
            with open(config_path, 'r') as f:
                config_content = f.read()
                # Show first 20 lines
                lines = config_content.split('\n')[:20]
                for line in lines:
                    print(f"   {line}")
                if len(config_content.split('\n')) > 20:
                    print(f"   ... (truncated, see full file)")
        except Exception as e:
            print(f"   Could not preview file: {e}")
        
        # Step 7: Generate CLI commands
        print(f"\n🚀 Step 7: Claude Flow CLI Commands:")
        print(f"   # Validate the configuration")
        print(f"   claude-flow config validate --file {config_path}")
        print(f"   ")
        print(f"   # Start Claude Flow with this configuration")
        print(f"   claude-flow --config {config_path} start")
        print(f"   ")
        print(f"   # Show specific configuration values")
        print(f"   claude-flow config get orchestrator.maxConcurrentAgents")
        print(f"   claude-flow config get memory.backend")
        
        return True
        
    except Exception as e:
        print(f"❌ Demo failed with error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


async def demo_different_environments():
    """Demo: Generate configurations for different environments."""
    
    print("\n\n🎯 Demo: Environment-Specific Configurations")
    print("=" * 60)
    
    analyzer = ProjectAnalyzer()
    pattern_library = PatternLibrary()
    config_generator = ClaudeFlowConfigGenerator()
    
    # Simple prototype project
    prototype_description = """
    Create a simple prototype web API for a todo list application.
    Use Python Flask, SQLite database. Solo developer, 2-week timeline.
    """
    
    # Enterprise mission-critical project
    enterprise_description = """
    Build a mission-critical financial trading system backend.
    High-frequency trading, real-time data processing, strict compliance.
    Java Spring Boot, PostgreSQL cluster, Redis, Kafka.
    Large team of 20+ developers, enterprise security requirements.
    """
    
    projects = [
        ("Prototype", prototype_description),
        ("Enterprise", enterprise_description)
    ]
    
    for project_name, description in projects:
        print(f"\n📋 {project_name} Project Configuration:")
        
        try:
            analysis = await analyzer.analyze_project(description)
            pattern_name, pattern, score = pattern_library.select_best_pattern(analysis)
            config = await config_generator.generate_config(analysis, pattern)
            
            print(f"   - Quality Level: {analysis.constraints.quality_requirements}")
            print(f"   - Team Size: {analysis.constraints.team_size}")
            print(f"   - Max Agents: {config.orchestrator.maxConcurrentAgents}")
            print(f"   - Memory Cache: {config.memory.cacheSizeMB}MB")
            print(f"   - Encryption: {config.memory.encryptionEnabled}")
            print(f"   - Audit Logging: {config.logging.audit.get('enabled', False)}")
            print(f"   - Failover: {config.orchestrator.failover['enabled']}")
            
        except Exception as e:
            print(f"   ❌ Failed: {str(e)}")


async def main():
    """Run all demos."""
    
    print("🎯 Standard Claude Flow Configuration Generator - Demo")
    print("=" * 70)
    print("This demo shows the new standard configuration generation")
    print("that conforms to the official Claude Flow format.")
    print("=" * 70)
    
    # Run demos
    success1 = await demo_standard_config_generation()
    await demo_different_environments()
    
    print(f"\n🎉 Demo Summary:")
    print(f"   - Standard Config Generation: {'✅ Success' if success1 else '❌ Failed'}")
    
    if success1:
        print(f"\n🎊 Demo completed successfully!")
        print(f"   Check the 'standard_config_output' directory for generated configurations.")
        print(f"   The configuration is now ready for use with Claude Flow!")
    else:
        print(f"\n⚠️ Demo failed. Check the error messages above.")


if __name__ == "__main__":
    asyncio.run(main())
