"""
Data models for DAVAI POC workflow.
"""

from typing import List, Dict
from pydantic import BaseModel, Field


class ProjectIdea(BaseModel):
    """Initial project idea input."""
    description: str = Field(..., description="Brief description of the project idea")


class Questions(BaseModel):
    """Generated clarifying questions."""
    questions: List[str] = Field(..., description="List of clarifying questions")


class ProjectData(BaseModel):
    """Complete project data including idea, questions, and answers."""
    project_idea: str = Field(..., description="Original project idea")
    questions: List[str] = Field(..., description="Clarifying questions")
    answers: List[str] = Field(..., description="User answers to questions")


class Documentation(BaseModel):
    """Generated project documentation."""
    documents: Dict[str, str] = Field(..., description="Generated documentation files")


class WorkflowStep(BaseModel):
    """Individual workflow step result."""
    step_name: str = Field(..., description="Name of the workflow step")
    input_data: Dict = Field(..., description="Input data for the step")
    output_data: Dict = Field(..., description="Output data from the step")
    success: bool = Field(..., description="Whether the step completed successfully")
    error_message: str = Field(None, description="Error message if step failed")


class WorkflowResult(BaseModel):
    """Complete workflow execution result."""
    project_idea: str = Field(..., description="Original project idea")
    steps: List[WorkflowStep] = Field(..., description="List of workflow steps")
    final_documentation: Dict[str, str] = Field(None, description="Final generated documentation")
    success: bool = Field(..., description="Whether the entire workflow succeeded")
    total_duration: float = Field(..., description="Total execution time in seconds")
