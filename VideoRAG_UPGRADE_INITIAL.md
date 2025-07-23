## FEATURE:
Upgrade the VideoRAG project (https://github.com/HKUDS/VideoRAG) to support dynamic video segmentation based on scene detection instead of fixed 30-second intervals, adapt the system for RTX 5090ti (16GB VRAM) instead of RTX 3090 (24GB VRAM), replace faster-whisper with OpenAI Whisper API, and set up the environment using conda virtual environment with fixed dependency versions.

The core modifications include:
1. Replace fixed 30-second video segmentation with intelligent scene-based segmentation using PySceneDetect
2. Adapt video processing pipeline to handle variable-length segments (from 0.1 seconds to any length)
3. Modify memory management and batch processing to work within 16GB VRAM constraints
4. Replace faster-whisper implementation with OpenAI Whisper API calls for audio transcription
5. Create conda environment setup with pinned dependency versions for stability

## EXAMPLES:
- `examples/video_segmentation.py` - PySceneDetect integration for scene-based video cutting
- `examples/openai_whisper_api.py` - OpenAI Whisper API implementation replacing faster-whisper
- `examples/memory_optimization.py` - GPU memory management for 16GB VRAM constraints
- `examples/variable_segment_processing.py` - Processing pipeline adaptation for variable-length segments
- `examples/conda_environment.yml` - Complete conda environment specification with pinned versions

## DOCUMENTATION:
- VideoRAG Original Project: https://github.com/HKUDS/VideoRAG
- VideoRAG Paper: https://arxiv.org/abs/2502.01549
- PySceneDetect Documentation: https://scenedetect.com/
- OpenAI Whisper API Documentation: https://platform.openai.com/docs/guides/speech-to-text
- MiniCPM-V Model Documentation: https://huggingface.co/openbmb/MiniCPM-V-2_6-int4
- Conda Environment Management: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
- PyTorch Memory Management: https://pytorch.org/docs/stable/notes/cuda.html#memory-management

## OTHER CONSIDERATIONS:
- Ensure backward compatibility with existing VideoRAG knowledge indexing and retrieval systems
- Implement robust error handling for variable-length video segments in the processing pipeline
- Optimize MiniCPM-V-2.6-int4 model loading and inference for 16GB VRAM constraints
- Add comprehensive logging for scene detection parameters and segment statistics
- Implement proper API key management and error handling for OpenAI Whisper API calls
- Consider rate limiting and cost optimization for OpenAI API usage
- Maintain the original VideoRAG's graph-based knowledge indexing architecture
- Ensure scene detection parameters are configurable and tunable for different video types
- Add validation for minimum and maximum segment lengths if needed in the future
- Implement proper exception handling for GPU memory overflow scenarios
- Create comprehensive testing suite for variable-length segment processing
- Document performance differences between fixed and dynamic segmentation approaches
- Ensure compatibility with the existing LongerVideos benchmark dataset
- Add monitoring and metrics for scene detection accuracy and processing performance
