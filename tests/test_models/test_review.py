import unittest
from datetime import datetime
from models.review import Review

class TestReview(unittest.TestCase):

    def setUp(self):
        """Create an instance of Review for testing"""
        self.review = Review()

    def test_attributes_inherited(self):
        """Test if the Review class inherits attributes from BaseModel"""
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_review_attributes(self):
        """Test if the review-specific attributes are present"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_str_representation(self):
        """Test if the __str__ method returns the expected string"""
        expected_str = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)

    def test_save_method(self):
        """Test if the save method updates the updated_at attribute and performs saving (mocked)"""
        original_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(self.review.updated_at, original_updated_at)

    def test_to_dict_method(self):
        """Test if the to_dict method returns the expected dictionary"""
        dict_representation = self.review.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertIn("created_at", dict_representation)
        self.assertIn("updated_at", dict_representation)
        self.assertIn("__class__", dict_representation)
        self.assertIn("place_id", dict_representation)
        self.assertIn("user_id", dict_representation)
        self.assertIn("text", dict_representation)

if __name__ == '__main__':
    unittest.main()
