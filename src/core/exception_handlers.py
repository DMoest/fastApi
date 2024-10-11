#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Exception handlers module for the FastAPI application.
"""

from fastapi import Request, HTTPException
from fastapi.responses import ORJSONResponse

from core.custom_exceptions import AuthException, BadRequestException, \
    ConflictException, DatabaseException, InternalServerException, \
    NotFoundException, ValidationException


async def auth_exception_handler(request: Request,
                                 exc: AuthException) -> ORJSONResponse:
    """
    Exception handler for AuthException exceptions.
    """
    return ORJSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )


async def bab_request_exception_handler(request: Request,
                                        exc: BadRequestException) -> (
        ORJSONResponse):
    """
    Exception handler for HTTPException exceptions.
    """
    return ORJSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )


async def conflict_exception_handler(request: Request,
                                     exc: ConflictException) -> ORJSONResponse:
    """
    Exception handler for ConflictException exceptions.
    """
    return ORJSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )


async def database_exception_handler(request: Request,
                                     exc: DatabaseException) -> ORJSONResponse:
    """
    Exception handler for DatabaseException exceptions.
    """
    return ORJSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )


async def internal_server_exception_handler(request: Request,
                                            exc: InternalServerException) -> (
        ORJSONResponse):
    """
    Exception handler for InternalServerException exceptions.
    """
    return ORJSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )


async def not_found_exception_handler(request: Request,
                                      exc: NotFoundException) -> (
        ORJSONResponse):
    """
    Exception handler for NotFoundException exceptions.
    """
    return ORJSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )


async def validation_exception_handler(request: Request,
                                       exc: ValidationException) -> ORJSONResponse:
    """
    Exception handler for ValidationException exceptions.
    """
    return ORJSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )


async def http_exception_handler(request: Request,
                                 exc: HTTPException) -> ORJSONResponse:
    """
    Exception handler for HTTPException exceptions.
    """
    return ORJSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )
