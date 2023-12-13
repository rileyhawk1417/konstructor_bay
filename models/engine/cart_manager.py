#!/usr/bin/env python3
"""
cart manager crud opreations
"""
from models import storage
from models.cart import Cart

class Cart_manager:
    @staticmethod
    def create_Cart(user_id, product_id):
        """
        creating a new cart
        """
        cart = Cart(user_id=user_id, product_id=product_id)
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
        cart = storage.new_get(Cart, cart_id)
        if product_id not in cart.product_id:
            cart.product_id.append(product_id)
            storage.save()
            return cart

    @staticmethod
    def delete_product(cart_id, product_id):
        """
        delete product in cart
        """

        product = storage.new_get(Cart, product_id)
        if product_id in Cart.product_id:
            storage.delete(product_id)
            storage.save()
            return cart
        
    @staticmethod
    def delete_cart(cart_id):
        """
        delete the cart
        """
        cart = storage.new_get(Cart, cart_id)
        storage.delete(cart)
        storage.save()
        return None


        