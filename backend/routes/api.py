"""
API routes for DAVAI POC.
"""

from fastapi import APIRouter, HTTPException
from typing import List
from models.workflow_models import Questions, Documentation, WorkflowResult
from services.workflow_orchestrator import WorkflowOrchestrator
from config.llm_config import LlmConfig
from services.llm_factory import get_default_config
from utils.logger import logger

router = APIRouter()

# Initialize workflow orchestrator
orchestrator = WorkflowOrchestrator()


@router.post("/generate-questions", response_model=Questions)
async def generate_questions(project_idea: str) -> Questions:
    """
    Generate clarifying questions for a project idea.

    Args:
        project_idea: Brief description of the project

    Returns:
        Generated clarifying questions
    """
    try:
        logger.info(f"Generating questions for project: {project_idea[:100]}...")
        questions = await orchestrator.generate_questions(project_idea)
        return questions
    except Exception as e:
        logger.error(f"Failed to generate questions: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/generate-documentation", response_model=Documentation)
async def generate_documentation(
    project_idea: str,
    questions: List[str],
    answers: List[str]
) -> Documentation:
    """
    Generate complete project documentation.

    Args:
        project_idea: Original project idea
        questions: List of clarifying questions
        answers: User answers to the questions

    Returns:
        Generated project documentation
    """
    try:
        logger.info(f"Generating documentation for project: {project_idea[:100]}...")

        if len(questions) != len(answers):
            raise HTTPException(
                status_code=400,
                detail="Number of questions and answers must match"
            )

        documentation = await orchestrator.generate_documentation(
            project_idea, questions, answers
        )
        return documentation
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to generate documentation: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/complete-workflow", response_model=WorkflowResult)
async def complete_workflow(
    project_idea: str,
    answers: List[str]
) -> WorkflowResult:
    """
    Run the complete workflow: generate questions then documentation.

    Note: This endpoint assumes you already have answers to the questions.
    For interactive use, call generate-questions first, then this endpoint.

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
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "message": "DAVAI POC API is running",
        "version": "0.1.0"
    }
