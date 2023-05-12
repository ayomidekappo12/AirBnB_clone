#!/usr/bin/python3
""" BaseModel Module """
import uuid
from datetime import datetime as dt


class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = dt.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = dt.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()

    def save(self):
        if self.created_at != dt.now():
            self.updated_at = dt.now()

    def to_dict(self):
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat("T")
        self.__dict__["updated_at"] = self.updated_at.isoformat("T")
        return self.__dict__

    def __str__(self):
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)


my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
