#!/usr/bin/env python3
"""
Initial to PRP System Demo.

This script demonstrates the complete Initial.md to PRP generation workflow,
replicating the context-engineering-intro project functionality.
"""

import asyncio
import sys
from pathlib import Path

# Add coordinator to path
sys.path.insert(0, str(Path(__file__).parent))

from coordinator.initial_to_prp_generator import InitialToPRPGenerator, PRPGenerationConfig
from coordinator.initial_parser import InitialParser


async def demo_initial_parsing():
    """Demonstrate INITIAL.md parsing capabilities."""
    
    print("📋 Initial Document Parsing Demo")
    print("=" * 50)
    
    parser = InitialParser()
    
    # Parse the example INITIAL.md
    try:
        print("📄 Parsing INITIAL_EXAMPLE.md...")
        initial_analysis = await parser.parse_initial_file("INITIAL_EXAMPLE.md")
        
        print(f"✅ Successfully parsed INITIAL.md file")
        print(f"📁 File: {initial_analysis.file_path}")
        print()
        
        print("📊 Extracted Information:")
        print(f"   🎯 Feature: {initial_analysis.feature[:100]}{'...' if len(initial_analysis.feature) > 100 else ''}")
        print(f"   📚 Examples: {len(initial_analysis.examples)} items")
        for i, example in enumerate(initial_analysis.examples[:3], 1):
            print(f"      {i}. {example[:60]}{'...' if len(example) > 60 else ''}")
        
        print(f"   📖 Documentation: {len(initial_analysis.documentation)} references")
        for i, doc in enumerate(initial_analysis.documentation[:3], 1):
            print(f"      {i}. {doc[:60]}{'...' if len(doc) > 60 else ''}")
        
        print(f"   ⚠️  Other Considerations: {len(initial_analysis.other_considerations)} items")
        for i, consideration in enumerate(initial_analysis.other_considerations[:3], 1):
            print(f"      {i}. {consideration[:60]}{'...' if len(consideration) > 60 else ''}")
        
        return initial_analysis
        
    except Exception as e:
        print(f"❌ Error parsing INITIAL.md: {str(e)}")
        return None


async def demo_codebase_analysis():
    """Demonstrate codebase context analysis."""
    
    print("\n🔍 Codebase Context Analysis Demo")
    print("=" * 50)
    
    parser = InitialParser()
    
    try:
        print("🔍 Analyzing current codebase...")
        codebase_context = await parser.analyze_codebase_context(".")
        
        print("✅ Codebase analysis complete")
        print()
        
        print("📊 Codebase Context:")
        print("   📁 Current Tree Structure:")
        tree_lines = codebase_context.current_tree.split('\n')[:10]
        for line in tree_lines:
            print(f"      {line}")
        if len(codebase_context.current_tree.split('\n')) > 10:
            print("      ... (truncated)")
        
        print(f"\n   🔍 Similar Patterns Found: {len(codebase_context.similar_patterns)}")
        for i, pattern in enumerate(codebase_context.similar_patterns[:3], 1):
            print(f"      {i}. {pattern}")
        
        print(f"\n   📋 Existing Conventions: {len(codebase_context.existing_conventions)}")
        for i, convention in enumerate(codebase_context.existing_conventions[:3], 1):
            print(f"      {i}. {convention}")
        
        print(f"\n   🧪 Test Patterns: {len(codebase_context.test_patterns)}")
        for i, pattern in enumerate(codebase_context.test_patterns[:3], 1):
            print(f"      {i}. {pattern}")
        
        print(f"\n   🔗 Integration Points: {len(codebase_context.integration_points)}")
        for i, point in enumerate(codebase_context.integration_points[:3], 1):
            print(f"      {i}. {point}")
        
        return codebase_context
        
    except Exception as e:
        print(f"❌ Error analyzing codebase: {str(e)}")
        return None


