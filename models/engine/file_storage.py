#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
import os
from models.base_model import BaseModel
from datetime import datetime
import models


class FileStorage:
    """Represents a class for serializing and deserializing instances
    to and from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add obj to __objects."""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file __file_path."""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, mode="w") as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """Deserialize __objects from JSON file __file_path."""
        try:
            with open(FileStorage.__file_path, mode="r") as json_file:
                obj_dict = json.load(json_file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    value["created_at"] = datetime.strptime(value["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                    value["updated_at"] = datetime.strptime(value["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                    cls = getattr(models, class_name)
                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects."""
        if obj is None:
            return
        key = obj.__class__.__name__ + "." + obj.id
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]

    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()
