#!/usr/bin/python3
"""Unittest for City"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for City class"""

    def setUp(self):
        """Set up test environment"""
        self.city = City()

    def tearDown(self):
        """Tear down test environment"""
        del self.city

    def test_class(self):
        """Test City class"""
        self.assertEqual(City.__name__, "City")

    def test_attributes(self):
        """Test City attributes"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_attributes_types(self):
        """Test City attributes types"""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_save(self):
        """Test that save method saves successfully"""
        self.city.name = "San Francisco"
        self.city.state_id = "CA"
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """Test that to_dict method returns dict as expected"""
        self.city.name = "San Francisco"
        self.city.state_id = "CA"
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["name"], "San Francisco")
        self.assertEqual(city_dict["state_id"], "CA")
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)
        self.assertIsInstance(city_dict["id"], str)


if __name__ == "__main__":
    unittest.main()
