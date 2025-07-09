"""
LLM Factory for DAVAI POC.

Provides centralized management of Language Model providers (OpenAI, Claude, Gemini)
optimized for project documentation generation tasks.
"""

from langchain_anthropic import ChatAnthropic
from langchain_core.language_models import BaseChatModel
from langchain_openai import ChatOpenAI

from config.api_keys_config import init_api_keys_config
from config.llm_config import LlmConfig
from utils.logger import logger

# Available providers and their models optimized for documentation generation
PROVIDERS = {
    "openai": {
        "models": ["gpt-4", "gpt-4-turbo", "gpt-3.5-turbo"],
        "config": {"temperature": 0.7, "response_format": {"type": "json_object"}},
    },
    "claude": {
        "models": [
            "claude-3-opus-20240229",
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307",
        ],
        "config": {"temperature": 0.7},
    },
}


def get_llm(config: LlmConfig) -> BaseChatModel:
    """
    Factory function to create and configure LLM instances.

    Args:
        config: LLM configuration specifying provider, model, and parameters

    Returns:
        Configured language model instance

    Raises:
        ValueError: If provider/model combination is not supported
        RuntimeError: If required API keys are missing
    """
    # Initialize API keys config
    api_keys_config = init_api_keys_config()

    provider = config.provider.lower()

    if provider not in PROVIDERS:
        raise ValueError(f"Unsupported provider: {provider}")

    if config.model not in PROVIDERS[provider]["models"]:
        raise ValueError(f"Unsupported model {config.model} for provider {provider}")

    # Get base configuration for the provider
    base_config = PROVIDERS[provider]["config"].copy()

    # Override with user-specified configuration
    if config.temperature is not None:
        base_config["temperature"] = config.temperature

    # Handle response format properly for OpenAI
    if config.response_format is not None and provider == "openai":
        if config.response_format == "json_object":
            # Move response_format to model_kwargs to avoid the warning
            if "model_kwargs" not in base_config:
                base_config["model_kwargs"] = {}
            base_config["model_kwargs"]["response_format"] = {"type": "json_object"}
        # Remove from base config to avoid duplication
        base_config.pop("response_format", None)

    # Add any additional model kwargs
    if config.model_kwargs:
        if "model_kwargs" in base_config:
            base_config["model_kwargs"].update(config.model_kwargs)
        else:
            base_config["model_kwargs"] = config.model_kwargs

    # Create LLM instance based on provider
    try:
        if provider == "openai":
            if not api_keys_config.openai_api_key:
                raise RuntimeError("OpenAI API key is required but not configured")

            return ChatOpenAI(
                model=config.model,
                api_key=api_keys_config.openai_api_key,
                **base_config,
            )

        elif provider == "claude":
            if not api_keys_config.anthropic_api_key:
                raise RuntimeError("Anthropic API key is required but not configured")

            return ChatAnthropic(
                model=config.model,
                api_key=api_keys_config.anthropic_api_key,
                **base_config,
            )

        else:
            raise ValueError(f"Provider {provider} not implemented")

    except Exception as e:
        logger.error(f"Failed to create LLM for {provider}/{config.model}: {e}")
        raise


def get_default_config(provider: str = "openai") -> LlmConfig:
    """
    Get default LLM configuration for a provider.

    Args:
        provider: LLM provider name

    Returns:
        Default configuration for the provider
    """
    if provider not in PROVIDERS:
        raise ValueError(f"Unsupported provider: {provider}")

    default_model = PROVIDERS[provider]["models"][0]
    default_config = PROVIDERS[provider]["config"]

    return LlmConfig(
        model=default_model,
        provider=provider,
        temperature=default_config.get("temperature", 0.7),
        response_format="json_object" if provider == "openai" else None,
    )
