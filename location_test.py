import unittest
from models.location import Location
from models.user import User

class TestLocation(unittest.TestCase):
    def setUp(self):
        self.user = User(id='123', username='test_user')

    def test_location_attributes(self):
        location = Location(user_id='123', country='Country', county='County', zone='Zone')
        
        self.assertEqual(location.user_id, '123')
        self.assertEqual(location.country, 'Country')
        self.assertEqual(location.county, 'County')
        self.assertEqual(location.zone, 'Zone')

    def test_location_relationship(self):
        location = Location(user_id='123', country='Country', county='County', zone='Zone', user=self.user)
        
        self.assertEqual(location.user, self.user)

    def test_invalid_location_creation(self):
        # Test creation with invalid data
        with self.assertRaises(ValueError):
            # Supplying missing required fields
            Location(user_id='123', country=None, county='County', zone='Zone')

        with self.assertRaises(ValueError):
            # Supplying too long values for attributes
            Location(user_id='123', country='C' * 25, county='County', zone='Zone')

    def test_default_values(self):
        # Test default values
        location = Location(user_id='123', country='Country', county='County', zone='Zone')
        self.assertIsNone(location.user)  # The user should be None if not explicitly provided

  
if __name__ == '__main__':
    unittest.main()
