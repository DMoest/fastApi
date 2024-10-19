#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Application model for the database
"""

from datetime import datetime

from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.orm import Mapped

from src.db.config.base import Base


class ApplicationModel(Base):
    """
    Application model for the database
    """
    __tablename__ = 'applications'

    id: Mapped[str] = Column(String, primary_key=True, index=True)
    name: Mapped[str] = Column(String, unique=True, index=True)
    description: Mapped[str] = Column(String)
    url: Mapped[str] = Column(String)
    is_active: Mapped[bool] = Column(Boolean, default=True)
    api_key: Mapped[str] = Column(String)

    # Timestamps
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = Column(DateTime, default=datetime.utcnow)
    deleted_at: Mapped[datetime] = Column(DateTime, default=None)

    def __dir__(self) -> list:
        """
        Return the list of columns in the table

        :return: The list of columns in the table
        :rtype: list
        """
        return self.__table__.columns.keys()

    def __str__(self) -> str:
        """
        Return the string representation of the model

        :return: The string representation of the model
        :rtype: str
        """
        return (f"ApplicationModel(id={self.id}, name={self.name}, "
                f"description={self.description}, url={self.url})")

    def __eq__(self, other) -> bool:
        """
        Check if two ApplicationModel instances are equal

        :param other: The other ApplicationModel instance to compare with
        :type other: ApplicationModel
        :return: True if the two instances are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, ApplicationModel):
            return self.id == other.id
        return False
