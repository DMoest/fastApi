#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Utility routes for the FastAPI application.
"""

from fastapi import APIRouter

from src.api.health_check_routes import check_routes

api_utility_router = APIRouter(
    prefix="/api/utils",
    # dependencies=[Depends(get_api_key)],
    responses={
        404: {"description": "Not found"}
    },
)

api_utility_router.include_router(
    check_routes.health_check_router,
    prefix="/health_check",
    tags=["health"]
)
