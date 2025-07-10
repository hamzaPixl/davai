"""
Question Generator Agent routes.
"""

from fastapi import APIRouter, HTTPException
from models.project_idea import ProjectIdea
from models.questions import Questions
from services.workflow_orchestrator import WorkflowOrchestrator
from utils.logger import logger

router = APIRouter(prefix="/question-generator", tags=["Question Generator"])

# Initialize workflow orchestrator
orchestrator = WorkflowOrchestrator()


@router.post("/generate", response_model=Questions)
async def generate_questions(project_idea: ProjectIdea) -> Questions:
    """
    Generate clarifying questions for a project idea.

    Args:
        project_idea: Project idea input

    Returns:
        Generated clarifying questions
    """
    try:
        logger.info(
            f"Generating questions for project: {project_idea.description[:100]}..."
        )
        questions = await orchestrator.generate_questions(project_idea.description)
        return questions
    except Exception as e:
        logger.error(f"Failed to generate questions: {e}")
        raise HTTPException(status_code=500, detail=str(e))
