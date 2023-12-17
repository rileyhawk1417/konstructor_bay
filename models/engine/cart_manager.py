#!/usr/bin/env python3
"""
cart manager crud opreations
"""
from models import storage
from models.cart import Cart
import re as regex


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
        cart = storage.new_get(Cart, cart_id)
        if cart.product_id is None:
            new_list = []
            new_list.append(product_id)
            cart.product_id = new_list
            storage.save()
            return cart
        elif product_id in cart.product_id:
            return "product is already in cart"
        else:
            cart.product_id = cart.product_id + ", " + product_id
            print(cart.product_id)
            for items in cart.product_id:
                print(items)
            storage.save()
            return cart

    @staticmethod
    def delete_product(cart_id, product_id):
        """
        delete product in cart
        """

        product = storage.new_get(Cart, cart_id)
        # BUG: This wont work throws SQLAlchemy error
        # Saying builtins.stre is not mapped
        # Was trying to do a regex then replace the string
        for item in product:
            if product_id in item.product_id:
                item.product_id.replace(product_id, "")
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

    @staticmethod
    def find_cart(user_id):
        """
        Find the cart with user id
        """
        cart = storage.new_get(Cart, user_id=user_id)
        if cart:
            return cart.id
        return None
