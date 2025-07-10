"""
Suggestion Agent routes.
"""

from fastapi import APIRouter, HTTPException
from models.suggestion_input import SuggestionInput
from models.suggestions import Suggestions
from services.workflow_orchestrator import WorkflowOrchestrator
from utils.logger import logger

router = APIRouter(prefix="/suggestion-agent", tags=["Suggestion Agent"])

# Initialize workflow orchestrator
orchestrator = WorkflowOrchestrator()


@router.post("/generate", response_model=Suggestions)
async def generate_suggestions(suggestion_input: SuggestionInput) -> Suggestions:
    """
    Generate suggested answers to clarifying questions based on project idea.

    Args:
        suggestion_input: Project idea and questions to answer

    Returns:
        Suggested answers to the questions
    """
    try:
        logger.info(
            f"Generating suggested answers for project: {suggestion_input.project_idea[:100]}..."
        )
        suggestions = await orchestrator.generate_suggestions(suggestion_input)
        return suggestions
    except Exception as e:
        logger.error(f"Failed to generate suggested answers: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e
