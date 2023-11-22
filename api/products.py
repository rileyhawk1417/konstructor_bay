#!/usr/bin/env/python3
"""
endpoints for products
"""
from flask import Blueprint, jsonify
from models.engine.inventory_manager import Inventory_manager
from models.product import Product

#from models.base_model import to_dict

products_bp = Blueprint('products', __name__, url_prefix='/api/products')

@products_bp.route('/', methods=['GET'])
def get_products():
    """
    listing all products
    """
    inventory_manager = Inventory_manager()
    products = inventory_manager.read_all_products()
    serialized_products = [Product.serialize(product) for product in products]
    return jsonify(serialized_products), 200
