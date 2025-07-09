# DAVAI POC Backend

A FastAPI-based backend for the DAVAI (Complete Project Generator) POC. This service uses AI agents to generate comprehensive project documentation through an interactive workflow.

## Features

- **AI-Powered Question Generation**: Automatically generates clarifying questions for any project idea
- **Complete Documentation Generation**: Creates 7 comprehensive documentation files
- **Multiple LLM Providers**: Supports OpenAI, Claude/Anthropic models
- **RESTful API**: Individual endpoints for each workflow step plus complete workflow
- **Structured Architecture**: Clean separation of agents, models, services, and configuration

## Quick Start

### 1. Install Dependencies

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .
```

### 2. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your API keys
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

### 3. Run the Server

You have several options to start the server:

#### Option 1: Direct uvicorn command
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

#### Option 2: Using the start script
```bash
./start.sh
```

#### Option 3: Using Python main
```bash
python main.py
```

#### Option 4: Using the CLI script
```bash
python run_server.py --help  # See all options
python run_server.py --port 8080 --log-level debug
```

The API will be available at:

- **API Documentation**: http://localhost:8000/docs
- **API Base URL**: http://localhost:8000/api

## API Endpoints

### Individual Steps

#### 1. Generate Questions

```http
POST /api/generate-questions
Content-Type: application/json

{
  "project_idea": "An AI-powered fitness coach that creates personalized workout plans"
}
```

#### 2. Generate Documentation

```http
POST /api/generate-documentation
Content-Type: application/json

{
  "project_idea": "An AI-powered fitness coach...",
  "questions": ["Who is your target audience?", "What equipment..."],
  "answers": ["Fitness enthusiasts aged 25-45", "Gym equipment and bodyweight..."]
}
```

### Complete Workflow

#### 3. Run Complete Workflow

```http
POST /api/complete-workflow
Content-Type: application/json

{
  "project_idea": "An AI-powered fitness coach that creates personalized workout plans",
  "answers": [
    "Fitness enthusiasts aged 25-45",
    "Gym equipment and bodyweight exercises",
    "Mobile app with web dashboard",
    "Up to 10,000 users initially",
    "Team of 3 developers",
    "$50,000 budget over 6 months",
    "React Native, Node.js, MongoDB preferred",
    "HIPAA compliance not required",
    "Integration with fitness wearables",
    "User engagement and workout completion rates"
  ]
}
```

## Generated Documentation

The system generates 7 comprehensive documentation files:

1. **context.md** - Project overview and value proposition
2. **architecture.md** - System architecture and component design
3. **tech-stack-selection.md** - Technology choices with detailed analysis
4. **TASK_BREAKDOWN.md** - Complete implementation roadmap
5. **project-rules.md** - Development standards and conventions
6. **CLAUDE.md** - Claude Code integration guide
7. **README.md** - Main project documentation
