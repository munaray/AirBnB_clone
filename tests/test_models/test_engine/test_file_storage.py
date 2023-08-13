import unittest
import json
from unittest.mock import patch
from io import StringIO
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "test_file.json"
        self.file_storage = FileStorage()
        self.file_storage.__file_path = self.file_path

    def tearDown(self):
        """Remove the test file after each test"""
        try:
            with open(self.file_path, "w") as f:
                f.write("")  # Clear the contents of the file
        except FileNotFoundError:
            pass

    def test_all_method_returns_dict(self):
        result = self.file_storage.all()
        self.assertIsInstance(result, dict)

    def test_new_method(self):
        new_model = BaseModel()
        self.file_storage.new(new_model)
        self.assertIn("{}.{}".format(new_model.__class__.__name__, new_model.id), self.file_storage.all())

    def test_save_method(self):
        """Create a new model, save, and then load the data from the file"""
        new_model = BaseModel()
        self.file_storage.new(new_model)
        self.file_storage.save()

        loaded_file_data = None
        with open(self.file_path, "r") as f:
            loaded_file_data = json.load(f)

        self.assertIn("{}.{}".format(new_model.__class__.__name__, new_model.id), loaded_file_data)

    def test_reload_method(self):
        """Create a new model, save, then reload the data and check if it exists"""
        new_model = BaseModel()
        self.file_storage.new(new_model)
        self.file_storage.save()

        new_file_storage = FileStorage()
        new_file_storage.__file_path = self.file_path
        new_file_storage.reload()

        self.assertIn("{}.{}".format(new_model.__class__.__name__, new_model.id), new_file_storage.all())

    def test_reload_method_file_not_found(self):
        """Test that reload method handles FileNotFoundError"""
        with patch("builtins.open", side_effect=FileNotFoundError()):
            self.file_storage.reload()

    def test_reload_method_invalid_json(self):
        """Test that reload method handles invalid JSON data"""
        with open(self.file_path, "w") as f:
            f.write("invalid json")

        self.file_storage.reload()

    def test_reload_method_with_existing_objects(self):
        """Test that reload method properly adds loaded objects to __objects"""
        model_data = {
            "BaseModel.abc123": {"__class__": "BaseModel", "id": "abc123"},
            "User.xyz456": {"__class__": "User", "id": "xyz456"}
        }

        with open(self.file_path, "w") as f:
            json.dump(model_data, f)

        self.file_storage.reload()
        self.assertIn("BaseModel.abc123", self.file_storage.all())
        self.assertIn("User.xyz456", self.file_storage.all())

if __name__ == '__main__':
    unittest.main()
