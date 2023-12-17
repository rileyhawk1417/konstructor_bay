#!/usr/bin/env python3
"""
cart endpoints
"""
from flask import Blueprint, jsonify, request
from models.engine.cart_manager import Cart_manager
from models.engine.inventory_manager import Inventory_manager
from models.engine.search_manager import Search_manager

cart_bp = Blueprint("cart", __name__, url_prefix="/api/cart")


@cart_bp.route("/create_cart/<user_id>", methods=["GET"], strict_slashes=False)
def create_cart(user_id):
    """create cart"""
    cm = Cart_manager()
    if user_id is None:
        return jsonify({"message": "User id missing cant create cart!"}), 403
    existing_cart = cm.find_cart(user_id)
    if existing_cart:
        return jsonify(
            {"cart_id": existing_cart, "message": "Cart already exists!"}
        ), 201

    new_cart = Cart_manager().create_Cart(user_id)
    if new_cart:
        return jsonify(
            {"cart_id": new_cart.id, "message": "new cart created successfully"}
        ), 201
    else:
        return jsonify("Something went wrong"), 404


@cart_bp.route("/add_product", methods=["POST"], strict_slashes=False)
def add_product():
    """
    add product to cart
    """
    data = request.get_json()
    cart_id = data.get("cart_id")
    product_id = data.get("product_id")
    qty = data.get("qty")
    cm = Cart_manager()

    res = Cart_manager.add_product(cart_id, product_id)
    if res:
        return jsonify("product added successfully"), 201
    else:
        return jsonify("unable to add product to cart"), 500


@cart_bp.route("/remove_product", methods=["POST"], strict_slashes=False)
def remove_product():
    """
    add product to cart
    """
    data = request.get_json()
    cart_id = data.get("cart_id")
    product_id = data.get("product_id")

    res = Cart_manager.delete_product(cart_id, product_id)
    if res:
        return jsonify("product deleted successfully"), 201
    else:
        return jsonify("unable to delete product from cart"), 500


@cart_bp.route("/<user_id>", methods=["GET"], strict_slashes=False)
def get_user_cart(user_id):
    """
    read products in cart
    """
    cm = Cart_manager()

    cart_id = cm.find_cart(user_id)
    if cart_id:
        return jsonify(cart_id), 200
    else:
        return jsonify("users cart does not exist"), 404


@cart_bp.route("/<user_id>/fetch/<cart_id>", methods=["GET"], strict_slashes=False)
def read_products(user_id, cart_id):
    """
    read products in cart
    """
    cm = Cart_manager().read_Cart(cart_id)
    im = Inventory_manager()

    product_list = []
    prod_id_list = cm.product_id.split(", ")
    if cm:
        for item in prod_id_list:
            product = im.read_specific_product(item)
            serialized_product = {
                "id": product.id,
                "product_name": product.product_name,
                "description": product.description,
                "quantity": product.quantity,
                "price": product.price,
                "supplier_id": product.supplier_id,
                "supplier_name": product.supplier.business_name
                if product.supplier
                else None,
                "location_id": product.location_id,
            }
            product_list.append(serialized_product)
        return jsonify(product_list), 200
    else:
        return jsonify("cart does not exist"), 404
