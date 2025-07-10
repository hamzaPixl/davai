"""
README Agent routes.
"""

from fastapi import APIRouter, HTTPException
from typing import Dict
from models.project_data import ProjectData
from services.workflow_orchestrator import WorkflowOrchestrator
from utils.logger import logger

router = APIRouter(prefix="/readme", tags=["README"])

# Initialize workflow orchestrator
orchestrator = WorkflowOrchestrator()


@router.post("/generate", response_model=Dict[str, str])
async def generate_readme(project_data: ProjectData) -> Dict[str, str]:
    """
    Generate README documentation.

    Args:
        project_data: Complete project data with questions and answers

    Returns:
        Generated README documentation
    """
    try:
        logger.info("Generating README documentation")
        result = await orchestrator.generate_readme(project_data)
        return result
    except Exception as e:
        logger.error(f"Failed to generate README: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e
