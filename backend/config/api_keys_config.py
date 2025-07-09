from pydantic_settings import BaseSettings
from typing import Optional


class ApiKeysConfig(BaseSettings):
    """Configuration for API keys."""

    # OpenAI API Key
    openai_api_key: Optional[str] = None

    # Anthropic API Key
    anthropic_api_key: Optional[str] = None

    # Google API Key
    google_api_key: Optional[str] = None

    class Config:
        env_file = ".env"
        env_prefix = ""


api_keys_config = ApiKeysConfig()
