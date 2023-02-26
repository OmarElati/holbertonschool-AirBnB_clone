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

    def test_all(self):
        """Test that all() method returns dictionary of all objects"""
        objects = FileStorage().all()
        self.assertEqual(type(objects), dict)
        key = '{}.{}'.format(type(self.my_model).__name__, self.my_model.id)
        self.assertIn(key, objects.keys())

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

    def test_reload_create_instance(self):
        """Test that reload method creates an instance of the stored class"""
        my_model = BaseModel()
        my_model.save()
        FileStorage().reload()
        key = '{}.{}'.format(type(my_model).__name__, my_model.id)
        obj = FileStorage._FileStorage__objects.get(key)
        self.assertIsNotNone(obj)
        self.assertEqual(obj.id, my_model.id)

    def test_reload_create_instance_with_dict(self):
        """Test that reload method creates instance from dictionary"""
        my_model = BaseModel()
        my_model.save()
        FileStorage().reload()
        key = '{}.{}'.format(type(my_model).__name__, my_model.id)
        obj = FileStorage._FileStorage__objects.get(key)
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertIsNotNone(new_obj)
        self.assertEqual(new_obj.id, my_model.id)

    def test_reload_all(self):
        """Test that reload method loads all objects"""
        my_model1 = BaseModel()
        my_model1.save()
        my_model2 = BaseModel()
        my_model2.save()
        FileStorage().reload()
        key1 = '{}.{}'.format(type(my_model1).__name__, my_model1.id)
        obj1 = FileStorage._FileStorage__objects.get(key1)
        key2 = '{}.{}'.format(type(my_model2).__name__, my_model2.id)
        obj2 = FileStorage._FileStorage__objects.get(key2)
        self.assertIsNotNone(obj1)
        self.assertEqual(obj1.id, my_model1.id)
        self.assertIsNotNone(obj2)
        self.assertEqual(obj2.id, my_model2.id)


if __name__ == '__main__':
    unittest.main()
