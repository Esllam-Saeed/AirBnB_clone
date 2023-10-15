#!/usr/bin/python3
"""This is the file storage module: it creates
a new class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class FileStorage:
    """File Storage Engine Class Definition

    Class Attributes:
    __file_path: Data Storage Engine File Path
    __objects: Dictionary of objects to serialize/deserialize
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the dictionary of objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dict_obj = FileStorage.__objects
        j_dict_obj = {obj: dict_obj[obj].to_dict() for obj in dict_obj.keys()}
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(j_dict_obj, json_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as json_file:
                dict_obj = json.load(json_file)
                for value in dict_obj.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            return
