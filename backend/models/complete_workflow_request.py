"""
Complete Workflow Request model.
"""

from typing import List
from pydantic import BaseModel, Field


class CompleteWorkflowRequest(BaseModel):
    """Request model for complete workflow execution."""

    project_idea: str = Field(..., description="Brief description of the project idea")
    answers: List[str] = Field(..., description="User answers to clarifying questions")
