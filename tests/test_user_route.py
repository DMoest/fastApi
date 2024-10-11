#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Test suit for the User routes in the FastAPI application.
"""

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_read_main():
    """
    Test the options endpoint of the FastAPI application.
    """
    response = client.options("/api/v1/users")

    assert response.status_code == 204
    assert response.headers["allow"] == "GET, POST, PUT, PATCH, DELETE"
    assert response.content == b""

# def test_read_users():
#     """
#     Test the GET endpoint of the /users route.
#     """
#     response = client.get("/api/v1/users")
#
#     assert response.status_code == 200
#     assert response.json() == []
