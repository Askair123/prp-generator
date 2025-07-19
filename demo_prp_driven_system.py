#!/usr/bin/env python3
"""
Demo script for PRP-driven Coordinator Pattern system.

This script demonstrates the CORRECT architecture:
Input: PRP document → Output: claude-flow.config.json
"""

import asyncio
import sys
from pathlib import Path

# Add coordinator to path
sys.path.insert(0, str(Path(__file__).parent))

from coordinator import PatternLibrary
from coordinator.prp_parser import PRPParser
from coordinator.claude_flow_config_generator import ClaudeFlowConfigGenerator


class PRPDrivenCoordinator:
    """
    PRP-driven Coordinator Pattern system.
    
    This is the CORRECT implementation that takes PRP documents as input
    and generates Claude Flow configurations as output.
    """
    
    def __init__(self):
        """Initialize the PRP-driven coordinator."""
        self.prp_parser = PRPParser()
        self.pattern_library = PatternLibrary()
        self.config_generator = ClaudeFlowConfigGenerator()
    
    async def process_prp(self, prp_path: str, output_dir: str = "prp_output") -> bool:
        """
        Process a PRP document and generate Claude Flow configuration.
        
        Args:
            prp_path: Path to the PRP document
            output_dir: Output directory for generated configuration
            
        Returns:
            True if successful, False otherwise
        """
        try:
            print(f"🎯 Processing PRP: {prp_path}")
            print("=" * 60)
            
            # Step 1: Parse PRP document
            print("\n📋 Step 1: Parsing PRP document...")
            prp_analysis = await self.prp_parser.parse_prp_file(prp_path)
            
            print(f"✅ PRP Analysis Complete:")
            print(f"   - Project: {prp_analysis.name}")
            print(f"   - Goal: {prp_analysis.goal[:100]}...")
            print(f"   - Success Criteria: {len(prp_analysis.success_criteria)} items")
            print(f"   - Tech Requirements: {len(prp_analysis.technical_requirements)} categories")
            print(f"   - Agent Requirements: {', '.join(prp_analysis.agent_requirements)}")
            print(f"   - Coordination Hints: {', '.join(prp_analysis.coordination_hints)}")
            
            # Step 2: Convert PRP to project analysis
            print(f"\n🔍 Step 2: Converting PRP to project analysis...")
            project_analysis = await self.prp_parser.convert_prp_to_project_analysis(prp_analysis)
            
            print(f"✅ Project Analysis:")
            print(f"   - Project Type: {project_analysis.project_type}")
            print(f"   - Complexity Level: {project_analysis.complexity_metrics.complexity_level}")
            print(f"   - Team Size: {project_analysis.constraints.team_size}")
            print(f"   - Quality Level: {project_analysis.constraints.quality_requirements}")
            print(f"   - Confidence: {project_analysis.confidence_score:.2f}")
            
            # Step 3: Select coordination pattern
            print(f"\n🎯 Step 3: Selecting coordination pattern...")
            pattern_name, pattern, score = self.pattern_library.select_best_pattern(project_analysis)
            
            print(f"✅ Pattern Selected: {pattern_name} (score: {score:.3f})")
            print(f"   - Description: {pattern.description}")
            print(f"   - Agents: {', '.join(pattern.agents)}")
            print(f"   - Coordination: {pattern.coordination_rules}")
            
            # Step 4: Generate Claude Flow configuration
            print(f"\n⚙️ Step 4: Generating Claude Flow configuration...")
            config = await self.config_generator.generate_config(project_analysis, pattern)
            
            print(f"✅ Configuration Generated:")
            print(f"   - Orchestrator: {config.orchestrator.maxConcurrentAgents} max agents")
            print(f"   - Memory: {config.memory.backend} backend, {config.memory.cacheSizeMB}MB cache")
            print(f"   - Coordination: {config.coordination.loadBalancingStrategy} load balancing")
            print(f"   - MCP Tools: {len(config.mcp.allowedTools)} allowed tools")
            print(f"   - Security: Encryption={config.memory.encryptionEnabled}, Sandbox={config.terminal.security.get('sandboxed', False)}")
            
            # Step 5: Save configuration
            print(f"\n💾 Step 5: Saving configuration...")
            
            # Create output directory
            output_path = Path(output_dir)
            output_path.mkdir(exist_ok=True)
            
            # Generate filename based on PRP name
            prp_name = Path(prp_path).stem
            config_filename = f"claude-flow-{prp_name}.config.json"
            config_path = output_path / config_filename
            
            # Save configuration
            config.save_to_file(str(config_path))
            
            print(f"✅ Configuration saved to: {config_path}")
            
            # Step 6: Generate usage instructions
            print(f"\n📋 Step 6: Usage Instructions:")
            print(f"   # Validate the generated configuration")
            print(f"   claude-flow config validate --file {config_path}")
            print(f"   ")
            print(f"   # Start Claude Flow with this configuration")
            print(f"   claude-flow --config {config_path} start")
            print(f"   ")
            print(f"   # Monitor the system")
            print(f"   claude-flow status")
            
            # Step 7: Show configuration preview
            print(f"\n📄 Configuration Preview:")
            try:
                with open(config_path, 'r') as f:
                    config_content = f.read()
                    lines = config_content.split('\n')[:15]
                    for line in lines:
                        print(f"   {line}")
                    if len(config_content.split('\n')) > 15:
                        print(f"   ... (see full file for complete configuration)")
            except Exception as e:
                print(f"   Could not preview file: {e}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error processing PRP: {str(e)}")
            import traceback
            traceback.print_exc()
            return False


