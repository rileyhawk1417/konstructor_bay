#!/usr/bin/env python3
"""
registration and login api endpoint
"""
from flask import Blueprint, jsonify, request
from models.engine.user_manager import User_manager
from models.user import User
from models import storage

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/register", methods=['POST'], strict_slashes=False)
def register_user():
    """
    registering a user
    """
    data = request.get_json()

    first_name = data.get('first_name')
    second_name = data.get('second_name')
    user_name = data.get('username')
    email = data.get('email')
    password = data.get('password')
    #create_user(<firstName>, <secName>, user_name, email, password)
    existing_user = storage.new_get(User, username=user_name)
    if existing_user.username == user_name:
        return jsonify("user already exists"), 409

    new_user = User_manager.create_user(first_name, second_name, user_name, email, password)

    if new_user:
        return jsonify("new user  added successfully"), 201
    else:
        return jsonify("Unable to add user"), 500

@auth_bp.route("/login", methods=['POST'], strict_slashes=False)
def login():
    """
    user login
    """
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    um = User_manager()
    if um.login(username, password):
        return jsonify("login successful"), 200
    else:
        return jsonify("invalid credentials"), 401