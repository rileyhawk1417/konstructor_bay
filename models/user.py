from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel  # Assuming BaseModel is correctly defined

class User(BaseModel):
    __tablename__ = "users"  # Adjusted table name to plural form

    user_id = Column(Integer, primary_key=True)
    firstName = Column(String(18), nullable=False)
    sec_name = Column(String(18), nullable=False)
    username = Column(String(25), nullable=False)
    email = Column(String(256), nullable=True)
    phone_num = Column(String(20), nullable=False)
    password = Column(String(256), nullable=False)

    # Adjusted ForeignKey reference corresponding to the Location table
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    location = relationship("Location", backref="user")
