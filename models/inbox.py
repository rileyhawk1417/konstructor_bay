#!/usr/bin/env python3
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Inbox(Base, BaseModel):
    __tablename__ = "inbox"
    message= Column(String(4096), nullable=True)
    user_id = Column(String(256), ForeignKey('user.id'), nullable=True)
    user = relationship("User", backref="inbox")
    
    supplier = relationship("Supplier", backref="inbox")