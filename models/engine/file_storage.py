#!/usr/bin/python3
"""
This module defines the FileStorage class
"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    This class defines the FileStorage engine for AirBnB
    """

    __file_path = "file.json"
    __objects = {}

    classes = {
        'BaseModel': BaseModel
    }

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()

        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(json_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                json_dict = json.load(f)

            for key, value in json_dict.items():
                cls_name = value['__class__']
                if cls_name in self.classes:
                    self.__objects[key] = self.classes[cls_name](**value)
