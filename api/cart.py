#!/usr/bin/env python3
"""
cart endpoints
"""
from flask import Blueprint, jsonify
from models.engine.cart_manager import Cart_manager

cart_bp = Blueprint("cart", __name__, url_prefix="/api/cart")

@cart_bp.route("/create_cart/<user_id>", methods=['POST'], strict_slashes=False)
def create_cart(user_id): 
    """create cart
    """
    new_cart = Cart_manager().create_Cart(user_id)
    if new_cart:
        return jsonify("new cart created succeefully"), 201
    else:
        return jsonify("Something went wrong"), 404

@cart_bp.route("/add_product/<product_id>/cart/<cart_id>", methods=['POST'], strict_slashes=False)
def add_product(product_id, cart_id):
    """
    add product to cart
    """
    cm = Cart_manager()
    
    res = cm.add_product(cart_id, product_id)
    if res:
        return jsonify("product added successfully"), 201
    else:
        return jsonify("unable to add product to cart"), 500

@cart_bp.route("/read/<cart_id>", methods=["GET"], strict_slashes=False)
def read_products(cart_id):
    """
    read products in cart
    """
    cm = Cart_manager()

    products_in_cart = cm.read_cart(cart_id)
    if products_in_cart:
        return jsonify(products_in_cart), 200
    else:
        return jsonify("cart does not exist"), 404

