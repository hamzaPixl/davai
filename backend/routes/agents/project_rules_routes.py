"""
Project Rules Agent routes.
"""

from fastapi import APIRouter, HTTPException
from typing import Dict
from models.project_data import ProjectData
from services.workflow_orchestrator import WorkflowOrchestrator
from utils.logger import logger

router = APIRouter(prefix="/project-rules", tags=["Project Rules"])

# Initialize workflow orchestrator
orchestrator = WorkflowOrchestrator()


@router.post("/generate", response_model=Dict[str, str])
async def generate_project_rules(project_data: ProjectData) -> Dict[str, str]:
    """
    Generate project rules and development standards documentation.

    Args:
        project_data: Complete project data with questions and answers

    Returns:
        Generated project rules documentation
    """
    try:
        logger.info("Generating project rules documentation")
        result = await orchestrator.generate_project_rules(project_data)
        return result
    except Exception as e:
        logger.error(f"Failed to generate project rules: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e
