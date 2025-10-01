# Astro AI - Local AI Assistant

## Project Overview

This project is a comprehensive rebranding of the GPT4All application to **Astro AI**, maintaining all the powerful local AI capabilities while updating the branding, interface, and identity to reflect your company's vision.

## What is Astro AI?

Astro AI is a free-to-use, locally running, privacy-aware chatbot that requires no GPU or internet connection. It provides access to large language models (LLMs) on your personal computer, ensuring your conversations remain private and secure.

### Key Features

- **Privacy-First**: All processing happens locally on your machine
- **No Internet Required**: Run AI models without any external dependencies
- **Free to Use**: No subscriptions or API costs
- **Cross-Platform**: Available for Windows, macOS, and Linux
- **LocalDocs Integration**: Chat with your documents using RAG (Retrieval-Augmented Generation)
- **Multiple Model Support**: Compatible with various LLM formats

## Rebranding Transformation

### What Was Changed

This project transformed the original GPT4All application into Astro AI with the following comprehensive changes:

#### 1. Visual Identity
- **Application Title**: Changed from "GPT4All" to "Astro AI"
- **Window Branding**: All UI references updated to Astro AI
- **Color Scheme**: Implemented teal (#00BFA5) and purple (#6A1B9A) brand colors

#### 2. Package Identity
- **Python Package**: Renamed from `gpt4all` to `astro_ai`
- **TypeScript Package**: Renamed from `gpt4all` to `astro-ai`
- **Project Name**: Updated in all configuration files

#### 3. Documentation & Links
- **Website**: Updated to point to `astro-ai.app` domain
- **Download Links**: All references point to Astro AI repositories
- **Installation Commands**: Updated for new package names

#### 4. System Integration
- **Desktop Shortcuts**: Creates "Astro AI" entries in system menus
- **Application Icons**: References updated to astro-ai branding
- **System Tray**: Displays as Astro AI application

## Technical Architecture

### Core Technologies
- **Frontend**: Qt 6.8.1 with QML for cross-platform desktop UI
- **Backend**: llama.cpp for efficient LLM inference
- **Build System**: CMake with cross-platform compatibility
- **Language Support**: C++, Python, and TypeScript bindings

### System Requirements
- **macOS**: 10.15+ with Metal support
- **Memory**: Minimum 4GB RAM (8GB+ recommended)
- **Storage**: 3-10GB depending on models used
- **Processor**: Modern CPU (Apple Silicon optimized)

## Current Project Status

### ✅ Completed Features
- Complete visual rebranding to Astro AI
- Updated package names and repository references
- Modified installation scripts and desktop integration
- Created functional demo applications
- Updated all documentation and README files

### ⚠️ Known Issues
- Qt compilation currently blocked by usearch library compatibility
- Python package installation needs directory restructure
- Full application build requires dependency resolution

### 🚀 Demo Applications

Two Python demo applications showcase the complete Astro AI branding:

#### `astro_ai_demo.py`
Basic demonstration of the rebranded interface with:
- Astro AI branded chat window
- Teal and purple color scheme
- Interactive message simulation

#### `astro_ai_fixed.py`
Enhanced demo with improved features:
- Scrollable chat history
- Better UI responsiveness
- Complete branding implementation

## Installation & Usage

### Running Demo Applications

```bash
# Navigate to project directory
cd /Users/alexandertrifonidis/Downloads/Projects/gpt4all

# Run the enhanced demo
python3 astro_ai_fixed.py
```

### Building from Source (When Dependencies Resolved)

```bash
# Install dependencies
brew install qt6 cmake

# Build the application
mkdir build && cd build
cmake .. -DCMAKE_PREFIX_PATH=/opt/homebrew
make -j$(nproc)
```

## File Structure

### Key Modified Files
```
gpt4all/
├── README.md                    # Main documentation (rebranded)
├── main.qml                     # UI window title updated
├── CMakeLists.txt              # Project name changed
├── package.json                # Package identity updated
├── astro_ai_demo.py            # Demo application
├── astro_ai_fixed.py           # Enhanced demo
└── gpt4all-bindings/
    └── python/
        └── setup.py            # Python package renamed
```

## Branding Guidelines

### Colors
- **Primary Teal**: #00BFA5
- **Secondary Purple**: #6A1B9A
- **Background**: Dark theme optimized

### Typography
- Application uses system fonts
- Consistent "Astro AI" branding throughout

### Voice & Tone
- Professional yet approachable
- Emphasizes privacy and local processing
- Highlights ease of use and accessibility

## Development Roadmap

### Phase 1: Foundation (Completed)
- ✅ Complete visual rebranding
- ✅ Package name updates
- ✅ Demo applications

### Phase 2: Technical Resolution (In Progress)
- 🔄 Resolve usearch compilation issues
- 🔄 Fix Python package installation
- 🔄 Complete Qt application build

### Phase 3: Enhancement (Planned)
- 📋 Custom Astro AI model integration
- 📋 Enhanced UI with brand-specific features
- 📋 Improved installation experience

## Contributing

This is a rebranded version of GPT4All. For technical contributions:

1. Focus on resolving compilation issues
2. Maintain Astro AI branding consistency
3. Test across multiple platforms
4. Document any changes thoroughly

## License

This project maintains the original GPT4All licensing while operating under the Astro AI brand.

## Contact

For questions about this Astro AI implementation, refer to the demo applications and rebranding documentation provided in this repository.

---

**Note**: This project represents a complete rebranding of GPT4All to Astro AI, maintaining all core functionality while updating the visual identity and package names to reflect your company's branding requirements.
