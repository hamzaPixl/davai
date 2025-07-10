# DAVAI Agent Prompt Analysis

## Overview

This document provides detailed analysis of each agent's prompt file, showing their specific instructions, output requirements, and dependencies.

## Agent Prompt Details

### 1. Question Generator Agent

**Prompt File**: `agents/question_generator/question_generator_prompt.md`

**Purpose**: Generate strategic clarifying questions to gather comprehensive project requirements.

**Key Instructions**:

- Analyze the project idea for gaps and ambiguities
- Generate 5-10 targeted questions covering different aspects
- Focus on technical requirements, user needs, and constraints
- Questions should be specific and actionable

**Example Questions Generated**:

- "What type of application are you building (web, mobile, desktop)?"
- "Who is your target audience and how many users do you expect?"
- "What are the core features you want to include in the MVP?"
- "Do you need real-time features like chat, notifications, or live updates?"
- "What are your performance, security, and scalability requirements?"

---

### 2. Context Agent

**Prompt File**: `agents/context_agent/context_agent_prompt.md`

**Purpose**: Create comprehensive project context and background documentation.

**Key Instructions**:

- Synthesize project idea with user answers
- Define problem statement and motivation
- Identify target audience and use cases
- Establish success criteria and goals

**Output Structure**:

```markdown
# Project Context

## Problem Statement

[Clear definition of the problem being solved]

## Target Audience

[Detailed user personas and stakeholders]

## Business Requirements

[High-level business goals and objectives]

## Success Criteria

[Measurable outcomes and KPIs]
```

---

### 3. Architecture Agent

**Prompt File**: `agents/architecture_agent/architecture_agent_prompt.md`

**Purpose**: Design system architecture and technical structure.

**Key Instructions**:

- Design scalable and maintainable architecture
- Consider technical requirements from user answers
- Define system components and their interactions
- Include data flow and integration patterns

**Output Structure**:

```markdown
# System Architecture

## Architecture Overview

[High-level system design]

## Core Components

[Detailed component breakdown]

## Data Flow

[How data moves through the system]

## Integration Patterns

[External system integrations]

## Scalability Considerations

[Performance and scaling strategies]
```

---

### 4. Tech Stack Agent

**Prompt File**: `agents/tech_stack_agent/tech_stack_agent_prompt.md`

**Purpose**: Recommend optimal technology stack and development tools.

**Key Instructions**:

- Analyze technical requirements and constraints
- Recommend appropriate technologies for each layer
- Consider team expertise and project timeline
- Include development, testing, and deployment tools

**Output Structure**:

```markdown
# Technology Stack Selection

## Frontend Technologies

[Framework, libraries, and tools]

## Backend Technologies

[Runtime, framework, and services]

## Database Solutions

[Primary and caching databases]

## DevOps and Deployment

[CI/CD, hosting, and monitoring tools]

## Development Tools

[IDEs, testing frameworks, and utilities]
```

---

### 5. Task Breakdown Agent

**Prompt File**: `agents/task_breakdown_agent/task_breakdown_agent_prompt.md`

**Purpose**: Create detailed project breakdown and task organization.

**Key Instructions**:

- Break down project into manageable phases and tasks
- Organize tasks by feature areas and dependencies
- Provide effort estimates and priority levels
- Define clear acceptance criteria for each task

**Output Structure**:

```markdown
# Task Breakdown

## Phase 1: Foundation

[Core infrastructure and setup tasks]

## Phase 2: Core Features

[Primary functionality implementation]

## Phase 3: Advanced Features

[Secondary and enhancement features]

## Phase 4: Polish and Launch

[Testing, optimization, and deployment]
```

---

### 6. Project Rules Agent

**Prompt File**: `agents/project_rules_agent/project_rules_agent_prompt.md`

**Purpose**: Establish coding standards, conventions, and project guidelines.

**Key Instructions**:

