#!/usr/bin/python3
"""Unit Testing for Base Model"""
from contextlib import redirect_stdout
from datetime import datetime
from io import StringIO
import io
from models.review import Review
import unittest
import time


class TestInstantation(unittest.TestCase):
    """Test the User Class"""
    def test_instantiation(self):
        review = Review()
        self.assertIsInstance(review, Review)

    def test_id_type(self):
        review = Review()
        self.assertEqual(type(review.id), str)

    def test_uuid(self):
        review = Review()
        other_review = Review()
        self.assertNotEqual(review.id, other_review.id)

    def test_datetime(self):
        review = Review()
        self.assertNotEqual(review.created_at, datetime.now())

    def test_datetime_type(self):
        review = Review()
        self.assertEqual(type(review.created_at), datetime)

    def test_kwargs(self):
        review = Review(new_review="5 star")
        self.assertTrue(hasattr(review, 'new_review'))


class TestMethods(unittest.TestCase):
    """Tests public instance methods of basemodel"""
    def test_to_dict_type(self):
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(type(review_dict), dict)

    def test_dict_datetime_type(self):
        review = Review()
        new_dict = review.to_dict()
        self.assertEqual(type(new_dict.get('created_at')), str)

    def test_save(self):
        """Tests the save() method"""
        review = Review()
        time.sleep(0.5)
        date_now = datetime.now()
        review.save()
        diff = review.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_str(self):
        review = Review()
        expected = "[{}] ({}) {}\n".format(type(review).__name__, review.id,
                                           review.__dict__)
        with io.StringIO() as buf, redirect_stdout(buf):
            print(review)
            self.assertEqual(buf.getvalue(), expected)


if __name__ == "__main__":
    unittest.main()
