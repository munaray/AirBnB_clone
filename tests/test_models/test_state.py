import unittest
from datetime import datetime
from models.state import State

class TestState(unittest.TestCase):

    def setUp(self):
        """Create an instance of State for testing"""
        self.state = State()

    def test_attributes_inherited(self):
        """Test if the State class inherits attributes from BaseModel"""
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_state_attribute(self):
        """Test if the state-specific attribute is present"""
        self.assertTrue(hasattr(self.state, "name"))

    def test_str_representation(self):
        """Test if the __str__ method returns the expected string"""
        expected_str = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_save_method(self):
        """Test if the save method updates the updated_at attribute and performs saving (mocked)"""
        original_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(self.state.updated_at, original_updated_at)

    def test_to_dict_method(self):
        """Test if the to_dict method returns the expected dictionary"""
        dict_representation = self.state.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertIn("created_at", dict_representation)
        self.assertIn("updated_at", dict_representation)
        self.assertIn("__class__", dict_representation)
        self.assertIn("name", dict_representation)

if __name__ == '__main__':
    unittest.main()
