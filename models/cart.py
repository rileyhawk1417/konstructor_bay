#!/usr/bin/env python3
"""
creating shopping chart table
"""
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

"""
creates a new table with table with association of product and cart
"""

cart_product_association = Table(
    'cart_product_association', Base.metadata,
    Column('cart_id', String(100), ForeignKey('cart.id')),
    Column('product_id', String(100), ForeignKey('products.id'))
)

class Cart(Base, BaseModel):
    """
    cart
    """

    __tablename__ = 'cart'
    user_id = Column(String(100), ForeignKey('user.id'), nullable=True)
    #product_id = Column(String(100), ForeignKey('products.id'), nullable=True)
    user = relationship('User', backref='cart')
    #product = relationship('Product', backref='cart')
    products = relationship('Product', secondary=cart_product_association, backref='carts')
 
    
