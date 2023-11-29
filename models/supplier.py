#!/usr/bin/env python3
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
#from models.user import User

class Supplier(Base, BaseModel):
    """
    supplier
    """
    __tablename__ = "supplier"
    business_name = Column(String(150), nullable=True)
    business_location = Column(String(120), nullable=True)
    email = Column(String(170), nullable=True)
    phone_num = Column(String(50), nullable=True)
    delivery = Column(Boolean, nullable=True)
    user = relationship("User", backref="supplier")
    user_id = Column(String(256), ForeignKey('user.id'), nullable=True)
    #inbox = relationship("Inbox", backref="supplier")
    inbox_id = Column(String(256), ForeignKey('inbox.id'), nullable=True)
