#!/usr/bin/python3
"""Unit Testing for Base Model"""
from contextlib import redirect_stdout
from datetime import datetime
from io import StringIO
import io
from models.state import State
import unittest
import time


class TestInstantation(unittest.TestCase):
    """Test the User Class"""
    def test_instantiation(self):
        state = State()
        self.assertIsInstance(state, State)

    def test_id_type(self):
        state = State()
        self.assertEqual(type(state.id), str)

    def test_uuid(self):
        state = State()
        other_state = State()
        self.assertNotEqual(state.id, other_state.id)

    def test_datetime(self):
        state = State()
        self.assertNotEqual(state.created_at, datetime.now())

    def test_datetime_type(self):
        state = State()
        self.assertEqual(type(state.created_at), datetime)

    def test_kwargs(self):
        state = State(new_state="Kentucky")
        self.assertTrue(hasattr(state, 'new_state'))


class TestMethods(unittest.TestCase):
    """Tests public instance methods of basemodel"""
    def test_to_dict_type(self):
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(type(state_dict), dict)

    def test_dict_datetime_type(self):
        state = State()
        new_dict = state.to_dict()
        self.assertEqual(type(new_dict.get('created_at')), str)

    def test_save(self):
        """Tests the save() method"""
        state = State()
        time.sleep(0.5)
        date_now = datetime.now()
        state.save()
        diff = state.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_str(self):
        state = State()
        expected = "[{}] ({}) {}\n".format(type(state).__name__, state.id,
                                           state.__dict__)
        with io.StringIO() as buf, redirect_stdout(buf):
            print(state)
            self.assertEqual(buf.getvalue(), expected)


if __name__ == "__main__":
    unittest.main()
