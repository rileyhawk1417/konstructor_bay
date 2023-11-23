#!/usr/bin/env python3
"""
users crud operations api end points
"""
from models.user import User
from flask import Blueprint, jsonify, request
from models.engine.user_manager import User_manager
users_bp = Blueprint('user', __name__, url_prefix='/api/add_user')

@users_bp.route("", methods=['POST'], strict_slashes=False)
def add_user():
    """
    adding a user to the site
    """
    data = request.get_json()

    first_name = data.get('first_name')
    second_name = data.get('second_name')
    user_name = data.get('username')
    email = data.get('email')
    password = data.get('password')
    #create_user(<firstName>, <secName>, user_name, email, password)
    new_user = User_manager.create_user(first_name, second_name, user_name, email, password)

    if new_user:
        return jsonify("new user  added successfully"), 201
    else:
        return jsonify("Unable to add user"), 500

#def 

#if __name__ == "__main__":
 #   users_bp.run(debug=True)