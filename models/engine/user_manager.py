#!/usr/bin/env python3
"""
this class defines crud operations for the user model
"""
from models.base_model import BaseModel, Base   
from models.user import User
from models.supplier import Supplier
from models.product import Product
from models.inbox import Inbox
from models.location import Location
from models import storage
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import uuid

class User_manager:
    """
    user manager class
    """
    def __init__(self):
        pass

    @staticmethod
    def create_user(first_name, sec_name, user_name, email, password):
        """
        create user
        """
        user = User()
        user.id = str(uuid.uuid4())
        user.first_name = first_name
        user.sec_name = sec_name
        user.user_name = user_name
        user.email = email
        user.password = password
        storage.new(user)
        storage.save()
        return user
    
    @staticmethod
    def update_passwd(user_id, passwd):
        """
        update user password
        """
        user = storage.new_get(User, user_id)
        if user is None:
            print ("user not found")
            return 'user not found'
        user.password = passwd
        storage.save()
        return user

    @staticmethod
    def read_users():
        """
        read all users
        """
        return storage.all(User)

    @staticmethod
    def delete_a_user(user_id):
        """
        delete user
        """

        user = storage.new_get(User, user_id)
        if user is None:
            print ("user not found")
            return 'user not found'
        storage.delete(user)
        storage.save()
        return user

    @staticmethod
    def create_supplier(supplier_name, email, phone_num):
        """
        create supplier
        """
        supplier = Supplier()
        supplier.supplier_name = supplier_name
        supplier.email = email
        supplier.phone_num = phone_num
        storage.new(supplier)
        storage.save()
        return supplier

    @staticmethod
    def read_suppliers():
        """
        read all suppliers
        """
        return storage.all(Supplier)

    @staticmethod
    def delete_supplier(supplier_id):
        """
        delete supplier
        """
        supplier = storage.get(Supplier, supplier_id)
        if supplier is None:
            print ("supplier not found")
            return 'supplier not found'
        storage.delete(supplier)
        storage.save()
        return supplier
