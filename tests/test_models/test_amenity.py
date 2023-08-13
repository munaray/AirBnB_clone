#!/usr/bin/python3
"""Unit Testing for Base Model"""
from contextlib import redirect_stdout
from datetime import datetime
from io import StringIO
import io
from models.amenity import Amenity
import unittest
import time


class TestInstantation(unittest.TestCase):
    """Test the User Class"""
    def test_instantiation(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_id_type(self):
        amenity = Amenity()
        self.assertEqual(type(amenity.id), str)

    def test_uuid(self):
        amenity = Amenity()
        other_amenity = Amenity()
        self.assertNotEqual(amenity.id, other_amenity.id)

    def test_datetime(self):
        amenity = Amenity()
        self.assertNotEqual(amenity.created_at, datetime.now())

    def test_datetime_type(self):
        amenity = Amenity()
        self.assertEqual(type(amenity.created_at), datetime)

    def test_kwargs(self):
        amenity = Amenity(new_amenity="toilet")
        self.assertTrue(hasattr(amenity, 'new_amenity'))


class TestMethods(unittest.TestCase):
    """Tests public instance methods of basemodel"""
    def test_to_dict_type(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(type(amenity_dict), dict)

    def test_dict_datetime_type(self):
        amenity = Amenity()
        new_dict = amenity.to_dict()
        self.assertEqual(type(new_dict.get('created_at')), str)

    def test_save(self):
        """Tests the save() method"""
        amenity = Amenity()
        time.sleep(0.5)
        date_now = datetime.now()
        amenity.save()
        diff = amenity.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_str(self):
        amenity = Amenity()
        expected = "[{}] ({}) {}\n".format(type(amenity).__name__,
                                           amenity.id, amenity.__dict__)
        with io.StringIO() as buf, redirect_stdout(buf):
            print(amenity)
            self.assertEqual(buf.getvalue(), expected)


if __name__ == "__main__":
    unittest.main()
