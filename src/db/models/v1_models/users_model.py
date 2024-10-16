#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
User model for the database
"""

from datetime import datetime

from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.orm import Mapped

from src.db.config.base import Base


class UserModel(Base):
    """
    User model for the database
    """
    __tablename__ = 'users'

    id: Mapped[str] = Column(String, primary_key=True, index=True)
    username: Mapped[str] = Column(String, unique=True, index=True)
    email: Mapped[str] = Column(String, unique=True, index=True)
    password: Mapped[str] = Column(String)

    # User details
    first_name: Mapped[str] = Column(String)
    last_name: Mapped[str] = Column(String)
    phone_number: Mapped[str] = Column(String)
    address: Mapped[str] = Column(String)
    city: Mapped[str] = Column(String)
    state: Mapped[str] = Column(String)
    country: Mapped[str] = Column(String)
    zip_code: Mapped[str] = Column(String)

    # User roles
    is_active: Mapped[bool] = Column(Boolean, default=True)
    is_superuser: Mapped[bool] = Column(Boolean, default=False)

    # Timestamps
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = Column(DateTime, default=datetime.utcnow)
    deleted_at: Mapped[datetime] = Column(DateTime, default=None)
