#!/usr/bin/env python3
"""
CLI script to run DAVAI POC with uvicorn.
"""

import click
import uvicorn
from config.settings import settings


@click.command()
@click.option('--host', default=None, help='Host to bind to')
@click.option('--port', default=None, type=int, help='Port to bind to')
@click.option('--reload/--no-reload', default=None, help='Enable auto-reload')
@click.option('--log-level', default=None, help='Log level')
@click.option('--workers', default=1, type=int, help='Number of worker processes')
def main(host, port, reload, log_level, workers):
    """Run DAVAI POC API server with uvicorn."""
    
    # Use command line args or fall back to settings
    run_host = host or settings.api_host
    run_port = port or settings.api_port
    run_reload = reload if reload is not None else settings.api_reload
    run_log_level = log_level or settings.log_level.lower()
    
    click.echo(f"🚀 Starting DAVAI POC API server")
    click.echo(f"📍 Server: http://{run_host}:{run_port}")
    click.echo(f"📚 Docs: http://{run_host}:{run_port}/docs")
    click.echo(f"🔄 Reload: {run_reload}")
    click.echo(f"📝 Log Level: {run_log_level}")
    
    uvicorn.run(
        "main:app",
        host=run_host,
        port=run_port,
        reload=run_reload,
        log_level=run_log_level,
        workers=workers if not run_reload else 1,  # Workers don't work with reload
        access_log=True
    )


if __name__ == "__main__":
    main()
