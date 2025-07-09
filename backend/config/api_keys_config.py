"""
API Keys configuration that reads from the main settings.
"""


class ApiKeysConfig:
    """Configuration for API keys."""

    def __init__(self, main_settings):
        self.openai_api_key = main_settings.openai_api_key
        self.anthropic_api_key = main_settings.anthropic_api_key
        self.google_api_key = main_settings.google_api_key


def get_api_keys_config():
    """Get API keys configuration from main settings."""
    from config.settings import settings

    return ApiKeysConfig(settings)


# Create the global instance
api_keys_config = None


def init_api_keys_config():
    """Initialize the API keys configuration."""
    global api_keys_config
    if api_keys_config is None:
        api_keys_config = get_api_keys_config()
    return api_keys_config
