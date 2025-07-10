"""
Questions model.
"""

from typing import List
from pydantic import BaseModel, Field


class Questions(BaseModel):
    """Generated clarifying questions."""

    questions: List[str] = Field(..., description="List of clarifying questions")
