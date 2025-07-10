"""
Tech Stack Agent routes.
"""

from fastapi import APIRouter, HTTPException
from typing import Dict
from models.project_data import ProjectData
from models.agent_requests import TechStackAgentRequest
from services.workflow_orchestrator import WorkflowOrchestrator
from utils.logger import logger

router = APIRouter(prefix="/tech-stack", tags=["Tech Stack"])

# Initialize workflow orchestrator
orchestrator = WorkflowOrchestrator()


@router.post("/generate", response_model=Dict[str, str])
async def generate_tech_stack(request: TechStackAgentRequest) -> Dict[str, str]:
    """
    Generate technology stack selection documentation.

    Args:
        request: Tech stack agent request with optional context and architecture dependencies

    Returns:
        Generated tech stack documentation
    """
    try:
        logger.info("Generating tech stack documentation")

        # Create base project data
        project_data = ProjectData(
            project_idea=request.project_idea,
            questions=request.questions,
            answers=request.answers,
        )

        # If previous docs are provided, enhance the project data
        if request.context_docs or request.architecture_docs:
            logger.info("Enhancing tech stack generation with dependencies")
            previous_docs = {}
            if request.context_docs:
                previous_docs["context"] = request.context_docs
            if request.architecture_docs:
                previous_docs["architecture"] = request.architecture_docs

            enhanced_project_data = orchestrator.enhance_project_data_with_docs(
                project_data, previous_docs
            )
            result = await orchestrator.generate_tech_stack(enhanced_project_data)
        else:
            logger.info("Generating tech stack without dependencies")
            result = await orchestrator.generate_tech_stack(project_data)

        return result
    except Exception as e:
        logger.error(f"Failed to generate tech stack: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e
