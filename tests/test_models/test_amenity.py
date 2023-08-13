import unittest
from datetime import datetime
from models.amenity import Amenity  # Import the Amenity class from your module

class TestAmenity(unittest.TestCase):

    def setUp(self):
        # Create an instance of Amenity for testing
        self.amenity = Amenity()

    def test_attributes_inherited(self):
        # Test if the Amenity class inherits attributes from BaseModel
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_amenity_attribute(self):
        # Test if the amenity-specific attribute is present
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_str_representation(self):
        # Test if the __str__ method returns the expected string
        expected_str = "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_save_method(self):
        # Test if the save method updates the updated_at attribute and performs saving (mocked)
        original_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(self.amenity.updated_at, original_updated_at)

    def test_to_dict_method(self):
        # Test if the to_dict method returns the expected dictionary
        dict_representation = self.amenity.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertIn("created_at", dict_representation)
        self.assertIn("updated_at", dict_representation)
        self.assertIn("__class__", dict_representation)
        self.assertIn("name", dict_representation)

if __name__ == '__main__':
    unittest.main()
