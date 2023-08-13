#!/usr/bin/python3
"""Unit Testing for Base Model"""
from contextlib import redirect_stdout
from datetime import datetime
from io import StringIO
import io
from models.place import Place
import unittest
import time


class TestInstantation(unittest.TestCase):
    """Test the User Class"""
    def test_instantiation(self):
        place = Place()
        self.assertIsInstance(place, Place)

    def test_id_type(self):
        place = Place()
        self.assertEqual(type(place.id), str)

    def test_uuid(self):
        place = Place()
        other_place = Place()
        self.assertNotEqual(place.id, other_place.id)

    def test_datetime(self):
        place = Place()
        self.assertNotEqual(place.created_at, datetime.now())

    def test_datetime_type(self):
        place = Place()
        self.assertEqual(type(place.created_at), datetime)

    def test_kwargs(self):
        place = Place(new_place="Kisumu")
        self.assertTrue(hasattr(place, 'new_place'))


class TestMethods(unittest.TestCase):
    """Tests public instance methods of basemodel"""
    def test_to_dict_type(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(type(place_dict), dict)

    def test_dict_datetime_type(self):
        place = Place()
        new_dict = place.to_dict()
        self.assertEqual(type(new_dict.get('created_at')), str)

    def test_save(self):
        """Tests the save() method"""
        place = Place()
        time.sleep(0.5)
        date_now = datetime.now()
        place.save()
        diff = place.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_str(self):
        place = Place()
        expected = "[{}] ({}) {}\n".format(type(place).__name__, place.id,
                                           place.__dict__)
        with io.StringIO() as buf, redirect_stdout(buf):
            print(place)
            self.assertEqual(buf.getvalue(), expected)


if __name__ == "__main__":
    unittest.main()
