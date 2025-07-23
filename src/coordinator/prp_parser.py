"""
PRP Parser for Coordinator Pattern system.

This module parses Product Requirement Prompt (PRP) documents and extracts
structured project requirements for Claude Flow configuration generation.
"""

import re
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

from .models import (
    ProjectAnalysis,
    TechnicalRequirements,
    ComplexityMetrics,
    ProjectConstraints,
    ProjectType,
    ComplexityLevel,
    TeamSize,
    QualityLevel,
)


@dataclass
class PRPAnalysis:
    """Structured analysis of a PRP document."""
    name: str
    goal: str
    why: str
    what: str
    success_criteria: List[str]
    technical_requirements: Dict[str, Any]
    documentation_refs: List[Dict[str, str]]
    validation_gates: List[str]
    constraints: Dict[str, Any]
    agent_requirements: List[str]
    coordination_hints: List[str]


class PRPParser:
    """
    Parser for Product Requirement Prompt (PRP) documents.
    
    Extracts structured project requirements from PRP markdown files
    and converts them to ProjectAnalysis objects for configuration generation.
    """
    
    def __init__(self):
        """Initialize the PRP parser."""
        self._section_patterns = self._build_section_patterns()
        self._tech_extractors = self._build_tech_extractors()
    
    async def parse_prp_file(self, prp_path: str) -> PRPAnalysis:
        """
        Parse a PRP file and extract structured requirements.
        
        Args:
            prp_path: Path to the PRP markdown file
            
        Returns:
            Structured PRP analysis
        """
        prp_content = self._load_prp_file(prp_path)
        
        return PRPAnalysis(
            name=self._extract_name(prp_content),
            goal=self._extract_goal(prp_content),
            why=self._extract_why(prp_content),
            what=self._extract_what(prp_content),
            success_criteria=self._extract_success_criteria(prp_content),
            technical_requirements=self._extract_technical_requirements(prp_content),
            documentation_refs=self._extract_documentation_refs(prp_content),
            validation_gates=self._extract_validation_gates(prp_content),
            constraints=self._extract_constraints(prp_content),
            agent_requirements=self._extract_agent_requirements(prp_content),
            coordination_hints=self._extract_coordination_hints(prp_content),
        )
    
    async def convert_prp_to_project_analysis(self, prp_analysis: PRPAnalysis) -> ProjectAnalysis:
        """
        Convert PRP analysis to ProjectAnalysis for configuration generation.
        
        Args:
            prp_analysis: Structured PRP analysis
            
        Returns:
            ProjectAnalysis object
        """
        # Extract technical requirements
        tech_requirements = self._build_technical_requirements(prp_analysis)
        
        # Assess complexity based on PRP content
        complexity_metrics = self._assess_prp_complexity(prp_analysis)
        
        # Identify project type from PRP content
        project_type = self._identify_prp_project_type(prp_analysis)
        
        # Extract constraints from PRP
        constraints = self._build_project_constraints(prp_analysis)
        
        # Generate pattern recommendations based on PRP
        recommended_patterns = self._suggest_prp_patterns(prp_analysis, complexity_metrics)
        
        # Calculate confidence based on PRP completeness
        confidence_score = self._calculate_prp_confidence(prp_analysis)
        
        return ProjectAnalysis(
            description=f"{prp_analysis.goal}\n\n{prp_analysis.what}",
            project_type=project_type,
            technical_requirements=tech_requirements,
            complexity_metrics=complexity_metrics,
            constraints=constraints,
            recommended_patterns=recommended_patterns,
            confidence_score=confidence_score,
        )
    
    def _load_prp_file(self, prp_path: str) -> str:
        """Load PRP file content."""
        with open(prp_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def _extract_name(self, content: str) -> str:
        """Extract project name from PRP."""
        # Look for name field at the top
        name_match = re.search(r'^name:\s*["\']?([^"\'\n]+)["\']?', content, re.MULTILINE)
        if name_match:
            return name_match.group(1).strip()
        
        # Fallback to first heading
        heading_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if heading_match:
            return heading_match.group(1).strip()
        
        return "Unknown Project"
    
    def _extract_goal(self, content: str) -> str:
        """Extract project goal from PRP."""
        goal_section = self._extract_section(content, "Goal")
        if goal_section:
            return goal_section.strip()
        
        # Fallback to purpose section
        purpose_section = self._extract_section(content, "Purpose")
        return purpose_section.strip() if purpose_section else ""
    
    def _extract_why(self, content: str) -> str:
        """Extract project rationale from PRP."""
        why_section = self._extract_section(content, "Why")
        return why_section.strip() if why_section else ""
    
    def _extract_what(self, content: str) -> str:
        """Extract project requirements from PRP."""
        what_section = self._extract_section(content, "What")
        return what_section.strip() if what_section else ""
    
    def _extract_success_criteria(self, content: str) -> List[str]:
        """Extract success criteria from PRP."""
        criteria_section = self._extract_section(content, "Success Criteria")
        if not criteria_section:
            return []
        
        # Extract checkbox items
        criteria = []
        for line in criteria_section.split('\n'):
            line = line.strip()
            if line.startswith('- [ ]') or line.startswith('- [x]'):
                criteria.append(line[5:].strip())
        
        return criteria
    
    def _extract_technical_requirements(self, content: str) -> Dict[str, Any]:
        """Extract technical requirements from PRP."""
        tech_section = self._extract_section(content, "Technical Requirements")
        if not tech_section:
            # Try alternative section names
            tech_section = self._extract_section(content, "Tech Stack")
            if not tech_section:
                tech_section = self._extract_section(content, "Implementation Details")
        
        if not tech_section:
            return {}
        
        # Extract structured tech requirements
        tech_reqs = {
            "languages": self._extract_languages(tech_section),
            "frameworks": self._extract_frameworks(tech_section),
            "databases": self._extract_databases(tech_section),
            "infrastructure": self._extract_infrastructure(tech_section),
            "tools": self._extract_tools(tech_section),
            "apis": self._extract_apis(tech_section),
        }
        
        return tech_reqs
    
    def _extract_documentation_refs(self, content: str) -> List[Dict[str, str]]:
        """Extract documentation references from PRP."""
        docs_section = self._extract_section(content, "Documentation & References")
        if not docs_section:
            return []
        
        refs = []
        # Look for YAML-style references
        yaml_match = re.search(r'```yaml\s*\n(.*?)\n```', docs_section, re.DOTALL)
        if yaml_match:
            try:
                yaml_content = yaml.safe_load(yaml_match.group(1))
                if isinstance(yaml_content, list):
                    refs.extend(yaml_content)
            except yaml.YAMLError:
                pass
        
        # Look for URL patterns
        url_pattern = r'- url:\s*([^\s]+)\s*\n\s*why:\s*([^\n]+)'
        for match in re.finditer(url_pattern, docs_section):
            refs.append({
                "url": match.group(1),
                "why": match.group(2).strip()
            })
        
        return refs
    
    def _extract_validation_gates(self, content: str) -> List[str]:
        """Extract validation gates from PRP."""
        validation_section = self._extract_section(content, "Validation Gates")
        if not validation_section:
            validation_section = self._extract_section(content, "Testing")
        
        if not validation_section:
            return []
        
        gates = []
        for line in validation_section.split('\n'):
            line = line.strip()
            if line.startswith('- ') or line.startswith('* '):
                gates.append(line[2:].strip())
        
        return gates
    
    def _extract_constraints(self, content: str) -> Dict[str, Any]:
        """Extract project constraints from PRP."""
        constraints = {}
        
        # Look for timeline mentions
        timeline_patterns = [
            r'(\d+)\s*days?',
            r'(\d+)\s*weeks?',
            r'(\d+)\s*months?',
        ]
        
        for pattern in timeline_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                constraints['timeline'] = match.group(0)
                break
        
        # Look for team size mentions
        if re.search(r'solo|single\s+developer', content, re.IGNORECASE):
            constraints['team_size'] = 'solo'
        elif re.search(r'small\s+team|2-5\s+developers?', content, re.IGNORECASE):
            constraints['team_size'] = 'small'
        elif re.search(r'large\s+team|enterprise', content, re.IGNORECASE):
            constraints['team_size'] = 'large'
        
        # Look for quality requirements
        if re.search(r'prototype|mvp|proof\s+of\s+concept', content, re.IGNORECASE):
            constraints['quality'] = 'prototype'
        elif re.search(r'production|enterprise|mission\s+critical', content, re.IGNORECASE):
            constraints['quality'] = 'production'
        
        return constraints
    
    def _extract_agent_requirements(self, content: str) -> List[str]:
        """Extract agent requirements from PRP."""
        agents = []
        
        # Look for agent mentions
        agent_patterns = [
            r'(\w+)\s+agent',
            r'agent\s+(\w+)',
            r'(\w+)\s+sub-agent',
        ]
        
        for pattern in agent_patterns:
            for match in re.finditer(pattern, content, re.IGNORECASE):
                agent_type = match.group(1).lower()
                if agent_type not in ['the', 'an', 'a'] and agent_type not in agents:
                    agents.append(agent_type)
        
        return agents
    
    def _extract_coordination_hints(self, content: str) -> List[str]:
        """Extract coordination hints from PRP."""
        hints = []
        
        # Look for coordination keywords
        coordination_keywords = [
            'multi-agent', 'agent-as-tool', 'hierarchical', 'pipeline',
            'coordination', 'orchestration', 'delegation', 'collaboration'
        ]
        
        for keyword in coordination_keywords:
            if keyword in content.lower():
                hints.append(keyword)
        
        return hints
    
    def _extract_section(self, content: str, section_name: str) -> Optional[str]:
        """Extract a specific section from PRP content."""
        # Try different heading formats
        patterns = [
            rf'^##\s+{section_name}\s*\n(.*?)(?=^##|\Z)',
            rf'^###\s+{section_name}\s*\n(.*?)(?=^###|\Z)',
            rf'^#\s+{section_name}\s*\n(.*?)(?=^#|\Z)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, content, re.MULTILINE | re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return None
    
    def _build_section_patterns(self) -> Dict[str, str]:
        """Build regex patterns for section extraction."""
        return {
            "goal": r"##\s+Goal\s*\n(.*?)(?=^##|\Z)",
            "why": r"##\s+Why\s*\n(.*?)(?=^##|\Z)",
            "what": r"##\s+What\s*\n(.*?)(?=^##|\Z)",
        }
    
    def _build_tech_extractors(self) -> Dict[str, List[str]]:
        """Build technology extraction patterns."""
        return {
            "languages": ["python", "javascript", "java", "go", "rust", "php", "ruby"],
            "frameworks": ["django", "flask", "fastapi", "react", "vue", "angular"],
            "databases": ["postgresql", "mysql", "mongodb", "redis", "sqlite"],
            "infrastructure": ["aws", "gcp", "azure", "docker", "kubernetes"],
        }

    def _extract_languages(self, tech_section: str) -> List[str]:
        """Extract programming languages from tech section."""
        languages = []
        for lang in self._tech_extractors["languages"]:
            if lang.lower() in tech_section.lower():
                languages.append(lang)
        return languages

    def _extract_frameworks(self, tech_section: str) -> List[str]:
        """Extract frameworks from tech section."""
        frameworks = []
        for framework in self._tech_extractors["frameworks"]:
            if framework.lower() in tech_section.lower():
                frameworks.append(framework)
        return frameworks

    def _extract_databases(self, tech_section: str) -> List[str]:
        """Extract databases from tech section."""
        databases = []
        for db in self._tech_extractors["databases"]:
            if db.lower() in tech_section.lower():
                databases.append(db)
        return databases

    def _extract_infrastructure(self, tech_section: str) -> List[str]:
        """Extract infrastructure from tech section."""
        infrastructure = []
        for infra in self._tech_extractors["infrastructure"]:
            if infra.lower() in tech_section.lower():
                infrastructure.append(infra)
        return infrastructure

    def _extract_tools(self, tech_section: str) -> List[str]:
        """Extract development tools from tech section."""
        tools = []
        tool_patterns = ["git", "docker", "kubernetes", "jenkins", "ci/cd", "testing"]
        for tool in tool_patterns:
            if tool.lower() in tech_section.lower():
                tools.append(tool)
        return tools

    def _extract_apis(self, tech_section: str) -> List[str]:
        """Extract APIs from tech section."""
        apis = []
        api_patterns = ["rest", "graphql", "api", "webhook", "integration"]
        for api in api_patterns:
            if api.lower() in tech_section.lower():
                apis.append(api)
        return apis

    def _build_technical_requirements(self, prp_analysis: PRPAnalysis) -> TechnicalRequirements:
        """Build TechnicalRequirements from PRP analysis."""
        tech_reqs = prp_analysis.technical_requirements

        return TechnicalRequirements(
            languages=tech_reqs.get("languages", []),
            frameworks=tech_reqs.get("frameworks", []),
            databases=tech_reqs.get("databases", []),
            infrastructure=tech_reqs.get("infrastructure", []),
            tools=tech_reqs.get("tools", []),
            apis=tech_reqs.get("apis", []),
        )

    def _assess_prp_complexity(self, prp_analysis: PRPAnalysis) -> ComplexityMetrics:
        """Assess complexity based on PRP content."""
        # Technical complexity based on tech stack and requirements
        tech_complexity = self._calculate_tech_complexity_from_prp(prp_analysis)

        # Organizational complexity based on team and process indicators
        org_complexity = self._calculate_org_complexity_from_prp(prp_analysis)

        # Temporal complexity based on timeline and success criteria
        temporal_complexity = self._calculate_temporal_complexity_from_prp(prp_analysis)

        return ComplexityMetrics(
            technical_complexity=tech_complexity,
            organizational_complexity=org_complexity,
            temporal_complexity=temporal_complexity,
            overall_score=0.0,  # Will be calculated by validator
            complexity_level=ComplexityLevel.SIMPLE,  # Will be determined by validator
        )

    def _calculate_tech_complexity_from_prp(self, prp_analysis: PRPAnalysis) -> int:
        """Calculate technical complexity from PRP."""
        score = 1

        # Count technologies
        tech_count = (
            len(prp_analysis.technical_requirements.get("languages", [])) +
            len(prp_analysis.technical_requirements.get("frameworks", [])) +
            len(prp_analysis.technical_requirements.get("databases", [])) +
            len(prp_analysis.technical_requirements.get("infrastructure", []))
        )

        if tech_count <= 3:
            score += 1
        elif tech_count <= 6:
            score += 3
        else:
            score += 5

        # Check for complexity indicators in goal and what sections
        complexity_text = f"{prp_analysis.goal} {prp_analysis.what}".lower()
        complexity_indicators = [
            'multi-agent', 'distributed', 'scalable', 'real-time',
            'machine learning', 'ai', 'microservices', 'enterprise'
        ]

        complexity_count = sum(1 for indicator in complexity_indicators if indicator in complexity_text)
        score += min(complexity_count, 3)

        return min(score, 10)

    def _calculate_org_complexity_from_prp(self, prp_analysis: PRPAnalysis) -> int:
        """Calculate organizational complexity from PRP."""
        score = 1

        # Check constraints for team size indicators
        constraints = prp_analysis.constraints
        if constraints.get('team_size') == 'large':
            score += 4
        elif constraints.get('team_size') == 'small':
            score += 2

        # Check for process complexity in success criteria
        criteria_text = ' '.join(prp_analysis.success_criteria).lower()
        if 'test' in criteria_text or 'quality' in criteria_text:
            score += 1
        if 'integration' in criteria_text or 'deployment' in criteria_text:
            score += 1

        return min(score, 10)

    def _calculate_temporal_complexity_from_prp(self, prp_analysis: PRPAnalysis) -> int:
        """Calculate temporal complexity from PRP."""
        score = 1

        # Check timeline constraints
        timeline = prp_analysis.constraints.get('timeline', '')
        if 'day' in timeline.lower():
            score += 4
        elif 'week' in timeline.lower():
            score += 2
        elif 'month' in timeline.lower():
            score += 1

        # Check success criteria count (more criteria = more time pressure)
        criteria_count = len(prp_analysis.success_criteria)
        if criteria_count > 10:
            score += 2
        elif criteria_count > 5:
            score += 1

        return min(score, 10)

    def _identify_prp_project_type(self, prp_analysis: PRPAnalysis) -> ProjectType:
        """Identify project type from PRP content."""
        content = f"{prp_analysis.goal} {prp_analysis.what}".lower()

        # Multi-agent system indicators
        if 'multi-agent' in content or 'agent' in content:
            if 'research' in content:
                return ProjectType.RESEARCH
            elif 'api' in content or 'backend' in content:
                return ProjectType.WEB_BACKEND
            else:
                return ProjectType.AUTOMATION

        # Web project indicators
        if 'api' in content or 'backend' in content:
            return ProjectType.WEB_BACKEND
        elif 'frontend' in content or 'ui' in content:
            return ProjectType.WEB_FRONTEND
        elif 'web' in content:
            return ProjectType.WEB_FULLSTACK

        # Data project indicators
        if 'data' in content or 'analytics' in content:
            return ProjectType.DATA_PROCESSING

        # Default fallback
        return ProjectType.AUTOMATION

    def _build_project_constraints(self, prp_analysis: PRPAnalysis) -> ProjectConstraints:
        """Build ProjectConstraints from PRP analysis."""
        constraints = prp_analysis.constraints

        # Map team size
        team_size_mapping = {
            'solo': TeamSize.SOLO,
            'small': TeamSize.SMALL,
            'medium': TeamSize.MEDIUM,
            'large': TeamSize.LARGE,
        }
        team_size = team_size_mapping.get(constraints.get('team_size', 'small'), TeamSize.SMALL)

        # Map quality level
        quality_mapping = {
            'prototype': QualityLevel.PROTOTYPE,
            'production': QualityLevel.PRODUCTION,
            'enterprise': QualityLevel.ENTERPRISE,
            'mission_critical': QualityLevel.MISSION_CRITICAL,
        }
        quality = quality_mapping.get(constraints.get('quality', 'production'), QualityLevel.PRODUCTION)

        return ProjectConstraints(
            team_size=team_size,
            quality_requirements=quality,
            compliance_requirements=[],
            performance_requirements={},
        )

    def _suggest_prp_patterns(self, prp_analysis: PRPAnalysis, complexity_metrics: ComplexityMetrics) -> List[str]:
        """Suggest coordination patterns based on PRP analysis."""
        patterns = []

        # Check coordination hints
        hints = prp_analysis.coordination_hints
        if 'multi-agent' in hints:
            patterns.append('hierarchical')
        if 'agent-as-tool' in hints:
            patterns.append('hierarchical')
        if 'pipeline' in hints:
            patterns.append('pipeline')

        # Fallback based on complexity
        if not patterns:
            if complexity_metrics.technical_complexity <= 3:
                patterns.append('peer_to_peer')
            elif complexity_metrics.technical_complexity <= 6:
                patterns.append('hierarchical')
            else:
                patterns.append('hybrid')

        return patterns[:2]  # Return top 2

    def _calculate_prp_confidence(self, prp_analysis: PRPAnalysis) -> float:
        """Calculate confidence score based on PRP completeness."""
        score = 0.5  # Base confidence

        # Increase confidence for complete sections
        if prp_analysis.goal:
            score += 0.1
        if prp_analysis.what:
            score += 0.1
        if prp_analysis.success_criteria:
            score += 0.1
        if prp_analysis.technical_requirements:
            score += 0.1
        if prp_analysis.documentation_refs:
            score += 0.1

        return min(score, 1.0)
