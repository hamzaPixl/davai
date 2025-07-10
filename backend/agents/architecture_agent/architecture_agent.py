"""
Architecture Agent for DAVAI POC.
Generates system architecture documentation (architecture.md).
"""

from pathlib import Path
from typing import Dict
from agents.base_agent import BaseAgent
from models.project_data import ProjectData


class ArchitectureAgent(BaseAgent[ProjectData, Dict[str, str]]):
    """Agent that generates system architecture documentation."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prompt_file = Path(__file__).parent / "architecture_agent_prompt.md"

    def get_system_prompt(self) -> str:
        """Load system prompt from file."""
        try:
            return self.prompt_file.read_text(encoding="utf-8")
        except FileNotFoundError:
            return self._get_default_system_prompt()

    def _get_default_system_prompt(self) -> str:
        """Fallback system prompt if file is not found."""
        return """You are a senior software architect with expertise in designing scalable, maintainable systems.

Generate a comprehensive architecture.md file that defines the complete system architecture for the project.

The document should include:
1. System Overview
2. Component Architecture
3. Data Architecture
4. Security Architecture
5. Scalability & Performance
6. Deployment Architecture
7. Integration Architecture

Return the complete markdown content for the architecture.md file."""

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

Based on this project information, generate a comprehensive architecture.md file that defines the complete system architecture.

Focus on creating a document that includes:
- Detailed system design and component architecture
- Technology choices with clear rationale
- Data flow and storage strategies
- Security and scalability considerations
- Deployment and integration patterns

The architecture should be practical, scalable, and ready for implementation by a development team."""

    async def process(self, input_data: ProjectData) -> Dict[str, str]:
        """Generate architecture documentation."""
        system_prompt = self.get_system_prompt()
        user_prompt = self.get_user_prompt(input_data)

        response = await self._invoke_llm(user_prompt, system_prompt)

        return {"architecture.md": response.strip()}
