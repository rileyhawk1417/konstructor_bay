#!/usr/bin/env python3
"""
search api endpoint
"""
from flask import Blueprint, jsonify
from models.engine.search_manager import Search_manager

search_bp = Blueprint("search", __name__, url_prefix="/api")


@search_bp.route("/search/<product_name>", methods=["GET"], strict_slashes=False)
def search_product(product_name):
    """
    search product by its name
    """
    sm = Search_manager()
    product = sm.search_product_name(product_name)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({"error": "No product found with that name"}), 404
