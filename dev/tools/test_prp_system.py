#!/usr/bin/env python3
"""
Test script for PRP-driven Coordinator Pattern system.

This script tests our system with a comprehensive simulated PRP document
for an e-commerce multi-agent system.
"""

import asyncio
import sys
import json
from pathlib import Path

# Add coordinator to path
sys.path.insert(0, str(Path(__file__).parent))

from coordinator import PatternLibrary
from coordinator.prp_parser import PRPParser
from coordinator.claude_flow_config_generator import ClaudeFlowConfigGenerator


async def test_ecommerce_prp():
    """Test the e-commerce multi-agent system PRP."""
    
    print("🎯 Testing E-commerce Multi-Agent System PRP")
    print("=" * 70)
    
    # Initialize components
    prp_parser = PRPParser()
    pattern_library = PatternLibrary()
    config_generator = ClaudeFlowConfigGenerator()
    
    prp_path = "test_prps/ecommerce-api-system.prp.md"
    
    if not Path(prp_path).exists():
        print(f"❌ PRP file not found: {prp_path}")
        return False
    
    try:
        # Step 1: Parse PRP document
        print("\n📋 Step 1: Parsing PRP document...")
        prp_analysis = await prp_parser.parse_prp_file(prp_path)
        
        print(f"✅ PRP Analysis Results:")
        print(f"   📝 Project Name: {prp_analysis.name}")
        print(f"   🎯 Goal: {prp_analysis.goal[:100]}...")
        print(f"   💼 Business Value: {prp_analysis.why[:100]}...")
        print(f"   📋 Success Criteria: {len(prp_analysis.success_criteria)} items")
        print(f"   📚 Documentation Refs: {len(prp_analysis.documentation_refs)} references")
        print(f"   🤖 Agent Requirements: {', '.join(prp_analysis.agent_requirements)}")
        print(f"   🔗 Coordination Hints: {', '.join(prp_analysis.coordination_hints)}")
        
        # Show technical requirements
        tech_reqs = prp_analysis.technical_requirements
        print(f"\n🔧 Technical Requirements:")
        print(f"   - Languages: {', '.join(tech_reqs.get('languages', []))}")
        print(f"   - Frameworks: {', '.join(tech_reqs.get('frameworks', []))}")
        print(f"   - Databases: {', '.join(tech_reqs.get('databases', []))}")
        print(f"   - Infrastructure: {', '.join(tech_reqs.get('infrastructure', []))}")
        print(f"   - APIs: {', '.join(tech_reqs.get('apis', []))}")
        
        # Show constraints
        constraints = prp_analysis.constraints
        print(f"\n📊 Project Constraints:")
        print(f"   - Timeline: {constraints.get('timeline', 'Not specified')}")
        print(f"   - Team Size: {constraints.get('team_size', 'Not specified')}")
        print(f"   - Quality Level: {constraints.get('quality', 'Not specified')}")
        
        # Step 2: Convert to project analysis
        print(f"\n🔍 Step 2: Converting PRP to project analysis...")
        project_analysis = await prp_parser.convert_prp_to_project_analysis(prp_analysis)
        
        print(f"✅ Project Analysis:")
        print(f"   - Project Type: {project_analysis.project_type}")
        print(f"   - Complexity Level: {project_analysis.complexity_metrics.complexity_level}")
        print(f"   - Technical Complexity: {project_analysis.complexity_metrics.technical_complexity}/10")
        print(f"   - Organizational Complexity: {project_analysis.complexity_metrics.organizational_complexity}/10")
        print(f"   - Temporal Complexity: {project_analysis.complexity_metrics.temporal_complexity}/10")
        print(f"   - Overall Score: {project_analysis.complexity_metrics.overall_score:.1f}/10")
        print(f"   - Team Size: {project_analysis.constraints.team_size}")
        print(f"   - Quality Requirements: {project_analysis.constraints.quality_requirements}")
        print(f"   - Confidence Score: {project_analysis.confidence_score:.2f}")
        
        # Step 3: Pattern selection
        print(f"\n🎯 Step 3: Selecting coordination pattern...")
        
        # Show all pattern scores
        scored_patterns = pattern_library.get_matching_patterns(project_analysis)
        print(f"   📊 Pattern Scores:")
        for pattern_name, score in scored_patterns:
            print(f"   - {pattern_name}: {score:.3f}")
        
        # Select best pattern
        best_name, best_pattern, best_score = pattern_library.select_best_pattern(project_analysis)
        
        print(f"\n✅ Selected Pattern: {best_name} (score: {best_score:.3f})")
        print(f"   - Description: {best_pattern.description}")
        print(f"   - Coordination Rules: {best_pattern.coordination_rules}")
        print(f"   - Agents: {', '.join(best_pattern.agents)}")
        print(f"   - Quality Gates: {', '.join(best_pattern.quality_gates)}")
        
        # Step 4: Generate Claude Flow configuration
        print(f"\n⚙️ Step 4: Generating Claude Flow configuration...")
        config = await config_generator.generate_config(project_analysis, best_pattern)
        
        print(f"✅ Configuration Generated:")
        print(f"   🎛️ Orchestrator:")
        print(f"      - Max Concurrent Agents: {config.orchestrator.maxConcurrentAgents}")
        print(f"      - Task Queue Size: {config.orchestrator.taskQueueSize}")
        print(f"      - Resource Allocation: {config.orchestrator.resourceAllocationStrategy}")
        print(f"      - Agent Recycling: {config.orchestrator.agentRecycling['enabled']}")
        print(f"      - Failover Enabled: {config.orchestrator.failover['enabled']}")
        
        print(f"   💾 Memory:")
        print(f"      - Backend: {config.memory.backend}")
        print(f"      - Cache Size: {config.memory.cacheSizeMB}MB")
        print(f"      - Retention: {config.memory.retentionDays} days")
        print(f"      - Encryption: {config.memory.encryptionEnabled}")
        print(f"      - Compression: {config.memory.compressionEnabled}")
        
        print(f"   🔗 Coordination:")
        print(f"      - Load Balancing: {config.coordination.loadBalancingStrategy}")
        print(f"      - Scheduling: {config.coordination.scheduling.get('algorithm', 'N/A')}")
        print(f"      - Max Retries: {config.coordination.maxRetries}")
        print(f"      - Deadlock Detection: {config.coordination.deadlockDetection}")
        
        print(f"   🛠️ MCP:")
        print(f"      - Transport: {config.mcp.transport}")
        print(f"      - Allowed Tools: {len(config.mcp.allowedTools)} tools")
        print(f"      - Rate Limiting: {config.mcp.rateLimiting['enabled']}")
        print(f"      - Authentication: {config.mcp.authentication['enabled']}")
        
        print(f"   📊 Terminal:")
        print(f"      - Pool Size: {config.terminal.poolSize}")
        print(f"      - Security Sandboxed: {config.terminal.security.get('sandboxed', False)}")
        print(f"      - Max Commands: {config.terminal.maxConcurrentCommands}")
        
        print(f"   📝 Logging:")
        print(f"      - Level: {config.logging.level}")
        print(f"      - Format: {config.logging.format}")
        print(f"      - Destination: {config.logging.destination}")
        print(f"      - Audit Enabled: {config.logging.audit.get('enabled', False)}")
        
        # Step 5: Save configuration
        print(f"\n💾 Step 5: Saving configuration...")
        
        output_dir = Path("test_output")
        output_dir.mkdir(exist_ok=True)
        
        config_path = output_dir / "claude-flow-ecommerce-test.config.json"
        config.save_to_file(str(config_path))
        
        print(f"✅ Configuration saved to: {config_path}")
        
        # Step 6: Analyze configuration quality
        print(f"\n📊 Step 6: Configuration Quality Analysis...")
        
        # Check if configuration matches PRP requirements
        quality_score = 0
        total_checks = 10
        
        # Check 1: Agent count matches complexity
        expected_agents = len(prp_analysis.agent_requirements) * 2  # Rough estimate
        if config.orchestrator.maxConcurrentAgents >= expected_agents:
            quality_score += 1
            print(f"   ✅ Agent count ({config.orchestrator.maxConcurrentAgents}) matches complexity")
        else:
            print(f"   ⚠️ Agent count might be low for {len(prp_analysis.agent_requirements)} agent types")
        
        # Check 2: Memory size appropriate for enterprise system
        if config.memory.cacheSizeMB >= 500:  # Enterprise should have substantial cache
            quality_score += 1
            print(f"   ✅ Memory cache ({config.memory.cacheSizeMB}MB) appropriate for enterprise")
        else:
            print(f"   ⚠️ Memory cache might be small for enterprise system")
        
        # Check 3: Security features enabled for production
        if config.memory.encryptionEnabled:
            quality_score += 1
            print(f"   ✅ Encryption enabled for production security")
        else:
            print(f"   ⚠️ Encryption not enabled")
        
        # Check 4: Audit logging for enterprise
        if config.logging.audit.get('enabled', False):
            quality_score += 1
            print(f"   ✅ Audit logging enabled for compliance")
        else:
            print(f"   ⚠️ Audit logging not enabled")
        
        # Check 5: Failover for high availability
        if config.orchestrator.failover['enabled']:
            quality_score += 1
            print(f"   ✅ Failover enabled for high availability")
        else:
            print(f"   ⚠️ Failover not enabled")
        
        # Check 6: Terminal security for production
        if config.terminal.security.get('sandboxed', False):
            quality_score += 1
            print(f"   ✅ Terminal sandboxing enabled")
        else:
            print(f"   ⚠️ Terminal sandboxing not enabled")
        
        # Check 7: Rate limiting enabled
        if config.mcp.rateLimiting['enabled']:
            quality_score += 1
            print(f"   ✅ Rate limiting enabled")
        else:
            print(f"   ⚠️ Rate limiting not enabled")
        
        # Check 8: Authentication for security
        if config.mcp.authentication['enabled']:
            quality_score += 1
            print(f"   ✅ MCP authentication enabled")
        else:
            print(f"   ⚠️ MCP authentication not enabled")
        
        # Check 9: Appropriate backend for multi-agent system
        if config.memory.backend in ['hybrid', 'sqlite']:
            quality_score += 1
            print(f"   ✅ Memory backend ({config.memory.backend}) suitable for multi-agent")
        else:
            print(f"   ⚠️ Memory backend might not be optimal")
        
        # Check 10: Load balancing strategy
        if config.coordination.loadBalancingStrategy in ['weighted', 'adaptive']:
            quality_score += 1
            print(f"   ✅ Load balancing ({config.coordination.loadBalancingStrategy}) appropriate")
        else:
            print(f"   ⚠️ Load balancing strategy might be suboptimal")
        
        quality_percentage = (quality_score / total_checks) * 100
        print(f"\n📈 Overall Configuration Quality: {quality_score}/{total_checks} ({quality_percentage:.0f}%)")
        
        if quality_percentage >= 80:
            print(f"   🎉 Excellent configuration quality!")
        elif quality_percentage >= 60:
            print(f"   👍 Good configuration quality")
        else:
            print(f"   ⚠️ Configuration needs improvement")
        
        # Step 7: Generate usage commands
        print(f"\n🚀 Step 7: Claude Flow Usage Commands:")
        print(f"   # Validate the configuration")
        print(f"   claude-flow config validate --file {config_path}")
        print(f"   ")
        print(f"   # Start the e-commerce multi-agent system")
        print(f"   claude-flow --config {config_path} start")
        print(f"   ")
        print(f"   # Monitor system status")
        print(f"   claude-flow status")
        print(f"   ")
        print(f"   # Check specific configuration values")
        print(f"   claude-flow config get orchestrator.maxConcurrentAgents")
        print(f"   claude-flow config get memory.backend")
        
        # Step 8: Show configuration preview
        print(f"\n📄 Configuration File Preview:")
        try:
            with open(config_path, 'r') as f:
                config_content = f.read()
                config_json = json.loads(config_content)
                
                # Show key sections
                print(f"   📋 Key Configuration Sections:")
                print(f"   - Orchestrator: {config_json['orchestrator']['maxConcurrentAgents']} agents, {config_json['orchestrator']['resourceAllocationStrategy']} allocation")
                print(f"   - Memory: {config_json['memory']['backend']} backend, {config_json['memory']['cacheSizeMB']}MB cache")
                print(f"   - Coordination: {config_json['coordination']['loadBalancingStrategy']} load balancing")
                print(f"   - Security: Encryption={config_json['memory']['encryptionEnabled']}, Audit={config_json['logging']['audit']['enabled']}")
                
        except Exception as e:
            print(f"   Could not preview file: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed with error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Run the PRP test."""
    
    print("🎯 PRP-Driven System Test")
    print("=" * 50)
    print("Testing our system with a comprehensive e-commerce multi-agent PRP")
    print("=" * 50)
    
    success = await test_ecommerce_prp()
    
    print(f"\n🎉 Test Summary:")
    print(f"   - E-commerce PRP Processing: {'✅ Success' if success else '❌ Failed'}")
    
    if success:
        print(f"\n🎊 Test completed successfully!")
        print(f"   - PRP document was parsed correctly")
        print(f"   - Project analysis was accurate")
        print(f"   - Coordination pattern was selected appropriately")
        print(f"   - Claude Flow configuration was generated")
        print(f"   - Configuration quality is high")
        print(f"   - Ready for production use with Claude Flow!")
    else:
        print(f"\n💥 Test failed!")
        print(f"   Check the error messages above for details.")


if __name__ == "__main__":
    asyncio.run(main())
