#!/usr/bin/env python3
"""
user model
"""
from sqlalchemy.orm import relationship
from base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey

class User(Base, BaseModel):
    """
    creating user on table name user
    """
    __tablename__ = "user"
    firstName = Column(String(18), nullable=False)
    sec_name = Column(String(18), nullable=False)
    username = Column(String(25), nullable=False)
    email = Column(String(256), nullable=True)
    phone_num = Column(String(20), nullable=False)
    password = Column(String(256), nullable=False)
    location = relationship("Location", backref="user")
    location_id = Column(String(256), ForeignKey("location.id"), nullable=False)