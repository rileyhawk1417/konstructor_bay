#!/usr/bin/env python3
"""
manage orders
"""
from models.engine.cart_manager import Cart_manager
from flask import Blueprint

orders_bp = Blueprint('orders', __name__, url_prefix='/api')

@orders_bp.route('/create_cart/user/<user_id>/product/<product_id>', methods=['POST'], strict_slashes=False)
def create_cart(user_id, product_id):
    """
    create cart 
    """
    cm = Cart_manager()
    cm.create_Cart(user_id, cart_id)

@orders_bp.route('/orders/<cart_id>', methods=['GET'], strict_slashes=False)
def list_products_in_cart(cart_id):
    """
    endpoint to list all product in cart
    """
    cm = Cart_manager()
    cm.read_Cart(cart_id)