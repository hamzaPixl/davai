"""
Suggestion input model for question answers.
"""

from typing import List
from pydantic import BaseModel, Field


class SuggestionInput(BaseModel):
    """Input for generating suggested answers to project questions."""

    project_idea: str = Field(..., description="Original project idea")
    questions: List[str] = Field(
        ..., description="Clarifying questions to answer", min_items=1
    )
