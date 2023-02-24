#!/usr/bin/python3
""" Test suite for Amenity class. """
import unittest
import models
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unit tests for Amenity class"""

    def test_instantiation(self):
        """Test that instance of Amenity can be instantiated."""
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, Amenity)

    def test_inheritance(self):
        """Test that the instance inherits from BaseModel."""
        self.assertTrue(issubclass(Amenity, models.base_model.BaseModel))

    def test_attributes(self):
        """Test that the instance has expected attributes."""
        my_amenity = Amenity()
        self.assertTrue(hasattr(my_amenity, 'name'))
        self.assertEqual(my_amenity.name, '')

    def test_str(self):
        """Test that str method returns expected string."""
        my_amenity = Amenity()
        expected = "[{}] ({}) {}".format(my_amenity.__class__.__name__, my_amenity.id, my_amenity.__dict__)
        self.assertEqual(str(my_amenity), expected)

    def test_save(self):
        """Test that save method updates updated_at attribute."""
        my_amenity = Amenity()
        created_at = my_amenity.created_at
        updated_at = my_amenity.updated_at
        my_amenity.save()
        self.assertNotEqual(updated_at, my_amenity.updated_at)
        self.assertEqual(created_at, my_amenity.created_at)

    def test_to_dict(self):
        """Test that to_dict method returns expected dictionary."""
        my_amenity = Amenity()
        my_amenity.name = "wifi"
        my_amenity_dict = my_amenity.to_dict()
        expected_dict = {
            'id': my_amenity.id,
            'created_at': my_amenity.created_at.isoformat(),
            'updated_at': my_amenity.updated_at.isoformat(),
            '__class__': 'Amenity',
            'name': 'wifi'
        }
        self.assertDictEqual(my_amenity_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
