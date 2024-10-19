#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
This module contains the logger configuration for the FastAPI application.
"""

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from src.core.env_config import get_settings
from src.core.logger_config import init_logger


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
        self.logger = init_logger(settings.app_logger_name)

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
        self.log_request_details(request)

        # Call the next middleware
        response = await call_next(request)

        # Log the response
        self.log_response_details(response)

        return response

    def log_request_details(self, request: Request):
        """
        Log detailed information about the request

        :param request: Request object
        :type request: Request
        """
        self.logger.info("Request details: %s %s", request.method, request.url)

    def log_response_details(self, response: Response):
        """
        Log detailed information about the response

        :param response: Response object
        :type response: Response
        """
        self.logger.info("Response details: %s", response.status_code)
