#!/usr/bin/python3
"""Unittest for FileStorage"""
import os
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for file_storage.py"""

    def setUp(self):
        """Set up test environment"""
        try:
            os.remove("file.json")
        except Exception:
            pass
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down test environment"""
        try:
            os.remove("file.json")
        except Exception:
            pass

if __name__ == '__main__':
    unittest.main()
