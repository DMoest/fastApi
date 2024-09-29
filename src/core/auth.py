#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains the authentication logic for the FastAPI application.
"""

import os
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyQuery, APIKeyHeader


# Auth headers & query params
api_key_query = APIKeyQuery(name="api_key", auto_error=False)
api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)

# Allowed API keys for authentication of applications accessing the API
API_KEYS = [
    os.getenv("API_KEY_1", None),
    os.getenv("API_KEY_2", None)
]

async def get_api_key(
        query_api_key: str = Security(api_key_query),
        header_api_key: str = Security(api_key_header),
) -> str:
    """
    Validate the API key provided in the query parameters or headers.

    This function checks if the API key provided in the query parameters or
    headers matches any of the predefined API keys. If a valid API key is
    found, it is returned. Otherwise, an HTTP 401 Unauthorized exception is
    raised.

    :param query_api_key: The API key provided in the query parameters.
    :type query_api_key: str
    :param header_api_key: The API key provided in the headers.
    :type header_api_key: str
    :return: The valid API key.
    :rtype: str
    :raises HTTPException: If the API key is invalid or missing.
    """
    if api_key_query in API_KEYS:
        return query_api_key
    if header_api_key in API_KEYS:
        return header_api_key
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )
