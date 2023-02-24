#!/usr/bin/python3
"""Unittest for FileStorage"""
import os
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage"""

    def setUp(self):
        """Sets up test environment"""
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """Tears down test environment"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_initialization(self):
        """Tests for initialization of FileStorage"""
        self.assertTrue(isinstance(self.storage, FileStorage))
        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(self.storage, "_FileStorage__objects"))
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertEqual(type(self.storage._FileStorage__objects), dict)
        self.assertEqual(len(self.storage.all()), 0)

    def test_all(self):
        """Tests for all method of FileStorage"""
        obj = BaseModel()
        obj_key = obj.__class__.__name__ + '.' + obj.id
        self.storage.new(obj)
        self.storage.save()
        self.assertEqual(type(self.storage.all()), dict)
        self.assertEqual(len(self.storage.all()), 1)
        self.assertIn(obj_key, self.storage.all().keys())
        self.assertIn(obj, self.storage.all().values())

    def test_new(self):
        """Tests for new method of FileStorage"""
        obj = BaseModel()
        obj_key = obj.__class__.__name__ + '.' + obj.id
        self.storage.new(obj)
        self.assertEqual(len(self.storage.all()), 1)
        self.assertIn(obj_key, self.storage.all().keys())
        self.assertIn(obj, self.storage.all().values())

    def test_save(self):
        """Tests for save method of FileStorage"""
        obj = BaseModel()
        obj_key = obj.__class__.__name__ + '.' + obj.id
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path, mode='r') as f:
            data = json.load(f)
        self.assertEqual(len(data), 1)
        self.assertIn(obj_key, data.keys())
        self.assertEqual(data[obj_key], obj.to_dict())

    def test_reload(self):
        """Tests for reload method of FileStorage"""
        obj = BaseModel()
        obj_key = obj.__class__.__name__ + '.' + obj.id
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 1)
        self.assertIn(obj_key, self.storage.all().keys())
        self.assertIn(obj, self.storage.all().values())


if __name__ == '__main__':
    unittest.main()
