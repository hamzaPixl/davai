"""
Tech Stack Agent routes.
"""

from fastapi import APIRouter, HTTPException
from typing import Dict
from models.project_data import ProjectData
from services.workflow_orchestrator import WorkflowOrchestrator
from utils.logger import logger

router = APIRouter(prefix="/tech-stack", tags=["Tech Stack"])

# Initialize workflow orchestrator
orchestrator = WorkflowOrchestrator()


@router.post("/generate", response_model=Dict[str, str])
async def generate_tech_stack(project_data: ProjectData) -> Dict[str, str]:
    """
    Generate technology stack selection documentation.

    Args:
        project_data: Complete project data with questions and answers

    Returns:
        Generated tech stack documentation
    """
    try:
        logger.info("Generating tech stack documentation")
        result = await orchestrator.generate_tech_stack(project_data)
        return result
    except Exception as e:
        logger.error(f"Failed to generate tech stack: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e
