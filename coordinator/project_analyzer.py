"""
Project Analyzer for Coordinator Pattern system.

This module implements intelligent project analysis using NLP techniques and pattern
recognition to extract technical requirements, assess complexity, and identify
optimal coordination patterns.
"""

import re
from typing import Dict, List
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
class TechStackPatterns:
    """Technology stack identification patterns."""

    # Programming languages
    LANGUAGES = {
        'python': ['python', 'py', 'django', 'flask', 'fastapi', 'pandas', 'numpy'],
        'javascript': ['javascript', 'js', 'node', 'nodejs', 'npm', 'yarn'],
        'typescript': ['typescript', 'ts', 'angular', 'nest'],
        'java': ['java', 'spring', 'maven', 'gradle', 'hibernate'],
        'go': ['go', 'golang', 'gin', 'echo', 'gorilla'],
        'rust': ['rust', 'cargo', 'actix', 'tokio', 'serde'],
        'php': ['php', 'laravel', 'symfony', 'composer'],
        'ruby': ['ruby', 'rails', 'gem', 'bundler'],
        'csharp': ['c#', 'csharp', '.net', 'dotnet', 'asp.net'],
        'swift': ['swift', 'ios', 'xcode'],
        'kotlin': ['kotlin', 'android'],
        'dart': ['dart', 'flutter'],
    }

    # Frameworks and libraries
    FRAMEWORKS = {
        'react': ['react', 'reactjs', 'jsx', 'next.js', 'nextjs'],
        'vue': ['vue', 'vuejs', 'nuxt', 'nuxtjs'],
        'angular': ['angular', 'angularjs'],
        'django': ['django', 'drf', 'django-rest-framework'],
        'flask': ['flask', 'werkzeug'],
        'fastapi': ['fastapi', 'starlette'],
        'express': ['express', 'expressjs'],
        'spring': ['spring', 'spring-boot', 'spring-mvc'],
        'laravel': ['laravel', 'eloquent'],
        'rails': ['rails', 'ruby-on-rails'],
    }

    # Databases
    DATABASES = {
        'postgresql': ['postgresql', 'postgres', 'psql'],
        'mysql': ['mysql', 'mariadb'],
        'mongodb': ['mongodb', 'mongo', 'mongoose'],
        'redis': ['redis', 'elasticache'],
        'elasticsearch': ['elasticsearch', 'elastic', 'opensearch'],
        'sqlite': ['sqlite', 'sqlite3'],
        'cassandra': ['cassandra', 'scylla'],
        'dynamodb': ['dynamodb', 'dynamo'],
    }

    # Infrastructure and deployment
    INFRASTRUCTURE = {
        'aws': ['aws', 'amazon', 'ec2', 's3', 'lambda', 'cloudformation'],
        'gcp': ['gcp', 'google-cloud', 'gke', 'cloud-run'],
        'azure': ['azure', 'microsoft-cloud'],
        'docker': ['docker', 'dockerfile', 'container'],
        'kubernetes': ['kubernetes', 'k8s', 'kubectl', 'helm'],
        'terraform': ['terraform', 'tf'],
        'ansible': ['ansible', 'playbook'],
    }


