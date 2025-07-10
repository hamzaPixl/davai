"""
Context Agent routes.
"""

from fastapi import APIRouter, HTTPException
from typing import Dict
from models.project_data import ProjectData
from services.workflow_orchestrator import WorkflowOrchestrator
from utils.logger import logger

router = APIRouter(prefix="/context", tags=["Context"])

# Initialize workflow orchestrator
orchestrator = WorkflowOrchestrator()


@router.post("/generate", response_model=Dict[str, str])
async def generate_context(project_data: ProjectData) -> Dict[str, str]:
    """
    Generate project context documentation.

    Args:
        project_data: Complete project data with questions and answers

    Returns:
        Generated context documentation
    """
    try:
        logger.info("Generating context documentation")
        result = await orchestrator.generate_context(project_data)
        return result
    except Exception as e:
        logger.error(f"Failed to generate context: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e
