#!/usr/bin/python3
"""Definition of the FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This represent an engine storage

    Attributes:
        __file_path: string - path to the JSON file
        __objects: empty dict but will store all objects by class name id
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        new_dict = FileStorage.__objects
        to_serialized = {obj: new_dict[obj].to_dict() for obj in new_dict.keys()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(to_serialized, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                to_deserialize = json.load(f)
                loaded_objects = {}
                for k,v in to_deserialize.items():
                    cls_name = globals()[v['__class__']]
                    loaded_objects[k] = cls_name(**v)
                FileStorage.__objects = loaded_objects
        except Exception as e:
            pass
