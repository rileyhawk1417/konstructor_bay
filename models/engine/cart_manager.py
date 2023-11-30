#!/usr/bin/env python3
"""
cart manager crud opreations
"""
from models import storage
from models.cart import Cart

class Cart_manager:
    @staticmethod
    def create_Cart(user_id, product_id):
        cart = Cart(user_id=user_id, product_id=product_id)
        storage.new(cart)
        storage.save()
        return cart

    @staticmethod
    def read_Cart(cart_id):
        return storage.new_get(Cart, cart_id)

    @staticmethod
    def add_product(cart_id, product_id):
        cart = storage.new_get(Cart, cart_id)
        cart.product_id = product_id
        storage.save()
        return cart
    @staticmethod
    def delete_product(cart_id):
        product = storage.new_get(Cart, product_id)
        storage.delete(product_id)
        storage.save()
        return cart
    @staticmethod
    def delete_cart(cart_id):
        cart = storage.new_get(Cart, cart_id)
        storage.delete(cart)
        storage.save()
        return cart


        