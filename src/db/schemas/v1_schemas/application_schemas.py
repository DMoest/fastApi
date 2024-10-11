#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Application schema for the database
"""

import json
from collections import namedtuple
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict, field_serializer

from src.utils.nano_id import generate_nano_id


class ApplicationCreate(BaseModel):
    """
    Schema for creating a new Application instance.
    """
    id: Optional[str] = Field(default_factory=generate_nano_id)
    name: str
    description: str
    url: str
    is_active: bool = True
    api_key: str

    # Timestamps
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    deleted_at: Optional[datetime] = None

    @field_serializer('created_at', 'updated_at', 'deleted_at')
    def serialize_datetime(self, value: datetime) -> float:
        """ Serialize datetime to timestamp """
        return value.timestamp()

    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
        arbitrary_types_allowed=True,
        str_min_length=1,
        str_max_length=255
    )


class ApplicationUpdate(BaseModel):
    """
    Schema for updating an existing Application instance.
    """
    name: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    is_active: Optional[bool] = None
    api_key: Optional[str] = None

    # Timestamps
    updated_at: Optional[datetime] = datetime.utcnow()
    deleted_at: Optional[datetime]

    @field_serializer('updated_at', 'deleted_at')
    def serialize_datetime(self, value: datetime) -> float:
        """ Serialize datetime to timestamp """
        return value.timestamp()

    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
        arbitrary_types_allowed=True,
        str_min_length=1,
        str_max_length=255
    )


class ApplicationOutput(ApplicationCreate):
    """
    Schema for returning an Application instance.
    """
    id: Optional[str]
    name: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    is_active: Optional[bool] = None
    api_key: Optional[str] = None

    def __str__(self) -> str:
        """
        String representation of the ApplicationOutput instance.

        :return: Object representation as a string
        :rtype: str
        """
        return json.dumps(self.dict(), indent=2)

    def __eq__(self, other: object) -> bool:
        """
        Equality comparison between two ApplicationOutput instances.

        :param other: ApplicationOutput instance
        :type other: object
        :return: Boolean value indicating equality
        :rtype: bool
        """
        return self.dict() == other.__dict__

    def __ne__(self, other: object) -> bool:
        """
        Inequality comparison between two ApplicationOutput instances.

        :param other: ApplicationOutput instance
        :type other: object
        :return: Boolean value indicating inequality
        :rtype: bool
        """
        return self.dict() != other.__dict__

    def __getattr__(self, item):
        """
        Returns the value of the attribute with the given name.
        """
        if item in self.model_fields_set:
            return getattr(self, item)
        raise AttributeError(
            f"'{type(self).__name__}' object has no attribute '{item}'")

    def as_named_tuple(self) -> namedtuple:
        """
        Returns the ApplicationOutput instance as a named tuple.

        :return: ApplicationOutput instance as a named tuple
        :rtype: namedtuple
        """
        return namedtuple(
            'Application',
            self.dict().keys())(**self.dict())
