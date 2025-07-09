"""
Question Generator Agent for DAVAI POC.
Generates clarifying questions based on a project idea.
"""

import json
from typing import List
from agents.base_agent import BaseAgent
from models.workflow_models import ProjectIdea, Questions


class QuestionGeneratorAgent(BaseAgent[ProjectIdea, Questions]):
    """Agent that generates clarifying questions for a project idea."""

    def get_system_prompt(self) -> str:
        return """You are an expert project analyst who helps gather comprehensive requirements for software projects.

Your task is to generate 8-10 specific, targeted questions that will help gather all the information needed to create complete project documentation.

The questions should cover:
- Target users and use cases
- Key features and functionality
- Performance and scale requirements
- Team size and technical expertise
- Budget constraints and timeline
- Technology preferences (if any)
- Security and compliance needs
- Integration requirements
- Success metrics and goals

Make each question specific and actionable. Avoid generic questions.

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