async def demo_prp_generation():
    """Demonstrate complete PRP generation."""
    
    print("\n📝 PRP Generation Demo")
    print("=" * 50)
    
    # Configure PRP generation
    config = PRPGenerationConfig(
        output_directory="PRPs",
        include_research=True,
        include_validation=True,
        confidence_threshold=7
    )
    
    generator = InitialToPRPGenerator(config)
    
    try:
        print("🚀 Starting PRP generation from INITIAL_EXAMPLE.md...")
        
        # Generate PRP
        generated_prp = await generator.generate_prp_from_initial(
            "INITIAL_EXAMPLE.md",
            "."
        )
        
        print("\n🎉 PRP Generation Complete!")
        print(f"📄 Generated file: {generated_prp.file_path}")
        print(f"🎯 Confidence score: {generated_prp.confidence_score}/10")
        print(f"📝 Feature name: {generated_prp.feature_name}")
        print(f"⏰ Generated at: {generated_prp.generation_timestamp}")
        print()
        
        # Show research context
        print("🔬 Research Context:")
        print(f"   📖 External docs: {len(generated_prp.research_context.external_documentation)}")
        print(f"   💡 Best practices: {len(generated_prp.research_context.best_practices)}")
        print(f"   ⚠️  Common pitfalls: {len(generated_prp.research_context.common_pitfalls)}")
        print(f"   🔧 Library quirks: {len(generated_prp.research_context.library_quirks)}")
        print()
        
        # Show validation commands
        print("✅ Validation Commands:")
        for i, cmd in enumerate(generated_prp.validation_commands, 1):
            print(f"   {i}. {cmd}")
        print()
        
        # Show content preview
        print("📄 PRP Content Preview:")
        content_lines = generated_prp.content.split('\n')[:20]
        for line in content_lines:
            print(f"   {line}")
        print("   ... (content continues)")
        
        return generated_prp
        
    except Exception as e:
        print(f"❌ Error generating PRP: {str(e)}")
        return None


async def demo_prp_quality_analysis():
    """Demonstrate PRP quality analysis."""
    
    print("\n📊 PRP Quality Analysis Demo")
    print("=" * 50)
    
    # Check if PRP was generated
    prp_files = list(Path("PRPs").glob("*.md"))
    
    if not prp_files:
        print("⚠️  No PRP files found. Run PRP generation first.")
        return
    
    latest_prp = max(prp_files, key=lambda p: p.stat().st_mtime)
    
    try:
        content = latest_prp.read_text(encoding='utf-8')
        
        print(f"📄 Analyzing PRP: {latest_prp.name}")
        print()
        
        # Analyze content structure
        sections = {
            'Goal': '## Goal' in content,
            'Why': '## Why' in content,
            'What': '## What' in content,
            'Success Criteria': '### Success Criteria' in content,
            'Documentation & References': '### Documentation & References' in content,
            'Current Codebase tree': '### Current Codebase tree' in content,
            'Known Gotchas': '### Known Gotchas' in content,
            'Implementation Blueprint': '## Implementation Blueprint' in content,
            'Validation Loop': '## Validation Loop' in content,
            'Anti-Patterns': '## Anti-Patterns to Avoid' in content,
            'Confidence Score': 'Confidence Score:' in content
        }
        
        print("📋 PRP Structure Analysis:")
        for section, present in sections.items():
            status = "✅" if present else "❌"
            print(f"   {status} {section}")
        
        # Calculate completeness score
        completeness = sum(sections.values()) / len(sections) * 100
        print(f"\n📊 Completeness Score: {completeness:.1f}%")
        
        # Analyze content depth
        lines = content.split('\n')
        total_lines = len(lines)
        code_blocks = content.count('```')
        yaml_blocks = content.count('```yaml')
        python_blocks = content.count('```python')
        bash_blocks = content.count('```bash')
        
        print(f"\n📈 Content Analysis:")
        print(f"   📄 Total lines: {total_lines}")
        print(f"   💻 Code blocks: {code_blocks // 2}")  # Divide by 2 for opening/closing
        print(f"   📋 YAML blocks: {yaml_blocks}")
        print(f"   🐍 Python blocks: {python_blocks}")
        print(f"   🔧 Bash blocks: {bash_blocks}")
        
        # Quality assessment
        if completeness >= 90 and total_lines >= 200:
            quality = "🏆 Excellent"
        elif completeness >= 80 and total_lines >= 150:
            quality = "👍 Good"
        elif completeness >= 70 and total_lines >= 100:
            quality = "⚠️  Fair"
        else:
            quality = "❌ Poor"
        
        print(f"\n🎯 Overall Quality: {quality}")
        
    except Exception as e:
        print(f"❌ Error analyzing PRP quality: {str(e)}")


