#!/usr/bin/env python3
"""
location model
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Location(Base, BaseModel):
    """
    location for user, product
    """
    __tablename__ = "location"
    user_id = Column(String(100), ForeignKey('user.id'), nullable=True)
    user = relationship("User", back_populates="location")
    country = Column(String(24), nullable=True)
    state = Column(String(50), nullable=True)
    town = Column(String(60), nullable=True)
