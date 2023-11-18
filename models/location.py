from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel  # Assuming BaseModel is correctly defined

class Location(BaseModel):
    __tablename__ = "locations"  # Adjusted table name to plural form

    id = Column(Integer, primary_key=True)  # Assuming 'id' is the primary key for Location
    user_id = Column(String(50), ForeignKey('users.user_id'), nullable=False)  # Foreign key to User table
    user = relationship("User", backref="locations")  # Relationship with User

    country = Column(String(24), nullable=False)
    county = Column(String(50), nullable=False)
    zone = Column(String(60), nullable=True)
