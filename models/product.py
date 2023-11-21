#!/usr/bin/env python3
"""
products model
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class Product(Base, BaseModel):
    __tablename__ = "products"
    product_name = Column(String(239), nullable=True)
    description = Column(String(350), nullable=True)
    quantity = Column(Integer, nullable=True)
    price = Column(Integer, nullable=True)
    #img_filename = Column(String(256), nullable=True)
    user_id = Column(String(256), ForeignKey('user.id'), nullable=True)
    location_id = Column(String(256), ForeignKey('location.id'), nullable=True)
    user = relationship("User", backref="product")