async def demo_multi_agent_prp():
    """Demo: Process the multi-agent PRP example."""
    
    print("🎯 Demo: PRP-Driven Multi-Agent System Configuration")
    print("=" * 70)
    
    coordinator = PRPDrivenCoordinator()
    
    # Process the example multi-agent PRP
    prp_path = "PRPs/EXAMPLE_multi_agent_prp.md"
    
    if not Path(prp_path).exists():
        print(f"❌ PRP file not found: {prp_path}")
        return False
    
    success = await coordinator.process_prp(prp_path, "prp_multi_agent_output")
    
    if success:
        print(f"\n🎉 Multi-Agent PRP processed successfully!")
        print(f"   The generated configuration is ready for Claude Flow!")
    else:
        print(f"\n💥 Failed to process multi-agent PRP!")
    
    return success


async def demo_coordinator_prp():
    """Demo: Process the coordinator pattern PRP."""
    
    print("\n\n🎯 Demo: PRP-Driven Coordinator Pattern System")
    print("=" * 70)
    
    coordinator = PRPDrivenCoordinator()
    
    # Process the coordinator pattern PRP
    prp_path = "PRPs/coordinator-pattern-system.md"
    
    if not Path(prp_path).exists():
        print(f"❌ PRP file not found: {prp_path}")
        return False
    
    success = await coordinator.process_prp(prp_path, "prp_coordinator_output")
    
    if success:
        print(f"\n🎉 Coordinator PRP processed successfully!")
        print(f"   The generated configuration is ready for Claude Flow!")
    else:
        print(f"\n💥 Failed to process coordinator PRP!")
    
    return success


async def compare_architectures():
    """Compare the old vs new architecture."""
    
    print("\n\n📊 Architecture Comparison")
    print("=" * 50)
    
    print("❌ OLD (Incorrect) Architecture:")
    print("   Input: Natural language description")
    print("   Process: Text analysis → Pattern selection → Config generation")
    print("   Output: claude-flow.config.json")
    print("   Problem: Bypasses structured requirements")
    
    print("\n✅ NEW (Correct) Architecture:")
    print("   Input: PRP document (structured requirements)")
    print("   Process: PRP parsing → Project analysis → Pattern selection → Config generation")
    print("   Output: claude-flow.config.json")
    print("   Benefits: Structured input, better analysis, higher confidence")
    
    print("\n🎯 Key Improvements:")
    print("   - Structured requirement extraction from PRP")
    print("   - Better technical requirement identification")
    print("   - Higher confidence scores due to structured input")
    print("   - Alignment with Context Engineering principles")
    print("   - Support for complex multi-agent specifications")


async def main():
    """Run all demos."""
    
    print("🎯 PRP-Driven Coordinator Pattern System - Demo")
    print("=" * 80)
    print("This demo shows the CORRECT architecture that processes PRP documents")
    print("and generates Claude Flow configurations.")
    print("=" * 80)
    
    # Compare architectures
    await compare_architectures()
    
    # Run PRP processing demos
    success1 = await demo_multi_agent_prp()
    success2 = await demo_coordinator_prp()
    
    print(f"\n🎉 Demo Summary:")
    print(f"   - Multi-Agent PRP: {'✅ Success' if success1 else '❌ Failed'}")
    print(f"   - Coordinator PRP: {'✅ Success' if success2 else '❌ Failed'}")
    
    if success1 or success2:
        print(f"\n🎊 PRP-driven system working correctly!")
        print(f"   Check the output directories for generated configurations.")
        print(f"   The configurations are ready for direct use with Claude Flow!")
    else:
        print(f"\n⚠️ Some demos failed. Check the error messages above.")
    
    print(f"\n📋 Next Steps:")
    print(f"   1. Review the generated claude-flow.config.json files")
    print(f"   2. Validate them with: claude-flow config validate --file <config>")
    print(f"   3. Start Claude Flow with: claude-flow --config <config> start")


if __name__ == "__main__":
    asyncio.run(main())
