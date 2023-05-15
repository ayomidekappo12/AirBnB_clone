#!/usr/bin/python3
<<<<<<< HEAD

import json
import os


class FileStorage:
=======
"""
FileStorage that serializes and deserializes instances to a JSON file
"""
import json
import os.path

"""
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
"""


class FileStorage:
    """ String representing a simple data structure in JSON format.
        ex: '{ "12": { "numbers": [1, 2, 3], "name": "John" } }'
    """
>>>>>>> 5445d2765fc987d395eb6a949eb87aba334ef654
    __file_path = "file.json"
    __objects = {}

    def all(self):
<<<<<<< HEAD
        return FileStorage.__objects

    def new(self, obj):
        dict_key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[dict_key] = obj

    def save(self):
        sel_objects = {}
        for k, v in FileStorage.__objects.items():
            sel_objects[k] = v.dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(sel_objects, f)

    def reload(self):
        try:
	if not os.path.isfile(FileStorage.__file_path):
                return
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                sel_objects = json.load(f)
                for k, v in sel_objects.items():
                    cls_name, obj_id = k.split(".")
                    cls = eval(cls_name)
                    obj = cls(**v)
                    FileStorage.__objects[k] = obj
        except FileNotFoundError:
                pass
=======
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        dict_key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects.update({dict_key: obj})

    def save(self):
        """ serializes __objects to the JSON file """
        sel_objects = {}
        for key in self.__objects:
            sel_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(sel_objects, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                json_obj = json.load(f)
            for key, val in json_obj.items():
                self.__objects[key] = eval(val["__class__"])(**val)
>>>>>>> 5445d2765fc987d395eb6a949eb87aba334ef654
