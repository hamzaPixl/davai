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


def validate_api_keys() -> bool:
    """
    Validate that required API keys are available.

    Returns:
        True if OpenAI API key is available, False otherwise
    """
    try:
        api_keys_config = init_api_keys_config()

        if not api_keys_config.openai_api_key:
            logger.error(
                "❌ OpenAI API key is required but not found in environment variables"
            )
            logger.error("Please set OPENAI_API_KEY environment variable")
            return False

        logger.info("✅ OpenAI API key found and configured")
        return True

    except Exception as e:
        logger.error(f"❌ Failed to validate API keys: {e}")
        return False


# Available providers and their models optimized for documentation generation
PROVIDERS = {
    "openai": {
        "models": ["gpt-3.5-turbo-0125", "gpt-4o", "gpt-4o-mini"],
        "config": {"temperature": 0.7},
        "json_models": [
            "gpt-3.5-turbo-0125",
            "gpt-4o",
            "gpt-4o-mini",
        ],  # Models that support JSON response format
        "text_models": [
            "gpt-3.5-turbo-0125",
            "gpt-4o-mini",
        ],  # Cheaper models for text generation
    },
    "claude": {
        "models": [
            "claude-3-haiku-20240307",
            "claude-3-sonnet-20240229",
            "claude-3-opus-20240229",
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

    # Initialize model_kwargs if not present
    model_kwargs = {}
    if config.model_kwargs:
        model_kwargs.update(config.model_kwargs)

    # Add response format only for OpenAI models that support it
    if provider == "openai" and config.response_format == "json_object":
        if config.model in PROVIDERS[provider]["json_models"]:
            model_kwargs["response_format"] = {"type": "json_object"}
        else:
            logger.warning(
                f"Model {config.model} does not support JSON response format, ignoring"
            )

    # Add model_kwargs to base_config if any
    if model_kwargs:
        base_config["model_kwargs"] = model_kwargs

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


def get_default_config(provider: str = "openai", use_json: bool = False) -> LlmConfig:
    """
    Get default LLM configuration for a provider.

    Args:
        provider: LLM provider name
        use_json: Whether JSON response format is needed (will use GPT-4 if True)

    Returns:
        Default configuration for the provider
    """
    if provider not in PROVIDERS:
        raise ValueError(f"Unsupported provider: {provider}")

    if provider == "openai" and use_json:
        # Use GPT-4 for JSON responses
        default_model = PROVIDERS[provider]["json_models"][0]  # gpt-4
        response_format = "json_object"
    else:
        # Use cheaper models for text generation
        if provider == "openai":
            default_model = PROVIDERS[provider]["text_models"][0]  # gpt-3.5-turbo
        else:
            default_model = PROVIDERS[provider]["models"][0]
        response_format = None

    default_config = PROVIDERS[provider]["config"]

    return LlmConfig(
        model=default_model,
        provider=provider,
        temperature=default_config.get("temperature", 0.7),
        response_format=response_format,
    )


def get_json_config(provider: str = "openai") -> LlmConfig:
    """
    Get LLM configuration optimized for JSON responses.

    Args:
        provider: LLM provider name

    Returns:
        Configuration for JSON responses
    """
    return get_default_config(provider=provider, use_json=True)


def get_text_config(provider: str = "openai") -> LlmConfig:
    """
    Get LLM configuration optimized for text generation.

    Args:
        provider: LLM provider name

    Returns:
        Configuration for text generation
    """
    return get_default_config(provider=provider, use_json=False)
