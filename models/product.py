#!/usr/bin/env python3
"""
products model
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
class Product(Base, BaseModel):
    __tablename__ = "products"
    product_name = Column(String(239), nullable=False)
    description = Column(String(350), nullable=False)
    img_filename = Column(String(256), nullable=False)
    user_id = Column(String(256), ForeignKey('user.id'), nullable=False)
    location_id = Column(String(256), ForeignKey('locations.id'), nullable=True)
    user = relationship("User", backref="location_ref")
