#!/usr/bin/env python3
"""
connecting to the db
"""
from models.supplier import Supplier
from models.inbox import Inbox
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
    "Product": Product, "Supplier": Supplier,
    "Inbox": Inbox
}

class Db_storage:
    """
    Interacting with the mysql database
    """

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

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

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

    def delete(self, obj=None):
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
        allClasses = [User, Product, Location, Cart, Order, Supplier, Inbox]
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
        #returns the obj based on the class name and its id 
        #If not it returns None
        """
        if cls not in classes:
            return None
        all_classes = models.storage.all(cls)
        for value in all_classes.values():
            if value.id == id:
                return value

        return None
        
    def new_get(self, cls, id=None):
        if id is None:
            return self.__session.query(cls).all()
        else:
            return self.__session.query(cls).get(id)

    def close(self):
        """
        removes the method on the current private session
        """
        self.__session.remove()

    def insert_data(self, *args):
        """Insert data into tables"""
        for arg in args:
            self.new(arg)
        self.save()

    def update_data(self, obj, **kwargs):
        """Update data in tables"""
        for key, val in kwargs.items():
            if key != 'id' and key != 'created_at' and key != 'updated_at':
                setattr(obj, key, val)
        self.save()
    def select_data(self, cls):
        """Select data from tables"""
        return self.__session.query(cls).all()

    def create_data(self, cls, **kwargs):
        """Create data in tables"""
        obj = cls(**kwargs)
        self.new(obj)
        self.save()
        return obj
    
    def delete_data(self, obj):
        """Delete data from tables"""
        self.delete(obj)
        self.save()
