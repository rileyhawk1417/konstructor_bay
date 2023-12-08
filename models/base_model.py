# /usr/bin/env python3
"""BaseModel class"""
import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime
import models

time = "%Y-%m-%dT-%H-%M-%.%f"
Base = declarative_base()


class BaseModel:
    """BaseModel class"""

    id = Column(String(100), primary_key=True, default=str(uuid.uuid4()), nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        """initialize the class BaseModel"""
        if kwargs:
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            if not kwargs.get("id", None):
                self.id = str(uuid.uuid4())

            for key, val in kwargs.items():
                if key != "__class__":
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """returns a string representation of this class"""
        return f"ID ({self.id}) class_name: [{self.__class__.__name__}] Dictionaryself.__dict__"

    def save(self):
        """updates an instance with current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary representation of this class"""
        dict_repr = self.__dict__.copy()
        if "created_at" in dict_repr:
            dict_repr["created_at"] = self.created_at.strftime(time)
        if "updated_at" in dict_repr:
            dict_repr["updated_at"] = self.updated_at.strftime(time)
        dict_repr["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in dict_repr:
            del dict_repr["_sa_instance_state"]

        return dict_repr

    def delete(self):
        """delete current instance from storage"""
        models.storage.delete(self)
