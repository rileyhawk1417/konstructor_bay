#!/usr/bin/env python3
"""
creating shopping chart table
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Cart(Base, BaseModel):
    """
    cart
    """
    __tablename__ = 'cart'
    user_id = Column(String(100), ForeignKey('user.id'), nullable=True)
    product_id = Column(String(100), ForeignKey('products.id'), nullable=False)
    user = relationship('User', backref='cart')
    product = relationship('Product', backref='cart')
