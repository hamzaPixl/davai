"""
Suggestions model for suggested answers.
"""

from typing import List
from pydantic import BaseModel, Field


class Suggestions(BaseModel):
    """Suggested answers to project clarifying questions."""

    suggested_answers: List[str] = Field(
        ...,
        description="List of suggested answers corresponding to the questions",
        min_items=1,
    )
    reasoning: str = Field(
        ..., description="Brief explanation of the reasoning behind these suggestions"
    )
