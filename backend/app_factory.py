"""
FastAPI application factory for DAVAI POC.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.settings import settings
from routes.workflow_routes import router as workflow_router
from routes.agents.question_generator_routes import router as question_generator_router
from routes.agents.context_routes import router as context_router
from routes.agents.architecture_routes import router as architecture_router
from routes.agents.tech_stack_routes import router as tech_stack_router
from routes.agents.task_breakdown_routes import router as task_breakdown_router
from routes.agents.project_rules_routes import router as project_rules_router
from routes.agents.claude_guide_routes import router as claude_guide_router
from routes.agents.readme_routes import router as readme_router
from utils.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan events."""
    # Startup
    logger.info("🚀 Starting DAVAI POC API server")

    # Validate API keys first
    from services.llm_factory import validate_api_keys

    if not validate_api_keys():
        logger.error("❌ API key validation failed - server cannot start")
        raise RuntimeError("Required API keys are missing")

    # Create necessary directories
    settings.temp_storage_path.mkdir(exist_ok=True)
    settings.cache_storage_path.mkdir(exist_ok=True)

    logger.info("🎉 DAVAI POC API server startup completed")
    logger.info(
        f"📚 Visit http://{settings.api_host}:{settings.api_port}/docs for API documentation"
    )

    yield

    # Shutdown
    logger.info("🛑 Shutting down DAVAI POC API server...")
    logger.info("👋 DAVAI POC API server shutdown completed")


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""

    # Create FastAPI app
    app = FastAPI(
        title="DAVAI - Complete Project Generator",
        description="Generate complete project documentation using AI agents",
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=settings.cors_methods,
        allow_headers=settings.cors_headers,
    )

    # Include all routers
    app.include_router(workflow_router, prefix="/api", tags=["Workflow"])
    app.include_router(question_generator_router, prefix="/api", tags=["Agents"])
    app.include_router(context_router, prefix="/api", tags=["Agents"])
    app.include_router(architecture_router, prefix="/api", tags=["Agents"])
    app.include_router(tech_stack_router, prefix="/api", tags=["Agents"])
    app.include_router(task_breakdown_router, prefix="/api", tags=["Agents"])
    app.include_router(project_rules_router, prefix="/api", tags=["Agents"])
    app.include_router(claude_guide_router, prefix="/api", tags=["Agents"])
    app.include_router(readme_router, prefix="/api", tags=["Agents"])

    # Root health and status endpoints
    @app.get("/health", tags=["System"])
    async def health_check():
        """Root health check endpoint."""
        return {
            "status": "healthy",
            "message": "DAVAI API is running",
            "version": "0.1.0",
        }

    return app
