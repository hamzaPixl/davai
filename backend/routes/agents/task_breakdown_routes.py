"""
Task Breakdown Agent routes.
"""

from fastapi import APIRouter, HTTPException
from typing import Dict
from models.project_data import ProjectData
from services.workflow_orchestrator import WorkflowOrchestrator
from utils.logger import logger

router = APIRouter(prefix="/task-breakdown", tags=["Task Breakdown"])

# Initialize workflow orchestrator
orchestrator = WorkflowOrchestrator()


@router.post("/generate", response_model=Dict[str, str])
async def generate_task_breakdown(project_data: ProjectData) -> Dict[str, str]:
    """
    Generate task breakdown documentation.

    Args:
        project_data: Complete project data with questions and answers

    Returns:
        Generated task breakdown documentation
    """
    try:
        logger.info("Generating task breakdown documentation")
        result = await orchestrator.generate_task_breakdown(project_data)
        return result
    except Exception as e:
        logger.error(f"Failed to generate task breakdown: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e
