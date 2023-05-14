#!/usr/bin/python3
""" BaseModel Module """
import uuid
from datetime import datetime as dt
import engine.file_storage

storage = engine.file_storage.FileStorage()


class BaseModel:
    """BaseModel Class"""
    def __init__(self, *args, **kwargs):
        """Initilize BaseModel"""
        if kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = dt.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = dt.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    if key != "__class__":
                        self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)

    def save(self):
        """Update the updated_at"""
        if self.created_at != dt.now():
            self.updated_at = dt.now()
            storage.save()

    def to_dict(self):
        """Generate Object dictionary"""
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat("T")
        self.__dict__["updated_at"] = self.updated_at.isoformat("T")
        return self.__dict__

    def __str__(self):
        """Override the object string representation"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
