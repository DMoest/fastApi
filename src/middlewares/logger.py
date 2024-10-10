# src/utils/logger.py
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Logger utility module for the FastAPI application.
"""
import os
from datetime import datetime
from src.core.config import get_settings
import logging
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response


class LoggerMiddleware(BaseHTTPMiddleware):
    """
    Middleware class for logging requests
    """

    def __init__(self, app):
        env_settings = get_settings()
        super().__init__(app)
        self.logger = logging.getLogger(env_settings.app_log_name)
        self.logger.setLevel(env_settings.app_log_level)

        formatter = logging.Formatter(fmt=env_settings.app_log_format)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        log_dir = env_settings.app_log_file_dir
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(
            log_dir,
            f'{datetime.date(datetime.utcnow())}_'
            f'{env_settings.app_log_name}.log'
        )
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)

    async def dispatch(self, request: Request, call_next):
        self.logger.info(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        self.logger.info(f"Response: {response.status_code}")
        return response
