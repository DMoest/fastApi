#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Test suit for the User routes in the FastAPI application.
"""

import os

from fastapi.testclient import TestClient

from src.db.config.base import Base
from src.db.connectors.postgres_db import get_pg_db
from src.db.connectors.sqlite_db import SQLiteConnector
from src.main import app

# Ensure the directory exists
os.makedirs(os.path.dirname("src/db/test_data_storage.db"), exist_ok=True)

# Initialize SQLiteConnector
TEST_DB_URL = "sqlite:///src/db/test_data_storage.db"
sqlite_connector = SQLiteConnector(TEST_DB_URL)

# Override the get_pg_db dependency
app.dependency_overrides[get_pg_db] = sqlite_connector.get_sqlite_db
client = TestClient(app)


def setup():
    """
    Creates all the database tables.
    """
    Base.metadata.create_all(sqlite_connector.sqlite_engine)


def teardown():
    """
    Drop all the database tables.
    """
    Base.metadata.drop_all(sqlite_connector.sqlite_engine)


def test_users_options_route():
    """
    Test the options endpoint of the FastAPI application.
    """
    response = client.options("/api/v1/users")
    assert response.status_code == 204
    assert response.headers["allow"] == "GET, POST, PUT, PATCH, DELETE"
    assert response.content == b""


def test_read_users():
    """
    Test the GET endpoint of the /users route.
    """
    response = client.get("/api/v1/users")
    assert response.status_code == 200
    assert response.json() == []
