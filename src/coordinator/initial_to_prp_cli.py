"""
Command Line Interface for Initial to PRP Generation.

This module provides a CLI for generating PRPs from INITIAL.md files,
following the context-engineering-intro project patterns.
"""

import asyncio
import argparse
import sys
from pathlib import Path
from typing import Optional

# Add the parent directory to sys.path to enable imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from coordinator.initial_to_prp_generator import InitialToPRPGenerator, PRPGenerationConfig


class InitialToPRPCLI:
    """Command line interface for Initial to PRP generation."""
    
    def __init__(self):
        """Initialize the CLI."""
        self.generator = InitialToPRPGenerator()
    
    def create_parser(self) -> argparse.ArgumentParser:
        """Create the argument parser."""
        parser = argparse.ArgumentParser(
            description="Generate comprehensive PRPs from INITIAL.md files",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  # Generate PRP from INITIAL.md
  python -m coordinator.initial_to_prp_cli generate INITIAL.md
  
  # Generate PRP with custom output directory
  python -m coordinator.initial_to_prp_cli generate INITIAL.md --output PRPs/custom
  
  # Generate PRP without research (faster)
  python -m coordinator.initial_to_prp_cli generate INITIAL.md --no-research
  
  # Validate an existing INITIAL.md file
  python -m coordinator.initial_to_prp_cli validate INITIAL.md
            """
        )
        
        subparsers = parser.add_subparsers(dest='command', help='Available commands')
        
        # Generate command
        generate_parser = subparsers.add_parser(
            'generate',
            help='Generate PRP from INITIAL.md file'
        )
        generate_parser.add_argument(
            'initial_file',
            help='Path to INITIAL.md file'
        )
        generate_parser.add_argument(
            '--output', '-o',
            default='PRPs',
            help='Output directory for generated PRP (default: PRPs)'
        )
        generate_parser.add_argument(
            '--project-root', '-p',
            default='.',
            help='Project root directory (default: current directory)'
        )
        generate_parser.add_argument(
            '--no-research',
            action='store_true',
            help='Skip research phase for faster generation'
        )
        generate_parser.add_argument(
            '--template',
            help='Custom PRP template file'
        )
        
        # Validate command
        validate_parser = subparsers.add_parser(
            'validate',
            help='Validate INITIAL.md file format'
        )
        validate_parser.add_argument(
            'initial_file',
            help='Path to INITIAL.md file to validate'
        )
        
        # List command
        list_parser = subparsers.add_parser(
            'list',
            help='List existing PRPs'
        )
        list_parser.add_argument(
            '--directory', '-d',
            default='PRPs',
            help='Directory to search for PRPs (default: PRPs)'
        )
        
        return parser
    
    async def run_generate(self, args) -> int:
        """Run the generate command."""
        try:
            # Validate input file
            initial_file = Path(args.initial_file)
            if not initial_file.exists():
                print(f"❌ Error: INITIAL.md file not found: {args.initial_file}")
                return 1
            
            # Create configuration
            config = PRPGenerationConfig(
                output_directory=args.output,
                include_research=not args.no_research,
                template_path=args.template or "PRPs/templates/prp_base.md"
            )
            
            # Update generator configuration
            self.generator.config = config
            
            print("🚀 Starting PRP generation from INITIAL.md...")
            print(f"📁 Input file: {args.initial_file}")
            print(f"📁 Output directory: {args.output}")
            print(f"📁 Project root: {args.project_root}")
            print(f"🔬 Research enabled: {not args.no_research}")
            print()
            
            # Generate PRP
            generated_prp = await self.generator.generate_prp_from_initial(
                str(initial_file),
                args.project_root
            )
            
            print()
            print("🎉 PRP Generation Complete!")
            print(f"📄 Generated file: {generated_prp.file_path}")
            print(f"🎯 Confidence score: {generated_prp.confidence_score}/10")
            print(f"⏰ Generated at: {generated_prp.generation_timestamp}")
            print()
            
            # Show validation commands
            if generated_prp.validation_commands:
                print("✅ Validation commands to run after implementation:")
                for i, cmd in enumerate(generated_prp.validation_commands, 1):
                    print(f"  {i}. {cmd}")
                print()
            
            # Show next steps
            print("📋 Next steps:")
            print(f"  1. Review the generated PRP: {generated_prp.file_path}")
            print("  2. Use the PRP to implement your feature")
            print("  3. Run the validation commands to ensure quality")
            print("  4. Iterate based on validation results")
            
            return 0
            
        except Exception as e:
            print(f"❌ Error generating PRP: {str(e)}")
            return 1
    
    async def run_validate(self, args) -> int:
        """Run the validate command."""
        try:
            # Parse the INITIAL.md file
            initial_analysis = await self.generator.initial_parser.parse_initial_file(args.initial_file)
            
            print("✅ INITIAL.md Validation Results:")
            print(f"📁 File: {args.initial_file}")
            print()
            
            # Check feature section
            if initial_analysis.feature and len(initial_analysis.feature) > 10:
                print("✅ Feature section: Well-defined")
            else:
                print("⚠️  Feature section: Needs more detail")
            
            # Check examples section
            if initial_analysis.examples:
                print(f"✅ Examples section: {len(initial_analysis.examples)} examples provided")
            else:
                print("⚠️  Examples section: No examples provided")
            
            # Check documentation section
            if initial_analysis.documentation:
                print(f"✅ Documentation section: {len(initial_analysis.documentation)} references")
            else:
                print("⚠️  Documentation section: No documentation references")
            
            # Check other considerations
            if initial_analysis.other_considerations:
                print(f"✅ Other considerations: {len(initial_analysis.other_considerations)} items")
            else:
                print("ℹ️  Other considerations: None specified")
            
            print()
            
            # Overall assessment
            score = 0
            if initial_analysis.feature and len(initial_analysis.feature) > 10:
                score += 3
            if initial_analysis.examples:
                score += 2
            if initial_analysis.documentation:
                score += 2
            if initial_analysis.other_considerations:
                score += 1
            
            if score >= 7:
                print("🎉 Overall: Excellent - Ready for PRP generation")
            elif score >= 5:
                print("👍 Overall: Good - Minor improvements recommended")
            elif score >= 3:
                print("⚠️  Overall: Needs improvement - Add more detail")
            else:
                print("❌ Overall: Poor - Significant improvements needed")
            
            print(f"📊 Score: {score}/8")
            
            return 0
            
        except Exception as e:
            print(f"❌ Error validating INITIAL.md: {str(e)}")
            return 1
    
    def run_list(self, args) -> int:
        """Run the list command."""
        try:
            prp_dir = Path(args.directory)
            if not prp_dir.exists():
                print(f"❌ Error: PRP directory not found: {args.directory}")
                return 1
            
            # Find PRP files
            prp_files = list(prp_dir.glob("*.md"))
            prp_files.extend(list(prp_dir.glob("**/*.md")))
            
            if not prp_files:
                print(f"📁 No PRP files found in {args.directory}")
                return 0
            
            print(f"📋 Found {len(prp_files)} PRP files in {args.directory}:")
            print()
            
            for prp_file in sorted(prp_files):
                # Try to extract basic info from the file
                try:
                    content = prp_file.read_text(encoding='utf-8')
                    lines = content.split('\n')
                    
                    # Look for name and description
                    name = "Unknown"
                    description = ""
                    
                    for line in lines[:10]:
                        if line.startswith('name:'):
                            name = line.replace('name:', '').strip().strip('"')
                        elif line.startswith('## Goal'):
                            # Find the next line with content
                            idx = lines.index(line)
                            if idx + 1 < len(lines):
                                description = lines[idx + 1].strip()
                    
                    print(f"📄 {prp_file.name}")
                    print(f"   Name: {name}")
                    if description:
                        print(f"   Goal: {description[:80]}{'...' if len(description) > 80 else ''}")
                    print(f"   Path: {prp_file}")
                    print()
                    
                except Exception:
                    print(f"📄 {prp_file.name}")
                    print(f"   Path: {prp_file}")
                    print()
            
            return 0
            
        except Exception as e:
            print(f"❌ Error listing PRPs: {str(e)}")
            return 1
    
    async def run(self, args: Optional[list] = None) -> int:
        """Run the CLI with given arguments."""
        parser = self.create_parser()
        parsed_args = parser.parse_args(args)
        
        if not parsed_args.command:
            parser.print_help()
            return 1
        
        if parsed_args.command == 'generate':
            return await self.run_generate(parsed_args)
        elif parsed_args.command == 'validate':
            return await self.run_validate(parsed_args)
        elif parsed_args.command == 'list':
            return self.run_list(parsed_args)
        else:
            print(f"❌ Unknown command: {parsed_args.command}")
            return 1


async def main():
    """Main entry point for the CLI."""
    cli = InitialToPRPCLI()
    exit_code = await cli.run()
    sys.exit(exit_code)


if __name__ == "__main__":
    asyncio.run(main())
