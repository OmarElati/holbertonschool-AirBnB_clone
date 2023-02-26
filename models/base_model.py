#!/usr/bin/python3
"""
BaseModel module.
"""
import models
from datetime import datetime
import uuid


class BaseModel:
    """ class BasseModel. """
    def __init__(self, *args, **kwargs):
        """ Initialization of a new instance of BaseModel. """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            self.id = kwargs.get("id", str(uuid.uuid4()))
            self.created_at = kwargs.get("created_at", datetime.now())
            self.updated_at = kwargs.get("updated_at", datetime.now())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ String representation of BaseModel instance. """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Update the attribute 'updated_at' with the current datetime. """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing allkeys/
        values of __dict__ of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        if isinstance(obj_dict["created_at"], datetime):
            obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        if isinstance(obj_dict["updated_at"], datetime):
            obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict

    # Define the first_name attribute
    first_name = ""
