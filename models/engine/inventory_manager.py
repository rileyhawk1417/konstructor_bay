#!/usr/bin/env python3
from models.product import Product
from models.cart import Cart
from models.location import Location
from models.engine.db_engine import Db_storage
from uuid import uuid4
import uuid

class Inventory_manager:
    def __init__(self):
        self.db = Db_storage()

    def add_product(self, name, quantity, price, description, supplier_id):
        product_id = str(uuid.uuid4())
        new_product = Product(
            id=product_id, 
            product_name=name, 
            quantity=quantity, 
            price=price, 
            description=description, 
            supplier_id=supplier_id)
        self.db.new(new_product)
        self.db.save()

    def update_product_quantity(self, product_id, new_quantity):
        product = self.db.get(Product, product_id)
        if product:
            products.quantity = new_product
            self.db.new()
            self.db.save()
        else:
            print("The product is not available")

    def delete_product(self, product_id):
        product = self.db.new_get(Product, product_id)
        if product:
            self.db.delete(product)
            self.db.save()
        else:
            print("The product is not available")

    def read_all_products(self):
        return self.db.new_get(Product)

    def read_specific_product(self, product_id):
        return self.db.new_get(Product, product_id)

    """
    when an order is completed deduct from inventory
    """
    def deduct_from_inventory(self, product_id, quantity):
        product = self.db.new_get(Product, product_id)
        if product:
            product.quantity -= quantity
            self.db.new()
            self.db.save()
        else:
            print("The product is not available")

    def total_products_in_cart(self, cart_id):
        """
        getting total number of product in a cart
        """
        cart = self.db.new_get(Cart, cart_id)
        if cart:
            total = len(cart)
            return total
        else:
            print("Cart doesn't exist: specify a valid id")
        
    def list_products_in_cart(self, cart_id):
        """
        list all products in a cart
        """

        cart = self.db.new_get(Cart, cart_id)
        if cart:
            for product in cart:
                return product.product_name
        else:
            print("Cart doesn't exist")

    def total_price_in_cart(self, cart_id):
        cart = self.db.new_get(Cart, cart_id)
        if cart:
            price = 0
            for product in cart:
                price += product.product_name
            return price

        else:
            print("cart doesn't exist.\n\t CART ID SPECIFIED DOES NOT EXIST")
        