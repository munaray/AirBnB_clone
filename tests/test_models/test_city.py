#!/usr/bin/python3
"""Unit Testing for Base Model"""
from contextlib import redirect_stdout
from datetime import datetime
from io import StringIO
import io
from models.city import City
import unittest
import time


class TestInstantation(unittest.TestCase):
    """Test the User Class"""
    def test_instantiation(self):
        city = City()
        self.assertIsInstance(city, City)

    def test_id_type(self):
        city = City()
        self.assertEqual(type(city.id), str)

    def test_uuid(self):
        city = City()
        other_city = City()
        self.assertNotEqual(city.id, other_city.id)

    def test_datetime(self):
        city = City()
        self.assertNotEqual(city.created_at, datetime.now())

    def test_datetime_type(self):
        city = City()
        self.assertEqual(type(city.created_at), datetime)

    def test_kwargs(self):
        city = City(new_city= "Kisumu")
        self.assertTrue(hasattr(city, 'new_city'))


class TestMethods(unittest.TestCase):
    """Tests public instance methods of basemodel"""
    def test_to_dict_type(self):
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(type(city_dict), dict)

    def test_dict_datetime_type(self):
        city = City()
        new_dict = city.to_dict()
        self.assertEqual(type(new_dict.get('created_at')), str)

    def test_save(self):
        """Tests the save() method"""
        city = City()
        time.sleep(0.5)
        date_now = datetime.now()
        city.save()
        diff = city.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_str(self):
        city = City()
        expected = "[{}] ({}) {}\n".format(type(city).__name__, city.id,
                                           city.__dict__)
        with io.StringIO() as buf, redirect_stdout(buf):
            print(city)
            self.assertEqual(buf.getvalue(), expected)


if __name__ == "__main__":
    unittest.main()
