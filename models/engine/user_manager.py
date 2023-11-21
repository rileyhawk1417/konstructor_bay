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
        user.first_name = first_name
        user.sec_name = sec_name
        user.user_name = user_name
        user.email = email
        user.password = password
        storage.new(user)
        storage.save()
        return user
    
    @staticmethod
    def update_email(user_id, email):
        """
        update user email
        """
        user = storage.query_id(User)
        if user is None:
            print ("user not found")
            return 'user not found'
        user.email = email
        storage.save()
        return user

    @staticmethod
    def read_users():
        """
        read all users
        """
        return storage.all(User)

    @staticmethod
    def delete_user(user_id):
        """
        delete user
        """
        user = storage.get(User, user_id)
        if user is None:
            print ("user not found")
            return 'user not found'
        storage.delete(user)