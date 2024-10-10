#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
User schema for the database
"""

import json
from collections import namedtuple
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from sqlalchemy import String
from src.utils.nano_id import generate_nano_id


class UserCreate(BaseModel):
    """
    Schema for creating a new User instance.
    """
    id: Optional[str] = Field(default_factory=generate_nano_id)
    username: str
    email: str
    hashed_password: str
    first_name: str
    last_name: str
    phone_number: str
    address: str
    city: str
    state: str
    country: str
    zip_code: str

    # User roles
    is_active: bool = True
    is_superuser: bool = False

    # Timestamps
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    deleted_at: Optional[datetime] = None

    class Config:
        """
        Pydantic configuration schema. Inherits from BaseModel.Config.
        """
        from_attributes = True
        str_strip_whitespace = True
        arbitrary_types_allowed = True
        str_min_length = 1
        str_max_length = 255
        json_encoders = {
            datetime: lambda dt: dt.timestamp()
        }


class UserUpdate(BaseModel):
    """
    Schema for updating an existing User instance.
    """
    id: Optional[str]
    username: Optional[str]
    email: Optional[str]
    hashed_password: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    zip_code: Optional[str]


class UserSimple(BaseModel):
    """
    Schema for retrieving a simple representation of a User instance.
    """
    id: str
    username: str
    email: str
    first_name: str
    last_name: str

    class Config:
        """
        Pydantic configuration schema. Inherits from BaseModel.Config.
        """
        from_attributes = True
        str_min_length = 1
        str_max_length = 255
        str_strip_whitespace = True
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda dt: dt.timestamp()
        }


class UserOutput(UserCreate):
    """
    Schema for retrieving a User instance.
    """
    id: Optional[str]
    username: Optional[str]
    email: Optional[str]
    hashed_password: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    zip_code: Optional[str]

    class Config:
        """
        Pydantic configuration schema. Inherits from UserCreate.Config.
        """
        from_attributes = True
        str_strip_whitespace = True
        arbitrary_types_allowed = True
        str_min_length = 1
        str_max_length = 255
        json_encoders = {
            datetime: lambda dt: dt.timestamp()
        }

    def __str__(self) -> str:
        """
        Returns a string representation of the UserOutput instance.
        """
        return json.dumps(self.dict(), indent=2)

    def __eq__(self, other: UserOutput) -> bool:
        """
        Compares two UserOutput instances for equality.
        """
        return self.dict() == other.dict()

    def __ne__(self, other: UserOutput) -> bool:
        """
        Compares two UserOutput instances for inequality.
        """
        return self.dict() != other.dict()

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
        Returns a namedtuple representation of the UserOutput instance.
        """
        user_named_tuple = namedtuple('User', self.model_fields.keys())
        return user_named_tuple(**self.model_dump())
