#!/usr/bin/python3

import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
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
