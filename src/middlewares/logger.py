#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains the logger configuration for the FastAPI application.
"""
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from core.config import get_settings
from core.logger_config import init_logger


class LoggerMiddleware(BaseHTTPMiddleware):
    """
    Middleware class for logging requests
    """

    def __init__(self, app):
        """
        Constructor method for the LoggerMiddleware class

        :param app: FastAPI application instance
        :type app: FastAPI
        """
        settings = get_settings()

        super().__init__(app)
        self.logger = init_logger(settings.console_logger_name)

    async def dispatch(self, request: Request, call_next) -> Response:
        """
        Log the request and response

        :param request: Request object
        :type request: Request
        :param call_next: Next middleware to call
        :type call_next: Callable
        :return: Response object
        :rtype: Response
        """
        # Log the request
        self.logger.info("Request: %s %s", request.method, request.url)

        # Call the next middleware
        response = await call_next(request)

        # Log the response
        self.logger.info("Response: %s", response.status_code)

        return response
