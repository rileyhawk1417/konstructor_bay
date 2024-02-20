#!/usr/bin/env python3
"""
cart manager crud opreations
"""
import sys 
sys.path.append('/home/user/sandbox/project/konstructor_bay')
from models import storage
from models.product import Product

class Cart():
    def __init__(self):
        self.products_cart = {}

    def add_product(self, product_id: str, quantity: int) -> None:
        existing_product = storage.new_get(Product, product_id)
        name = existing_product.product_name
        if existing_product is None:
            return 'Product does not exist'
        
        if existing_product.id in self.products_cart:
            self.products_cart[product_id]['quantity'] += quantity
        else:
            self.products_cart[product_id] = {'name': name, 'quantity': quantity}
        print(self.products_cart)
            
if __name__ == '__main__':
    c = Cart()
    c.add_product('2bfb4f40-8ef8-42b2-9765-37786567cecb', 5)
    c.add_product('2bfb4f40-8ef8-42b2-9765-37786567cecb', 3)
