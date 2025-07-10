"""
Project Idea model.
"""

from pydantic import BaseModel, Field


class ProjectIdea(BaseModel):
    """Initial project idea input."""

    description: str = Field(..., description="Brief description of the project idea")
