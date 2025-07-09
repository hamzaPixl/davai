# 🚀 AI Project Documentation Templates

This directory contains generic documentation templates and AI prompts for quickly defining and documenting new AI projects. Based on the successful architecture patterns from the AI Video Generator project.

## 📁 Structure

```
project-templates/
├── README.md                           # This file - template system guide
├── QUICK_START.md                      # Step-by-step workflow guide
├── COMPLETE_PROJECT_GENERATOR.md       # 🆕 One-shot documentation generator
├── prompts/                            # AI prompts for generating each doc type
│   ├── 01_project_overview_prompt.md   # Prompt for generating project overview
│   ├── 02_architecture_prompt.md       # Prompt for system architecture
│   ├── 03_task_breakdown_prompt.md     # Prompt for detailed task planning
│   ├── 04_project_rules_prompt.md      # Prompt for development standards
│   ├── 05_context_prompt.md            # Prompt for project context
│   ├── 06_claude_guide_prompt.md       # Prompt for Claude Code integration
│   └── 07_tech_stack_prompt.md         # Prompt for technology stack selection
└── templates/                          # Document templates with placeholders
    ├── architecture.md                 # System architecture template
    ├── context.md                      # Project context template
    ├── project-rules.md                # Development standards template
    ├── TASK_BREAKDOWN.md               # Task planning template
    ├── CLAUDE.md                       # Claude Code guide template
    ├── tech-stack-selection.md         # Technology stack analysis template
    └── README.md                       # Main project README template
```

## 🎯 How to Use

### 🚀 **Method 1: Complete Project Generator** (Recommended)

Use `COMPLETE_PROJECT_GENERATOR.md` for the fastest, most consistent approach:

1. **Provide your project idea** in 1-2 sentences
2. **Answer clarifying questions** from the AI (8-10 questions about requirements, constraints, etc.)
3. **Receive complete documentation** - all 7 files generated automatically and consistently

**Benefits**: Single session, no missing details, consistent across all documents, ready for immediate development.

### 📝 **Method 2: Step-by-Step Process** (Manual Control)

### Step 1: Project Definition

1. Take your project idea and use the prompts in `prompts/` directory in order:
   - `01_project_overview_prompt.md` → generates `context.md`
   - `02_architecture_prompt.md` → generates `architecture.md`
   - `07_tech_stack_prompt.md` → generates `tech-stack-selection.md`
   - `03_task_breakdown_prompt.md` → generates `TASK_BREAKDOWN.md`
   - `04_project_rules_prompt.md` → generates `project-rules.md`
   - `05_context_prompt.md` → generates refined `context.md`
   - `06_claude_guide_prompt.md` → generates `CLAUDE.md`
2. Feed each prompt to an AI assistant (Claude, GPT-4, etc.) with your project details
3. Generate documentation for each aspect of your project

### Step 2: Repository Creation

1. Create a new repository for your project
2. Use the generated documentation to populate the `docs/` directory
3. The comprehensive documentation will provide Claude Code with everything needed for implementation

### Step 3: Implementation

1. Share the repository with Claude Code
2. The comprehensive documentation will enable autonomous development
3. Follow the established patterns for modular, maintainable code

## 📋 Prompt Usage Instructions

Each prompt file contains:

- **Purpose**: What this document defines
- **Input Requirements**: What information you need to provide
- **AI Prompt**: The actual prompt to use with AI assistants
- **Output**: What you should expect to receive

### Example Workflow

```bash
# 1. Use architecture prompt with your project idea
"I want to build an AI-powered fitness coach that creates personalized workout plans..."

# 2. Generate architecture.md using the AI response
# 3. Repeat for all document types
# 4. Create repository with generated docs
# 5. Claude Code can now implement the full project
```

## 🔧 Customization

### Adding New Document Types

1. Create new prompt file in `prompts/`
2. Create corresponding template in `templates/`
3. Follow the established naming convention
4. Update this README with the new document type

### Modifying Templates

- Templates use `{{PLACEHOLDER}}` syntax for variable content
- Maintain consistent structure across all templates
- Include all sections that proved successful in the video generator project

## 🏗️ Template Philosophy

Based on lessons learned from the AI Video Generator project:

1. **Modular Architecture**: Clear separation of concerns
2. **Agent-Based Design**: Specialized components for specific tasks
3. **Type Safety**: Pydantic models for all data structures
4. **Comprehensive Testing**: Full test coverage requirements
5. **Clear Documentation**: Everything Claude Code needs to implement

## 🎯 Success Criteria

A well-documented project should enable:

- ✅ Autonomous implementation by Claude Code
- ✅ Clear understanding of system architecture
- ✅ Detailed task breakdown with dependencies
- ✅ Consistent development standards
- ✅ Comprehensive testing strategy
- ✅ Deployment and maintenance guidelines

## 🔄 Continuous Improvement

This template system should evolve based on:

- Feedback from implemented projects
- New architectural patterns discovered
- AI assistant capabilities improvements
- Industry best practices updates

---

_Start building your next AI project with confidence - comprehensive documentation leads to successful implementation._
