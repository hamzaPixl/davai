"""
Project Rules Agent for DAVAI POC.
Generates development standards and project rules documentation (project-rules.md).
"""

from pathlib import Path
from typing import Dict
from agents.base_agent import BaseAgent
from models.project_data import ProjectData


class ProjectRulesAgent(BaseAgent[ProjectData, Dict[str, str]]):
    """Agent that generates project rules and development standards documentation."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prompt_file = Path(__file__).parent / "project_rules_agent_prompt.md"

    def get_system_prompt(self) -> str:
        """Load system prompt from file."""
        try:
            return self.prompt_file.read_text(encoding="utf-8")
        except FileNotFoundError:
            return self._get_default_system_prompt()

    def _get_default_system_prompt(self) -> str:
        """Fallback system prompt if file is not found."""
        return """You are an expert software development lead with extensive experience in establishing development standards and project governance.

Generate a comprehensive project-rules.md file that defines development standards, conventions, and best practices for the project.

The document should include:
1. Development Standards
2. Git Workflow & Version Control
3. Code Quality Standards
4. Technology-Specific Guidelines
5. Team Collaboration Rules
6. Deployment & Operations
7. Quality Assurance

Return the complete markdown content for the project-rules.md file."""

    def get_user_prompt(self, input_data: ProjectData) -> str:
        """Create user prompt with project data."""
        qa_pairs = "\n".join(
            [
                f"Q: {q}\nA: {a}\n"
                for q, a in zip(input_data.questions, input_data.answers)
            ]
        )

        return f"""Project Idea: "{input_data.project_idea}"

Clarifying Questions and Answers:
{qa_pairs}

Based on this project information, generate a comprehensive project-rules.md file that defines development standards and best practices.

Focus on creating a document that includes:
- Clear coding standards and conventions
- Git workflow and version control practices
- Code quality and testing requirements
- Team collaboration and communication rules
- Deployment and operational procedures

The rules should be practical, enforceable, and appropriate for the project's technology stack and team structure."""

    async def process(self, input_data: ProjectData) -> Dict[str, str]:
        """Generate project rules documentation."""
        system_prompt = self.get_system_prompt()
        user_prompt = self.get_user_prompt(input_data)

        response = await self._invoke_llm(user_prompt, system_prompt)

        return {"project-rules.md": response.strip()}
