#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Base module for the database configuration.

This module contains the base class for the database configuration.

The following class is defined:

- Base: The declarative base class for SQLAlchemy.

Each class includes a detailed docstring with information about its purpose.
"""

import logging

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure

from src.core.env_config import get_settings

settings = get_settings()
logger = logging.getLogger(settings.app_logger_name)


class MongoDBConnector:
    """
    MongoDBConnector is a singleton class that creates a single instance of an
    async MongoDB client.

    This class defines the following methods:

    - __new__: Creates a single instance of the MongoDBConnector class.
    - client: Returns the MongoDB client instance.
    - test_connection: Asynchronously tests the connection to the MongoDB
        deployment.
    - get_collection: Returns a MongoDB collection.
    - close_connection: Closes the MongoDB connection.
    """
    _instance = None
    _uri = None

    def __new__(cls, uri) -> AsyncIOMotorClient:
        """
        Creates a single instance of the MongoDBConnector class.

        :param uri: The MongoDB connection URI.
        :type uri: str
        :return: The MongoDBConnector instance.
        :rtype: MongoDBConnector
        """
        logger.info("Initializing the MongoDBConnector instance...")

        if cls._instance is None:
            cls._instance = super(MongoDBConnector, cls).__new__(cls)
            cls._uri = uri
            cls._client = AsyncIOMotorClient(cls._uri)

        return cls._instance

    @property
    def client(self):
        """
        Returns the MongoDB client instance.

        :return: The MongoDB client instance.
        :rtype: AsyncIOMotorClient

        """
        return self._client

    async def test_connection(self):
        """
        Asynchronously tests the connection to the MongoDB deployment.
        """
        logger.info("Testing the MongoDB Connection...")

        try:
            await self._client.admin.command('ping')
            print("Successfully CONNECTED to MongoDB!")
        except ConnectionFailure as e:
            print(f"Failed to connect to MongoDB:\n{e}")
            raise

    def get_collection(self, collection_name: str):
        """
        Returns a MongoDB collection.

        :param collection_name: The name of the MongoDB collection.
        :type collection_name: str
        :return: The MongoDB collection.
        :rtype: Collection
        """
        logger.info("Get MongoDB collection...")

        return self._client.db_name[collection_name]

    async def close_connection(self):
        """
        Closes the MongoDB connection.
        """
        logger.info("Closing MongoDB connection...")
        self._client.close()
        logger.info("MongoDB connection is closed...")


# Register MongoDBConnector as a FastAPI dependency
async def get_mongo_connector() -> MongoDBConnector:
    """
    Returns the MongoDBConnector instance.

    :return: The MongoDBConnector instance.
    :rtype: MongoDBConnector
    """
    logger.info("Getting the MongoDBConnector instance...")
    mongo_connector = MongoDBConnector(uri=settings.mongo_db_url)
    yield mongo_connector
    await mongo_connector.close_connection()
    logger.info("MongoDB connection closed...")
