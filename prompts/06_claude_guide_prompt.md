# 🤖 Claude Code Integration Guide Prompt

## Purpose

Generate a comprehensive CLAUDE.md file that provides Claude Code with all the context and guidelines needed for autonomous development of the project.

## Input Requirements

Before using this prompt, gather:

- **All Previous Documents**: context.md, architecture.md, task breakdown, project rules
- **Development Preferences**: Any specific coding patterns or tools preferred
- **Project Constraints**: Budget, timeline, or technical limitations
- **Integration Requirements**: External systems or APIs to connect with

## AI Prompt

```
Based on all the project documentation created, please generate a comprehensive Claude Code integration guide:

**PROJECT CONTEXT**: [Paste or summarize your context.md content]

**SYSTEM ARCHITECTURE**: [Paste or summarize your architecture.md content]

**DEVELOPMENT RULES**: [Paste or summarize your project-rules.md content]

**TASK BREAKDOWN**: [Reference your TASK_BREAKDOWN.md structure]

**DEVELOPMENT PREFERENCES**: [Any specific preferences for Claude to follow]

**PROJECT CONSTRAINTS**: [Budget, timeline, or technical limitations]

Please create a CLAUDE.md file that includes:

1. **Project Overview**: Brief summary of what the system does
2. **Architecture Summary**: High-level technical architecture
3. **Key Directory Structure**: Critical folders and their purposes
4. **Agent/Component Architecture**: How different parts interact
5. **Core Dependencies**: Essential libraries and frameworks
6. **Development Standards**: Critical coding conventions to follow
7. **File Protection Rules**: Any files/directories Claude should never modify
8. **MCP Integration Guidelines**: How to use MCP servers if available
9. **Git Workflow Process**: Branching, commits, and PR standards
10. **Implementation Priorities**: What to build first and why
11. **Testing Requirements**: How to validate implementations
12. **External Services Integration**: API keys, service setup
13. **Critical Considerations**: Important warnings or gotchas
14. **Success Criteria**: How to know if implementation is working

Format requirements:
- Use clear section headers with emojis
- Include specific code examples where helpful
- Provide actionable guidelines, not just descriptions
- Structure for easy scanning and reference
- Include both high-level strategy and specific implementation details

The document should enable Claude Code to:
- Understand the project completely from this one file
- Start development immediately without additional questions
- Follow consistent patterns and standards
- Avoid common pitfalls and mistakes
- Implement features autonomously with confidence

Use the AI Video Generator CLAUDE.md as a reference for comprehensiveness and structure, adapting the content to your specific project needs.
```

## Expected Output

- A complete CLAUDE.md file ready for your project repository
- Comprehensive integration guide for autonomous development
- Clear project context and technical requirements
- Specific guidelines for consistent implementation
- Protection rules for critical project files

## Usage Tips

1. Include specific examples of code patterns to follow
2. Mention any files or directories that should never be modified
3. Provide clear priorities for which features to implement first
4. Include debugging and troubleshooting guidance
5. Specify testing requirements and validation steps
6. Document any external service setup requirements
7. Include common pitfalls and how to avoid them
