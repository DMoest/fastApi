#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Utility routes for the FastAPI application.
"""

import logging

from fastapi import APIRouter, status
from fastapi.responses import ORJSONResponse

from src.core.env_config import get_settings

health_check_router = APIRouter()
settings = get_settings()
logger = logging.getLogger(settings.app_logger_name or "application_logger")


# Health check endpoint
@health_check_router.get("")
async def health_check() -> ORJSONResponse:
    """
    Health check endpoint to verify the application status

    :return: JSON response with status code 200
    :rtype: ORJSONResponse
    """
    logger.info("Health check endpoint called...")
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content="Server is OK"
    )
