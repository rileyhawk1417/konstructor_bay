#!/usr/bin/env python3
"""
cart endpoints
"""
from flask import Blueprint, jsonify

cart_bp = Blueprint("cart", __name__, url_prefix="/api/cart")



