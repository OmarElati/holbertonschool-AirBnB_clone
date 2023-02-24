#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
import json
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel"""

    def test_init(self):
        """Test that an instance of BaseModel is properly initialized"""
        my_model = BaseModel()
        self.assertTrue(isinstance(my_model, BaseModel))
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model.created_at).__name__, "datetime")
        self.assertEqual(type(my_model.updated_at).__name__, "datetime")

    def test_save(self):
        """Test the save method of BaseModel"""
        my_model = BaseModel()
        updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(my_model.updated_at, updated_at)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel"""
        my_model = BaseModel()
        my_model.name = "Test"
        my_model.my_number = 123
        my_model_dict = my_model.to_dict()
        self.assertTrue(isinstance(my_model_dict, dict))
        self.assertTrue("__class__" in my_model_dict)
        self.assertTrue("id" in my_model_dict)
        self.assertTrue("created_at" in my_model_dict)
        self.assertTrue("updated_at" in my_model_dict)
        self.assertTrue("name" in my_model_dict)
        self.assertTrue("my_number" in my_model_dict)
        self.assertEqual(my_model_dict["__class__"], "BaseModel")
        self.assertEqual(my_model_dict["name"], "Test")
        self.assertEqual(my_model_dict["my_number"], 123)

    def test_str(self):
        """Test the __str__ method of BaseModel"""
        my_model = BaseModel()
        my_model.name = "Test"
        my_model.my_number = 123
        my_model_str = str(my_model)
        self.assertTrue("[BaseModel]" in my_model_str)
        self.assertTrue("id" in my_model_str)
        self.assertTrue("created_at" in my_model_str)
        self.assertTrue("updated_at" in my_model_str)
        self.assertTrue("name" in my_model_str)
        self.assertTrue("my_number" in my_model_str)
        self.assertTrue("Test" in my_model_str)
        self.assertTrue("123" in my_model_str)


if __name__ == '__main__':
    unittest.main()
