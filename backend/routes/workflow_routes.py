"""
Complete workflow routes.
"""

from fastapi import APIRouter, HTTPException
from typing import List
from models.project_idea import ProjectIdea
from models.questions import Questions
from models.workflow_result import WorkflowResult
from services.workflow_orchestrator import WorkflowOrchestrator
from utils.logger import logger

router = APIRouter(prefix="/workflow", tags=["Workflow"])

# Initialize workflow orchestrator
orchestrator = WorkflowOrchestrator()


@router.post("/complete", response_model=WorkflowResult)
async def complete_workflow(project_idea: str, answers: List[str]) -> WorkflowResult:
    """
    Run the complete workflow: generate questions then documentation.

    Args:
        project_idea: Brief description of the project
        answers: User answers to clarifying questions

    Returns:
        Complete workflow result with all documentation
    """
    try:
        logger.info(f"Running complete workflow for project: {project_idea[:100]}...")
        result = await orchestrator.run_complete_workflow(project_idea, answers)
        return result
    except Exception as e:
        logger.error(f"Complete workflow failed: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "message": "DAVAI POC Workflow API is running",
        "version": "0.1.0",
    }
