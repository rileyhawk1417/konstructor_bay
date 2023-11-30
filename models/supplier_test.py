import unittest
from models.base_model import Base, BaseModel
from models.supplier import Supplier
from models.user import User
from models.inbox import Inbox

class TestSupplier(unittest.TestCase):
    def setUp(self):
        # Create instances for testing relationships
        self.user = User(username="test_user")
        self.inbox = Inbox(name="test_inbox")

    def test_supplier_creation(self):
        supplier = Supplier(
            business_name="Test Business",
            business_location="Test Location",
            email="test@example.com",
            phone_num="1234567890",
            delivery=True,
            user=self.user,
            inbox=self.inbox
            # Add other attributes as necessary
        )
        # Validate attributes
        self.assertEqual(supplier.business_name, "Test Business")
        self.assertEqual(supplier.business_location, "Test Location")
        self.assertEqual(supplier.email, "test@example.com")
        self.assertEqual(supplier.phone_num, "1234567890")
        self.assertTrue(supplier.delivery)
        # Add more assertions as needed to cover other attributes

    def test_supplier_relationships(self):
        supplier = Supplier(
            business_name="Test Business",
            business_location="Test Location",
            email="test@example.com",
            phone_num="1234567890",
            delivery=True,
            user=self.user,
            inbox=self.inbox
        )
        # Check if relationships are correctly set
        self.assertEqual(supplier.user, self.user)
        self.assertEqual(supplier.inbox, self.inbox)

    # Add more test cases to cover additional scenarios, e.g. validation, edge cases, methods, etc.
    # ...

if __name__ == '__main__':
    unittest.main()
