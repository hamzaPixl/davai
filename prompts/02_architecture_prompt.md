# 🏗️ Architecture Design Prompt

## Purpose

Generate a comprehensive system architecture document that defines the technical structure, components, and data flow for an AI project.

## Input Requirements

Before using this prompt, gather:

- **Project Overview**: Your completed context.md document
- **Core Functionality**: Main features and user workflows
- **AI Components**: Which parts of the system use AI/ML
- **Integration Requirements**: External APIs, databases, or services
- **Scale Requirements**: Expected users, data volume, performance needs
- **Deployment Preferences**: Cloud providers, containerization, etc.

## AI Prompt

```
Based on this project overview, please create a comprehensive system architecture document:

**PROJECT OVERVIEW**: [Paste or summarize your project context]

**CORE FUNCTIONALITY**: [Describe the main user workflows and features]

**AI COMPONENTS**: [Specify which parts use AI - LLMs, computer vision, TTS, etc.]

**INTEGRATION REQUIREMENTS**: [External APIs, databases, third-party services needed]

**SCALE REQUIREMENTS**: [Expected users, data volume, performance requirements]

**DEPLOYMENT PREFERENCES**: [Cloud platform, containerization, infrastructure preferences]

Please create a system architecture document that includes:

1. **System Overview**: High-level architecture diagram description
2. **Component Architecture**: Detailed breakdown of system components
   - AI Agents/Services (if applicable)
   - Core Services
   - External Integrations
   - Data Storage
   - API Layer
3. **Data Flow**: How data moves through the system
4. **Technology Stack**: Recommended technologies for each layer
   - Frontend Framework
   - Backend Framework
   - AI/ML Services
   - Database
   - Infrastructure
5. **AI Model Strategy**: Which AI models to use for each component
6. **Folder Structure**: Detailed directory organization
7. **Integration Points**: How components communicate
8. **Scalability Considerations**: How the system can grow
9. **Security Architecture**: Authentication, authorization, data protection
10. **Deployment Architecture**: Infrastructure and deployment strategy

Format as a professional markdown document with:
- Clear section headers with emojis
- Tables for technology comparisons
- ASCII diagrams for data flow
- Detailed folder structure
- Component interaction descriptions

Make it detailed enough that a development team can start implementation immediately. Use the AI Video Generator architecture as a reference for quality and depth, but adapt to the new project's specific needs.
```

## Expected Output

- A complete architecture.md file ready for your project repository
- Detailed technical blueprint for implementation
- Clear component separation and interaction patterns
- Technology stack recommendations with justifications
- Folder structure that enables organized development

## Usage Tips

1. Include specific AI model preferences if you have them
2. Mention any existing systems that need integration
3. Specify performance requirements (response times, throughput)
4. Include any compliance or security requirements
5. Mention team size and technical expertise level
6. Specify budget constraints for AI services if relevant
