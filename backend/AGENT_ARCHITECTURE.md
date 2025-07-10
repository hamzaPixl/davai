# DAVAI POC Agent Architecture Summary

## Complete Agent List

### 1. Question Generator Agent

- **Directory**: `agents/question_generator/`
- **Files**: `question_generator_agent.py`, `question_generator_prompt.md`
- **Input**: `ProjectIdea`
- **Output**: `Questions`
- **Purpose**: Generates 8-10 clarifying questions based on project idea
- **Workflow Step**: `generate_questions`
- **API Route**: `/generate-questions`

### 2. Context Agent

- **Directory**: `agents/context_agent/`
- **Files**: `context_agent.py`, `context_agent_prompt.md`
- **Input**: `ProjectData`
- **Output**: `Dict[str, str]` (context.md)
- **Purpose**: Generates project context and overview documentation
- **Workflow Step**: `generate_context`
- **API Route**: `/generate-context`

### 3. Architecture Agent

- **Directory**: `agents/architecture_agent/`
- **Files**: `architecture_agent.py`, `architecture_agent_prompt.md`
- **Input**: `ProjectData`
- **Output**: `Dict[str, str]` (architecture.md)
- **Purpose**: Generates system architecture documentation
- **Workflow Step**: `generate_architecture`
- **API Route**: `/generate-architecture`

### 4. Tech Stack Agent

- **Directory**: `agents/tech_stack_agent/`
- **Files**: `tech_stack_agent.py`, `tech_stack_agent_prompt.md`
- **Input**: `ProjectData`
- **Output**: `Dict[str, str]` (tech-stack-selection.md)
- **Purpose**: Generates technology stack selection documentation
- **Workflow Step**: `generate_tech_stack`
- **API Route**: `/generate-tech-stack`

### 5. Task Breakdown Agent

- **Directory**: `agents/task_breakdown_agent/`
- **Files**: `task_breakdown_agent.py`, `task_breakdown_agent_prompt.md`
- **Input**: `ProjectData`
- **Output**: `Dict[str, str]` (TASK_BREAKDOWN.md)
- **Purpose**: Generates implementation task breakdown documentation
- **Workflow Step**: `generate_task_breakdown`
- **API Route**: `/generate-task-breakdown`

### 6. Project Rules Agent

- **Directory**: `agents/project_rules_agent/`
- **Files**: `project_rules_agent.py`, `project_rules_agent_prompt.md`
- **Input**: `ProjectData`
- **Output**: `Dict[str, str]` (project-rules.md)
- **Purpose**: Generates development standards and project rules
- **Workflow Step**: `generate_project_rules`
- **API Route**: `/generate-project-rules`

### 7. Claude Guide Agent

- **Directory**: `agents/claude_guide_agent/`
- **Files**: `claude_guide_agent.py`, `claude_guide_agent_prompt.md`
- **Input**: `ProjectData`
- **Output**: `Dict[str, str]` (CLAUDE.md)
- **Purpose**: Generates Claude AI integration guide
- **Workflow Step**: `generate_claude_guide`
- **API Route**: `/generate-claude-guide`

### 8. README Agent

- **Directory**: `agents/readme_agent/`
- **Files**: `readme_agent.py`, `readme_agent_prompt.md`
- **Input**: `ProjectData`
- **Output**: `Dict[str, str]` (README.md)
- **Purpose**: Generates main project README documentation
- **Workflow Step**: `generate_readme`
- **API Route**: `/generate-readme`

## Workflow Overview

### Complete Workflow Steps

1. **Project Idea Input** → User provides initial project idea
2. **Question Generation** → Question Generator Agent creates clarifying questions
3. **Answer Collection** → User or AI provides answers to questions
4. **Parallel Documentation Generation**:
   - Context Agent → context.md
   - Architecture Agent → architecture.md
   - Tech Stack Agent → tech-stack-selection.md
   - Task Breakdown Agent → TASK_BREAKDOWN.md
   - Project Rules Agent → project-rules.md
   - Claude Guide Agent → CLAUDE.md
   - README Agent → README.md
5. **File Generation** → Create project directory with all documentation files
6. **Result Compilation** → Return comprehensive JSON with all step results

### API Endpoints

#### Individual Step Testing

- `POST /generate-questions` - Test question generation
- `POST /generate-context` - Test context generation
- `POST /generate-architecture` - Test architecture generation
- `POST /generate-tech-stack` - Test tech stack generation
- `POST /generate-task-breakdown` - Test task breakdown generation
- `POST /generate-project-rules` - Test project rules generation
- `POST /generate-claude-guide` - Test Claude guide generation
- `POST /generate-readme` - Test README generation

#### Complete Workflow

- `POST /complete-workflow` - Run entire workflow with all agents
- `POST /generate-project-files` - Generate actual file directory structure

### Input/Output Models

#### Core Models

- `ProjectIdea` - Initial project description
- `Questions` - Generated clarifying questions
- `ProjectData` - Project idea + questions + answers
- `Documentation` - Generated documentation files
- `WorkflowStep` - Individual step result with metadata
- `WorkflowResult` - Complete workflow execution result

#### Response Structure

```json
{
  "project_idea": "Original project description",
  "steps": [
    {
      "step_name": "generate_questions",
      "input_data": {...},
      "output_data": {...},
      "success": true,
      "error_message": null
    },
    // ... all steps
  ],
  "final_documentation": {
    "context.md": "...",
    "architecture.md": "...",
    "tech-stack-selection.md": "...",
    "TASK_BREAKDOWN.md": "...",
    "project-rules.md": "...",
    "CLAUDE.md": "...",
    "README.md": "..."
  },
  "success": true,
  "total_duration": 45.2
}
```

## Implementation Status

### ✅ Completed

- All agent directories and files created
- All prompt files with comprehensive documentation structures
- Base agent class with proper typing
- Core workflow models defined
- Initial workflow orchestrator structure

### 🔄 In Progress

- Update workflow orchestrator to use all agents
- Create comprehensive API routes for all steps
- Add file generation service
- Update Postman collection

### 📋 TODO

- Implement parallel agent execution
- Add error handling and validation
- Create project file directory generation
- Add comprehensive testing
- Performance optimization

## Architecture Benefits

### Modularity

- Each agent is independently testable
- Clear separation of concerns
- Easy to add/remove/modify agents

### Scalability

- Agents can run in parallel
- Independent scaling of different components
- Efficient resource utilization

### Maintainability

- Separate prompt files for easy updates
- Clear input/output contracts
- Comprehensive error handling

### Testability

- Each step can be tested individually
- Clear API endpoints for all operations
- Comprehensive workflow validation
