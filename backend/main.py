"""
DAVAI POC FastAPI Application
"""

from app_factory import create_app
from config.settings import settings

# Create FastAPI app using the factory
app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.api_reload,
        log_level=settings.log_level.lower()
    )