- Define coding standards based on chosen tech stack
- Establish file organization and naming conventions
- Create Git workflow and collaboration guidelines
- Include testing and quality assurance rules

**Output Structure**:

```markdown
# Project Rules and Guidelines

## Coding Standards

[Language-specific style guides]

## File Organization

[Directory structure and naming]

## Git Workflow

[Branch strategy and commit conventions]

## Testing Guidelines

[Testing requirements and frameworks]

## Code Review Process

[Review criteria and procedures]
```

---

### 7. Claude Guide Agent

**Prompt File**: `agents/claude_guide_agent/claude_guide_agent_prompt.md`

**Purpose**: Create AI-assisted development guide for working with Claude/LLMs.

**Key Instructions**:

- Provide project-specific AI collaboration strategies
- Include effective prompting techniques for the project
- Define AI-human workflow patterns
- Establish guidelines for code review with AI assistance

**Output Structure**:

```markdown
# AI Development Guide

## Working with Claude

[Project-specific AI collaboration strategies]

## Effective Prompting

[Techniques for better AI interactions]

## Code Review Workflow

[AI-assisted review processes]

## Best Practices

[Guidelines for productive AI collaboration]
```

---

### 8. README Agent

**Prompt File**: `agents/readme_agent/readme_agent_prompt.md`

**Purpose**: Generate comprehensive project README synthesizing all information.

**Key Instructions**:

- Synthesize information from all other agents
- Create clear project overview and setup instructions
- Include usage examples and contribution guidelines
- Reference detailed documentation files

**Dependencies**: Requires outputs from all other documentation agents

**Output Structure**:

```markdown
# Project Name

## Overview

[Project description and key features]

## Installation

[Setup and installation instructions]

## Usage

[Basic usage examples and guides]

## Architecture

[Link to detailed architecture documentation]

## Contributing

[Development guidelines and processes]

## Documentation

[Links to all generated documentation files]
```

---

## Agent Interaction Patterns

### Input Processing Pattern

All documentation agents follow a consistent input processing pattern:

1. **Parse ProjectData**: Extract project idea, questions, and answers
2. **Context Analysis**: Understand project requirements and constraints
3. **Domain-Specific Processing**: Apply agent-specific logic and templates
4. **Output Generation**: Create structured markdown documentation

### Prompt Engineering Principles

Each agent prompt follows these principles:

1. **Clear Role Definition**: Explicitly state the agent's role and expertise
2. **Structured Instructions**: Break down tasks into clear, actionable steps
3. **Output Format Specification**: Define exact markdown structure expected
4. **Context Integration**: Instructions for incorporating user answers
5. **Quality Guidelines**: Criteria for high-quality output generation

### Error Handling in Prompts

Each prompt includes instructions for handling edge cases:

- **Missing Information**: How to proceed with incomplete answers
- **Conflicting Requirements**: Strategies for resolving contradictions
- **Technical Constraints**: Fallback options for unsupported technologies
- **Scope Management**: Guidelines for keeping outputs focused and relevant

### Consistency Mechanisms

To ensure consistency across agents:

1. **Shared Terminology**: Common vocabulary and definitions
2. **Cross-References**: Instructions to reference other documentation
3. **Style Guidelines**: Consistent markdown formatting and structure
4. **Quality Standards**: Uniform criteria for completeness and clarity

## Prompt Optimization Strategies

### Performance Optimization

- **Token Efficiency**: Concise instructions that minimize token usage
- **Response Structure**: Clear formatting instructions for consistent parsing
- **Context Prioritization**: Focus on most relevant information first

### Quality Optimization

- **Example Inclusion**: Sample outputs to guide generation quality
- **Validation Criteria**: Specific quality checkpoints in prompts
- **Iterative Refinement**: Instructions for self-correction and improvement

### Maintainability

- **Modular Design**: Each prompt is self-contained and reusable
- **Version Control**: Clear documentation of prompt changes and rationale
- **Testing Support**: Instructions that facilitate automated testing
