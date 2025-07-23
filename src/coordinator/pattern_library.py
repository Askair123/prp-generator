"""
Pattern Library for Coordinator Pattern system.

This module manages coordination patterns, best practices, and pattern selection
algorithms for optimal multi-agent coordination strategies.
"""

from typing import Dict, List, Optional, Tuple
import json
from pathlib import Path

from .models import (
    CoordinationPattern,
    ComplexityLevel,
    TeamSize,
    ProjectType,
    ProjectAnalysis,
)


class PatternLibrary:
    """
    Registry and management system for coordination patterns.

    Provides pattern matching, scoring, and selection algorithms
    to recommend optimal coordination strategies based on project analysis.
    """

    def __init__(self):
        """Initialize the pattern library with predefined patterns."""
        self._patterns: Dict[str, CoordinationPattern] = {}
        self._load_default_patterns()

    def _load_default_patterns(self) -> None:
        """Load default coordination patterns."""

        # Hierarchical coordination pattern
        hierarchical = CoordinationPattern(
            name="hierarchical",
            description="Central coordinator with specialized sub-agents",
            best_for=[
                "complex projects",
                "large teams",
                "enterprise requirements",
                "clear role separation needed"
            ],
            agents=[
                "architect", "backend_dev", "frontend_dev",
                "database_designer", "tester", "devops", "security"
            ],
            coordination_rules="central_decision_making",
            quality_gates=[
                "code_review", "integration_testing",
                "security_scan", "performance_testing"
            ],
            complexity_fit=[
                ComplexityLevel.MODERATE,
                ComplexityLevel.COMPLEX,
                ComplexityLevel.ENTERPRISE
            ],
            team_size_fit=[TeamSize.SMALL, TeamSize.MEDIUM, TeamSize.LARGE],
        )

        # Peer-to-peer coordination pattern
        peer_to_peer = CoordinationPattern(
            name="peer_to_peer",
            description="Distributed coordination with consensus",
            best_for=[
                "research projects",
                "small teams",
                "experimental work",
                "collaborative analysis"
            ],
            agents=["researcher", "analyst", "writer", "reviewer"],
            coordination_rules="consensus_based",
            quality_gates=["peer_review", "validation_testing"],
            complexity_fit=[ComplexityLevel.SIMPLE, ComplexityLevel.MODERATE],
            team_size_fit=[TeamSize.SOLO, TeamSize.SMALL],
        )

        # Pipeline coordination pattern
        pipeline = CoordinationPattern(
            name="pipeline",
            description="Sequential processing with handoffs",
            best_for=[
                "data processing",
                "content creation",
                "linear workflows",
                "batch processing"
            ],
            agents=["collector", "processor", "transformer", "publisher"],
            coordination_rules="sequential_handoff",
            quality_gates=["stage_validation", "output_verification"],
            complexity_fit=[
                ComplexityLevel.SIMPLE,
                ComplexityLevel.MODERATE,
                ComplexityLevel.COMPLEX
            ],
            team_size_fit=[TeamSize.SOLO, TeamSize.SMALL, TeamSize.MEDIUM],
        )

        # Event-driven coordination pattern
        event_driven = CoordinationPattern(
            name="event_driven",
            description="Reactive coordination based on events",
            best_for=[
                "monitoring systems",
                "real-time processing",
                "reactive workflows",
                "microservices architecture"
            ],
            agents=["monitor", "analyzer", "responder", "notifier"],
            coordination_rules="event_triggered",
            quality_gates=["event_validation", "response_testing"],
            complexity_fit=[
                ComplexityLevel.MODERATE,
                ComplexityLevel.COMPLEX,
                ComplexityLevel.ENTERPRISE
            ],
            team_size_fit=[TeamSize.SMALL, TeamSize.MEDIUM, TeamSize.LARGE],
        )

        # Hybrid coordination pattern
        hybrid = CoordinationPattern(
            name="hybrid",
            description="Combination of hierarchical and peer-to-peer patterns",
            best_for=[
                "complex enterprise projects",
                "mixed team structures",
                "multi-phase projects",
                "flexible coordination needs"
            ],
            agents=[
                "coordinator", "architect", "lead_dev", "specialist_dev",
                "researcher", "tester", "reviewer"
            ],
            coordination_rules="adaptive_mixed",
            quality_gates=[
                "phase_review", "peer_validation",
                "integration_testing", "final_review"
            ],
            complexity_fit=[ComplexityLevel.COMPLEX, ComplexityLevel.ENTERPRISE],
            team_size_fit=[TeamSize.MEDIUM, TeamSize.LARGE],
        )

        # Register all patterns
        self._patterns = {
            "hierarchical": hierarchical,
            "peer_to_peer": peer_to_peer,
            "pipeline": pipeline,
            "event_driven": event_driven,
            "hybrid": hybrid,
        }

    def get_coordination_patterns(self) -> Dict[str, CoordinationPattern]:
        """Get all available coordination patterns."""
        return self._patterns.copy()

    def get_pattern(self, name: str) -> Optional[CoordinationPattern]:
        """Get a specific coordination pattern by name."""
        return self._patterns.get(name)

    def get_matching_patterns(self, analysis: ProjectAnalysis) -> List[Tuple[str, float]]:
        """
        Get patterns that match the project analysis with scores.

        Args:
            analysis: Project analysis results

        Returns:
            List of (pattern_name, score) tuples sorted by score descending
        """
        scored_patterns = []

        for name, pattern in self._patterns.items():
            score = self._score_pattern_fit(pattern, analysis)
            scored_patterns.append((name, score))

        # Sort by score descending
        scored_patterns.sort(key=lambda x: x[1], reverse=True)
        return scored_patterns

    def select_best_pattern(self, analysis: ProjectAnalysis) -> Tuple[str, CoordinationPattern, float]:
        """
        Select the best coordination pattern for the given analysis.

        Args:
            analysis: Project analysis results

        Returns:
            Tuple of (pattern_name, pattern, score)
        """
        scored_patterns = self.get_matching_patterns(analysis)

        if not scored_patterns:
            # Fallback to hierarchical pattern
            return "hierarchical", self._patterns["hierarchical"], 0.5

        best_name, best_score = scored_patterns[0]
        best_pattern = self._patterns[best_name]

        return best_name, best_pattern, best_score

    def _score_pattern_fit(self, pattern: CoordinationPattern, analysis: ProjectAnalysis) -> float:
        """
        Score how well a pattern fits the project analysis.

        Args:
            pattern: Coordination pattern to evaluate
            analysis: Project analysis results

        Returns:
            Fit score between 0.0 and 1.0
        """
        score = 0.0

        # Complexity fit scoring (40% weight)
        complexity_score = self._score_complexity_fit(pattern, analysis.complexity_metrics.complexity_level)
        score += complexity_score * 0.4

        # Team size fit scoring (30% weight)
        team_score = self._score_team_size_fit(pattern, analysis.constraints.team_size)
        score += team_score * 0.3

        # Project type fit scoring (20% weight)
        project_type_score = self._score_project_type_fit(pattern, analysis.project_type)
        score += project_type_score * 0.2

        # Quality requirements fit scoring (10% weight)
        quality_score = self._score_quality_fit(pattern, analysis.constraints.quality_requirements)
        score += quality_score * 0.1

        return min(score, 1.0)

    def _score_complexity_fit(self, pattern: CoordinationPattern, complexity: ComplexityLevel) -> float:
        """Score complexity fit."""
        if complexity in pattern.complexity_fit:
            return 1.0

        # Partial scoring for adjacent complexity levels
        complexity_order = [
            ComplexityLevel.SIMPLE,
            ComplexityLevel.MODERATE,
            ComplexityLevel.COMPLEX,
            ComplexityLevel.ENTERPRISE
        ]

        try:
            pattern_indices = [complexity_order.index(c) for c in pattern.complexity_fit]
            project_index = complexity_order.index(complexity)

            # Find closest match
            closest_distance = min(abs(project_index - pi) for pi in pattern_indices)

            if closest_distance == 0:
                return 1.0
            elif closest_distance == 1:
                return 0.7
            elif closest_distance == 2:
                return 0.4
            else:
                return 0.1
        except ValueError:
            return 0.5  # Default if complexity not found

    def _score_team_size_fit(self, pattern: CoordinationPattern, team_size: TeamSize) -> float:
        """Score team size fit."""
        if team_size in pattern.team_size_fit:
            return 1.0

        # Partial scoring for adjacent team sizes
        team_order = [TeamSize.SOLO, TeamSize.SMALL, TeamSize.MEDIUM, TeamSize.LARGE]

        try:
            pattern_indices = [team_order.index(t) for t in pattern.team_size_fit]
            project_index = team_order.index(team_size)

            closest_distance = min(abs(project_index - pi) for pi in pattern_indices)

            if closest_distance == 0:
                return 1.0
            elif closest_distance == 1:
                return 0.8
            elif closest_distance == 2:
                return 0.5
            else:
                return 0.2
        except ValueError:
            return 0.5

    def _score_project_type_fit(self, pattern: CoordinationPattern, project_type: ProjectType) -> float:
        """Score project type fit based on pattern characteristics."""

        # Project type to pattern affinity mapping
        type_affinities = {
            ProjectType.WEB_FRONTEND: {
                "hierarchical": 0.8,
                "peer_to_peer": 0.6,
                "pipeline": 0.4,
                "event_driven": 0.3,
                "hybrid": 0.7,
            },
            ProjectType.WEB_BACKEND: {
                "hierarchical": 0.9,
                "peer_to_peer": 0.5,
                "pipeline": 0.6,
                "event_driven": 0.7,
                "hybrid": 0.8,
            },
            ProjectType.MICROSERVICES: {
                "hierarchical": 0.7,
                "peer_to_peer": 0.4,
                "pipeline": 0.5,
                "event_driven": 0.9,
                "hybrid": 0.8,
            },
            ProjectType.DATA_PROCESSING: {
                "hierarchical": 0.6,
                "peer_to_peer": 0.5,
                "pipeline": 0.9,
                "event_driven": 0.7,
                "hybrid": 0.7,
            },
            ProjectType.ML_PIPELINE: {
                "hierarchical": 0.7,
                "peer_to_peer": 0.6,
                "pipeline": 0.9,
                "event_driven": 0.6,
                "hybrid": 0.8,
            },
            ProjectType.RESEARCH: {
                "hierarchical": 0.5,
                "peer_to_peer": 0.9,
                "pipeline": 0.7,
                "event_driven": 0.4,
                "hybrid": 0.6,
            },
        }

        # Get affinity for this project type and pattern
        if project_type in type_affinities:
            return type_affinities[project_type].get(pattern.name, 0.5)

        return 0.5  # Default neutral score

    def _score_quality_fit(self, pattern: CoordinationPattern, quality_level) -> float:
        """Score quality requirements fit."""

        # Quality gates count as indicator of quality support
        quality_gates_count = len(pattern.quality_gates)

        if quality_level.value == "prototype":
            # Prototype needs fewer quality gates
            return 1.0 if quality_gates_count <= 2 else 0.7
        elif quality_level.value == "production":
            # Production needs moderate quality gates
            return 1.0 if 2 <= quality_gates_count <= 4 else 0.8
        elif quality_level.value == "enterprise":
            # Enterprise needs comprehensive quality gates
            return 1.0 if quality_gates_count >= 3 else 0.6
        elif quality_level.value == "mission_critical":
            # Mission critical needs maximum quality gates
            return 1.0 if quality_gates_count >= 4 else 0.5

        return 0.7  # Default

    def get_quality_gates(self, tech_stack: List[str]) -> List[str]:
        """Get recommended quality gates based on technology stack."""
        gates = ["code_review", "unit_testing"]

        # Add tech-specific gates
        if any(tech in tech_stack for tech in ["python", "javascript", "java"]):
            gates.append("static_analysis")

        if any(tech in tech_stack for tech in ["web", "api", "backend"]):
            gates.extend(["integration_testing", "security_scan"])

        if any(tech in tech_stack for tech in ["database", "sql", "mongodb"]):
            gates.append("data_validation")

        if any(tech in tech_stack for tech in ["docker", "kubernetes", "aws"]):
            gates.append("deployment_testing")

        return list(set(gates))  # Remove duplicates

    def get_common_pitfalls(self, project_type: str) -> List[str]:
        """Get common pitfalls for a project type."""
        pitfalls = {
            "web_backend": [
                "Insufficient error handling",
                "Missing input validation",
                "Poor database connection management",
                "Inadequate logging and monitoring"
            ],
            "web_frontend": [
                "Poor state management",
                "Inadequate error boundaries",
                "Missing accessibility considerations",
                "Poor performance optimization"
            ],
            "microservices": [
                "Service communication complexity",
                "Data consistency challenges",
                "Monitoring and debugging difficulties",
                "Network latency issues"
            ],
            "data_processing": [
                "Poor error handling in pipelines",
                "Inadequate data validation",
                "Memory management issues",
                "Lack of idempotency"
            ],
        }

        return pitfalls.get(project_type, [
            "Insufficient testing coverage",
            "Poor error handling",
            "Inadequate documentation",
            "Missing monitoring"
        ])

    def add_custom_pattern(self, pattern: CoordinationPattern) -> None:
        """Add a custom coordination pattern to the library."""
        self._patterns[pattern.name] = pattern

    def save_patterns_to_file(self, filepath: str) -> None:
        """Save all patterns to a JSON file."""
        patterns_data = {
            name: pattern.dict() for name, pattern in self._patterns.items()
        }

        with open(filepath, 'w') as f:
            json.dump(patterns_data, f, indent=2)

    def load_patterns_from_file(self, filepath: str) -> None:
        """Load patterns from a JSON file."""
        with open(filepath, 'r') as f:
            patterns_data = json.load(f)

        for name, pattern_dict in patterns_data.items():
            pattern = CoordinationPattern(**pattern_dict)
            self._patterns[name] = pattern