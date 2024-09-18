#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
PostgreSQL Database configuration module for the FastAPI application.

This module contains the configuration for the PostgreSQL database used in
the application.

The following functions are defined:

- init_db: Function to initialize the database.
- get_db: Function to get a database session.
- run_pg_dump: Function to run the pg_dump command to backup the database.

Each function includes a detailed docstring with information about its
purpose, the parameters it takes, the response it returns, and any
exceptions it might raise.
"""

# import subprocess
# from app.config import get_settings
# from app.exceptions.custom_exceptions import DatabaseError
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# Import all models here...
# from app.db.v1_models.ab_point_model import ABPoint
# from app.db.v1_models.boundary_point_model import BoundaryPoint
# from app.db.v1_models.detection_model import Detection
# from app.db.v1_models.field_model import Field
# from app.db.v1_models.location_model import Location
# from app.db.v1_models.mission_model import Mission
# from app.db.v1_models.robot_model import Robot
# from app.db.v1_models.row_model import Row
# from app.db.v1_models.row_point_model import RowPoint
# from app.db.v1_models.sliproad_model import Sliproad
# from app.db.v1_models.sliproad_point_model import SliproadPoint
# from app.db.v1_models.tool_model import Tool
# from app.db.v1_models.user_model import User

# Get the database URL from the settings
settings = get_settings()
DATABASE_URL = settings.pg_db_url

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a sessionmaker class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """
    Function to initialize the database.

    This function does not take any parameters and does not return anything.
    """
    # User.metadata.create_all(engine)
    # Robot.metadata.create_all(engine)
    # Tool.metadata.create_all(engine)
    # Mission.metadata.create_all(engine)
    # ABPoint.metadata.create_all(engine)
    # BoundaryPoint.metadata.create_all(engine)
    # Location.metadata.create_all(engine)
    # Field.metadata.create_all(engine)
    # Sliproad.metadata.create_all(engine)
    # SliproadPoint.metadata.create_all(engine)
    # Row.metadata.create_all(engine)
    # RowPoint.metadata.create_all(engine)
    # Detection.metadata.create_all(engine)


def get_db():
    """
    Function to get a database session.

    This function does not take any parameters and returns a database session.

    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def run_pg_dump(command: str) -> bytes:
    """
    Run the pg_dump command to backup the database.

    :param command: Command to run.
    :type command: str
    :return: Output of the command.
    :rtype: bytes
    :raises DatabaseError: If there is an error running the command.

    """
    try:
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE
        )
        output, error = process.communicate()

        if error:
            raise DatabaseError(error)
        return output

    except DatabaseError as error:
        raise error
