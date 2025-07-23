# 🚀 PRP Generator

> **Initial.md to PRP generation system** - Intelligent context engineering for AI coding assistants

Transform your project ideas from simple Initial.md files into comprehensive Project Requirements and Patterns (PRPs) that supercharge AI coding assistants.

## ⚡ Quick Start

```bash
# One-click setup
curl -sSL https://raw.githubusercontent.com/Askair123/prp-generator/main/scripts/setup/quick_setup.sh | bash
```

## 🎯 What is PRP Generator?

PRP Generator converts simple project descriptions into detailed, structured requirements that help AI assistants understand your project context better. It bridges the gap between human ideas and AI implementation.

**Input:** Simple Initial.md file with basic project description
**Output:** Comprehensive PRP with context, patterns, and implementation guidance

## 📚 Documentation

- **[Installation Guide](docs/user-guide/installation.md)** - Get started quickly
- **[Quick Reference](docs/user-guide/QUICK_REFERENCE.md)** - Common commands and usage
- **[GitHub Setup](docs/deployment/github-setup.md)** - Deploy to your repository
- **[API Reference](docs/developer-guide/)** - Developer documentation

## 🔧 Core Features

- **Intelligent Parsing** - Extracts context from Initial.md files
- **Pattern Recognition** - Identifies common development patterns
- **Claude Flow Integration** - Generates Claude Flow configurations
- **Template System** - Customizable PRP templates
- **CLI Interface** - Easy command-line usage

## 📁 Project Structure

```
prp-generator/
├── src/coordinator/          # Core PRP generation system
├── templates/               # PRP templates
├── examples/               # Usage examples and generated PRPs
├── docs/                   # Documentation
├── scripts/                # Setup and utility scripts
├── tests/                  # Test files
└── dev/                    # Development tools and demos
```

## 🚀 Usage Examples

### Basic Usage
```bash
# Generate PRP from Initial.md
python src/coordinator/initial_to_prp_cli.py --input INITIAL.md --output my_project.prp.md
```

### With Claude Flow Config
```bash
# Generate both PRP and Claude Flow configuration
python src/coordinator/initial_to_prp_cli.py --input INITIAL.md --output my_project.prp.md --claude-flow
```

See [examples/](examples/) directory for more usage examples.

## 🤝 Contributing

We welcome contributions! See [docs/developer-guide/contributing.md](docs/developer-guide/contributing.md) for guidelines.

## 📄 License

MIT License - see [LICENSE](LICENSE) file.

## 🔗 Links

- **GitHub Repository:** [Askair123/prp-generator](https://github.com/Askair123/prp-generator)
- **Issues:** [Report bugs or request features](https://github.com/Askair123/prp-generator/issues)
- **Discussions:** [Community discussions](https://github.com/Askair123/prp-generator/discussions)

---

*Built with ❤️ for better AI-human collaboration in software development*

