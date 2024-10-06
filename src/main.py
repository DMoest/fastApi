#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
This module is the main entry point of the FastAPI application.
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.core import config
from src.db.connectors.postgres_db import PostgresConnector
from src.db.connectors.sqlite_db import SQLiteConnector
from src.core.config import get_settings
from psycopg_pool import AsyncConnectionPool

# from core.settings import get_settings

@asynccontextmanager
async def app_lifespan(app_instance: FastAPI):
    """
    Lifespan context manager for the FastAPI application instance.
    """
    app_instance.settings = config.get_settings()

    # Initialize the database connector instances
    postgres_connector = PostgresConnector(db_path=app_instance.settings.pg_db_url)
    sqlite_connector = SQLiteConnector(db_path=app_instance.settings.sqlite_db_url)

    # Initialize the database connection pool
    app_instance.async_pool = AsyncConnectionPool(
        conninfo=postgres_connector.get_db_connection_str()
    )

    yield  # Pause for code to run here (API runtime)

    await app_instance.async_pool.close()


# Create FastAPI instance with lifespan context manager
app = FastAPI(
    title="FastAPI application",
    description="This is a description... write something better",
    version="0.1.0",
    openapi_url="/api/openapi.json",
    lifespan=app_lifespan
)

# CORS origins allowed
origins = ["*"]

# Initialize settings from environment configuration
settings = get_settings()

if __name__ == "__main__":
    import uvicorn

    # Initialize settings from environment configuration
    settings = get_settings()

    # Uvicorn Run Server
    uvicorn.run(
        app,
        host=settings.app_host,
        port=settings.app_port,
        reload=settings.app_reload,
    )
