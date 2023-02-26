#!/usr/bin/python3
""" This module contains test cases for State """

import unittest
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    """
        Testing State class
    """
    def test_init(self):
        """
            Testing State instantiates
        """
        my_state = State()
        self.assertTrue(isinstance(my_state, State))

    def test_name_attr(self):
        """
            Testing State name attribute
        """
        my_state = State()
        self.assertTrue(hasattr(my_state, "name"))
        self.assertEqual(my_state.name, "")

    def test_create(self):
        """
            Test creating a new instance of the class
        """
        my_state = State()
        my_state.name = "California"
        my_state.save()
        all_objs = storage.all()
        self.assertTrue(all_objs["State.{}".format(my_state.id)])

    def test_save(self):
        """
            Testing State save method
        """
        my_state = State()
        my_state.save()
        self.assertNotEqual(my_state.created_at, my_state.updated_at)

    def test_to_dict(self):
        """
            Testing State to_dict method
        """
        my_state = State()
        my_state.name = "California"
        my_state_dict = my_state.to_dict()
        self.assertEqual(my_state_dict["__class__"], "State")
        self.assertEqual(str(my_state.id), my_state_dict["id"])
        self.assertEqual(my_state.created_at.isoformat(),
                         my_state_dict["created_at"])
        self.assertEqual(my_state.updated_at.isoformat(),
                         my_state_dict["updated_at"])
        self.assertEqual(my_state.name, my_state_dict["name"])

    def test_str(self):
        """
            Testing __str__ method
        """
        my_state = State()
        string = "[State] ({}) {}".format(my_state.id, my_state.__dict__)
        self.assertEqual(string, str(my_state))


if __name__ == '__main__':
    unittest.main()
