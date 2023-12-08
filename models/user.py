#!/usr/bin/env python3
"""
user model
"""
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from models.supplier import Supplier

class User(Base, BaseModel):
    """
    creating user on table name user
    """
    __tablename__ = "user"
    firstName = Column(String(18), nullable=True)
    sec_name = Column(String(18), nullable=True)
    username = Column(String(25), nullable=True)
    email = Column(String(256), nullable=True)
    phone_num = Column(String(20), nullable=True)
    password = Column(String(256), nullable=True)
    location = relationship("Location", back_populates="user", uselist=False,cascade="all, delete")
    supplier_id = Column(String(256), ForeignKey("supplier.id"))
    supplier = relationship("Supplier", 
        back_populates="supplier_user", 
        uselist=False, cascade="all, delete", 
        primaryjoin='User.id == Supplier.user_id',
        foreign_keys=[Supplier.user_id],
        viewonly=True
    ) 
    
    def __repr__(self):
        """Returns a string representation of the User object"""
        return f"User: id={self.id}, firstName={self.firstName}, email={self.email}" 