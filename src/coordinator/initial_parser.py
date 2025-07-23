"""
Initial Document Parser for Coordinator Pattern System.

This module parses INITIAL.md files and extracts structured information
for PRP generation, following the context-engineering-intro project patterns.
"""

import re
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from pathlib import Path
import asyncio


@dataclass
class InitialAnalysis:
    """Structured analysis of an INITIAL.md document."""
    feature: str
    examples: List[str]
    documentation: List[str]
    other_considerations: List[str]
    raw_content: str
    file_path: str


@dataclass
class CodebaseContext:
    """Context about the current codebase for PRP generation."""
    current_tree: str
    similar_patterns: List[str]
    existing_conventions: List[str]
    test_patterns: List[str]
    integration_points: List[str]


class InitialParser:
    """
    Parser for INITIAL.md documents following context-engineering patterns.
    
    This parser extracts structured information from INITIAL.md files and
    prepares context for intelligent PRP generation.
    """
    
    def __init__(self):
        """Initialize the Initial document parser."""
        self.section_patterns = {
            'feature': r'## FEATURE:\s*(.*?)(?=##|$)',
            'examples': r'## EXAMPLES:\s*(.*?)(?=##|$)',
            'documentation': r'## DOCUMENTATION:\s*(.*?)(?=##|$)',
            'other_considerations': r'## OTHER CONSIDERATIONS:\s*(.*?)(?=##|$)'
        }
    
    async def parse_initial_file(self, file_path: str) -> InitialAnalysis:
        """
        Parse an INITIAL.md file and extract structured information.
        
        Args:
            file_path: Path to the INITIAL.md file
            
        Returns:
            InitialAnalysis with extracted information
        """
        try:
            # Read the file content
            path = Path(file_path)
            if not path.exists():
                raise FileNotFoundError(f"INITIAL.md file not found: {file_path}")
            
            content = path.read_text(encoding='utf-8')
            
            # Extract sections using regex patterns
            extracted_sections = {}
            for section_name, pattern in self.section_patterns.items():
                match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
                if match:
                    extracted_sections[section_name] = match.group(1).strip()
                else:
                    extracted_sections[section_name] = ""
            
            # Process and clean extracted content
            feature = self._clean_content(extracted_sections['feature'])
            examples = self._extract_list_items(extracted_sections['examples'])
            documentation = self._extract_list_items(extracted_sections['documentation'])
            other_considerations = self._extract_list_items(extracted_sections['other_considerations'])
            
            return InitialAnalysis(
                feature=feature,
                examples=examples,
                documentation=documentation,
                other_considerations=other_considerations,
                raw_content=content,
                file_path=file_path
            )
            
        except Exception as e:
            raise Exception(f"Failed to parse INITIAL.md file: {str(e)}")
    
    def _clean_content(self, content: str) -> str:
        """Clean and normalize content text."""
        if not content:
            return ""
        
        # Remove placeholder text
        placeholders = [
            r'\[Insert your feature here\]',
            r'\[Provide and explain examples.*?\]',
            r'\[List out any documentation.*?\]',
            r'\[Any other considerations.*?\]'
        ]
        
        cleaned = content
        for placeholder in placeholders:
            cleaned = re.sub(placeholder, '', cleaned, flags=re.IGNORECASE | re.DOTALL)
        
        # Clean up whitespace and newlines
        cleaned = re.sub(r'\n\s*\n', '\n', cleaned.strip())
        
        return cleaned
    
    def _extract_list_items(self, content: str) -> List[str]:
        """Extract list items from content."""
        if not content:
            return []
        
        # Clean content first
        cleaned = self._clean_content(content)
        if not cleaned:
            return []
        
        # Split by lines and extract meaningful items
        lines = [line.strip() for line in cleaned.split('\n') if line.strip()]
        
        # Filter out empty lines and common placeholders
        items = []
        for line in lines:
            if line and not any(placeholder in line.lower() for placeholder in [
                'insert', 'provide', 'list out', 'any other'
            ]):
                # Remove bullet points and numbering
                cleaned_line = re.sub(r'^[-*•]\s*', '', line)
                cleaned_line = re.sub(r'^\d+\.\s*', '', cleaned_line)
                if cleaned_line:
                    items.append(cleaned_line)
        
        return items
    
    async def analyze_codebase_context(self, project_root: str = ".") -> CodebaseContext:
        """
        Analyze the current codebase to provide context for PRP generation.
        
        Args:
            project_root: Root directory of the project
            
        Returns:
            CodebaseContext with codebase analysis
        """
        try:
            project_path = Path(project_root)
            
            # Generate current tree structure
            current_tree = await self._generate_tree_structure(project_path)
            
            # Find similar patterns in the codebase
            similar_patterns = await self._find_similar_patterns(project_path)
            
            # Identify existing conventions
            existing_conventions = await self._identify_conventions(project_path)
            
            # Analyze test patterns
            test_patterns = await self._analyze_test_patterns(project_path)
            
            # Find integration points
            integration_points = await self._find_integration_points(project_path)
            
            return CodebaseContext(
                current_tree=current_tree,
                similar_patterns=similar_patterns,
                existing_conventions=existing_conventions,
                test_patterns=test_patterns,
                integration_points=integration_points
            )
            
        except Exception as e:
            # Return basic context if analysis fails
            return CodebaseContext(
                current_tree="Unable to analyze codebase structure",
                similar_patterns=[],
                existing_conventions=[],
                test_patterns=[],
                integration_points=[]
            )
    
    async def _generate_tree_structure(self, project_path: Path) -> str:
        """Generate a tree structure of the project."""
        try:
            # Use system tree command if available
            import subprocess
            result = subprocess.run(
                ['tree', str(project_path), '-I', '__pycache__|*.pyc|.git|node_modules'],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                return result.stdout
            else:
                # Fallback to manual tree generation
                return self._manual_tree_generation(project_path)
                
        except (subprocess.TimeoutExpired, FileNotFoundError):
            # Fallback to manual tree generation
            return self._manual_tree_generation(project_path)
    
    def _manual_tree_generation(self, project_path: Path, max_depth: int = 3) -> str:
        """Generate tree structure manually."""
        tree_lines = []
        
        def add_directory(path: Path, prefix: str = "", depth: int = 0):
            if depth > max_depth:
                return
            
            try:
                items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))
                for i, item in enumerate(items):
                    if item.name.startswith('.') and item.name not in ['.env.example', '.gitignore']:
                        continue
                    if item.name in ['__pycache__', 'node_modules', '.git']:
                        continue
                    
                    is_last = i == len(items) - 1
                    current_prefix = "└── " if is_last else "├── "
                    tree_lines.append(f"{prefix}{current_prefix}{item.name}")
                    
                    if item.is_dir() and depth < max_depth:
                        next_prefix = prefix + ("    " if is_last else "│   ")
                        add_directory(item, next_prefix, depth + 1)
            except PermissionError:
                pass
        
        tree_lines.append(str(project_path.name))
        add_directory(project_path)
        
        return "\n".join(tree_lines)
    
    async def _find_similar_patterns(self, project_path: Path) -> List[str]:
        """Find similar patterns in the codebase."""
        patterns = []
        
        # Look for common patterns in Python files
        python_files = list(project_path.rglob("*.py"))
        
        for file_path in python_files[:10]:  # Limit to first 10 files
            try:
                content = file_path.read_text(encoding='utf-8')
                
                # Look for common patterns
                if 'class' in content and 'def __init__' in content:
                    patterns.append(f"Class pattern in {file_path.relative_to(project_path)}")
                
                if 'async def' in content:
                    patterns.append(f"Async pattern in {file_path.relative_to(project_path)}")
                
                if '@dataclass' in content:
                    patterns.append(f"Dataclass pattern in {file_path.relative_to(project_path)}")
                    
            except (UnicodeDecodeError, PermissionError):
                continue
        
        return patterns[:5]  # Return top 5 patterns
    
    async def _identify_conventions(self, project_path: Path) -> List[str]:
        """Identify coding conventions in the project."""
        conventions = []
        
        # Check for common convention indicators
        if (project_path / "pyproject.toml").exists():
            conventions.append("Uses pyproject.toml for project configuration")
        
        if (project_path / "requirements.txt").exists():
            conventions.append("Uses requirements.txt for dependencies")
        
        if (project_path / ".env.example").exists():
            conventions.append("Uses .env files for configuration")
        
        # Check Python files for import patterns
        python_files = list(project_path.rglob("*.py"))
        if python_files:
            sample_file = python_files[0]
            try:
                content = sample_file.read_text(encoding='utf-8')
                if 'from typing import' in content:
                    conventions.append("Uses typing annotations")
                if 'import asyncio' in content:
                    conventions.append("Uses asyncio for async operations")
            except (UnicodeDecodeError, PermissionError):
                pass
        
        return conventions
    
    async def _analyze_test_patterns(self, project_path: Path) -> List[str]:
        """Analyze test patterns in the project."""
        patterns = []
        
        # Look for test directories and files
        test_dirs = ['tests', 'test']
        test_files = []
        
        for test_dir in test_dirs:
            test_path = project_path / test_dir
            if test_path.exists():
                test_files.extend(list(test_path.rglob("test_*.py")))
                patterns.append(f"Test directory: {test_dir}/")
        
        # Look for test files in root
        test_files.extend(list(project_path.glob("test_*.py")))
        
        if test_files:
            patterns.append(f"Found {len(test_files)} test files")
            
            # Analyze first test file for patterns
            try:
                content = test_files[0].read_text(encoding='utf-8')
                if 'pytest' in content:
                    patterns.append("Uses pytest framework")
                if 'async def test_' in content:
                    patterns.append("Uses async test functions")
                if '@pytest.fixture' in content:
                    patterns.append("Uses pytest fixtures")
            except (UnicodeDecodeError, PermissionError):
                pass
        
        return patterns
    
    async def _find_integration_points(self, project_path: Path) -> List[str]:
        """Find potential integration points in the codebase."""
        integration_points = []
        
        # Look for configuration files
        config_files = ['config.py', 'settings.py', 'config.json', 'config.yaml']
        for config_file in config_files:
            if (project_path / config_file).exists():
                integration_points.append(f"Configuration: {config_file}")
        
        # Look for API/route files
        api_patterns = ['**/routes.py', '**/api.py', '**/endpoints.py']
        for pattern in api_patterns:
            files = list(project_path.glob(pattern))
            if files:
                integration_points.append(f"API integration: {files[0].name}")
        
        # Look for database files
        db_patterns = ['**/models.py', '**/database.py', '**/db.py']
        for pattern in db_patterns:
            files = list(project_path.glob(pattern))
            if files:
                integration_points.append(f"Database integration: {files[0].name}")
        
        return integration_points
