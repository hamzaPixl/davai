"""
Suggestion Agent for DAVAI POC.
Generates suggested answers to clarifying questions based on project idea.
"""

import json
from typing import Dict
from pathlib import Path

from agents.base_agent import BaseAgent
from models.suggestion_input import SuggestionInput
from models.suggestions import Suggestions
from utils.logger import logger


class SuggestionAgent(BaseAgent[SuggestionInput, Suggestions]):
    """
    Agent that generates suggested answers to clarifying questions.

    This agent analyzes the project idea and questions, then provides
    intelligent suggested answers that users can accept, modify, or replace.
    """

    def get_system_prompt(self) -> str:
        """Load system prompt from file."""
        prompt_file = Path(__file__).parent / "suggestion_agent_prompt.md"

        try:
            with open(prompt_file, "r", encoding="utf-8") as f:
                return f.read().strip()
        except FileNotFoundError:
            logger.error(f"Prompt file not found: {prompt_file}")
            return self._get_fallback_prompt()

    def _get_fallback_prompt(self) -> str:
        """Fallback prompt if file is not found."""
        return """You are an expert project advisor. Based on the project idea and questions,
        provide suggested answers in JSON format with 'suggested_answers' array and 'reasoning' string."""

    def get_user_prompt(self, input_data: SuggestionInput) -> str:
        """Generate user prompt from suggestion input."""

        # Format questions
        questions_text = "\n".join(
            [f"{i+1}. {q}" for i, q in enumerate(input_data.questions)]
        )

        prompt = f"""
## Project Idea
{input_data.project_idea}

## Questions to Answer
{questions_text}

## Request
Based on the project idea above, provide intelligent suggested answers to each of the questions.
The answers should be specific, practical, and well-reasoned for this particular project.

Please respond with a JSON object containing:
- suggested_answers: Array of suggested answers (one for each question, in order)
- reasoning: Brief explanation of why these suggestions make sense for this project

Focus on providing helpful, actionable answers that a project owner would likely choose
while considering best practices, common patterns, and the specific context of the project idea.
"""

        return prompt.strip()

    async def process(self, input_data: SuggestionInput) -> Suggestions:
        """Generate suggested answers based on project idea and questions."""
        try:
            logger.info(
                f"Generating suggested answers for project: {input_data.project_idea[:50]}..."
            )

            system_prompt = self.get_system_prompt()
            user_prompt = self.get_user_prompt(input_data)

            # Get response from LLM
            response = await self._invoke_llm(user_prompt, system_prompt)

            # Parse JSON response
            logger.debug(f"Raw LLM response: {response}")

            # Clean response if needed
            response_clean = response.strip()
            if response_clean.startswith("```json"):
                response_clean = response_clean[7:]
            if response_clean.endswith("```"):
                response_clean = response_clean[:-3]
            response_clean = response_clean.strip()

            try:
                response_data = json.loads(response_clean)

                # Validate required fields
                if "suggested_answers" not in response_data:
                    raise ValueError("Response missing 'suggested_answers' field")
                if "reasoning" not in response_data:
                    raise ValueError("Response missing 'reasoning' field")

                suggestions = Suggestions(
                    suggested_answers=response_data["suggested_answers"],
                    reasoning=response_data["reasoning"],
                )

                logger.info(
                    f"Generated {len(suggestions.suggested_answers)} suggested answers"
                )
                return suggestions

            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse JSON response: {e}")
                logger.error(f"Response content: {response_clean}")
                raise ValueError(f"Invalid JSON response from LLM: {e}") from e

        except Exception as e:
            logger.error(f"Failed to generate suggested answers: {e}")
            raise ValueError(f"Failed to process suggested answers: {e}") from e
