#!/usr/bin/python3
"""Definition of the BaseModal class"""
from models import storage
from uuid import uuid4
from datetime import datetime

class BaseModel():
    """BaseModel that defines all common
    attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Constructing a new BaseModel

        Args:
            *args: Tuple that contains arguments
            **kwargs: A dictionary that contains
              arguments by key/value
        """
        self.created_at = datetime.now()
        self.id = str(uuid4())
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, time_format)
                else:
                    self.__dict__[i] = j
        else:
            storage.new(self)


    def __str__(self) -> str:
        """This should print: [<class name>] (<self.id>) <self.__dict__>"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
            with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        dict_rep = self.__dict__.copy()
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        dict_rep["__class__"] = self.__class__.__name__
        return dict_rep
