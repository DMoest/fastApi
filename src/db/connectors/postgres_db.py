#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Postgres Database configuration module for the FastAPI application.

This module contains the `PostgresConnector` class, which manages the PostgreSQL
database connection using SQLAlchemy's asynchronous engine and session maker.
"""

import os
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from src.core.config import get_settings

class PostgresConnector:
    """
    A class to manage the PostgreSQL database connection for a FastAPI application.

    This class encapsulates the configuration and management of the PostgreSQL
    database connection using SQLAlchemy's asynchronous engine and session maker.

    :ivar POSTGRES_DATABASE_URL: The database URL for connecting to PostgreSQL.
    :vartype POSTGRES_DATABASE_URL: str
    :ivar pgsql_engine: The SQLAlchemy asynchronous engine for the database.
    :vartype pgsql_engine: AsyncEngine
    :ivar AsyncSessionLocal: The SQLAlchemy session maker for creating async sessions.
    :vartype AsyncSessionLocal: async_sessionmaker

    Methods
    -------
    get_db() -> AsyncSession
        Asynchronously yields a database session.

    get_db_connection_str() -> str
        Returns the database connection string.
    """
    def __init__(self, db_path: str):
        """
        Initialize the PostgresConnector instance.

        This method sets up the database URL, creates an asynchronous database engine,
        and initializes the asynchronous session maker.

        Attributes
        ----------
        POSTGRES_DATABASE_URL : str
            The database URL for connecting to PostgreSQL, modified to use the asyncpg driver.
        pgsql_engine : AsyncEngine
            The SQLAlchemy asynchronous engine for the database.
        AsyncSessionLocal : async_sessionmaker
            The SQLAlchemy session maker for creating async sessions.
        """
        print(f"Initializing Postgres connector with db_path: {db_path}")

        settings = get_settings()
        self.POSTGRES_DATABASE_URL = f"postgresql+asyncpg://{db_path}"
        self.pgsql_engine = create_async_engine(self.POSTGRES_DATABASE_URL)
        self.AsyncSessionLocal = async_sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.pgsql_engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async def get_db(self) -> AsyncSession:
        """
        Method to get a database session.

        This method does not take any parameters and returns a database session.

        :return: A database session.
        :rtype: AsyncSession
        """
        async with self.AsyncSessionLocal() as db:
            try:
                yield db
            finally:
                await db.close()

    def get_db_connection_str(self) -> str:
        """
        Method to get the database connection string.

        :return: The database connection string.
        :rtype: str
        """
        return self.POSTGRES_DATABASE_URL
