"""
Workflow Result model.
"""

from typing import List, Dict
from pydantic import BaseModel, Field
from models.workflow_step import WorkflowStep


class WorkflowResult(BaseModel):
    """Complete workflow execution result."""

    project_idea: str = Field(..., description="Original project idea")
    steps: List[WorkflowStep] = Field(..., description="List of workflow steps")
    final_documentation: Dict[str, str] = Field(
        None, description="Final generated documentation"
    )
    success: bool = Field(..., description="Whether the entire workflow succeeded")
    total_duration: float = Field(..., description="Total execution time in seconds")
