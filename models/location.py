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
    user_id = Column(String(100), ForeignKey('user.id'), nullable=False)
    user = relationship("User", backref="locations_ref", foreign_keys=[user_id])
    country = Column(String(24), nullable=False)
    county = Column(String(50), nullable=False)
    zone = Column(String(60), nullable=True)
