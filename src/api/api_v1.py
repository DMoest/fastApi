#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
API v1 Router
"""

from fastapi import APIRouter, Depends
from core.auth import get_api_key

api_v1_router = APIRouter(
    prefix="/api/v1",
    dependencies=[Depends(get_api_key)],
    responses={
        404: {"description": "Not found"}
    },
)
