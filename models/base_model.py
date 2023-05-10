#!/usr/bin/python3
""" BaseModel Module """
import uuid
from datetime import datetime as dt


class BaseModel():

    def __init__(self):
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
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
