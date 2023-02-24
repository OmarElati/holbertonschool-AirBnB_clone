#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                json_dict = json.load(f)
            for key, value in json_dict.items():
                module_name, class_name = key.split('.')
                module = __import__('models.' + module_name, fromlist=[module_name])
                cls = getattr(module, class_name)
                self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
