"""
Integration tests for Coordinator Pattern system.

Tests the complete workflow from project analysis to Claude Flow configuration generation.
"""

import asyncio
import pytest
from pathlib import Path
import tempfile
import shutil

from coordinator import (
    ProjectAnalyzer,
    PatternLibrary,
    ClaudeFlowAdapter,
    ProjectType,
    ComplexityLevel,
)


class TestCoordinatorIntegration:
    """Integration tests for the complete coordinator workflow."""
    
    @pytest.fixture
    def temp_output_dir(self):
        """Create temporary output directory."""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def analyzer(self):
        """Create project analyzer instance."""
        return ProjectAnalyzer()
    
    @pytest.fixture
    def pattern_library(self):
        """Create pattern library instance."""
        return PatternLibrary()
    
    @pytest.fixture
    def adapter(self):
        """Create Claude Flow adapter instance."""
        return ClaudeFlowAdapter()
    
    @pytest.mark.asyncio
    async def test_simple_web_backend_workflow(
        self, analyzer, pattern_library, adapter, temp_output_dir
    ):
        """Test complete workflow for a simple web backend project."""
        
        # Test project description
        description = """
        Build a REST API for an e-commerce platform using Python and FastAPI.
        The API should handle user authentication, product catalog, shopping cart,
        and order processing. Use PostgreSQL for data storage and deploy on AWS.
        This is for a small team of 3 developers with a 2-month timeline.
        """
        
        # Step 1: Analyze project
        analysis = await analyzer.analyze_project(description)
        
        # Verify analysis results
        assert analysis.project_type == ProjectType.WEB_BACKEND
        assert analysis.complexity_metrics.complexity_level in [
            ComplexityLevel.MODERATE, ComplexityLevel.COMPLEX
        ]
        assert "python" in analysis.technical_requirements.languages
        assert "fastapi" in analysis.technical_requirements.frameworks
        assert "postgresql" in analysis.technical_requirements.databases
        assert analysis.confidence_score > 0.5
        
        # Step 2: Select pattern
        pattern_name, pattern, score = pattern_library.select_best_pattern(analysis)
        
        # Verify pattern selection
        assert pattern_name in ["hierarchical", "hybrid"]
        assert score > 0.5
        assert len(pattern.agents) > 0
        
        # Step 3: Generate configuration
        config = await adapter.generate_config(analysis, pattern)
        
        # Verify configuration
        assert config.hive_structure in ["hierarchical", "adaptive"]
        assert len(config.agents) > 0
        assert len(config.quality_gates) > 0
        assert config.memory_strategy is not None
        
        # Verify agent configurations
        agent_types = [agent.type for agent in config.agents]
        assert "architect" in agent_types or "backend_dev" in agent_types
        
        # Step 4: Validate configuration
        validation = await adapter.validate_config(config)
        
        assert validation.is_valid
        assert validation.score > 0.7
        
        # Step 5: Execute handoff
        handoff = await adapter.handoff_to_claude_flow(config, temp_output_dir)
        
        assert handoff.success
        assert handoff.claude_flow_ready
        assert Path(handoff.config_path).exists()
        
        # Verify config file content
        with open(handoff.config_path, 'r') as f:
            config_content = f.read()
            assert "hive_structure" in config_content
            assert "agents" in config_content
    
    @pytest.mark.asyncio
    async def test_data_processing_workflow(
        self, analyzer, pattern_library, adapter, temp_output_dir
    ):
        """Test workflow for a data processing project."""
        
        description = """
        Create a data processing pipeline that extracts data from multiple APIs,
        transforms it using Python pandas, and loads it into a data warehouse.
        The pipeline should run daily and handle error recovery.
        """
        
        # Analyze project
        analysis = await analyzer.analyze_project(description)
        
        # Should identify as data processing
        assert analysis.project_type == ProjectType.DATA_PROCESSING
        assert "python" in analysis.technical_requirements.languages
        
        # Select pattern - should prefer pipeline pattern
        pattern_name, pattern, score = pattern_library.select_best_pattern(analysis)
        
        # Pipeline pattern should score well for data processing
        assert pattern_name in ["pipeline", "hierarchical"]
        
        # Generate and validate configuration
        config = await adapter.generate_config(analysis, pattern)
        validation = await adapter.validate_config(config)
        
        assert validation.is_valid
        assert len(config.agents) > 0
    
    @pytest.mark.asyncio
    async def test_research_project_workflow(
        self, analyzer, pattern_library, adapter, temp_output_dir
    ):
        """Test workflow for a research project."""
        
        description = """
        Conduct a research analysis on market trends in renewable energy.
        The project involves data collection, statistical analysis, report writing,
        and peer review. This is for a solo researcher with flexible timeline.
        """
        
        # Analyze project
        analysis = await analyzer.analyze_project(description)
        
        # Should identify as research
        assert analysis.project_type == ProjectType.RESEARCH
        assert analysis.complexity_metrics.complexity_level in [
            ComplexityLevel.SIMPLE, ComplexityLevel.MODERATE
        ]
        
        # Select pattern - should prefer peer-to-peer for research
        pattern_name, pattern, score = pattern_library.select_best_pattern(analysis)
        
        # Peer-to-peer should score well for research
        assert pattern_name in ["peer_to_peer", "pipeline"]
        
        # Generate configuration
        config = await adapter.generate_config(analysis, pattern)
        
        # Research projects should have appropriate agents
        agent_types = [agent.type for agent in config.agents]
        assert any(agent_type in ["researcher", "analyst", "writer"] for agent_type in agent_types)
    
    def test_pattern_library_completeness(self, pattern_library):
        """Test that pattern library has all expected patterns."""
        
        patterns = pattern_library.get_coordination_patterns()
        
        expected_patterns = ["hierarchical", "peer_to_peer", "pipeline", "event_driven", "hybrid"]
        
        for expected in expected_patterns:
            assert expected in patterns
            pattern = patterns[expected]
            assert pattern.name == expected
            assert len(pattern.agents) > 0
            assert len(pattern.best_for) > 0
            assert len(pattern.quality_gates) > 0
    
    @pytest.mark.asyncio
    async def test_error_handling(self, analyzer, adapter):
        """Test error handling for invalid inputs."""
        
        # Test with empty description
        analysis = await analyzer.analyze_project("")
        assert analysis.confidence_score < 0.5
        
        # Test with minimal description
        analysis = await analyzer.analyze_project("build something")
        assert analysis.project_type is not None  # Should have a default
        
        # Configuration should still be generatable
        pattern_library = PatternLibrary()
        pattern_name, pattern, score = pattern_library.select_best_pattern(analysis)
        
        config = await adapter.generate_config(analysis, pattern)
        validation = await adapter.validate_config(config)
        
        # Should be valid even with minimal input
        assert validation.is_valid


if __name__ == "__main__":
    # Run a simple test
    async def run_simple_test():
        analyzer = ProjectAnalyzer()
        description = "Build a Python web API with FastAPI and PostgreSQL"
        analysis = await analyzer.analyze_project(description)
        print(f"Analysis complete: {analysis.project_type.value}, confidence: {analysis.confidence_score:.2f}")
    
    asyncio.run(run_simple_test())
