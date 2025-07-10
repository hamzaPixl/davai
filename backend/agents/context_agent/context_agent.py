"""
Context Agent for DAVAI POC.
Generates project context documentation (context.md).
"""

from pathlib import Path
from typing import Dict
from agents.base_agent import BaseAgent
from models.project_data import ProjectData


class ContextAgent(BaseAgent[ProjectData, Dict[str, str]]):
    """Agent that generates project context documentation."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prompt_file = Path(__file__).parent / "context_agent_prompt.md"

    def get_system_prompt(self) -> str:
        """Load system prompt from file."""
        try:
            return self.prompt_file.read_text(encoding="utf-8")
        except FileNotFoundError:
            return self._get_default_system_prompt()

    def _get_default_system_prompt(self) -> str:
        """Fallback system prompt if file is not found."""
        return """You are an expert technical writer specializing in creating comprehensive project context documentation.

Generate a complete context.md file that provides a comprehensive overview of the project, its purpose, value proposition, and strategic context.

The document should include:
1. Project Overview
2. Target Users
3. Business Context
4. Technical Context
5. Project Scope
6. Success Criteria

Return the complete markdown content for the context.md file."""

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

Based on this project information, generate a comprehensive context.md file that provides complete project context documentation.

Focus on creating a document that clearly explains:
- What the project does and why it matters
- Who will use it and how
- The business and technical context
- Project scope and success criteria

The document should be professional, detailed, and ready for use in a real development project."""

    async def process(self, input_data: ProjectData) -> Dict[str, str]:
        """Generate context documentation."""
        system_prompt = self.get_system_prompt()
        user_prompt = self.get_user_prompt(input_data)

        response = await self._invoke_llm(user_prompt, system_prompt)

        return {"context.md": response.strip()}
