"""
Workflow Step model.
"""

from typing import Dict
from pydantic import BaseModel, Field


class WorkflowStep(BaseModel):
    """Individual workflow step result."""

    step_name: str = Field(..., description="Name of the workflow step")
    input_data: Dict = Field(..., description="Input data for the step")
    output_data: Dict = Field(..., description="Output data from the step")
    success: bool = Field(..., description="Whether the step completed successfully")
    error_message: str = Field(None, description="Error message if step failed")
