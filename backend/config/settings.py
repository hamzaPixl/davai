from pydantic_settings import BaseSettings
from typing import Optional
from pathlib import Path


class Settings(BaseSettings):
    """
    Application settings for DAVAI POC.
    Loads configuration from environment variables and .env file.
    """

    # API Settings
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_debug: bool = False
    api_reload: bool = True

    # CORS Settings
    cors_origins: list[str] = ["*"]
    cors_methods: list[str] = ["*"]
    cors_headers: list[str] = ["*"]

    # AI Provider API Keys
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    google_api_key: Optional[str] = None

    # Project Generation Settings
    max_questions: int = 10
    default_templates_path: Path = Path("../templates")

    # Local Storage Settings
    temp_storage_path: Path = Path("temp")
    cache_storage_path: Path = Path("cache")

    # Caching Settings
    cache_enabled: bool = True
    cache_ttl: int = 3600  # 1 hour
    cache_max_size: int = 1000

    # Logging Settings
    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    log_file: Optional[str] = None

    class Config:
        env_file = ".env"


settings = Settings()
