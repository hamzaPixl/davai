# DAVAI - AI Documentation Generator

DAVAI (Documentation AI) is an AI-powered system that transforms a simple project idea into comprehensive documentation using specialized AI agents.

## 🚀 What DAVAI Does

Transform this:

```text
"A social media platform for developers"
```

Into complete project documentation:

- Project context and requirements
- System architecture design
- Technology stack recommendations
- Task breakdown and timelines
- Development guidelines
- AI integration guide
- Production-ready README

## 🎯 Key Features

- **8 Specialized AI Agents** - Each focused on specific documentation types
- **Complete Workflow** - From idea to full documentation in minutes
- **Multi-LLM Support** - OpenAI, Anthropic, Google providers
- **Auto-Save** - Generated docs saved to organized folders
- **REST API** - Easy integration and automation

## 📦 Repository Structure

```text
davai/
├── README.md              # This overview (you are here)
├── backend/               # DAVAI API server
│   ├── README.md         # 📖 Detailed documentation & setup
│   ├── agents/           # 8 specialized AI agents
│   ├── models/           # Data models
│   ├── routes/           # API endpoints
│   └── docs/             # API documentation & Postman collection
├── prompts/              # Agent prompt templates
└── templates/            # Documentation templates
```

## 🏃‍♂️ Quick Start

### 1. Setup Environment

```bash
export OPENAI_API_KEY=your_key
export ANTHROPIC_API_KEY=your_key
export GOOGLE_API_KEY=your_key
```

### 2. Start DAVAI

```bash
cd backend
chmod +x start.sh
./start.sh
```

### 3. Generate Documentation

```bash
curl -X POST "http://localhost:8000/api/workflow/complete" \
  -H "Content-Type: application/json" \
  -d '{
    "project_idea": "Personal fitness coaching app",
    "answers": ["Mobile app", "Fitness enthusiasts", "Real-time tracking"]
  }'
```

**📁 Generated documentation automatically saved to `backend/temp/generated_docs/`**

## 📖 Detailed Documentation

For comprehensive documentation, API reference, agent details, and advanced usage:

**👉 [Complete Documentation - backend/README.md](backend/README.md)**

## 🧪 Testing

- **Interactive API Docs**: <http://localhost:8000/docs>
- **Postman Collection**: [backend/docs/postman.json](backend/docs/postman.json)
- **Health Check**: <http://localhost:8000/health>

## 🔗 Quick Links

- [Backend Setup & API Reference](backend/README.md)
- [Agent Documentation](backend/README.md#agents)
- [API Endpoints](backend/README.md#api-usage)
- [Postman Collection](backend/docs/postman.json)

---

_Transform project ideas into production-ready documentation with AI-powered agents._
