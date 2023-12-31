#!/usr/bin/env python3
"""
registration and login api endpoint
"""
from flask import Blueprint, jsonify, request, Flask
from models.engine.user_manager import User_manager
from models.user import User
from models.supplier import Supplier
from models import storage
import random
import os

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.route("/upload/<user_id>", methods=["POST"], strict_slashes=False)
def upload_profile_pic(user_id):
    """
    uploading profile pic
    """

    um = User_manager()
    success = um.upload_profile_pic(user_id)
    if success:
        return jsonify(f"{success}")


@auth_bp.route("/register", methods=["POST"], strict_slashes=False)
def register_user():
    """
    registering a user
    """
    data = request.get_json()

    first_name = data.get("first_name")
    second_name = data.get("second_name")
    user_name = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # create_user(<firstName>, <secName>, user_name, email, password)
    existing_user = storage.new_get(User, username=user_name)
    if existing_user:
        if existing_user.username == user_name:
            return jsonify("user already exists"), 409

    new_user = User_manager.create_user(
        first_name, second_name, user_name, email, password
    )

    if new_user:
        return jsonify("new user  added successfully"), 201
    else:
        return jsonify("Unable to add user"), 500


@auth_bp.route("/fetch_user/<id>", methods=["POST"], strict_slashes=False)
def fetch_user(id):
    """
    fetch a user
    """
    found = False
    existing_user = storage.new_get(User, id)
    user_data = existing_user
    if existing_user:
        user_data = existing_user
        found = True
    if found:
        return jsonify(
            {
                "username": user_data.username,
                "email": user_data.email,
                "fname": user_data.firstName,
                "lname": user_data.sec_name,
                "user_id": user_data.id,
            }
        ), 200
    else:
        return jsonify("User not found"), 401


@auth_bp.route("/fetch_supplier_id/<id>", methods=["GET"], strict_slashes=False)
def fetch_supplier_id(id):
    """
    fetch a user
    """
    found = False
    existing_user = storage.new_get(Supplier, user_id=id)
    user_data = existing_user
    if existing_user:
        user_data = existing_user
        found = True
    if found:
        return jsonify(
            {
                "supplier_id": user_data.id,
                "business_name": user_data.business_name,
                "delivery": user_data.delivery,
                "phone_num": user_data.phone_num,
                "email": user_data.email,
            }
        ), 200
    else:
        return jsonify("User not found"), 401


@auth_bp.route("/fetch_supplier_info/<id>", methods=["GET"], strict_slashes=False)
def fetch_supplier_info(id):
    """
    fetch a user
    """
    found = False
    existing_user = storage.new_get(Supplier, id)
    user_data = existing_user
    if existing_user:
        user_data = existing_user
        found = True
    if found:
        return jsonify(
            {
                "supplier_id": user_data.id,
                "business_name": user_data.business_name,
                "delivery": user_data.delivery,
                "phone_num": user_data.phone_num,
                "email": user_data.email,
            }
        ), 200
    else:
        return jsonify("User not found"), 401


@auth_bp.route("/login", methods=["POST"], strict_slashes=False)
def login():
    """
    user login
    """
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    um = User_manager()
    user_id = um.login(username, password)
    if user_id:
        return jsonify({"message": "login is successfull", "user_id": user_id}), 200
    else:
        return jsonify("invalid credentials"), 401
