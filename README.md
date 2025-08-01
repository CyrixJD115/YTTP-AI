# YTTP AI - Enhanced YouTube Transcript Processor

## Overview
YTTP AI is a powerful desktop application that automates the entire workflow of extracting YouTube transcripts, processing them with local AI models, and creating polished documents. This tool is designed for content creators, researchers, and anyone who needs to work with YouTube video content in text format.

Key features:
- 🎥 Automatic YouTube transcript extraction
- ✂️ Intelligent text chunk splitting
- 🤖 AI-powered text processing with Ollama models
- 📝 Combined document generation (DOCX/TXT)
- 🎨 Modern animated GUI with responsive design
- ⚙️ Customizable processing settings
- 🔄 Automatic retry mechanism for reliability
- 🧹 Temporary file cleanup after processing
- 🚀 One-click installation and launch

## Requirements

### Software Requirements
- Python 3.8+
- [Ollama](https://ollama.com/) installed and running
- Ollama model of your choice (recommended: `llama3.2` or `deepseek-r1`)

### Hardware Recommendations
For optimal performance, we recommend:
- **CPU**: Intel i5 or equivalent (4 cores minimum)
- **RAM**: 8GB+ (16GB recommended)
- **GPU**: 2-4GB VRAM (for GPU acceleration)
- **Storage**: SSD preferred

For models like `llama3.2`:
- Minimum: 4GB RAM + 2GB VRAM
- Recommended: 8GB RAM + 4GB VRAM

## Installation & Setup

1. **Install Ollama**:
   - Follow official installation instructions: https://ollama.com/download

2. **Download a model**:
   ```bash
   ollama pull llama3.2  # Recommended for 2-4GB VRAM
   # or
   ollama pull deepseek-r1
   ```

3. **Run the application**:
   ```bash
   python Start.py
   ```
   
The application will automatically:
- Install required Python dependencies
- Create necessary directories
- Configure default settings

## Features in Detail

### Transcript Processing
- Automatic extraction of YouTube transcripts
- Configurable chunk size and overlap
- Retry mechanism for unreliable connections
- Support for multiple YouTube URL formats

### AI Processing
- Local processing with Ollama models
- **Customizable processing prompts** (tailor to your specific needs)
- Typewriter effect display with adjustable speed
- Cancellable processing operations

### Document Generation
- DOCX and TXT output formats
- Customizable document titles
- Title font size control
- Automatic filename suggestions

### User Interface
- Modern animated interface
- Responsive layout for all screen sizes
- Colorful theme with gradient backgrounds
- Animated progress indicators
- Inline error messages (no popups)
- Tab-based settings organization

## Quick Start Guide

1. **Launch the application**:
   ```bash
   python Start.py
   ```

2. **Process a YouTube video**:
   1. Enter YouTube URL in the Start screen
   2. View real-time processing in the Processing screen
   3. Adjust filename in the footer if needed
   4. Click "Combine" to save the final document

3. **Customize settings**:
   - Access settings via the Settings tab
   - Adjust chunking parameters
   - **Modify processing prompts** (critical for optimal results)
   - Configure output options

## Custom Processing Prompts

The processing prompt is **crucial** for getting high-quality results. The default prompt is a basic instruction that may need adjustment for your specific use case.

### Prompt Tips:
1. **Be specific** about what you want the AI to do
2. **Include examples** of desired output format
3. **Specify tone** (academic, casual, professional)
4. **Define structure** requirements (bullet points, paragraphs)

### Example Prompts:
```text
"Correct grammar, improve clarity, and convert to academic writing style. Maintain original meaning while enhancing vocabulary."
```
```text
"Summarize key points in bullet format. Include timestamps for each major topic. Keep technical terms accurate."
```
```text
"Transform into a professional blog post. Add section headers. Remove filler words and repetitions."
```

You can access and modify the processing prompt in Settings → Processing Settings.

## Performance Tips

1. **Model Selection**:
   - For 2-4GB VRAM: Use `llama3.2` (2B parameters)
   - For 4-8GB VRAM: Use `deepseek-r1` (7B parameters)
   - Adjust models based on your hardware capabilities

2. **Chunk Sizing**:
   - Start with 300 words/chunk for 2B models
   - Increase to 500-700 words for larger models
   - Adjust based on your hardware capabilities

3. **Prompt Efficiency**:
   - Keep prompts concise but descriptive
   - Avoid redundant instructions
   - Test prompts with small chunks first

## Troubleshooting

### Common Issues
1. **Transcript unavailable**:
   - Verify video has captions
   - Try different video
   - Increase retry count in settings

2. **Slow processing**:
   - Use smaller model (e.g., `llama3:2`)
   - Reduce chunk size
   - Close other resource-intensive applications

3. **Ollama connection issues**:
   - Ensure Ollama is running (`ollama serve`)
   - Check http://localhost:11434 in browser

4. **Poor output quality**:
   - Refine your processing prompt
   - Reduce chunk size for more focused processing
   - Try a different model

### Clearing Temporary Files
The application automatically clears temporary files after processing. To manually clear:
```bash
rm -rf temp/
```
Or simply delete the folder as normal

## Contribution
Contributions are welcome! Please open an issue or submit a pull request for:
- Bug fixes
- New features
- Documentation improvements
- Translation support
- Additional processing prompt templates

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: This application processes videos through YouTube's public API. Please respect content creators' rights and YouTube's Terms of Service when using this tool.
