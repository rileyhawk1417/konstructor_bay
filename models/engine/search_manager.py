#!/user/bin/env python3
"""
search manager
"""
from models.engine.db_engine import Db_storage
from models.product import Product
import re as regex


class Search_manager:
    @staticmethod
    def search_product_name(product_name):
        """
        search product by its name
        """
        products = Db_storage().new_get(Product)
        print(products)
        if products:
            found_products = []
            for product in products:
                if regex.search(product_name, product.product_name) or regex.search(
                    product_name, product.description
                ):
                    product = product.to_dict()
                    found_products.append(product)

            if found_products:
                return found_products
            else:
                return []
        else:
            return None
