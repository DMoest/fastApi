#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
This module contains the configuration settings for the FastAPI application.
"""

import os
from functools import lru_cache
from pydantic import (Field)
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Class to define the configuration settings for the application.
    """

    # --- Environment -------------------------------------------------------
    env_name: str = Field(default="development", env_name="ENV_NAME")

    # --- Application -------------------------------------------------------
    app_name: str = Field(default="Fast API application", env_name="APP_NAME")
    app_host: str = Field(default="localhost", env_name="APP_HOST")
    app_port: int = Field(default=1337, env_name="APP_PORT")
    app_reload: bool = Field(default=True, env_name="APP_RELOAD")

    # --- Secret Keys (JWT) --------------------------------------------------
    app_algorithm: str = Field(default="HS256", env_name="APP_ALGORITHM")
    app_jwt_secret_key: str = Field(default="a_secret_key",
                                    env_name="APP_JWT_SECRET_KEY")

    # --- Logging settings ---------------------------------------------------
    app_log_level: str = Field(default="DEBUG", env_name="APP_LOG_LEVEL")
    app_log_name: str = Field(default="api_logger", env_name="APP_LOG_NAME")
    app_log_file_dir: str = os.getcwd() + "../log"
    app_log_file_name: str = Field(default="fastapi_log",
                                   env_name="APP_LOG_FILE_NAME")
    app_log_file_mode: str = Field(default="w", env_name="APP_LOG_FILE_MODE")
    app_log_file_size: int = Field(default=1000000,
                                   env_name="APP_LOG_FILE_SIZE")
    app_log_file_count: int = Field(default=3, env_name="APP_LOG_FILE_COUNT")
    app_log_format: str = Field(
        default="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        env_name="APP_LOG_FORMAT")
    app_log_formatter: str = Field(default="defaut",
                                   env_name="APP_LOG_FORMATTER")
    app_log_propagate: bool = Field(default=False,
                                    env_name="APP_LOG_PROPAGATE")

    # --- Postgres Database --------------------------------------------------
    pg_db_url: str = Field(
        default="postgresql://a_postgresql_db_username"
                ":a_postgresql_db_password@the_db_host:5432/the_db_name",
        env_name="PG_DB_URL"
    )
    pg_db_name: str = Field(default="the_db_name", env_name="PG_DB_NAME")
    pg_db_host: str = Field(default="the_db_host", env_name="PG_DB_HOST")
    pg_db_port: int = Field(default=5432, env_name="PG_DB_PORT")
    pg_db_username: str = Field(default="a_postgresql_db_username",
                                env_name="PG_DB_USERNAME")
    pg_db_password: str = Field(default="a_postgresql_db_password",
                                env_name="PG_DB_PASSWORD")
    pg_db_backup_dir: str = os.getcwd() + "/db/backups"

    # --- MongoDB Database ---------------------------------------------------
    mongo_db_url: str = Field(
        default="mongodb://a_mongodb_db_username:a_mongodb_db_password"
                "@the_db_host:27017", env_name="MONGO_DB_URL")
    mongo_db_name: str = Field(default="the_mongo_db_name",
                               env_name="MONGO_DB_NAME")
    mongo_db_host: str = Field(default="the_mongo_db_host",
                               env_name="MONGO_DB_HOST")
    mongo_db_port: int = Field(default=27017, env_name="MONGO_DB_PORT")
    mongo_db_username: str = Field(default="a_mongodb_db_username",
                                   env_name="MONGO_DB_USERNAME")
    mongo_db_password: str = Field(default="a_mongodb_db_password",
                                   env_name="MONGO_DB_PASSWORD")

    # SQLite3 Database settings
    sqlite_db_url: str = Field(default="sqlite:///a_sqlite_db_name.db",
                               env_name="SQLITE_DB_URL")

    # Pydantic config of .env file
    model_config = SettingsConfigDict(env_file=".env")

    def __str__(self) -> str:
        """
        Method to return the string representation of the class.
        """
        return str(self.__dict__)


@lru_cache
def get_settings() -> Settings:
    """
    Function to get the settings.
    """
    return Settings()
