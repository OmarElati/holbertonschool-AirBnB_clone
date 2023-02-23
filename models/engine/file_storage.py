#!/usr/bin/python3
import json
import models
from datetime import datetime

class FileStorage:
    """
    Serialize instances to a JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized = {}
        for key, value in FileStorage.__objects.items():
            serialized[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(serialized, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                deserialized = json.load(f)
            for key, value in deserialized.items():
                cls_name, obj_id = key.split(".")
                value["created_at"] = datetime.strptime(value["created_at"],
                                                         "%Y-%m-%dT%H:%M:%S.%f")
                value["updated_at"] = datetime.strptime(value["updated_at"],
                                                         "%Y-%m-%dT%H:%M:%S.%f")
                cls = models[cls_name]
                obj = cls(**value)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
