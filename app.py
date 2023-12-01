#!/usr/bin/env python3
from flask import Flask
from api.products import products_bp
from api.users import users_bp
from api.orders import orders_bp
from api.search import search_bp
from api.auth import auth_bp
app = Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(search_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(products_bp)
app.register_blueprint(users_bp)