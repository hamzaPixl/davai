"""
Workflow orchestrator for DAVAI POC.
Manages the complete project documentation generation workflow.
"""

import time
import asyncio
from typing import List, Dict
from config.llm_config import LlmConfig
from services.llm_factory import get_default_config

# Import models for type annotations
from models.project_idea import ProjectIdea
from models.questions import Questions
from models.project_data import ProjectData
from models.documentation import Documentation
from models.workflow_step import WorkflowStep
from models.workflow_result import WorkflowResult

# Import agents
from agents.question_generator.question_generator_agent import QuestionGeneratorAgent
from agents.context_agent.context_agent import ContextAgent
from agents.architecture_agent.architecture_agent import ArchitectureAgent
from agents.tech_stack_agent.tech_stack_agent import TechStackAgent
from agents.task_breakdown_agent.task_breakdown_agent import TaskBreakdownAgent
from agents.project_rules_agent.project_rules_agent import ProjectRulesAgent
from agents.claude_guide_agent.claude_guide_agent import ClaudeGuideAgent
from agents.readme_agent.readme_agent import ReadmeAgent

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

        # Initialize all agents
        self.question_agent = QuestionGeneratorAgent(self.llm_config)
        self.context_agent = ContextAgent(self.llm_config)
        self.architecture_agent = ArchitectureAgent(self.llm_config)
        self.tech_stack_agent = TechStackAgent(self.llm_config)
        self.task_breakdown_agent = TaskBreakdownAgent(self.llm_config)
        self.project_rules_agent = ProjectRulesAgent(self.llm_config)
        self.claude_guide_agent = ClaudeGuideAgent(self.llm_config)
        self.readme_agent = ReadmeAgent(self.llm_config)

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

    async def generate_context(self, project_data: ProjectData) -> Dict[str, str]:
        """Generate context documentation."""
        logger.info("Generating context documentation")
        return await self.context_agent.run(project_data)

    async def generate_architecture(self, project_data: ProjectData) -> Dict[str, str]:
        """Generate architecture documentation."""
        logger.info("Generating architecture documentation")
        return await self.architecture_agent.run(project_data)

    async def generate_tech_stack(self, project_data: ProjectData) -> Dict[str, str]:
        """Generate tech stack documentation."""
        logger.info("Generating tech stack documentation")
        return await self.tech_stack_agent.run(project_data)

    async def generate_task_breakdown(
        self, project_data: ProjectData
    ) -> Dict[str, str]:
        """Generate task breakdown documentation."""
        logger.info("Generating task breakdown documentation")
        return await self.task_breakdown_agent.run(project_data)

    async def generate_project_rules(self, project_data: ProjectData) -> Dict[str, str]:
        """Generate project rules documentation."""
        logger.info("Generating project rules documentation")
        return await self.project_rules_agent.run(project_data)

    async def generate_claude_guide(self, project_data: ProjectData) -> Dict[str, str]:
        """Generate Claude guide documentation."""
        logger.info("Generating Claude guide documentation")
        return await self.claude_guide_agent.run(project_data)

    async def generate_readme(self, project_data: ProjectData) -> Dict[str, str]:
        """Generate README documentation."""
        logger.info("Generating README documentation")
        return await self.readme_agent.run(project_data)

    async def generate_all_documentation(
        self, project_idea: str, questions: List[str], answers: List[str]
    ) -> Documentation:
        """
        Generate complete project documentation using all agents.

        Args:
            project_idea: Original project idea
            questions: List of clarifying questions
            answers: User answers to the questions

        Returns:
            Generated documentation
        """
        logger.info("Generating complete project documentation")

        if len(questions) != len(answers):
            raise ValueError("Number of questions and answers must match")

        project_data = ProjectData(
            project_idea=project_idea, questions=questions, answers=answers
        )

        # Run all documentation agents in parallel
        tasks = [
            self.generate_context(project_data),
            self.generate_architecture(project_data),
            self.generate_tech_stack(project_data),
            self.generate_task_breakdown(project_data),
            self.generate_project_rules(project_data),
            self.generate_claude_guide(project_data),
            self.generate_readme(project_data),
        ]

        results = await asyncio.gather(*tasks)

        # Combine all documentation
        all_documents = {}
        for result in results:
            all_documents.update(result)

        logger.info(f"Generated {len(all_documents)} documentation files")
        return Documentation(documents=all_documents)

    async def run_complete_workflow(
        self, project_idea: str, answers: List[str]
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

            steps.append(
                WorkflowStep(
                    step_name="generate_questions",
                    input_data={"project_idea": project_idea},
                    output_data={"questions": questions.questions},
                    success=True,
                )
            )

            # Step 2: Generate documentation
            documentation = await self.generate_all_documentation(
                project_idea, questions.questions, answers
            )

            steps.append(
                WorkflowStep(
                    step_name="generate_documentation",
                    input_data={
                        "project_idea": project_idea,
                        "questions": questions.questions,
                        "answers": answers,
                    },
                    output_data={"documents": list(documentation.documents.keys())},
                    success=True,
                )
            )

            total_duration = time.time() - start_time

            return WorkflowResult(
                project_idea=project_idea,
                steps=steps,
                final_documentation=documentation.documents,
                success=True,
                total_duration=total_duration,
            )

        except Exception as e:
            logger.error(f"Workflow failed: {e}")

            # Add failed step
            steps.append(
                WorkflowStep(
                    step_name="workflow_failure",
                    input_data={"project_idea": project_idea},
                    output_data={},
                    success=False,
                    error_message=str(e),
                )
            )

            total_duration = time.time() - start_time

            return WorkflowResult(
                project_idea=project_idea,
                steps=steps,
                final_documentation=None,
                success=False,
                total_duration=total_duration,
            )
