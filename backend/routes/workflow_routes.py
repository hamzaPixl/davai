"""
Complete workflow routes.
"""

from fastapi import APIRouter, HTTPException
from typing import List
from pathlib import Path
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


@router.get("/saved-projects")
async def list_saved_projects():
    """List all saved documentation projects."""
    try:
        projects = orchestrator.list_saved_projects()
        return {
            "status": "success",
            "total_projects": len(projects),
            "projects": projects,
        }
    except Exception as e:
        logger.error(f"Failed to list saved projects: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e


@router.get("/saved-projects/{project_name}")
async def get_project_files(project_name: str):
    """Get files from a specific saved project."""
    try:
        projects = orchestrator.list_saved_projects()
        project = next((p for p in projects if p["folder_name"] == project_name), None)

        if not project:
            raise HTTPException(status_code=404, detail="Project not found")

        # Read all markdown files from the project folder
        project_path = Path(project["folder_path"])
        files = {}

        for file_path in project_path.glob("*.md"):
            with open(file_path, "r", encoding="utf-8") as f:
                files[file_path.stem] = f.read()

        return {"status": "success", "project_metadata": project, "files": files}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get project files: {e}")
        raise HTTPException(status_code=500, detail=str(e)) from e
