#!/usr/bin/env python3
from flask import Flask
from api.products import products_bp

app = Flask(__name__)

app.register_blueprint(products_bp)