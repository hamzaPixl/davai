"""
Project Data model.
"""

from typing import List
from pydantic import BaseModel, Field


class ProjectData(BaseModel):
    """Complete project data including idea, questions, and answers."""

    project_idea: str = Field(..., description="Original project idea")
    questions: List[str] = Field(..., description="Clarifying questions")
    answers: List[str] = Field(..., description="User answers to questions")
