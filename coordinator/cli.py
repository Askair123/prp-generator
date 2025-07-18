"""
CLI interface for Coordinator Pattern system.

This module provides a command-line interface for analyzing projects
and generating Claude Flow configurations.
"""

import asyncio
import sys
from pathlib import Path
from typing import Optional

from .project_analyzer import ProjectAnalyzer
from .pattern_library import PatternLibrary
from .claude_flow_adapter import ClaudeFlowAdapter


class CoordinatorCLI:
    """Command-line interface for the Coordinator Pattern system."""

    def __init__(self):
        """Initialize the CLI with core components."""
        self.analyzer = ProjectAnalyzer()
        self.pattern_library = PatternLibrary()
        self.adapter = ClaudeFlowAdapter()

    async def analyze_and_generate(self, description: str, output_path: str = "output") -> bool:
        """
        Analyze project and generate Claude Flow configuration.

        Args:
            description: Project description
            output_path: Output directory path

        Returns:
            True if successful, False otherwise
        """
        try:
            print("🔍 Analyzing project requirements...")

            # Step 1: Analyze project
            analysis = await self.analyzer.analyze_project(description)

            print(f"✅ Project Analysis Complete:")
            print(f"   - Type: {analysis.project_type.value}")
            print(f"   - Complexity: {analysis.complexity_metrics.complexity_level.value}")
            print(f"   - Confidence: {analysis.confidence_score:.2f}")
            print(f"   - Tech Stack: {', '.join(analysis.technical_requirements.languages)}")

            # Step 2: Select best pattern
            print("\n🎯 Selecting coordination pattern...")
            pattern_name, pattern, score = self.pattern_library.select_best_pattern(analysis)

            print(f"✅ Pattern Selected: {pattern_name} (score: {score:.2f})")
            print(f"   - Description: {pattern.description}")
            print(f"   - Agents: {', '.join(pattern.agents)}")

            # Step 3: Generate Claude Flow config
            print("\n⚙️ Generating Claude Flow configuration...")
            config = await self.adapter.generate_config(analysis, pattern)

            # Step 4: Validate configuration
            print("\n🔍 Validating configuration...")
            validation = await self.adapter.validate_config(config)

            if not validation.is_valid:
                print(f"❌ Validation failed:")
                for error in validation.errors:
                    print(f"   - Error: {error}")
                return False

            if validation.warnings:
                print(f"⚠️ Validation warnings:")
                for warning in validation.warnings:
                    print(f"   - Warning: {warning}")

            print(f"✅ Configuration valid (score: {validation.score:.2f})")

            # Step 5: Execute handoff
            print("\n🚀 Executing handoff to Claude Flow...")
            handoff = await self.adapter.handoff_to_claude_flow(config, output_path)

            if handoff.success:
                print(f"✅ Handoff successful!")
                print(f"   - Config saved to: {handoff.config_path}")
                print(f"   - Claude Flow ready: {handoff.claude_flow_ready}")

                print(f"\n📋 Next steps:")
                for step in handoff.next_steps:
                    print(f"   - {step}")

                return True
            else:
                print(f"❌ Handoff failed")
                for step in handoff.next_steps:
                    print(f"   - {step}")
                return False

        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return False

    def interactive_mode(self):
        """Run in interactive mode."""
        print("🎯 Coordinator Pattern System - Interactive Mode")
        print("=" * 50)

        while True:
            print("\nOptions:")
            print("1. Analyze project and generate config")
            print("2. List available patterns")
            print("3. Exit")

            choice = input("\nSelect option (1-3): ").strip()

            if choice == "1":
                description = input("\nEnter project description: ").strip()
                if description:
                    output_path = input("Output directory (default: output): ").strip() or "output"
                    print("\n" + "=" * 50)
                    success = asyncio.run(self.analyze_and_generate(description, output_path))
                    if success:
                        print("\n🎉 Configuration generated successfully!")
                    else:
                        print("\n💥 Configuration generation failed!")
                else:
                    print("❌ Please provide a project description")

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
        description = " ".join(sys.argv[1:])
        success = asyncio.run(cli.analyze_and_generate(description))
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