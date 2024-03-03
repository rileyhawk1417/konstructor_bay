#!/usr/bin/env python3
from flask import Flask
from flask_cors import CORS
from api.products import products_bp
from api.users import users_bp
from api.orders import orders_bp
from api.search import search_bp
from api.auth import auth_bp
from api.cart import cart_bp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
app.secret_key = 'secret_key'
username = "ks_developers"
password = ""
host = "localhost"
database = "ks_dev_db"
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqldb://{username}:{password}@{host}/{database}"
db = SQLAlchemy(app)  # Initialize SQLAlchemy
migrate = Migrate(app, db)


app.register_blueprint(cart_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(search_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(products_bp)
app.register_blueprint(users_bp)
