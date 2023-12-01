#!/user/bin/env python3
"""
search manager
"""
from models.engine.db_engine import Db_storage
from models.product import Product
from models import storage
from models.engine.inventory_manager import Inventory_manager
from flask import jsonify
from models.base_model import BaseModel

class Search_manager:

    @staticmethod
    def search_product_name(product_name):
        """
        search product by its name
        """
        products = Db_storage().new_get(Product)

        if products:
            found_products = []
            for product in products:
                if product.product_name == product_name:
                    product = product.to_dict()
                    found_products.append(product)

            if found_products:
                return found_products
            else:
                return []
        else:
            return None