class ProjectAnalyzer:
    """
    Intelligent project analyzer that extracts technical requirements,
    assesses complexity, and recommends coordination patterns.
    """

    def __init__(self):
        """Initialize the project analyzer."""
        self.tech_patterns = TechStackPatterns()
        self._complexity_keywords = self._build_complexity_keywords()
        self._project_type_patterns = self._build_project_type_patterns()

    async def analyze_project(self, description: str) -> ProjectAnalysis:
        """
        Perform comprehensive project analysis.

        Args:
            description: Natural language project description

        Returns:
            Complete project analysis with recommendations
        """
        # Normalize description for analysis
        normalized_desc = self._normalize_description(description)

        # Extract technical requirements
        tech_requirements = await self._extract_technical_requirements(normalized_desc)

        # Assess complexity
        complexity_metrics = await self._assess_complexity(normalized_desc, tech_requirements)

        # Identify project type
        project_type = await self._identify_project_type(normalized_desc, tech_requirements)

        # Extract constraints
        constraints = await self._extract_constraints(normalized_desc)

        # Generate pattern recommendations
        recommended_patterns = await self._suggest_patterns(
            project_type, complexity_metrics, constraints
        )

        # Calculate confidence score
        confidence_score = self._calculate_confidence_score(
            tech_requirements, complexity_metrics, project_type
        )

        return ProjectAnalysis(
            description=description,
            project_type=project_type,
            technical_requirements=tech_requirements,
            complexity_metrics=complexity_metrics,
            constraints=constraints,
            recommended_patterns=recommended_patterns,
            confidence_score=confidence_score,
        )

    def _normalize_description(self, description: str) -> str:
        """Normalize project description for analysis."""
        # Convert to lowercase and remove extra whitespace
        normalized = re.sub(r'\s+', ' ', description.lower().strip())

        # Remove common stop words that don't add technical value
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        words = normalized.split()
        filtered_words = [word for word in words if word not in stop_words or len(word) > 3]

        return ' '.join(filtered_words)

    async def _extract_technical_requirements(self, description: str) -> TechnicalRequirements:
        """Extract technical stack requirements from description."""
        languages = []
        frameworks = []
        databases = []
        infrastructure = []
        tools = []
        apis = []

        # Extract languages
        for lang, patterns in self.tech_patterns.LANGUAGES.items():
            if any(pattern in description for pattern in patterns):
                languages.append(lang)

        # Extract frameworks
        for framework, patterns in self.tech_patterns.FRAMEWORKS.items():
            if any(pattern in description for pattern in patterns):
                frameworks.append(framework)

        # Extract databases
        for db, patterns in self.tech_patterns.DATABASES.items():
            if any(pattern in description for pattern in patterns):
                databases.append(db)

        # Extract infrastructure
        for infra, patterns in self.tech_patterns.INFRASTRUCTURE.items():
            if any(pattern in description for pattern in patterns):
                infrastructure.append(infra)

        # Extract APIs and integrations
        api_patterns = ['api', 'rest', 'graphql', 'webhook', 'integration', 'third-party']
        if any(pattern in description for pattern in api_patterns):
            apis.extend([pattern for pattern in api_patterns if pattern in description])

        # Extract development tools
        tool_patterns = ['git', 'github', 'gitlab', 'jenkins', 'ci/cd', 'testing', 'pytest', 'jest']
        tools.extend([pattern for pattern in tool_patterns if pattern in description])

        return TechnicalRequirements(
            languages=languages,
            frameworks=frameworks,
            databases=databases,
            infrastructure=infrastructure,
            tools=tools,
            apis=apis,
        )

    async def _assess_complexity(
        self, description: str, tech_requirements: TechnicalRequirements
    ) -> ComplexityMetrics:
        """Assess project complexity across multiple dimensions."""

        # Technical complexity scoring
        tech_score = self._calculate_technical_complexity(description, tech_requirements)

        # Organizational complexity scoring
        org_score = self._calculate_organizational_complexity(description)

        # Temporal complexity scoring
        temporal_score = self._calculate_temporal_complexity(description)

        return ComplexityMetrics(
            technical_complexity=tech_score,
            organizational_complexity=org_score,
            temporal_complexity=temporal_score,
            overall_score=0.0,  # Will be calculated by validator
            complexity_level=ComplexityLevel.SIMPLE,  # Will be determined by validator
        )

    def _calculate_technical_complexity(
        self, description: str, tech_requirements: TechnicalRequirements
    ) -> int:
        """Calculate technical complexity score (1-10)."""
        score = 1

        # Base complexity from technology count
        total_tech = (
            len(tech_requirements.languages) +
            len(tech_requirements.frameworks) +
            len(tech_requirements.databases) +
            len(tech_requirements.infrastructure)
        )

        if total_tech <= 3:
            score += 1
        elif total_tech <= 6:
            score += 3
        elif total_tech <= 10:
            score += 5
        else:
            score += 7

        # Additional complexity indicators
        complexity_indicators = [
            'microservices', 'distributed', 'scalable', 'high-performance',
            'real-time', 'machine learning', 'ai', 'blockchain', 'websocket',
            'streaming', 'big data', 'analytics', 'enterprise', 'multi-tenant'
        ]

        complexity_count = sum(1 for indicator in complexity_indicators if indicator in description)
        score += min(complexity_count, 2)  # Cap at +2 for complexity indicators

        return min(score, 10)  # Cap at 10

    def _calculate_organizational_complexity(self, description: str) -> int:
        """Calculate organizational complexity score (1-10)."""
        score = 1

        # Team size indicators
        if any(term in description for term in ['team', 'multiple developers', 'collaboration']):
            score += 2
        if any(term in description for term in ['large team', 'enterprise', 'organization']):
            score += 3

        # Process complexity indicators
        if any(term in description for term in ['agile', 'scrum', 'ci/cd', 'devops']):
            score += 1
        if any(term in description for term in ['compliance', 'audit', 'governance', 'security']):
            score += 2

        return min(score, 10)

    def _calculate_temporal_complexity(self, description: str) -> int:
        """Calculate temporal complexity score (1-10)."""
        score = 1

        # Timeline pressure indicators
        if any(term in description for term in ['urgent', 'asap', 'quickly', 'fast']):
            score += 3
        if any(term in description for term in ['deadline', 'timeline', 'schedule']):
            score += 2
        if any(term in description for term in ['mvp', 'prototype', 'proof of concept']):
            score += 1

        # Long-term project indicators (reduce temporal pressure)
        if any(term in description for term in ['long-term', 'gradual', 'phased', 'iterative']):
            score = max(score - 2, 1)

        return min(score, 10)

    async def _identify_project_type(
        self, description: str, tech_requirements: TechnicalRequirements
    ) -> ProjectType:
        """Identify the primary project type based on description and tech stack."""

        # Frontend indicators
        frontend_indicators = ['frontend', 'ui', 'user interface', 'web app', 'spa']
        if any(indicator in description for indicator in frontend_indicators):
            if any(fw in tech_requirements.frameworks for fw in ['react', 'vue', 'angular']):
                return ProjectType.WEB_FRONTEND

        # Backend indicators
        backend_indicators = ['backend', 'api', 'server', 'database', 'rest', 'graphql']
        if any(indicator in description for indicator in backend_indicators):
            return ProjectType.WEB_BACKEND

        # Full-stack indicators
        fullstack_indicators = ['full-stack', 'fullstack', 'complete application', 'end-to-end']
        if any(indicator in description for indicator in fullstack_indicators):
            return ProjectType.WEB_FULLSTACK

        # Mobile indicators
        mobile_indicators = ['mobile', 'ios', 'android', 'app store', 'mobile app']
        if any(indicator in description for indicator in mobile_indicators):
            if 'flutter' in tech_requirements.frameworks or 'dart' in tech_requirements.languages:
                return ProjectType.MOBILE_CROSSPLATFORM
            return ProjectType.MOBILE_NATIVE

        # Microservices indicators
        if 'microservices' in description or 'micro-services' in description:
            return ProjectType.MICROSERVICES

        # Data processing indicators
        data_indicators = ['data processing', 'etl', 'pipeline', 'batch processing']
        if any(indicator in description for indicator in data_indicators):
            return ProjectType.DATA_PROCESSING

        # Analytics indicators
        analytics_indicators = ['analytics', 'reporting', 'dashboard', 'metrics', 'insights']
        if any(indicator in description for indicator in analytics_indicators):
            return ProjectType.DATA_ANALYTICS

        # ML indicators
        ml_indicators = ['machine learning', 'ml', 'ai', 'neural network', 'deep learning']
        if any(indicator in description for indicator in ml_indicators):
            return ProjectType.ML_PIPELINE

        # Automation indicators
        automation_indicators = ['automation', 'script', 'tool', 'utility', 'bot']
        if any(indicator in description for indicator in automation_indicators):
            return ProjectType.AUTOMATION

        # Default to web backend if API-related
        if any(indicator in description for indicator in ['api', 'rest', 'graphql']):
            return ProjectType.API_REST

        # Default fallback
        return ProjectType.WEB_BACKEND

    async def _extract_constraints(self, description: str) -> ProjectConstraints:
        """Extract project constraints from description."""

        # Determine team size
        team_size = TeamSize.SOLO
        if any(term in description for term in ['team', 'multiple developers']):
            team_size = TeamSize.SMALL
        if any(term in description for term in ['large team', 'many developers']):
            team_size = TeamSize.MEDIUM
        if any(term in description for term in ['enterprise', 'organization', 'company-wide']):
            team_size = TeamSize.LARGE

        # Determine quality requirements
        quality_level = QualityLevel.PRODUCTION
        if any(term in description for term in ['prototype', 'mvp', 'proof of concept']):
            quality_level = QualityLevel.PROTOTYPE
        if any(term in description for term in ['enterprise', 'mission critical', 'high availability']):
            quality_level = QualityLevel.ENTERPRISE
        if any(term in description for term in ['critical', 'safety', 'financial', 'healthcare']):
            quality_level = QualityLevel.MISSION_CRITICAL

        # Extract timeline if mentioned
        timeline_days = None
        timeline_patterns = [
            (r'(\d+)\s*days?', 1),
            (r'(\d+)\s*weeks?', 7),
            (r'(\d+)\s*months?', 30),
        ]

        for pattern, multiplier in timeline_patterns:
            match = re.search(pattern, description)
            if match:
                timeline_days = int(match.group(1)) * multiplier
                break

        return ProjectConstraints(
            timeline_days=timeline_days,
            team_size=team_size,
            quality_requirements=quality_level,
            compliance_requirements=[],
            performance_requirements={},
        )

    async def _suggest_patterns(
        self,
        project_type: ProjectType,
        complexity_metrics: ComplexityMetrics,
        constraints: ProjectConstraints,
    ) -> List[str]:
        """Suggest optimal coordination patterns based on analysis."""
        patterns = []

        # Calculate overall complexity for pattern selection
        overall_complexity = (
            complexity_metrics.technical_complexity * 0.5 +
            complexity_metrics.organizational_complexity * 0.3 +
            complexity_metrics.temporal_complexity * 0.2
        )

        # Pattern selection based on complexity and project type
        if overall_complexity <= 3.0:
            patterns.append("peer_to_peer")
        elif overall_complexity <= 6.0:
            patterns.append("hierarchical")
        elif overall_complexity <= 8.5:
            patterns.append("hybrid")
        else:
            patterns.append("hierarchical")
            patterns.append("event_driven")

        # Project type specific patterns
        if project_type in [ProjectType.DATA_PROCESSING, ProjectType.ML_PIPELINE]:
            patterns.append("pipeline")

        if project_type == ProjectType.MICROSERVICES:
            patterns.append("event_driven")

        if constraints.team_size in [TeamSize.LARGE]:
            if "hierarchical" not in patterns:
                patterns.append("hierarchical")

        return patterns[:2]  # Return top 2 recommendations

    def _calculate_confidence_score(
        self,
        tech_requirements: TechnicalRequirements,
        complexity_metrics: ComplexityMetrics,
        project_type: ProjectType,
    ) -> float:
        """Calculate confidence score for the analysis."""
        score = 0.5  # Base confidence

        # Increase confidence based on identified technologies
        total_tech = (
            len(tech_requirements.languages) +
            len(tech_requirements.frameworks) +
            len(tech_requirements.databases)
        )

        if total_tech >= 3:
            score += 0.2
        if total_tech >= 6:
            score += 0.1

        # Increase confidence if complexity assessment seems consistent
        if complexity_metrics.technical_complexity > 1:
            score += 0.1

        # Decrease confidence for very high complexity (might be overestimated)
        if complexity_metrics.overall_score > 9.0:
            score -= 0.1

        return min(max(score, 0.0), 1.0)

    def _build_complexity_keywords(self) -> Dict[str, int]:
        """Build complexity keyword scoring dictionary."""
        return {
            'simple': -1,
            'basic': -1,
            'complex': 2,
            'advanced': 2,
            'enterprise': 3,
            'scalable': 2,
            'distributed': 3,
            'microservices': 3,
            'real-time': 2,
            'high-performance': 2,
        }

    def _build_project_type_patterns(self) -> Dict[ProjectType, List[str]]:
        """Build project type identification patterns."""
        return {
            ProjectType.WEB_FRONTEND: ['frontend', 'ui', 'react', 'vue', 'angular'],
            ProjectType.WEB_BACKEND: ['backend', 'api', 'server', 'database'],
            ProjectType.WEB_FULLSTACK: ['full-stack', 'fullstack', 'complete'],
            ProjectType.MOBILE_NATIVE: ['mobile', 'ios', 'android', 'native'],
            ProjectType.API_REST: ['api', 'rest', 'endpoint'],
            ProjectType.MICROSERVICES: ['microservices', 'micro-services'],
            ProjectType.DATA_PROCESSING: ['data', 'etl', 'pipeline', 'processing'],
            ProjectType.ML_PIPELINE: ['ml', 'machine learning', 'ai', 'neural'],
            ProjectType.AUTOMATION: ['automation', 'script', 'tool', 'bot'],
        }