"""
Enhanced request models for agent routes with dependencies.
"""

from typing import List, Dict, Optional
from pydantic import BaseModel, Field


class BaseAgentRequest(BaseModel):
    """Base request for all agents."""

    project_idea: str = Field(..., description="Original project idea")
    questions: List[str] = Field(..., description="Clarifying questions")
    answers: List[str] = Field(..., description="User answers to questions")


class ContextAgentRequest(BaseAgentRequest):
    """Request for Context Agent - no dependencies."""

    # No additional fields needed - inherits all from base


class ArchitectureAgentRequest(BaseAgentRequest):
    """Request for Architecture Agent - depends on context."""

    context_docs: Optional[Dict[str, str]] = Field(
        None, description="Context documentation from previous step"
    )


class TechStackAgentRequest(BaseAgentRequest):
    """Request for Tech Stack Agent - depends on context + architecture."""

    context_docs: Optional[Dict[str, str]] = Field(
        None, description="Context documentation from previous step"
    )
    architecture_docs: Optional[Dict[str, str]] = Field(
        None, description="Architecture documentation from previous step"
    )


class TaskBreakdownAgentRequest(BaseAgentRequest):
    """Request for Task Breakdown Agent - depends on context + architecture + tech stack."""

    context_docs: Optional[Dict[str, str]] = Field(
        None, description="Context documentation from previous step"
    )
    architecture_docs: Optional[Dict[str, str]] = Field(
        None, description="Architecture documentation from previous step"
    )
    tech_stack_docs: Optional[Dict[str, str]] = Field(
        None, description="Tech stack documentation from previous step"
    )


class ProjectRulesAgentRequest(BaseAgentRequest):
    """Request for Project Rules Agent - depends on all documentation agents."""

    previous_docs: Optional[Dict[str, Dict[str, str]]] = Field(
        None, description="All previous documentation by category"
    )


class ClaudeGuideAgentRequest(BaseAgentRequest):
    """Request for Claude Guide Agent - depends on all documentation agents."""

    previous_docs: Optional[Dict[str, Dict[str, str]]] = Field(
        None, description="All previous documentation by category"
    )


class ReadmeAgentRequest(BaseAgentRequest):
    """Request for README Agent - depends on all documentation agents."""

    previous_docs: Optional[Dict[str, Dict[str, str]]] = Field(
        None, description="All previous documentation by category"
    )
