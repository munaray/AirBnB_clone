import unittest
from datetime import datetime
from models.place import Place

class TestPlace(unittest.TestCase):

    def setUp(self):
        """Create an instance of Place for testing"""
        self.place = Place()

    def test_attributes_inherited(self):
        """Test if the Place class inherits attributes from BaseModel"""
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.id, str)
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_place_attributes(self):
        """Test if the place-specific attributes are present"""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_str_representation(self):
        """Test if the __str__ method returns the expected string"""
        expected_str = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), expected_str)

    def test_save_method(self):
        """Test if the save method updates the updated_at attribute and performs saving (mocked)"""
        original_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(self.place.updated_at, original_updated_at)

    def test_to_dict_method(self):
        """Test if the to_dict method returns the expected dictionary"""
        dict_representation = self.place.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertIn("created_at", dict_representation)
        self.assertIn("updated_at", dict_representation)
        self.assertIn("__class__", dict_representation)
        self.assertIn("city_id", dict_representation)
        self.assertIn("user_id", dict_representation)
        self.assertIn("name", dict_representation)
        self.assertIn("description", dict_representation)
        self.assertIn("number_rooms", dict_representation)
        self.assertIn("number_bathrooms", dict_representation)
        self.assertIn("max_guest", dict_representation)
        self.assertIn("price_by_night", dict_representation)
        self.assertIn("latitude", dict_representation)
        self.assertIn("longitude", dict_representation)
        self.assertIn("amenity_ids", dict_representation)

if __name__ == '__main__':
    unittest.main()
