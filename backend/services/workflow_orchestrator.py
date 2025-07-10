"""
Workflow orchestrator for DAVAI POC.
Manages the complete project documentation generation workflow.
"""

import time
import json
from pathlib import Path
from typing import List, Dict
from datetime import datetime
from config.llm_config import LlmConfig
from config.settings import settings
from services.llm_factory import get_json_config, get_text_config

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
        # Use different configurations for different purposes
        self.json_config = get_json_config()  # GPT-4 for JSON responses
        self.text_config = get_text_config()  # GPT-3.5-turbo for text generation

        # Initialize agents with appropriate configurations
        self.question_agent = QuestionGeneratorAgent(self.json_config)  # Needs JSON
        self.context_agent = ContextAgent(self.text_config)  # Text generation
        self.architecture_agent = ArchitectureAgent(self.text_config)  # Text generation
        self.tech_stack_agent = TechStackAgent(self.text_config)  # Text generation
        self.task_breakdown_agent = TaskBreakdownAgent(
            self.text_config
        )  # Text generation
        self.project_rules_agent = ProjectRulesAgent(
            self.text_config
        )  # Text generation
        self.claude_guide_agent = ClaudeGuideAgent(self.text_config)  # Text generation
        self.readme_agent = ReadmeAgent(self.text_config)  # Text generation

        # Initialize output directory
        self.output_dir = settings.temp_storage_path / "generated_docs"
        self.output_dir.mkdir(parents=True, exist_ok=True)

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
        Generate complete project documentation using all agents in proper dependency order.

        Workflow Dependencies:
        1. Context (standalone)
        2. Architecture (depends on Context)
        3. Tech Stack (depends on Context + Architecture)
        4. Task Breakdown (depends on Context + Architecture + Tech Stack)
        5. Project Rules (depends on all previous outputs)
        6. Claude Guide (depends on all previous outputs)
        7. README (depends on all previous outputs)

        Args:
            project_idea: Original project idea
            questions: List of clarifying questions
            answers: User answers to the questions

        Returns:
            Generated documentation
        """
        logger.info("Generating complete project documentation with dependency chain")

        if len(questions) != len(answers):
            raise ValueError("Number of questions and answers must match")

        project_data = ProjectData(
            project_idea=project_idea, questions=questions, answers=answers
        )

        all_documents = {}

        # Step 1: Generate context (no dependencies)
        logger.info("Step 1: Generating context documentation")
        context_docs = await self.generate_context(project_data)
        all_documents.update(context_docs)

        # Step 2: Generate architecture (depends on context)
        logger.info("Step 2: Generating architecture documentation (with context)")
        enhanced_project_data = self.enhance_project_data_with_context(
            project_data, context_docs
        )
        architecture_docs = await self.generate_architecture(enhanced_project_data)
        all_documents.update(architecture_docs)

        # Step 3: Generate tech stack (depends on context + architecture)
        logger.info(
            "Step 3: Generating tech stack documentation (with context + architecture)"
        )
        enhanced_project_data = self.enhance_project_data_with_docs(
            project_data, {"context": context_docs, "architecture": architecture_docs}
        )
        tech_stack_docs = await self.generate_tech_stack(enhanced_project_data)
        all_documents.update(tech_stack_docs)

        # Step 4: Generate task breakdown (depends on context + architecture + tech stack)
        logger.info(
            "Step 4: Generating task breakdown (with context + architecture + tech stack)"
        )
        enhanced_project_data = self.enhance_project_data_with_docs(
            project_data,
            {
                "context": context_docs,
                "architecture": architecture_docs,
                "tech_stack": tech_stack_docs,
            },
        )
        task_breakdown_docs = await self.generate_task_breakdown(enhanced_project_data)
        all_documents.update(task_breakdown_docs)

        # Step 5: Generate project rules (depends on all previous)
        logger.info("Step 5: Generating project rules (with all previous outputs)")
        enhanced_project_data = self.enhance_project_data_with_docs(
            project_data,
            {
                "context": context_docs,
                "architecture": architecture_docs,
                "tech_stack": tech_stack_docs,
                "task_breakdown": task_breakdown_docs,
            },
        )
        project_rules_docs = await self.generate_project_rules(enhanced_project_data)
        all_documents.update(project_rules_docs)

        # Step 6: Generate Claude guide (depends on all previous)
        logger.info("Step 6: Generating Claude guide (with all previous outputs)")
        enhanced_project_data = self.enhance_project_data_with_docs(
            project_data,
            {
                "context": context_docs,
                "architecture": architecture_docs,
                "tech_stack": tech_stack_docs,
                "task_breakdown": task_breakdown_docs,
                "project_rules": project_rules_docs,
            },
        )
        claude_guide_docs = await self.generate_claude_guide(enhanced_project_data)
        all_documents.update(claude_guide_docs)

        # Step 7: Generate README (depends on all previous)
        logger.info("Step 7: Generating README (with all previous outputs)")
        enhanced_project_data = self.enhance_project_data_with_docs(
            project_data,
            {
                "context": context_docs,
                "architecture": architecture_docs,
                "tech_stack": tech_stack_docs,
                "task_breakdown": task_breakdown_docs,
                "project_rules": project_rules_docs,
                "claude_guide": claude_guide_docs,
            },
        )
        readme_docs = await self.generate_readme(enhanced_project_data)
        all_documents.update(readme_docs)

        logger.info(f"Generated {len(all_documents)} documentation files")
        return Documentation(documents=all_documents)

    async def run_complete_workflow(
        self, project_idea: str, answers: List[str]
    ) -> WorkflowResult:
        """
        Run the complete workflow with proper agent dependencies.

        Workflow Steps:
        1. Generate clarifying questions
        2. Generate context (standalone)
        3. Generate architecture (with context)
        4. Generate tech stack (with context + architecture)
        5. Generate task breakdown (with context + architecture + tech stack)
        6. Generate project rules (with all previous)
        7. Generate Claude guide (with all previous)
        8. Generate README (with all previous)

        Args:
            project_idea: Brief description of the project
            answers: User answers to clarifying questions

        Returns:
            Complete workflow result with detailed steps
        """
        start_time = time.time()
        steps = []

        try:
            # Step 1: Generate questions
            logger.info("Workflow Step 1: Generating clarifying questions")
            questions = await self.generate_questions(project_idea)

            steps.append(
                WorkflowStep(
                    step_name="generate_questions",
                    input_data={"project_idea": project_idea},
                    output_data={"questions": questions.questions},
                    success=True,
                )
            )

            # Create base project data
            project_data = ProjectData(
                project_idea=project_idea,
                questions=questions.questions,
                answers=answers,
            )

            all_documents = {}

            # Step 2: Generate context (no dependencies)
            logger.info("Workflow Step 2: Generating context documentation")
            context_docs = await self.generate_context(project_data)
            all_documents.update(context_docs)

            steps.append(
                WorkflowStep(
                    step_name="generate_context",
                    input_data={"project_data": "project_idea + questions + answers"},
                    output_data={"documents": list(context_docs.keys())},
                    success=True,
                )
            )

            # Step 3: Generate architecture (with context)
            logger.info("Workflow Step 3: Generating architecture (with context)")
            enhanced_project_data = self.enhance_project_data_with_context(
                project_data, context_docs
            )
            architecture_docs = await self.generate_architecture(enhanced_project_data)
            all_documents.update(architecture_docs)

            steps.append(
                WorkflowStep(
                    step_name="generate_architecture",
                    input_data={"dependencies": ["context"]},
                    output_data={"documents": list(architecture_docs.keys())},
                    success=True,
                )
            )

            # Step 4: Generate tech stack (with context + architecture)
            logger.info(
                "Workflow Step 4: Generating tech stack (with context + architecture)"
            )
            enhanced_project_data = self.enhance_project_data_with_docs(
                project_data,
                {"context": context_docs, "architecture": architecture_docs},
            )
            tech_stack_docs = await self.generate_tech_stack(enhanced_project_data)
            all_documents.update(tech_stack_docs)

            steps.append(
                WorkflowStep(
                    step_name="generate_tech_stack",
                    input_data={"dependencies": ["context", "architecture"]},
                    output_data={"documents": list(tech_stack_docs.keys())},
                    success=True,
                )
            )

            # Step 5: Generate task breakdown (with context + architecture + tech stack)
            logger.info(
                "Workflow Step 5: Generating task breakdown (with context + architecture + tech stack)"
            )
            enhanced_project_data = self.enhance_project_data_with_docs(
                project_data,
                {
                    "context": context_docs,
                    "architecture": architecture_docs,
                    "tech_stack": tech_stack_docs,
                },
            )
            task_breakdown_docs = await self.generate_task_breakdown(
                enhanced_project_data
            )
            all_documents.update(task_breakdown_docs)

            steps.append(
                WorkflowStep(
                    step_name="generate_task_breakdown",
                    input_data={
                        "dependencies": ["context", "architecture", "tech_stack"]
                    },
                    output_data={"documents": list(task_breakdown_docs.keys())},
                    success=True,
                )
            )

            # Step 6: Generate project rules (with all previous)
            logger.info(
                "Workflow Step 6: Generating project rules (with all previous outputs)"
            )
            enhanced_project_data = self.enhance_project_data_with_docs(
                project_data,
                {
                    "context": context_docs,
                    "architecture": architecture_docs,
                    "tech_stack": tech_stack_docs,
                    "task_breakdown": task_breakdown_docs,
                },
            )
            project_rules_docs = await self.generate_project_rules(
                enhanced_project_data
            )
            all_documents.update(project_rules_docs)

            steps.append(
                WorkflowStep(
                    step_name="generate_project_rules",
                    input_data={
                        "dependencies": [
                            "context",
                            "architecture",
                            "tech_stack",
                            "task_breakdown",
                        ]
                    },
                    output_data={"documents": list(project_rules_docs.keys())},
                    success=True,
                )
            )

            # Step 7: Generate Claude guide (with all previous)
            logger.info(
                "Workflow Step 7: Generating Claude guide (with all previous outputs)"
            )
            enhanced_project_data = self.enhance_project_data_with_docs(
                project_data,
                {
                    "context": context_docs,
                    "architecture": architecture_docs,
                    "tech_stack": tech_stack_docs,
                    "task_breakdown": task_breakdown_docs,
                    "project_rules": project_rules_docs,
                },
            )
            claude_guide_docs = await self.generate_claude_guide(enhanced_project_data)
            all_documents.update(claude_guide_docs)

            steps.append(
                WorkflowStep(
                    step_name="generate_claude_guide",
                    input_data={
                        "dependencies": [
                            "context",
                            "architecture",
                            "tech_stack",
                            "task_breakdown",
                            "project_rules",
                        ]
                    },
                    output_data={"documents": list(claude_guide_docs.keys())},
                    success=True,
                )
            )

            # Step 8: Generate README (with all previous)
            logger.info(
                "Workflow Step 8: Generating README (with all previous outputs)"
            )
            enhanced_project_data = self.enhance_project_data_with_docs(
                project_data,
                {
                    "context": context_docs,
                    "architecture": architecture_docs,
                    "tech_stack": tech_stack_docs,
                    "task_breakdown": task_breakdown_docs,
                    "project_rules": project_rules_docs,
                    "claude_guide": claude_guide_docs,
                },
            )
            readme_docs = await self.generate_readme(enhanced_project_data)
            all_documents.update(readme_docs)

            steps.append(
                WorkflowStep(
                    step_name="generate_readme",
                    input_data={
                        "dependencies": [
                            "context",
                            "architecture",
                            "tech_stack",
                            "task_breakdown",
                            "project_rules",
                            "claude_guide",
                        ]
                    },
                    output_data={"documents": list(readme_docs.keys())},
                    success=True,
                )
            )

            # Save all generated documentation to disk
            logger.info("Saving all generated documentation to disk")
            output_path = self.save_documentation_to_disk(all_documents, project_idea)

            total_duration = time.time() - start_time

            return WorkflowResult(
                project_idea=project_idea,
                steps=steps,
                final_documentation=all_documents,
                success=True,
                total_duration=total_duration,
            )

        except ValueError as e:
            logger.error(f"Workflow validation error: {e}")

            # Add failed step
            steps.append(
                WorkflowStep(
                    step_name="workflow_validation_failure",
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
        except RuntimeError as e:
            logger.error(f"Workflow runtime error: {e}")

            # Add failed step
            steps.append(
                WorkflowStep(
                    step_name="workflow_runtime_failure",
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

    def enhance_project_data_with_context(
        self, project_data: ProjectData, context_docs: Dict[str, str]
    ) -> ProjectData:
        """
        Enhance project data with context information for subsequent agents.

        Args:
            project_data: Original project data
            context_docs: Generated context documentation

        Returns:
            Enhanced project data with context included
        """
        # Create enhanced project data that includes context in the project idea
        context_summary = ""
        if "context.md" in context_docs:
            context_summary = f"\n\nCONTEXT ANALYSIS:\n{context_docs['context.md']}"

        enhanced_idea = f"{project_data.project_idea}{context_summary}"

        return ProjectData(
            project_idea=enhanced_idea,
            questions=project_data.questions,
            answers=project_data.answers,
        )

    def enhance_project_data_with_docs(
        self, project_data: ProjectData, previous_docs: Dict[str, Dict[str, str]]
    ) -> ProjectData:
        """
        Enhance project data with all previous agent outputs.

        Args:
            project_data: Original project data
            previous_docs: Dictionary of previous agent outputs by category

        Returns:
            Enhanced project data with all previous outputs included
        """
        # Combine all previous documentation into context
        combined_context = f"{project_data.project_idea}\n\n"

        for doc_type, docs in previous_docs.items():
            combined_context += f"\n=== {doc_type.upper()} DOCUMENTATION ===\n"
            for filename, content in docs.items():
                combined_context += f"\n--- {filename} ---\n{content}\n"

        return ProjectData(
            project_idea=combined_context,
            questions=project_data.questions,
            answers=project_data.answers,
        )

    def save_documentation_to_disk(
        self, all_documents: Dict[str, str], project_idea: str = "project"
    ):
        """
        Save all generated documentation to disk.

        Args:
            all_documents: Dictionary of all generated documents
            project_idea: Original project idea for folder naming
        """
        # Create a sanitized folder name from project idea
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = "".join(
            c for c in project_idea[:50] if c.isalnum() or c in (" ", "-", "_")
        ).rstrip()
        safe_name = safe_name.replace(" ", "_").lower()

        # Use the configured output directory
        project_dir = self.output_dir / f"{safe_name}_{timestamp}"
        project_dir.mkdir(parents=True, exist_ok=True)

        # Save each document as a separate markdown file
        for doc_name, content in all_documents.items():
            # Ensure .md extension
            filename = f"{doc_name}.md" if not doc_name.endswith(".md") else doc_name
            file_path = project_dir / filename
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            logger.info(f"Saved document: {file_path}")

        # Save metadata file with summary of all documents
        metadata = {
            "project_idea": project_idea,
            "generated_at": datetime.now().isoformat(),
            "total_documents": len(all_documents),
            "document_list": list(all_documents.keys()),
            "output_path": str(project_dir),
        }

        metadata_path = project_dir / "metadata.json"
        with open(metadata_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)

        logger.info(f"📁 All documentation saved to: {project_dir}")
        logger.info(
            f"📄 Generated {len(all_documents)} files: {', '.join(all_documents.keys())}"
        )

        return str(project_dir)

    def list_saved_projects(self) -> List[Dict[str, str]]:
        """
        List all saved projects with metadata.

        Returns:
            List of project metadata dictionaries
        """
        projects = []

        if not self.output_dir.exists():
            return projects

        for project_folder in self.output_dir.iterdir():
            if project_folder.is_dir():
                metadata_file = project_folder / "metadata.json"
                if metadata_file.exists():
                    try:
                        with open(metadata_file, "r", encoding="utf-8") as f:
                            metadata = json.load(f)
                        metadata["folder_name"] = project_folder.name
                        metadata["folder_path"] = str(project_folder)
                        projects.append(metadata)
                    except Exception as e:
                        logger.warning(
                            f"Could not read metadata for {project_folder}: {e}"
                        )

        # Sort by generation time (newest first)
        projects.sort(key=lambda x: x.get("generated_at", ""), reverse=True)
        return projects
