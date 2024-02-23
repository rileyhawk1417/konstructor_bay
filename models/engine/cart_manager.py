#!/usr/bin/env python3
"""
cart manager crud opreations
"""
import sys 
sys.path.append('/home/user/sandbox/project/konstructor_bay')
from models import storage
from models.product import Product
from flask import session, Flask
app = Flask(__name__)


class Cart():
    """
    The cart is stored in the current user session
    """
    def __init__(self):
        self.products_cart = session.get('cart', {})

    def add_product(self, product_id: str, quantity: int) -> None:
        """
        adds product to cart dictionary
        Args:
            product_id -> id of product which will be added to cart
            quantity -> quantity of the product that will be added to cart
        Return:
            returns None
        """
        existing_product = storage.new_get(Product, product_id)
        name = existing_product.product_name
        if existing_product is None:
            return 'Product does not exist'
        
        if existing_product.id in self.products_cart:
            self.products_cart[product_id]['quantity'] += quantity
        else:
            self.products_cart[product_id] = {'name': name, 'quantity': quantity}
        print(self.products_cart)


#route for testing cart the flask request(cookie kind storage)
@app.route('/test_cart')
def test_cart():
    ch = Cart()
    ch.add_product('7a3b5521-2945-48f1-b9c4-1a0ec625c936', 2)
    ch.add_product('2bfb4f40-8ef8-42b2-9765-37786567cecb', 1)
    ch.add_product('7a3b5521-2945-48f1-b9c4-1a0ec625c936', 9)
    return ch.products_cart

if __name__ == '__main__':
   app.run(debug=True)
