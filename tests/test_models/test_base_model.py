#!/usr/bin/python3
"""Unit Testing for Base Model"""
from contextlib import redirect_stdout
from datetime import datetime
from io import StringIO
import io
from models.base_model import BaseModel
import unittest
import time


class TestInstantiation(unittest.TestCase):
    """Test the Base Model Class"""
    def test_instantiation(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_id_type(self):
        my_model = BaseModel()
        self.assertEqual(type(my_model.id), str)

    def test_uuid(self):
        my_model = BaseModel()
        other_model = BaseModel()
        self.assertNotEqual(my_model.id, other_model.id)

    def test_datetime(self):
        my_model = BaseModel()
        self.assertNotEqual(my_model.created_at, datetime.now())

    def test_datetime_type(self):
        my_model = BaseModel()
        self.assertEqual(type(my_model.created_at), datetime)

    def test_kwargs(self):
        my_model = BaseModel(name="first")
        self.assertTrue(hasattr(my_model, 'name'))


class TestMethods(unittest.TestCase):
    """Tests public instance methods of base model"""
    def test_to_dict_type(self):
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertEqual(type(my_model_dict), dict)

    def test_dict_datetime_type(self):
        my_model = BaseModel()
        new_dict = my_model.to_dict()
        self.assertEqual(type(new_dict.get('created_at')), str)

    def test_save(self):
        """Tests the save() method"""
        my_model = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        my_model.save()
        diff = my_model.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_str(self):
        model = BaseModel()
        expected = "[{}] ({}) {}\n".format(type(model).__name__, model.id,
                                           model.__dict__)
        with io.StringIO() as buf, redirect_stdout(buf):
            print(model)
            self.assertEqual(buf.getvalue(), expected)


if __name__ == "__main__":
    unittest.main()
