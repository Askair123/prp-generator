"""
CLI interface for Coordinator Pattern system.

This module provides a command-line interface for processing PRP documents
and generating Claude Flow configurations.
"""

import asyncio
import sys
from pathlib import Path
from typing import Optional

from .prp_parser import PRPParser
from .pattern_library import PatternLibrary
from .claude_flow_config_generator import ClaudeFlowConfigGenerator


class CoordinatorCLI:
    """Command-line interface for the PRP-driven Coordinator Pattern system."""

    def __init__(self):
        """Initialize the CLI with core components."""
        self.prp_parser = PRPParser()
        self.pattern_library = PatternLibrary()
        self.config_generator = ClaudeFlowConfigGenerator()

    async def process_prp(self, prp_path: str, output_path: str = "output") -> bool:
        """
        Process PRP document and generate Claude Flow configuration.

        Args:
            prp_path: Path to PRP document
            output_path: Output directory path

        Returns:
            True if successful, False otherwise
        """
        try:
            print(f"🔍 Processing PRP document: {prp_path}")

            # Step 1: Parse PRP document
            prp_analysis = await self.prp_parser.parse_prp_file(prp_path)

            print(f"✅ PRP Analysis Complete:")
            print(f"   - Project: {prp_analysis.name}")
            print(f"   - Success Criteria: {len(prp_analysis.success_criteria)} items")
            print(f"   - Agent Requirements: {', '.join(prp_analysis.agent_requirements[:5])}...")
            print(f"   - Tech Stack: {', '.join(prp_analysis.technical_requirements.get('languages', []))}")

            # Step 2: Convert to project analysis
            print("\n🔍 Converting PRP to project analysis...")
            analysis = await self.prp_parser.convert_prp_to_project_analysis(prp_analysis)

            print(f"✅ Project Analysis:")
            print(f"   - Type: {analysis.project_type}")
            print(f"   - Complexity: {analysis.complexity_metrics.complexity_level}")
            print(f"   - Confidence: {analysis.confidence_score:.2f}")

            # Step 3: Select best pattern
            print("\n🎯 Selecting coordination pattern...")
            pattern_name, pattern, score = self.pattern_library.select_best_pattern(analysis)

            print(f"✅ Pattern Selected: {pattern_name} (score: {score:.2f})")
            print(f"   - Description: {pattern.description}")
            print(f"   - Agents: {', '.join(pattern.agents)}")

            # Step 4: Generate Claude Flow config
            print("\n⚙️ Generating Claude Flow configuration...")
            config = await self.config_generator.generate_config(analysis, pattern)

            # Step 5: Save configuration
            print("\n💾 Saving configuration...")

            # Create output directory
            output_dir = Path(output_path)
            output_dir.mkdir(exist_ok=True)

            # Generate filename
            prp_name = Path(prp_path).stem
            config_filename = f"claude-flow-{prp_name}.config.json"
            config_path = output_dir / config_filename

            # Save configuration
            config.save_to_file(str(config_path))

            print(f"✅ Configuration saved to: {config_path}")

            # Step 6: Show usage instructions
            print(f"\n🚀 Claude Flow Usage:")
            print(f"   # Validate the configuration")
            print(f"   claude-flow config validate --file {config_path}")
            print(f"   ")
            print(f"   # Start Claude Flow with this configuration")
            print(f"   claude-flow --config {config_path} start")
            print(f"   ")
            print(f"   # Monitor system status")
            print(f"   claude-flow status")

            return True

        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return False

    def interactive_mode(self):
        """Run in interactive mode."""
        print("🎯 Coordinator Pattern System - Interactive Mode")
        print("=" * 50)

        while True:
            print("\nOptions:")
            print("1. Process PRP document and generate config")
            print("2. List available patterns")
            print("3. Exit")

            choice = input("\nSelect option (1-3): ").strip()

            if choice == "1":
                prp_path = input("\nEnter PRP document path: ").strip()
                if prp_path and Path(prp_path).exists():
                    output_path = input("Output directory (default: output): ").strip() or "output"
                    print("\n" + "=" * 50)
                    success = asyncio.run(self.process_prp(prp_path, output_path))
                    if success:
                        print("\n🎉 Configuration generated successfully!")
                    else:
                        print("\n💥 Configuration generation failed!")
                else:
                    print("❌ Please provide a valid PRP document path")

            elif choice == "2":
                self._list_patterns()

            elif choice == "3":
                print("👋 Goodbye!")
                break

            else:
                print("❌ Invalid option. Please select 1-3.")

    def _list_patterns(self):
        """List available coordination patterns."""
        print("\n📚 Available Coordination Patterns:")
        print("=" * 40)

        patterns = self.pattern_library.get_coordination_patterns()

        for name, pattern in patterns.items():
            print(f"\n🎯 {name.title()}")
            print(f"   Description: {pattern.description}")
            print(f"   Best for: {', '.join(pattern.best_for[:3])}")
            print(f"   Agents: {', '.join(pattern.agents[:4])}")
            if len(pattern.agents) > 4:
                print(f"           ... and {len(pattern.agents) - 4} more")


def main():
    """Main CLI entry point."""
    cli = CoordinatorCLI()

    if len(sys.argv) > 1:
        # Command line mode
        prp_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else "output"
        success = asyncio.run(cli.process_prp(prp_path, output_path))
        sys.exit(0 if success else 1)
    else:
        # Interactive mode
        try:
            cli.interactive_mode()
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            sys.exit(0)


if __name__ == "__main__":
    main()