# 📐 Development Standards Prompt

## Purpose

Generate a comprehensive project rules document that defines coding standards, architecture patterns, and development conventions for consistent implementation.

## Input Requirements

Before using this prompt, gather:

- **Project Overview**: Your completed context.md document
- **System Architecture**: Your completed architecture.md document
- **Technology Stack**: Specific frameworks and tools chosen
- **Team Preferences**: Coding style preferences and conventions
- **Quality Requirements**: Testing, documentation, and code quality standards

## AI Prompt

```
Based on this project documentation, please create a comprehensive development standards document:

**PROJECT OVERVIEW**: [Paste or summarize your project context]

**SYSTEM ARCHITECTURE**: [Paste or summarize your architecture document]

**TECHNOLOGY STACK**: [List specific frameworks, languages, and tools]

**TEAM PREFERENCES**: [Any specific coding styles or conventions preferred]

**QUALITY REQUIREMENTS**: [Testing coverage, documentation standards, etc.]

Please create a project rules document that includes:

1. **Project Overview**: Brief summary of architecture and goals
2. **Folder Structure Convention**: Detailed directory organization rules
   - Required directory structure
   - File naming conventions
   - Directory purpose definitions
   - Import/export patterns
3. **Architecture Standards**: Implementation patterns
   - Component/Service architecture
   - Interface contracts
   - Data model requirements
   - Error handling patterns
4. **Naming Conventions**: Consistent naming across the project
   - File names (snake_case, kebab-case, etc.)
   - Class names (PascalCase)
   - Function names (camelCase, snake_case)
   - Variable names
   - Constants
   - API endpoints
5. **Code Quality Standards**: Development best practices
   - Documentation requirements
   - Type safety requirements
   - Testing standards (unit, integration)
   - Code coverage requirements
   - Linting and formatting rules
6. **API Design Standards**: Consistent API patterns
   - Request/response models
   - Error handling
   - Validation patterns
   - Authentication/authorization
7. **Database Design Standards**: Data modeling conventions
   - Schema naming
   - Relationship patterns
   - Migration practices
8. **Testing Standards**: Comprehensive testing strategy
   - Test structure and organization
   - Mock and fixture patterns
   - Coverage requirements
   - Performance testing
9. **Documentation Standards**: Clear documentation requirements
   - Code documentation (docstrings, comments)
   - API documentation
   - README requirements
   - Changelog practices
10. **Deployment Standards**: Production readiness
    - Environment configuration
    - Monitoring and logging
    - Security practices
    - Performance optimization

Format as a professional markdown document with:
- Clear section headers with emojis
- Code examples for conventions
- Detailed rules with explanations
- "Must", "Should", "May" requirements
- Reference examples from similar projects

Make it comprehensive enough that any developer can follow the standards consistently. Use the AI Video Generator project rules as a reference for structure and depth.
```

## Expected Output

- A complete project-rules.md file ready for your project repository
- Comprehensive development standards for consistent implementation
- Clear coding conventions and architecture patterns
- Quality gates and testing requirements
- Documentation and deployment standards

## Usage Tips

1. Include specific examples for each convention
2. Define clear "must have" vs "nice to have" requirements
3. Consider team experience level when setting standards
4. Include tooling recommendations (linters, formatters)
5. Plan for code review processes and quality gates
6. Define clear error handling and logging patterns
7. Include security best practices relevant to your domain
