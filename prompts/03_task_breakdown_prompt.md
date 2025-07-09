# 📋 Task Breakdown Planning Prompt

## Purpose

Generate a comprehensive task breakdown document that organizes the entire project into manageable, prioritized tasks with clear dependencies and implementation steps.

## Input Requirements

Before using this prompt, gather:

- **Project Overview**: Your completed context.md document
- **System Architecture**: Your completed architecture.md document
- **Timeline Preferences**: Desired completion timeframe
- **Team Size**: How many developers will work on this
- **Priority Features**: Which features are most critical for MVP
- **Technical Constraints**: Any limitations or requirements

## AI Prompt

```
Based on this project documentation, please create a comprehensive task breakdown document:

**PROJECT OVERVIEW**: [Paste or summarize your project context]

**SYSTEM ARCHITECTURE**: [Paste or summarize your architecture document]

**TIMELINE PREFERENCES**: [Desired completion timeframe - weeks/months]

**TEAM SIZE**: [Number of developers and their skill levels]

**PRIORITY FEATURES**: [Which features are most critical for MVP]

**TECHNICAL CONSTRAINTS**: [Any limitations, budget constraints, or requirements]

Please create a detailed task breakdown document that includes:

1. **Task Status Legend**: Clear symbols for tracking progress
2. **Phase Organization**: Logical grouping of development phases
   - Phase 1: Infrastructure Setup
   - Phase 2: Core Components
   - Phase 3: AI Implementation
   - Phase 4: Integration & Testing
   - Phase 5: Deployment & Optimization
3. **Detailed Task Structure**: For each task include:
   - **Task ID**: Unique identifier (e.g., INFRA-001)
   - **Task Name**: Clear, actionable title
   - **Status**: Current completion status
   - **GitHub Issue Link**: Placeholder for issue tracking
   - **Prompt**: Specific prompt for AI assistant implementation
   - **Context**: Background and requirements
   - **Goal**: What success looks like
   - **Steps**: Detailed implementation steps
   - **Dependencies**: What must be completed first
   - **Estimated Time**: Hours or days to complete
4. **Dependency Graph**: Visual representation of task dependencies
5. **Critical Path**: Tasks that could delay the project
6. **Risk Assessment**: Potential blockers and mitigation strategies
7. **Testing Strategy**: How each component will be validated
8. **Milestone Definitions**: Major project checkpoints

Format as a professional markdown document with:
- Clear phase separation
- Numbered task hierarchy
- Emoji status indicators
- Detailed task descriptions
- Dependency relationships
- Time estimates

Make it comprehensive enough that a development team can work autonomously following this breakdown. Use the AI Video Generator task breakdown as a reference for structure and detail level.
```

## Expected Output

- A complete TASK_BREAKDOWN.md file ready for your project repository
- Organized development roadmap with clear priorities
- Actionable tasks with specific implementation guidance
- Dependency mapping for efficient work planning
- GitHub issue templates for project management

## Usage Tips

1. Be realistic about timeline and team capabilities
2. Include buffer time for unexpected challenges
3. Prioritize core functionality over nice-to-have features
4. Consider parallel development opportunities
5. Include specific testing requirements for each component
6. Plan for documentation and deployment tasks
7. Account for AI service integration complexity
