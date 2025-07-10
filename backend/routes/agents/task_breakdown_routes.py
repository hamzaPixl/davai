"""
Task Breakdown Agent routes.
"""

from fastapi import APIRouter, HTTPException
from typing import Dict
from models.project_data import ProjectData
from models.agent_requests import TaskBreakdownAgentRequest
from services.workflow_orchestrator import WorkflowOrchestrator
from utils.logger import logger

router = APIRouter(prefix="/task-breakdown", tags=["Task Breakdown"])

# Initialize workflow orchestrator
orchestrator = WorkflowOrchestrator()


@router.post("/generate", response_model=Dict[str, str])
async def generate_task_breakdown(request: TaskBreakdownAgentRequest) -> Dict[str, str]:
    """
    Generate task breakdown documentation.

    Args:
        request: Task breakdown agent request with optional dependencies

    Returns:
        Generated task breakdown documentation
    """
    try:
        logger.info("Generating task breakdown documentation")

        # Create base project data
        project_data = ProjectData(
            project_idea=request.project_idea,
            questions=request.questions,
            answers=request.answers,
        )

        # If previous docs are provided, enhance the project data
        if request.context_docs or request.architecture_docs or request.tech_stack_docs:
            logger.info("Enhancing task breakdown generation with dependencies")
            previous_docs = {}
            if request.context_docs:
                previous_docs["context"] = request.context_docs
            if request.architecture_docs:
                previous_docs["architecture"] = request.architecture_docs
            if request.tech_stack_docs:
                previous_docs["tech_stack"] = request.tech_stack_docs

            enhanced_project_data = orchestrator.enhance_project_data_with_docs(
                project_data, previous_docs
            )
            result = await orchestrator.generate_task_breakdown(enhanced_project_data)
        else:
            logger.info("Generating task breakdown without dependencies")
            result = await orchestrator.generate_task_breakdown(project_data)

        return result
    except Exception as e:
        logger.error(f"Failed to generate task breakdown: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e
