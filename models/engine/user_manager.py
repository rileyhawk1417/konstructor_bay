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
from flask import request, jsonify
import os
import random


class User_manager:
    """
    user manager class
    """

    def __init__(self):
        pass

    @staticmethod
    def upload_profile_pic(user_id):
        """
        uploading profile pic
        """
        user = storage.new_get(User, id=user_id)
        if user:
            profile_pic = request.files.get('profilePic')
            if profile_pic:
                upload_folder = './images/user_profile'
                os.makedirs(upload_folder, exist_ok=True)

                profile_extension = os.path.splitext(profile_pic.filename)[1]
                profile_pic_name = f"{user_id}{profile_extension}"

                profile_pic.save(os.path.join(upload_folder, profile_pic_name))
                return "Image uploaded successfully"
            else:
                return "Something went wrong when getting the pic"
        else:
            return "Bad <id>, User not found"

    @staticmethod
    def create_user(first_name, sec_name, username, email, password):
        """
        registers a user into the database
        """
        existing_user = storage.new_get(User, username=username)
        if existing_user:
            return f"Username {username} already exists"
        else:
            new_user = User(
                id=str(uuid.uuid4()),
                firstName=first_name,
                sec_name=sec_name,
                username=username,
                email=email,
                password=password,
            )
            storage.new(new_user)
            storage.save()
            return new_user

    @staticmethod
    def login(username, password):
        """
        login a user if he/she is registerd
        """
        existing_user = storage.new_get(User, username=username)
        if existing_user and existing_user.password == password:
            print(f"Welcome {username}")
            return existing_user.id
            #
            # return True
        else:
            print("Invalid username or password. Please try againn")
            return None

    @staticmethod
    def search_user(user_id):
        """
        update user password
        """
        user = storage.new_get(User, user_id)
        if user is None:
            print("user not found")
            return "user not found"
        return user

    @staticmethod
    def update_passwd(user_id, passwd):
        """
        update user password
        """
        user = storage.new_get(User, user_id)
        if user is None:
            print("user not found")
            return "user not found"
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
            print("user not found")
            return "user not found"
        storage.delete(user)
        storage.save()
        return user

    @staticmethod
    def create_supplier(supplier_name, email, phone_num, user_id):
        """
        create supplier
        """
        supplier = Supplier()
        supplier.id = str(uuid.uuid4())
        supplier.business_name = supplier_name
        supplier.email = email
        supplier.phone_num = phone_num
        supplier.user_id = user_id
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
            print("supplier not found")
            return "supplier not found"
        storage.delete(supplier)
        storage.save()
        return supplier
