#!/usr/bin/env python3
"""
connecting to the db
"""
from models.base_model import Base, BaseModel
from models.user import User
from models.orders import Order
from models.location import Location
from models.cart import Cart
from models.product import Product
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import sqlalchemy
import models

classes = {
    "User": User, "Order": Order,
    "Location": Location, "Cart": Cart,
    "Product": Product
}

class Db_storage:
    __engine = None
    __session = None

    def __init__(self):
        """
        instantiate db objects
        """
        username = 'ks_developers'
        password = ''
        host = 'localhost'
        database = 'ks_dev_db'
        self.__engine = create_engine(f"mysql+mysqldb://{username}:{password}@{host}/{database}")

    def reload(self):
        """ reload data from our db
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session
    
    def save(self):
        """
        saves all changes of the current db session
        """
        self.__session.commit()

    def delete(self, obj):
        """
        delete obj from current db session 
        """
        if obj:
            self.__session.delete(obj)

    def new(self, obj):
        """
        adds the obj to the current db session"""

        self.__session.add(obj)

    def all(self, cls=None, id=None):
        """
        Query all classes or specific one by ID
        """
        allClasses = [User, Product, Location, Cart, Order]
        result = {}

        if cls is not None:
            if id is not None:
                obj = self.__session.query(cls).get(id)
                if obj is not None:
                    ClassName = obj.__class__.__name__
                    keyName = ClassName + "." + str(obj.id)
                    result[keyName] = obj
            else:
                for obj in self.__session.query(cls).all():
                    ClassName = obj.__class__.__name__
                    keyName = ClassName + "." + str(obj.id)
                    result[keyName] = obj
        else:
            for clss in allClasses:
                if id is not None:
                    obj = self.__session.query(clss).get(id)
                    if obj is not None:
                        ClassName = obj.__class__.__name__
                        keyName = ClassName + "." + str(obj.id)
                        result[keyName] = obj
                else:
                    for obj in self.__session.query(clss).all():
                        ClassName = obj.__class__.__name__
                        keyName = ClassName + "." + str(obj.id)
                        result[keyName] = obj
        return result


    def count(self, cls=None):
        """
        count number of objects in db
        """
        my_classes = classes.values()

        count = 0
        if not cls:
            for klass in my_classes:
                count = len(models.storage.all(klass).values())
        else:
            count = len(models.storage.all(cls).values())
        return count
    
    def get(self, cls, id):
        """
        returns the obj based on the class name and its id 
        If not it returns None
        """
        if cls not in classes:
            return None
        all_classes = models.storage.all(cls)
        for value in all_classes.values():
            if value.id == id:
                return value

        return None

    def close(self):
        """
        removes the method on the current private session
        """
        self.__session.remove()
