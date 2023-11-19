#!/usr/bin/env python3
"""
table for user orders
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Order(Base, BaseModel):
    """
    order class
    """
    __tablename__ = 'orders'
    product_id = Column(String(100), ForeignKey('products.id'), nullable=False)    
    user_id = Column(String(100), ForeignKey('user.id'), nullable=True)
    user = relationship('User', backref='order')
    product = relationship('Product', backref='order')
