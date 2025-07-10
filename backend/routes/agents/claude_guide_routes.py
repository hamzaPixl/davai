"""
Claude Guide Agent routes.
"""

from fastapi import APIRouter, HTTPException
from typing import Dict
from models.project_data import ProjectData
from services.workflow_orchestrator import WorkflowOrchestrator
from utils.logger import logger

router = APIRouter(prefix="/claude-guide", tags=["Claude Guide"])

# Initialize workflow orchestrator
orchestrator = WorkflowOrchestrator()


@router.post("/generate", response_model=Dict[str, str])
async def generate_claude_guide(project_data: ProjectData) -> Dict[str, str]:
    """
    Generate Claude AI integration guide documentation.

    Args:
        project_data: Complete project data with questions and answers

    Returns:
        Generated Claude guide documentation
    """
    try:
        logger.info("Generating Claude guide documentation")
        result = await orchestrator.generate_claude_guide(project_data)
        return result
    except Exception as e:
        logger.error(f"Failed to generate Claude guide: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e
