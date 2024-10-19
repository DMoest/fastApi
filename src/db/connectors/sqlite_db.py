#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
SQLite Database configuration module for the FastAPI application.

This module contains the `SQLiteConnector` class, which manages the SQLite
database connection using SQLAlchemy's asynchronous engine and session maker.
"""

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, \
    AsyncSession

from src.core.env_config import get_settings


class SQLiteConnector:
    """
    A class to manage the SQLite database connection for a FastAPI application.

    This class encapsulates the configuration and management of the SQLite
    database connection using SQLAlchemy's asynchronous engine and session maker.

    :ivar DATABASE_URL: The database URL for connecting to SQLite.
    :vartype DATABASE_URL: str
    :ivar sqlite_engine: The SQLAlchemy asynchronous engine for the database.
    :vartype sqlite_engine: AsyncEngine
    :ivar AsyncSessionLocal: The SQLAlchemy session maker for creating async sessions.
    :vartype AsyncSessionLocal: async_sessionmaker

    Methods
    -------
    get_db() -> AsyncSession
        Asynchronously yields a database session.

    get_db_connection_str() -> str
        Returns the database connection string.
    """

    def __init__(self, db_path: str = None):
        """
        Initialize the SQLiteConnector instance.

        This method sets up the database URL, creates an asynchronous database engine,
        and initializes the asynchronous session maker.

        :param db_path: The file path to the SQLite database.
        :type db_path: str
        """
        print(f"Initializing SQLite connector with db_path: {db_path}")
        settings = get_settings()

        if db_path is None:
            self._database_url = settings.sqlite_db_url.replace(
                "sqlite://",
                "sqlite+aiosqlite://")
        else:
            self._database_url = db_path.replace(
                "sqlite://",
                "sqlite+aiosqlite://")

        self.sqlite_engine = create_async_engine(self._database_url)
        self.AsyncSessionLocal = async_sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.sqlite_engine,
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

    def get_db_ulr(self) -> str:
        """
        Method to get the database URL.

        :return: The database URL.
        :rtype: str
        """
        return self._database_url
