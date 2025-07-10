# DAVAI Agent Routes with Dependencies

## Overview

The DAVAI agent routes have been updated to support the dependency chain architecture. Each route can now accept optional previous agent outputs to enhance the documentation generation quality.

## Request Models

### Base Agent Request

All agents inherit from the base request structure:

```json
{
  "project_idea": "A social media platform for developers",
  "questions": [
    "What type of application are you building?",
    "Who is your target audience?"
  ],
  "answers": [
    "Web application with mobile responsive design",
    "Individual developers and small teams"
  ]
}
```

### Enhanced Agent Requests

#### Context Agent (`POST /api/context/generate`)

**No dependencies** - Uses base request only:

```json
{
  "project_idea": "A social media platform for developers",
  "questions": ["What type of application?", "Who is your target audience?"],
  "answers": ["Web application", "Individual developers"]
}
```

#### Architecture Agent (`POST /api/architecture/generate`)

**Optional dependency**: Context documentation

```json
{
  "project_idea": "A social media platform for developers",
  "questions": ["What type of application?", "Who is your target audience?"],
  "answers": ["Web application", "Individual developers"],
  "context_docs": {
    "context.md": "# Project Context\n\n## Problem Statement\nDevelopers need a platform..."
  }
}
```

#### Tech Stack Agent (`POST /api/tech-stack/generate`)

**Optional dependencies**: Context + Architecture documentation

```json
{
  "project_idea": "A social media platform for developers",
  "questions": ["What type of application?", "Who is your target audience?"],
  "answers": ["Web application", "Individual developers"],
  "context_docs": {
    "context.md": "# Project Context\n..."
  },
  "architecture_docs": {
    "architecture.md": "# System Architecture\n..."
  }
}
```

#### Task Breakdown Agent (`POST /api/task-breakdown/generate`)

**Optional dependencies**: Context + Architecture + Tech Stack documentation

```json
{
  "project_idea": "A social media platform for developers",
  "questions": ["What type of application?", "Who is your target audience?"],
  "answers": ["Web application", "Individual developers"],
  "context_docs": {
    "context.md": "# Project Context\n..."
  },
  "architecture_docs": {
    "architecture.md": "# System Architecture\n..."
  },
  "tech_stack_docs": {
    "tech-stack-selection.md": "# Technology Stack\n..."
  }
}
```

#### Project Rules Agent (`POST /api/project-rules/generate`)

**Optional dependencies**: All previous documentation

```json
{
  "project_idea": "A social media platform for developers",
  "questions": ["What type of application?", "Who is your target audience?"],
  "answers": ["Web application", "Individual developers"],
  "previous_docs": {
    "context": {
      "context.md": "# Project Context\n..."
    },
    "architecture": {
      "architecture.md": "# System Architecture\n..."
    },
    "tech_stack": {
      "tech-stack-selection.md": "# Technology Stack\n..."
    },
    "task_breakdown": {
      "TASK_BREAKDOWN.md": "# Task Breakdown\n..."
    }
  }
}
```

#### Claude Guide Agent (`POST /api/claude-guide/generate`)

**Optional dependencies**: All previous documentation (same structure as Project Rules)

#### README Agent (`POST /api/readme/generate`)

**Optional dependencies**: All previous documentation (same structure as Project Rules)

## Usage Examples

### Testing Individual Agents

#### 1. Test Context Agent (No Dependencies)

```bash
curl -X POST "http://localhost:8000/api/context/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "project_idea": "A social media platform for developers",
    "questions": ["What type of application are you building?"],
    "answers": ["Web application with real-time features"]
  }'
```

#### 2. Test Architecture Agent (With Context)

```bash
curl -X POST "http://localhost:8000/api/architecture/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "project_idea": "A social media platform for developers",
    "questions": ["What type of application are you building?"],
    "answers": ["Web application with real-time features"],
    "context_docs": {
      "context.md": "# Project Context\n\n## Problem Statement\nDevelopers need a platform for sharing code and collaborating.\n\n## Target Audience\nIndividual developers and small development teams."
    }
  }'
```

#### 3. Test Tech Stack Agent (With Context + Architecture)

```bash
curl -X POST "http://localhost:8000/api/tech-stack/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "project_idea": "A social media platform for developers",
    "questions": ["What type of application are you building?"],
    "answers": ["Web application with real-time features"],
    "context_docs": {
      "context.md": "# Project Context\n..."
    },
    "architecture_docs": {
      "architecture.md": "# System Architecture\n\n## Overview\nMicroservices architecture with React frontend and Node.js backend.\n\n## Real-time Communication\nWebSocket integration for live collaboration."
    }
  }'
```

### Manual Dependency Chain Testing

You can manually test the dependency chain by:

1. **Generate Context**: Call context agent first
2. **Generate Architecture**: Use context output as input
3. **Generate Tech Stack**: Use context + architecture outputs as input
4. **Continue Chain**: Build up dependencies for subsequent agents

### Backward Compatibility

All routes maintain backward compatibility:

- If no dependency docs are provided, agents work with base project data only
- This allows testing individual agents without the full dependency chain
- Existing API clients continue to work without modification

## Benefits of Enhanced Routes

### 1. Testing Flexibility

- **Individual Testing**: Test each agent in isolation
- **Dependency Testing**: Test with specific dependency combinations
- **Chain Validation**: Verify that outputs improve with dependencies

### 2. Development Workflow

- **Iterative Development**: Regenerate specific agents with updated dependencies
- **Quality Comparison**: Compare outputs with and without dependencies
- **Debugging**: Isolate issues to specific agents or dependency combinations

### 3. Integration Options

- **Full Workflow**: Use `POST /api/workflow/complete` for end-to-end generation
- **Partial Chains**: Use individual routes for specific documentation types
- **Custom Workflows**: Build custom dependency chains for specific use cases

## Response Format

All agent routes return the same format:

```json
{
  "filename.md": "# Document Title\n\nDocument content..."
}
```

For example, Architecture Agent returns:

```json
{
  "architecture.md": "# System Architecture\n\n## Overview\n..."
}
```

## Error Handling

Enhanced error responses include dependency information:

```json
{
  "detail": "Failed to enhance project data with dependencies",
  "error": "Invalid context documentation format"
}
```

## Performance Considerations

### With Dependencies

- **Higher Quality**: Better informed decisions and consistent outputs
- **Longer Execution**: Additional processing time for dependency integration
- **Larger Payloads**: Requests include previous documentation

### Without Dependencies

- **Faster Execution**: No dependency processing overhead
- **Smaller Payloads**: Basic project data only
- **Independent Operation**: No dependency on previous agent outputs

## Migration Guide

### For Existing API Clients

No changes required - all routes maintain backward compatibility with the original `ProjectData` format.

### For New Implementations

Use the enhanced request models to take advantage of the dependency chain:

1. Start with Context Agent (no dependencies)
2. Use Context output for Architecture Agent
3. Use Context + Architecture for Tech Stack Agent
4. Continue building dependency chain
5. Use all previous outputs for final agents (Rules, Guide, README)

This approach ensures maximum quality and consistency in generated documentation.
