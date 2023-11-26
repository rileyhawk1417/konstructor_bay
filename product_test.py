import unittest
from models.product import Product  # Adjust the import path as per your project structure

class TestProduct(unittest.TestCase):
    def test_product_attributes(self):
        product = Product(
            product_name='Test Product',
            description='Product description',
            quantity=10,
            price=100
        )

        self.assertEqual(product.product_name, 'Test Product')
        self.assertEqual(product.description, 'Product description')
        self.assertEqual(product.quantity, 10)
        self.assertEqual(product.price, 100)

    def test_product_relationships(self):
        # Assuming Supplier and Location classes are defined
        supplier = Supplier(id='123', business_name='Test Supplier')
        location = Location(id='456', country='Country', county='County', zone='Zone')

        product = Product(
            product_name='Test Product',
            description='Product description',
            quantity=10,
            price=100,
            supplier=supplier,
            location=location
        )

        self.assertEqual(product.supplier, supplier)
        self.assertEqual(product.location, location)

    def test_invalid_product_creation(self):
        # Test creation with invalid data
        with self.assertRaises(ValueError):
            # Supplying missing required fields
            Product(product_name=None, description='Product description', quantity=10, price=100)

        with self.assertRaises(ValueError):
            # Supplying excessively long values for attributes
            Product(product_name='P' * 240, description='Product description', quantity=10, price=100)

        with self.assertRaises(ValueError):
            # Supplying negative quantity
            Product(product_name='Test Product', description='Product description', quantity=-1, price=100)

        with self.assertRaises(ValueError):
            # Supplying negative price
            Product(product_name='Test Product', description='Product description', quantity=10, price=-1)

    def test_serialize_method(self):
        product = Product(
            product_name='Test Product',
            description='Product description',
            quantity=10,
            price=100
        )
        serialized_product = Product.serialize(product)

        # Validate the structure of the serialized data
        self.assertIsInstance(serialized_product, dict)
        self.assertIn('id', serialized_product)
        self.assertIn('product_name', serialized_product)
        self.assertIn('description', serialized_product)
        self.assertIn('quantity', serialized_product)
        self.assertIn('price', serialized_product)
        self.assertIn('supplier_id', serialized_product)
        self.assertIn('supplier_name', serialized_product)
        self.assertIn('location_id', serialized_product)

    # Add more test cases as necessary for edge cases, validation checks, etc.

if __name__ == '__main__':
    unittest.main()
