#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """The base model class"""
    def __init__(self, *args, **kwargs):
        """Initialize the base model"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __repr__(self):
        """Return a string representation of the object"""
        return f"<{self.__class__.__name__} {self.id}>"

    def to_dict(self):
        """Return a dictionary representation of the object"""
        data = {}
        for key, value in self.__dict__.items():
            if key.startswith('_'):
                continue
            if isinstance(value, datetime):
                data[key] = value.isoformat()
            else:
                data[key] = value
        return data

    def save(self):
        """Save the object"""
        self.updated_at = datetime.now()

    def delete(self):
        """Delete the object"""
        pass
