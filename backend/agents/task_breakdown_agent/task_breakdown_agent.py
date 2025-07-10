"""
Task Breakdown Agent for DAVAI POC.
Generates implementation task breakdown documentation (TASK_BREAKDOWN.md).
"""

from pathlib import Path
from typing import Dict
from agents.base_agent import BaseAgent
from models.project_data import ProjectData


class TaskBreakdownAgent(BaseAgent[ProjectData, Dict[str, str]]):
    """Agent that generates task breakdown documentation."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prompt_file = Path(__file__).parent / "task_breakdown_agent_prompt.md"

    def get_system_prompt(self) -> str:
        """Load system prompt from file."""
        try:
            return self.prompt_file.read_text(encoding="utf-8")
        except FileNotFoundError:
            return self._get_default_system_prompt()

    def _get_default_system_prompt(self) -> str:
        """Fallback system prompt if file is not found."""
        return """You are an expert project manager and technical lead with extensive experience in breaking down complex software projects.

Generate a comprehensive TASK_BREAKDOWN.md file that provides a complete implementation roadmap for the project.

The document should include:
1. Project Phases Overview
2. Phase-wise task breakdown (Setup, Architecture, Development, Testing, Deployment, Maintenance)
3. Task details with priorities, estimates, and dependencies
4. Success criteria and deliverables

Return the complete markdown content for the TASK_BREAKDOWN.md file."""

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

Based on this project information, generate a comprehensive TASK_BREAKDOWN.md file that provides a complete implementation roadmap.

Focus on creating a document that includes:
- Detailed phase-wise task breakdown from setup to maintenance
- Specific, actionable tasks with clear deliverables
- Realistic time estimates and priority classifications
- Dependencies and prerequisites for each task
- Success criteria and acceptance criteria

The task breakdown should be practical, detailed enough for immediate implementation, and organized for efficient project execution."""

    async def process(self, input_data: ProjectData) -> Dict[str, str]:
        """Generate task breakdown documentation."""
        system_prompt = self.get_system_prompt()
        user_prompt = self.get_user_prompt(input_data)

        response = await self._invoke_llm(user_prompt, system_prompt)

        return {"TASK_BREAKDOWN.md": response.strip()}
