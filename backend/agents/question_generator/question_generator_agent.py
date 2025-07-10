"""
Question Generator Agent for DAVAI POC.
Generates clarifying questions based on project idea and required documentation.
"""

import json
from pathlib import Path
from typing import List
from agents.base_agent import BaseAgent
from models.project_idea import ProjectIdea
from models.questions import Questions


class QuestionGeneratorAgent(BaseAgent[ProjectIdea, Questions]):
    """Agent that generates clarifying questions for a project idea."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prompt_file = Path(__file__).parent / "question_generator_prompt.md"

    def get_system_prompt(self) -> str:
        """Load system prompt from file."""
        try:
            return self.prompt_file.read_text(encoding="utf-8")
        except FileNotFoundError:
            return self._get_default_system_prompt()

    def _get_default_system_prompt(self) -> str:
        """Fallback system prompt if file is not found."""
        return """You are an expert project analyst who helps gather comprehensive requirements for software projects.

Generate 8-10 specific clarifying questions to gather information needed for complete project documentation.

Return your response as a JSON object with this structure:
{
  "questions": [
    "Question 1 here?",
    "Question 2 here?",
    ...
  ]
}"""

    def get_user_prompt(self, input_data: ProjectIdea) -> str:
        return f"""Project Idea: "{input_data.description}"

Generate 8-10 specific clarifying questions that will help gather all the information needed to create comprehensive project documentation for this idea.

The documentation will include:
1. Project context and value proposition
2. System architecture design
3. Technology stack selection with rationale
4. Complete task breakdown and roadmap
5. Development rules and standards
6. Claude integration guide
7. Main README documentation

Focus on understanding:
- Who will use this and how
- What specific features are needed
- Technical constraints and requirements
- Business goals and success criteria
- Implementation considerations

Make each question targeted and specific to this project idea."""

    async def process(self, input_data: ProjectIdea) -> Questions:
        """Generate clarifying questions for the project idea."""
        system_prompt = self.get_system_prompt()
        user_prompt = self.get_user_prompt(input_data)

        response = await self._invoke_llm(user_prompt, system_prompt)

        try:
            response_data = json.loads(response)
            questions = response_data.get("questions", [])

            if not questions:
                raise ValueError("No questions generated")

            return Questions(questions=questions)

        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse LLM response as JSON: {e}")
        except Exception as e:
            raise ValueError(f"Failed to process questions: {e}")
