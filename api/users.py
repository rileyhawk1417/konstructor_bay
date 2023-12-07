#!/usr/bin/env python3
"""
users crud operations api end points
"""
from models import storage
from models.user import User
from flask import Blueprint, jsonify, request
from models.engine.user_manager import User_manager

users_bp = Blueprint("user", __name__, url_prefix="/api")


@users_bp.route("/add_user", methods=["POST"], strict_slashes=False)
def add_user():
    """
    adding a user to the site
    """
    data = request.get_json()

    first_name = data.get("first_name")
    second_name = data.get("second_name")
    user_name = data.get("username")
    email = data.get("email")
    password = data.get("password")
    # create_user(<firstName>, <secName>, user_name, email, password)
    new_user = User_manager.create_user(
        first_name, second_name, user_name, email, password
    )

    if new_user:
        return jsonify("new user  added successfully"), 201
    else:
        return jsonify("Unable to add user"), 500


@users_bp.route("/signin", methods=["GET"], strict_slashes=False)
def get_user():
    """
    adding a user to the site
    """
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")
    user = User_manager()
    check_user = user.check_user(email, password)

    if check_user:
        return jsonify("Found user"), 201
    else:
        return jsonify("User not found"), 500


@users_bp.route("/delete_user/<user_id>", methods=["DELETE"], strict_slashes=False)
def delete_user(user_id):
    """
    deleting user from db
    """
    um = User_manager()
    user = storage.new_get(User, user_id)
    if not user:
        return jsonify("user not found"), 404

    um.delete_a_user(user_id)

    return jsonify("user have been deleted"), 200


@users_bp.route("/update_passwd/<user_id>", methods=["PUT"], strict_slashes=False)
def update_passwd(user_id):
    """
    updating passwd of the user
    """
    return jsonify(update_passwd(user_id))


@users_bp.route("/users", methods=["GET"], strict_slashes=False)
def list_all_users():
    """
    listing all users
    """
    um = User_manager()
    return jsonify(um.read_users())

    
@users_bp.route("/supplier", methods=['POST'], strict_slashes=False)
def add_supplier():
    """
    adding supplier
    """
    um = User_manager()
    data = request.get_json()

    supplier_name = data.get('supplier_name')
    email = data.get('email')
    phone_num = data.get('phone_num')
    
    new_supplier = um.create_supplier(supplier_name, email, phone_num)
    if new_supplier:
        return jsonify("new supplier created successfully")
    else:
        return jsonify('Error: Something went wrong,\n\tError when creating supplier')
    
#if __name__ == "__main__":
 #   users_bp.run(debug=True)

