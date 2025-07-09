"""
Documentation Generator Agent for DAVAI POC.
Generates complete project documentation based on project idea and answers.
"""

import json
from typing import Dict, Any
from agents.base_agent import BaseAgent
from models.workflow_models import ProjectData, Documentation


class DocumentationGeneratorAgent(BaseAgent[ProjectData, Documentation]):
    """Agent that generates complete project documentation."""

    def get_system_prompt(self) -> str:
        return """You are an expert technical writer and software architect who creates comprehensive project documentation.

Your task is to generate ALL 7 required documentation files based on the project idea and user answers:

1. **context.md** - Project overview and value proposition
2. **architecture.md** - System architecture and component design
3. **tech-stack-selection.md** - Technology choices with detailed analysis
4. **TASK_BREAKDOWN.md** - Complete implementation roadmap
5. **project-rules.md** - Development standards and conventions
6. **CLAUDE.md** - Claude Code integration guide
7. **README.md** - Main project documentation

Each document should be:
- Complete and ready to use
- Professionally formatted with markdown
- Consistent across all files
- Detailed enough for autonomous development
- Based on proven patterns from successful projects

Return your response as a JSON object with this structure:
{
  "documents": {
    "context.md": "# Project Context\\n\\n...",
    "architecture.md": "# System Architecture\\n\\n...",
    "tech-stack-selection.md": "# Technology Stack\\n\\n...",
    "TASK_BREAKDOWN.md": "# Task Breakdown\\n\\n...",
    "project-rules.md": "# Project Rules\\n\\n...",
    "CLAUDE.md": "# Claude Integration\\n\\n...",
    "README.md": "# Project Name\\n\\n..."
  }
}"""

    def get_user_prompt(self, input_data: ProjectData) -> str:
        answers_text = "\n".join([f"Q: {q}\nA: {a}" for q, a in zip(input_data.questions, input_data.answers)])

        return f"""Project Idea: "{input_data.project_idea}"

User Answers to Clarifying Questions:
{answers_text}

Based on this project idea and the user's answers, generate ALL 7 complete documentation files that will serve as the foundation for this project.

Make sure each document is comprehensive and professionally written. The documentation should be ready for a development team to start implementation immediately.

Focus on creating:
1. Clear project context and value proposition
2. Well-architected system design
3. Justified technology choices
4. Detailed implementation roadmap
5. Development standards and best practices
6. Integration guidelines for Claude
7. Comprehensive README with setup instructions

Ensure all documents are consistent and reference the same project details."""

    async def process(self, input_data: ProjectData) -> Documentation:
        """Generate complete project documentation."""
        system_prompt = self.get_system_prompt()
        user_prompt = self.get_user_prompt(input_data)

        response = await self._invoke_llm(user_prompt, system_prompt)

        try:
            response_data = json.loads(response)
            documents = response_data.get("documents", {})

            required_docs = [
                "context.md",
                "architecture.md",
                "tech-stack-selection.md",
                "TASK_BREAKDOWN.md",
                "project-rules.md",
                "CLAUDE.md",
                "README.md"
            ]

            # Validate all required documents are present
            missing_docs = [doc for doc in required_docs if doc not in documents]
            if missing_docs:
                raise ValueError(f"Missing required documents: {missing_docs}")

            return Documentation(documents=documents)

        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse LLM response as JSON: {e}")
        except Exception as e:
            raise ValueError(f"Failed to process documentation: {e}")
