#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
This module is the main entry point of the FastAPI application.
"""

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from psycopg_pool import AsyncConnectionPool

from api.api_v1 import api_v1_router
from core.custom_exceptions import AuthException, BadRequestException, \
    ConflictException, DatabaseException, InternalServerException, \
    NotFoundException, ValidationException, HTTPException
from src.core import config
from src.core.auth import get_api_key
from src.core.config import get_settings
from src.core.exception_handlers import auth_exception_handler, \
    bab_request_exception_handler, conflict_exception_handler, \
    database_exception_handler, http_exception_handler, \
    internal_server_exception_handler, not_found_exception_handler, \
    validation_exception_handler
from src.db.connectors.postgres_db import PgsqlDbSessionManager
from src.middlewares.logger import LoggerMiddleware


@asynccontextmanager
async def app_lifespan(app_instance: FastAPI):
    """
    Lifespan context manager for the FastAPI application instance.
    """
    app_instance.settings = config.get_settings()

    # Initialize the database connector instances
    postgres_connector = PgsqlDbSessionManager()
    # sqlite_connector = SQLiteConnector()

    # Initialize the database connection pool
    app_instance.async_pool = AsyncConnectionPool(
        conninfo=postgres_connector.get_db_connection_str()
    )

    yield  # Pause for code to run here (API runtime)

    # Close the database connection pool
    await app_instance.async_pool.close()


# Create FastAPI instance with lifespan context manager
app = FastAPI(
    title="FastAPI application",
    description="This is a description... write something better",
    version="0.1.0",
    openapi_url="/api/openapi.json",
    lifespan=app_lifespan,
    debug=os.getenv("APP_DEBUG", False)
)

# CORS origins allowed
origins = ["*"]

# Initialize settings from environment configuration
settings = get_settings()

# Exception handlers
app.add_exception_handler(AuthException, auth_exception_handler)
app.add_exception_handler(BadRequestException, bab_request_exception_handler)
app.add_exception_handler(ConflictException, conflict_exception_handler)
app.add_exception_handler(DatabaseException, database_exception_handler)
app.add_exception_handler(InternalServerException,
                          internal_server_exception_handler)
app.add_exception_handler(NotFoundException, not_found_exception_handler)
app.add_exception_handler(ValidationException, validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)

# Middleware
app.add_middleware(LoggerMiddleware)

# Include routers
app.include_router(
    api_v1_router,
    dependencies=[Depends(get_api_key)]
)

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
