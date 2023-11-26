import unittest
from models.order import orders 
from models.user import user  
from models.product import product

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.user = user(id='456', username='test_user')
        self.product = product(id='123', name='Test Product')

    def test_order_attributes(self):
        order = orders(product_id='123', user_id='456')
        
        self.assertEqual(order.product_id, '123')
        self.assertEqual(order.user_id, '456')

    def test_order_relationships(self):
        order = orders(product_id='123', user_id='456', user=self.user, product=self.product)
        
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.product, self.product)

    def test_invalid_order_creation(self):
        # Test creation with invalid data
        with self.assertRaises(ValueError):
            # Supplying invalid user_id and missing product_id
            Order(product_id=None, user_id='invalid')

        with self.assertRaises(ValueError):
            # Supplying invalid product_id and missing user_id
            orders(product_id='invalid', user_id=None)

if __name__ == '__main__':
    unittest.main()
