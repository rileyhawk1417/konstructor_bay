#!/usr/bin/env/python3
"""
endpoints for products
"""
from flask import Blueprint, jsonify, request
from models.engine.inventory_manager import Inventory_manager
from models.product import Product

# from models.base_model import to_dict

products_bp = Blueprint("products", __name__, url_prefix="/api")


@products_bp.route("/products", methods=["GET"], strict_slashes=False)
def get_products():
    """
    listing all products
    """
    inventory_manager = Inventory_manager()
    products = inventory_manager.read_all_products()
    serialized_products = [Product.serialize(product) for product in products]
    return jsonify(serialized_products), 200


@products_bp.route("/products/<id>", methods=["GET"], strict_slashes=False)
def get_product(id):
    """
    retrieves details about a specific product based on id
    """
    im = Inventory_manager()
    product = im.read_specific_product(id)

    serialized_products = {
        "id": product.id,
        "product_name": product.product_name,
        "description": product.description,
        "quantity": product.quantity,
        "price": product.price,
        "supplier_id": product.supplier_id,
        "supplier_name": product.supplier.business_name if product.supplier else None,
        "location_id": product.location_id,
    }

    return jsonify(serialized_products)


@products_bp.route("/products", methods=["POST"], strict_slashes=False)
def post_product():
    """
    posts a product into the db
    """

    data = request.get_json()
    # print(data)

    if "description" not in data or data["description"] is None:
        return jsonify("Description is missing or None"), 400

    product_name = data.get("product_name")
    description = data.get("description")
    quantity = data.get("quantity")
    price = data.get("price")
    business_name = data.get("business_name")
    supplier_id = data.get("supplier_id")

    im = Inventory_manager()

    new_product = im.add_product(
        product_name, quantity, price, description, supplier_id
    )
    return jsonify(new_product), 201


"""
update product quantity
"""


@products_bp.route(
    "/products/<id>/update_quantity/<int:new_product_quantity>",
    methods=["PUT"],
    strict_slashes=False,
)
def update_quantity(id, new_product_quality):
    im = Inventory_manager()
    product = im.update_product_quantity(id, new_product_quality)
    return jsonify(product), 200


@products_bp.route("/products/<id>", methods=["DELETE"], strict_slashes=False)
def delete_product(id):
    """
    deletes a pproduct from the db
    """
    im = Inventory_manager()
    product = im.delete_product(id)
    return jsonify(product), 200


if __name__ == "__main__":
    debug = True
