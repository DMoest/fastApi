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
