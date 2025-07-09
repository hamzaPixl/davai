# 🛠️ Technology Stack Selection Prompt

## Purpose

Generate a comprehensive technology stack recommendation document that analyzes project requirements and selects optimal technologies for databases, cloud providers, programming languages, frameworks, and infrastructure.

## Input Requirements

Before using this prompt, gather:

- **Project Overview**: Your completed context.md document
- **System Architecture**: Your completed architecture.md document
- **Performance Requirements**: Expected load, response times, data volume
- **Team Expertise**: Current team skills and learning capacity
- **Budget Constraints**: Development and operational budget limits
- **Compliance Requirements**: Security, privacy, or regulatory needs
- **Timeline**: Development timeline and launch requirements

## AI Prompt

```
Based on this project documentation, please create a comprehensive technology stack selection guide:

**PROJECT OVERVIEW**: [Paste or summarize your project context]

**SYSTEM ARCHITECTURE**: [Paste or summarize your architecture document]

**PERFORMANCE REQUIREMENTS**: [Expected users, data volume, response times, throughput]

**TEAM EXPERTISE**: [Current team skills - Python, TypeScript, cloud experience, etc.]

**BUDGET CONSTRAINTS**: [Development budget, operational costs, service limits]

**COMPLIANCE REQUIREMENTS**: [Security, privacy, GDPR, HIPAA, etc.]

**TIMELINE**: [Development timeline, launch date, MVP requirements]

Please create a technology stack selection document that includes:

1. **Stack Selection Methodology**: How decisions were made
2. **Programming Language Selection**:
   - **Backend**: Python vs TypeScript vs Go vs Rust
   - **Frontend**: React vs Vue vs Svelte vs vanilla JS
   - **Rationale**: Performance, team skills, ecosystem, AI library support
3. **Database Selection**:
   - **Primary Database**: PostgreSQL vs MongoDB vs MySQL vs SQLite
   - **Caching Layer**: Redis vs Memcached vs in-memory
   - **Vector Database**: Pinecone vs Weaviate vs Chroma (if AI embeddings needed)
   - **Rationale**: Data structure, scale, consistency, cost
4. **Cloud Provider Selection**:
   - **Primary Provider**: AWS vs Google Cloud vs Azure vs DigitalOcean
   - **AI Services**: OpenAI vs Anthropic vs Google AI vs AWS Bedrock
   - **Compute**: Functions vs Containers vs VMs
   - **Rationale**: Cost, AI service availability, team expertise, compliance
5. **Framework Selection**:
   - **Backend Framework**: FastAPI vs Django vs Express vs Next.js API
   - **Frontend Framework**: Next.js vs Vite+React vs SvelteKit
   - **Rationale**: Development speed, performance, ecosystem
6. **Infrastructure & DevOps**:
   - **Containerization**: Docker vs none
   - **Orchestration**: Kubernetes vs Cloud Run vs Lambda
   - **CI/CD**: GitHub Actions vs GitLab CI vs Jenkins
   - **Monitoring**: New Relic vs DataDog vs built-in cloud monitoring
7. **AI/ML Stack**:
   - **LLM Integration**: OpenAI API vs local models vs cloud providers
   - **ML Framework**: LangChain vs LlamaIndex vs custom
   - **Model Management**: MLflow vs Weights & Biases vs simple versioning
8. **Development Tools**:
   - **Package Management**: npm/pnpm vs pip/poetry vs cargo
   - **Testing**: Jest vs pytest vs built-in
   - **Type Safety**: TypeScript vs Python type hints vs none
9. **Security & Authentication**:
   - **Authentication**: Auth0 vs Supabase Auth vs custom JWT
   - **API Security**: Rate limiting, CORS, validation approaches
   - **Data Protection**: Encryption, secrets management
10. **Cost Analysis**:
    - **Development Costs**: Time to market, learning curve
    - **Operational Costs**: Hosting, AI services, databases
    - **Scaling Costs**: How costs change with growth
11. **Migration & Vendor Lock-in**:
    - **Portability**: How easy to change providers
    - **Exit Strategy**: Backup plans if costs become prohibitive
12. **Recommended Stack**:
    - **Final Technology Matrix**: Complete stack recommendation
    - **Alternative Stacks**: Options for different constraints
    - **Implementation Priority**: Which technologies to implement first

Format as a professional markdown document with:
- Clear comparison tables for each technology category
- Pros/cons analysis for major decisions
- Cost estimates where relevant
- Risk assessment for each choice
- Implementation recommendations

Make it detailed enough that the development team can confidently choose technologies and understand the trade-offs. Include specific version recommendations and setup guidance.
```

## Expected Output

- A complete tech-stack-selection.md file ready for your project repository
- Detailed technology recommendations with clear justifications
- Comparison matrices for different technology options
- Cost analysis and scaling considerations
- Risk assessment and mitigation strategies for technology choices

## Usage Tips

1. Be honest about team skill levels - don't choose technologies the team can't support
2. Consider both development speed and long-term maintenance
3. Factor in AI service costs early - they can be significant
4. Plan for scale but don't over-engineer for day one
5. Include specific version numbers and compatibility requirements
6. Consider community support and documentation quality
7. Plan for testing and monitoring from the beginning
8. Include backup options if primary choices don't work out
