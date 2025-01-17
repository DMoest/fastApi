#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Test suit for the Health Check route in the FastAPI application.
"""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_app_healt_check() -> None:
    """
    Test the health check endpoint of the FastAPI application.
    """
    response = client.get("/api/utils/health_check")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == "Server is OK"
