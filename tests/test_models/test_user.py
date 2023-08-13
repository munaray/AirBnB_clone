import unittest
from datetime import datetime
from models.user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        """Create an instance of User for testing"""
        self.user = User()

    def test_attributes_inherited(self):
        """Test if the User class inherits attributes from BaseModel"""
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_user_attributes(self):
        """Test if the User-specific attributes are present"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_str_representation(self):
        """Test if the __str__ method returns the expected string"""
        expected_str = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected_str)

    def test_save_method(self):
        """Test if the save method updates the updated_at attribute and performs saving (mocked)"""
        original_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(self.user.updated_at, original_updated_at)

    def test_to_dict_method(self):
        """Test if the to_dict method returns the expected dictionary"""
        dict_representation = self.user.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertIn("created_at", dict_representation)
        self.assertIn("updated_at", dict_representation)
        self.assertIn("__class__", dict_representation)
        self.assertIn("email", dict_representation)
        self.assertIn("password", dict_representation)
        self.assertIn("first_name", dict_representation)
        self.assertIn("last_name", dict_representation)

if __name__ == '__main__':
    unittest.main()