async def demo_workflow_comparison():
    """Demonstrate workflow comparison with original context-engineering-intro."""
    
    print("\n🔄 Workflow Comparison Demo")
    print("=" * 50)
    
    print("📋 Original context-engineering-intro workflow:")
    print("   1. Edit INITIAL.md with feature requirements")
    print("   2. Run /generate-prp INITIAL.md in Claude Code")
    print("   3. AI researches codebase and external docs")
    print("   4. AI generates comprehensive PRP")
    print("   5. Run /execute-prp PRPs/feature-name.md")
    print("   6. AI implements feature with validation loops")
    print()
    
    print("🎯 Our Coordinator Pattern System workflow:")
    print("   1. Edit INITIAL.md with feature requirements")
    print("   2. Run: python demo_initial_to_prp_system.py")
    print("   3. System parses INITIAL.md and analyzes codebase")
    print("   4. System generates comprehensive PRP")
    print("   5. Use PRP with any AI coding assistant")
    print("   6. AI implements feature with validation loops")
    print()
    
    print("✅ Key Advantages of Our System:")
    print("   🔧 Standalone - doesn't require Claude Code")
    print("   🎯 Customizable - configurable generation parameters")
    print("   📊 Analyzable - provides quality metrics and validation")
    print("   🔍 Transparent - shows research and analysis process")
    print("   🚀 Extensible - can be integrated into any workflow")
    print()
    
    print("🎊 Feature Parity Achieved:")
    print("   ✅ INITIAL.md parsing")
    print("   ✅ Codebase analysis and pattern detection")
    print("   ✅ Research context generation")
    print("   ✅ Comprehensive PRP generation")
    print("   ✅ Validation loop creation")
    print("   ✅ Quality assessment and scoring")


async def main():
    """Run the complete Initial to PRP system demo."""
    
    print("🚀 Initial to PRP System - Complete Demo")
    print("=" * 80)
    print("Demonstrating complete replication of context-engineering-intro workflow")
    print("=" * 80)
    
    # Demo 1: Initial document parsing
    initial_analysis = await demo_initial_parsing()
    
    # Demo 2: Codebase analysis
    codebase_context = await demo_codebase_analysis()
    
    # Demo 3: PRP generation
    generated_prp = await demo_prp_generation()
    
    # Demo 4: Quality analysis
    await demo_prp_quality_analysis()
    
    # Demo 5: Workflow comparison
    await demo_workflow_comparison()
    
    print(f"\n🎉 Demo Complete!")
    print(f"📋 Summary:")
    print(f"   ✅ INITIAL.md parsing: {'Success' if initial_analysis else 'Failed'}")
    print(f"   ✅ Codebase analysis: {'Success' if codebase_context else 'Failed'}")
    print(f"   ✅ PRP generation: {'Success' if generated_prp else 'Failed'}")
    
    if generated_prp:
        print(f"\n📄 Generated PRP: {generated_prp.file_path}")
        print(f"🎯 Confidence Score: {generated_prp.confidence_score}/10")
        print(f"\n🚀 Next Steps:")
        print(f"   1. Review the generated PRP")
        print(f"   2. Use it with any AI coding assistant")
        print(f"   3. Implement your feature with confidence!")


if __name__ == "__main__":
    asyncio.run(main())
