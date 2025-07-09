"""
FastAPI application factory for DAVAI POC.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.settings import settings
from routes.api import router as api_router
from utils.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan events."""
    # Startup
    logger.info("🚀 Starting DAVAI POC API server")

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

    # Include API routes
    app.include_router(api_router, prefix="/api", tags=["API"])

    return app
