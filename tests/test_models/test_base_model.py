#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class
    """

    def setUp(self):
        """
        Set up test environment
        """
        self.model = BaseModel()

    def tearDown(self):
        """
        Tear down test environment
        """
        del self.model
        try:
            os.remove("file.json")
        except:
            pass

    def test_instance_type(self):
        """
        Test instance type
        """
        self.assertIsInstance(self.model, BaseModel)

    def test_id_generation(self):
        """
        Test id generation
        """
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at_type(self):
        """
        Test created_at type
        """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_type(self):
        """
        Test updated_at type
        """
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        """
        Test save method
        """
        self.model.save()
        self.assertNotEqual(self.model.created_at, self.model.updated_at)

    def test_to_dict(self):
        """
        Test to_dict method
        """
        dict_ = self.model.to_dict()
        self.assertIsInstance(dict_, dict)
        self.assertEqual(dict_["id"], self.model.id)
        self.assertEqual(dict_["created_at"], self.model.created_at.isoformat())
        self.assertEqual(dict_["updated_at"], self.model.updated_at.isoformat())
        self.assertEqual(dict_["__class__"], "BaseModel")

    def test_init_dict(self):
        """
        Test __init__ method with dictionary
        """
        dict_ = self.model.to_dict()
        model2 = BaseModel(**dict_)
        self.assertNotEqual(self.model, model2)
        self.assertEqual(self.model.id, model2.id)
        self.assertEqual(self.model.created_at, model2.created_at)
        self.assertEqual(self.model.updated_at, model2.updated_at)

    def test_init_new(self):
        """
        Test __init__ method with new instance
        """
        model1 = BaseModel()
        model2 = BaseModel(id=model1.id, created_at=model1.created_at,
                            updated_at=model1.updated_at)
        self.assertNotEqual(model1, model2)
        self.assertEqual(model1.id, model2.id)
        self.assertEqual(model1.created_at, model2.created_at)
        self.assertEqual(model1.updated_at, model2.updated_at)


if __name__ == "__main__":
    unittest.main()
