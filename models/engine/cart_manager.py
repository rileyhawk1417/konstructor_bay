#!/usr/bin/env python3
"""
cart manager crud opreations
"""
from models import storage
from models.cart import Cart
from models.product import Product
import sqlalchemy

class Cart_manager:
    @staticmethod
    def create_Cart(user_id):
        """
        creating a new cart
        """
        cart = Cart(user_id=user_id)
        storage.new(cart)
        storage.save()
        return cart

    @staticmethod
    def read_Cart(cart_id):
        """
        listing cart content
        """

        return storage.new_get(Cart, cart_id)

    @staticmethod
    def add_product(cart_id, product_id):
        """
        add product to cart
        """
        cart = storage.new_get(Cart, id=cart_id)
        product = storage.new_get(Product, id=product_id)

        if cart and product:
            # Check if the product is already in the cart's products
            if product in cart.products:
                return "Product is already in the cart"
            else:
                cart.products.append(product)
                storage.save()
                return cart
        else:
            return "Cart or product not found"
    @staticmethod
    def delete_product(cart_id, product_id):
        """
        delete product in cart
        """

        product = storage.new_get(Cart, product_id)
        if product_id in Cart.product_id:
            storage.delete(product_id)
            storage.save()
            return None
        
    @staticmethod
    def delete_cart(cart_id):
        """
        delete the cart
        """
        cart = storage.new_get(Cart, cart_id)
        storage.delete(cart)
        storage.save()
        return None


        