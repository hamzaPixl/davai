"""
Tech Stack Agent for DAVAI POC.
Generates technology stack selection documentation (tech-stack-selection.md).
"""

from pathlib import Path
from typing import Dict
from agents.base_agent import BaseAgent
from models.project_data import ProjectData


class TechStackAgent(BaseAgent[ProjectData, Dict[str, str]]):
    """Agent that generates technology stack selection documentation."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prompt_file = Path(__file__).parent / "tech_stack_agent_prompt.md"

    def get_system_prompt(self) -> str:
        """Load system prompt from file."""
        try:
            return self.prompt_file.read_text(encoding="utf-8")
        except FileNotFoundError:
            return self._get_default_system_prompt()

    def _get_default_system_prompt(self) -> str:
        """Fallback system prompt if file is not found."""
        return """You are a senior technology consultant with deep expertise in modern software development technologies.

Generate a comprehensive tech-stack-selection.md file that provides detailed technology recommendations for the project.

The document should include:
1. Technology Overview
2. Frontend Technologies
3. Backend Technologies
4. Database & Storage
5. AI/ML Technologies
6. DevOps & Infrastructure
7. Third-Party Integrations

For each technology choice, include justification, benefits, trade-offs, and implementation notes.

Return the complete markdown content for the tech-stack-selection.md file."""

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

Based on this project information, generate a comprehensive tech-stack-selection.md file that provides detailed technology recommendations.

Focus on creating a document that includes:
- Specific technology choices for frontend, backend, database, and infrastructure
- Clear rationale for each technology selection
- Consideration of project requirements, scale, and team capabilities
- Modern, proven technologies that align with best practices
- Detailed implementation guidance and best practices

The technology stack should be practical, scalable, and appropriate for the project's specific requirements and constraints."""

    async def process(self, input_data: ProjectData) -> Dict[str, str]:
        """Generate tech stack selection documentation."""
        system_prompt = self.get_system_prompt()
        user_prompt = self.get_user_prompt(input_data)

        response = await self._invoke_llm(user_prompt, system_prompt)

        return {"tech-stack-selection.md": response.strip()}
