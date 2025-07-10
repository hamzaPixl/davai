from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class LlmConfig:
    """
    Represents configuration parameters for a language model.

    Attributes:
        model: The name of the model to use (e.g., "gpt-3.5-turbo").
        provider: The provider of the model (e.g., "openai").
        temperature: Sampling temperature for the model's output.
        response_format: Format for model responses (e.g., "json_object").
    """

    model: str
    provider: str
    temperature: Optional[float] = 0.7
    response_format: Optional[str] = None
    model_kwargs: Optional[Dict[str, Any]] = None

    def copy(self, **kwargs) -> "LlmConfig":
        """
        Creates a copy of the configuration with optional parameter updates.

        Args:
            **kwargs: New values for any parameters to override in the copy

        Returns:
            A new LlmConfig instance with the specified updates
        """
        params = {
            "model": self.model,
            "provider": self.provider,
            "temperature": self.temperature,
            "response_format": self.response_format,
            "model_kwargs": self.model_kwargs.copy() if self.model_kwargs else None,
        }
        params.update(kwargs)
        return LlmConfig(**params)
