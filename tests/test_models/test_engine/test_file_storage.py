#!/usr/bin/python3
"""Unittest for FileStorage class"""

import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage"""

    def setUp(self):
        """Set up test environment"""
        self.file_path = FileStorage._FileStorage__file_path
        self.my_model = BaseModel()
        self.my_model.save()

    def tearDown(self):
        """Tear down test environment"""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_file_path_exists(self):
        """Test that __file_path is not None"""
        self.assertIsNotNone(FileStorage._FileStorage__file_path)

    def test_objects_dict_exists(self):
        """Test that __objects is not None"""
        self.assertIsNotNone(FileStorage._FileStorage__objects)

    def test_new(self):
        """Test that new object is stored in __objects"""
        key = '{}.{}'.format(type(self.my_model).__name__, self.my_model.id)
        self.assertIn(key, FileStorage._FileStorage__objects.keys())

    def test_save(self):
        """Test that __objects is saved to file"""
        key = '{}.{}'.format(type(self.my_model).__name__, self.my_model.id)
        self.my_model.save()
        with open(self.file_path, 'r') as f:
            self.assertIn(key, f.read())

    def test_reload(self):
        """Test that __objects is loaded from file"""
        key = '{}.{}'.format(type(self.my_model).__name__, self.my_model.id)
        self.my_model.save()
        FileStorage._FileStorage__objects.clear()
        self.assertEqual(len(FileStorage._FileStorage__objects), 0)
        FileStorage().reload()
        self.assertIn(key, FileStorage._FileStorage__objects.keys())

if __name__ == '__main__':
    unittest.main()
