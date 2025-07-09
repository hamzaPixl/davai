"""
Workflow orchestrator for DAVAI POC.
Manages the complete project documentation generation workflow.
"""

import time
from typing import List, Dict, Any
from config.llm_config import LlmConfig
from services.llm_factory import get_default_config
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.documentation_generator_agent import DocumentationGeneratorAgent
from models.workflow_models import (
    ProjectIdea,
    Questions,
    ProjectData,
    Documentation,
    WorkflowStep,
    WorkflowResult
)
from utils.logger import logger


class WorkflowOrchestrator:
    """Orchestrates the complete DAVAI workflow."""

    def __init__(self, llm_config: LlmConfig = None):
        """
        Initialize the workflow orchestrator.

        Args:
            llm_config: Optional LLM configuration. Uses default if not provided.
        """
        self.llm_config = llm_config or get_default_config()
        self.question_agent = QuestionGeneratorAgent(self.llm_config)
        self.documentation_agent = DocumentationGeneratorAgent(self.llm_config)

    async def generate_questions(self, project_idea: str) -> Questions:
        """
        Generate clarifying questions for a project idea.

        Args:
            project_idea: Brief description of the project

        Returns:
            Generated questions
        """
        logger.info("Generating clarifying questions")

        idea = ProjectIdea(description=project_idea)
        questions = await self.question_agent.run(idea)

        logger.info(f"Generated {len(questions.questions)} questions")
        return questions

    async def generate_documentation(
        self,
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
            Generated documentation
        """
        logger.info("Generating project documentation")

        if len(questions) != len(answers):
            raise ValueError("Number of questions and answers must match")

        project_data = ProjectData(
            project_idea=project_idea,
            questions=questions,
            answers=answers
        )

        documentation = await self.documentation_agent.run(project_data)

        logger.info(f"Generated {len(documentation.documents)} documentation files")
        return documentation

    async def run_complete_workflow(
        self,
        project_idea: str,
        answers: List[str]
    ) -> WorkflowResult:
        """
        Run the complete workflow: generate questions then documentation.

        Args:
            project_idea: Brief description of the project
            answers: User answers to clarifying questions

        Returns:
            Complete workflow result
        """
        start_time = time.time()
        steps = []

        try:
            # Step 1: Generate questions
            step_start = time.time()
            questions = await self.generate_questions(project_idea)

            steps.append(WorkflowStep(
                step_name="generate_questions",
                input_data={"project_idea": project_idea},
                output_data={"questions": questions.questions},
                success=True
            ))

            # Step 2: Generate documentation
            step_start = time.time()
            documentation = await self.generate_documentation(
                project_idea,
                questions.questions,
                answers
            )

            steps.append(WorkflowStep(
                step_name="generate_documentation",
                input_data={
                    "project_idea": project_idea,
                    "questions": questions.questions,
                    "answers": answers
                },
                output_data={"documents": list(documentation.documents.keys())},
                success=True
            ))

            total_duration = time.time() - start_time

            return WorkflowResult(
                project_idea=project_idea,
                steps=steps,
                final_documentation=documentation.documents,
                success=True,
                total_duration=total_duration
            )

        except Exception as e:
            logger.error(f"Workflow failed: {e}")

            # Add failed step
            steps.append(WorkflowStep(
                step_name="workflow_failure",
                input_data={"project_idea": project_idea},
                output_data={},
                success=False,
                error_message=str(e)
            ))

            total_duration = time.time() - start_time

            return WorkflowResult(
                project_idea=project_idea,
                steps=steps,
                final_documentation=None,
                success=False,
                total_duration=total_duration
            )
