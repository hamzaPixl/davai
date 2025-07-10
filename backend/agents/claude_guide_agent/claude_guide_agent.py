"""
Claude Guide Agent for DAVAI POC.
Generates Claude AI integration guide documentation (CLAUDE.md).
"""

from pathlib import Path
from typing import Dict
from agents.base_agent import BaseAgent
from models.project_data import ProjectData


class ClaudeGuideAgent(BaseAgent[ProjectData, Dict[str, str]]):
    """Agent that generates Claude AI integration guide documentation."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prompt_file = Path(__file__).parent / "claude_guide_agent_prompt.md"

    def get_system_prompt(self) -> str:
        """Load system prompt from file."""
        try:
            return self.prompt_file.read_text(encoding="utf-8")
        except FileNotFoundError:
            return self._get_default_system_prompt()

    def _get_default_system_prompt(self) -> str:
        """Fallback system prompt if file is not found."""
        return """You are an expert AI integration specialist with deep knowledge of Claude AI capabilities and AI-assisted development.

Generate a comprehensive CLAUDE.md file that provides guidance for integrating Claude AI into the development workflow.

The document should include:
1. Claude Integration Overview
2. Development Workflow with Claude
3. Prompt Engineering Guidelines
4. Project-Specific Claude Usage
5. Code Generation Best Practices
6. Collaboration Patterns
7. Advanced Integration Techniques

Return the complete markdown content for the CLAUDE.md file."""

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

Based on this project information, generate a comprehensive CLAUDE.md file that provides guidance for integrating Claude AI into the development workflow.

Focus on creating a document that includes:
- Practical AI-assisted development workflows
- Project-specific prompt engineering guidance
- Code generation and review best practices
- Team collaboration patterns with AI assistance
- Advanced integration techniques and automation

The guide should be tailored to this specific project's technology stack and development approach."""

    async def process(self, input_data: ProjectData) -> Dict[str, str]:
        """Generate Claude guide documentation."""
        system_prompt = self.get_system_prompt()
        user_prompt = self.get_user_prompt(input_data)

        response = await self._invoke_llm(user_prompt, system_prompt)

        return {"CLAUDE.md": response.strip()}
