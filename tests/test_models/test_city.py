import unittest
from datetime import datetime
from models.city import City

class TestCity(unittest.TestCase):

    def setUp(self):
        """Create an instance of City for testing"""
        self.city = City()

    def test_attributes_inherited(self):
        """Test if the City class inherits attributes from BaseModel"""
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_city_attributes(self):
        """Test if the city-specific attributes are present"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_str_representation(self):
        """Test if the __str__ method returns the expected string"""
        expected_str = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)

    def test_save_method(self):
        """Test if the save method updates the updated_at attribute and performs saving (mocked)"""
        original_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(self.city.updated_at, original_updated_at)

    def test_to_dict_method(self):
        """Test if the to_dict method returns the expected dictionary"""
        dict_representation = self.city.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertIn("created_at", dict_representation)
        self.assertIn("updated_at", dict_representation)
        self.assertIn("__class__", dict_representation)
        self.assertIn("state_id", dict_representation)
        self.assertIn("name", dict_representation)

if __name__ == '__main__':
    unittest.main()
