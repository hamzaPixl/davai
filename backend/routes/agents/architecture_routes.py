"""
Architecture Agent routes.
"""

from fastapi import APIRouter, HTTPException
from typing import Dict
from models.project_data import ProjectData
from models.agent_requests import ArchitectureAgentRequest
from services.workflow_orchestrator import WorkflowOrchestrator
from utils.logger import logger

router = APIRouter(prefix="/architecture", tags=["Architecture"])

# Initialize workflow orchestrator
orchestrator = WorkflowOrchestrator()


@router.post("/generate", response_model=Dict[str, str])
async def generate_architecture(request: ArchitectureAgentRequest) -> Dict[str, str]:
    """
    Generate system architecture documentation.

    Args:
        request: Architecture agent request with optional context dependencies

    Returns:
        Generated architecture documentation
    """
    try:
        logger.info("Generating architecture documentation")

        # Create base project data
        project_data = ProjectData(
            project_idea=request.project_idea,
            questions=request.questions,
            answers=request.answers,
        )

        # If context docs are provided, enhance the project data
        if request.context_docs:
            logger.info("Enhancing architecture generation with context dependencies")
            enhanced_project_data = orchestrator.enhance_project_data_with_context(
                project_data, request.context_docs
            )
            result = await orchestrator.generate_architecture(enhanced_project_data)
        else:
            logger.info("Generating architecture without context dependencies")
            result = await orchestrator.generate_architecture(project_data)

        return result
    except Exception as e:
        logger.error(f"Failed to generate architecture: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e
