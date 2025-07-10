"""
Architecture Agent routes.
"""

from fastapi import APIRouter, HTTPException
from typing import Dict
from models.project_data import ProjectData
from services.workflow_orchestrator import WorkflowOrchestrator
from utils.logger import logger

router = APIRouter(prefix="/architecture", tags=["Architecture"])

# Initialize workflow orchestrator
orchestrator = WorkflowOrchestrator()


@router.post("/generate", response_model=Dict[str, str])
async def generate_architecture(project_data: ProjectData) -> Dict[str, str]:
    """
    Generate system architecture documentation.

    Args:
        project_data: Complete project data with questions and answers

    Returns:
        Generated architecture documentation
    """
    try:
        logger.info("Generating architecture documentation")
        result = await orchestrator.generate_architecture(project_data)
        return result
    except Exception as e:
        logger.error(f"Failed to generate architecture: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e
