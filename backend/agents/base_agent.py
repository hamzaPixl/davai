"""
Base agent class for DAVAI POC agents.
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Dict, Any, Optional
from pydantic import BaseModel

from config.llm_config import LlmConfig
from services.llm_factory import get_llm
from utils.logger import logger

InputType = TypeVar('InputType', bound=BaseModel)
OutputType = TypeVar('OutputType', bound=BaseModel)


class BaseAgent(ABC, Generic[InputType, OutputType]):
    """
    Base class for all AI agents in the project documentation generation pipeline.

    All agents must inherit from this class and implement the abstract methods.
    Provides common functionality for LLM integration and error handling.
    """

    def __init__(self, llm_config: LlmConfig, **kwargs):
        """
        Initialize the agent with LLM configuration.

        Args:
            llm_config: Configuration for the underlying language model
            **kwargs: Additional configuration options
        """
        self.llm_config = llm_config
        self.llm = self._initialize_llm()

        logger.debug(f"Initialized {self.__class__.__name__} with model {llm_config.model}")

    def _initialize_llm(self):
        """Initialize the LLM with the provided configuration."""
        try:
            return get_llm(self.llm_config)
        except Exception as e:
            logger.error(f"Failed to initialize LLM for {self.__class__.__name__}: {e}")
            raise

    @abstractmethod
    async def process(self, input_data: InputType) -> OutputType:
        """
        Process input data and return the result.

        Args:
            input_data: Input data for the agent

        Returns:
            Processed output data
        """
        pass

    @abstractmethod
    def get_system_prompt(self) -> str:
        """
        Get the system prompt for this agent.

        Returns:
            System prompt string
        """
        pass

    @abstractmethod
    def get_user_prompt(self, input_data: InputType) -> str:
        """
        Generate user prompt from input data.

        Args:
            input_data: Input data to generate prompt from

        Returns:
            User prompt string
        """
        pass

    async def _invoke_llm(self, user_prompt: str, system_prompt: Optional[str] = None) -> str:
        """
        Invoke the LLM with the given prompts.

        Args:
            user_prompt: The user prompt
            system_prompt: Optional system prompt

        Returns:
            LLM response
        """
        try:
            messages = []

            if system_prompt:
                messages.append(("system", system_prompt))

            messages.append(("user", user_prompt))

            response = await self.llm.ainvoke(messages)
            return response.content

        except Exception as e:
            logger.error(f"LLM invocation failed in {self.__class__.__name__}: {e}")
            raise

    async def run(self, input_data: InputType) -> OutputType:
        """
        Main execution method that processes input and returns output.

        Args:
            input_data: Input data for processing

        Returns:
            Processed output
        """
        logger.info(f"Running {self.__class__.__name__}")

        try:
            result = await self.process(input_data)
            logger.info(f"Successfully completed {self.__class__.__name__}")
            return result

        except Exception as e:
            logger.error(f"Agent {self.__class__.__name__} failed: {e}")
            raise
