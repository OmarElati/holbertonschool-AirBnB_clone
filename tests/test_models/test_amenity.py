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

    def test_to_dict(self):
        """Test if dictionary is correctly formatted."""
        my_amenity = Amenity()
        amenity_dict = my_amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertTrue('name' in amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
