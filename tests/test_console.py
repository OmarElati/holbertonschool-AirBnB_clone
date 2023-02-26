#!/usr/bin/python3
"""Unittests for console.py"""

import sys
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test the console.py module"""

    def setUp(self):
        """Redirect stdout"""
        self.mock_stdout = StringIO()
        sys.stdout = self.mock_stdout

    def tearDown(self):
        """Restore stdout"""
        sys.stdout = sys.__stdout__


class TestHBNBCommand_quit(unittest.TestCase):
    """Unittests for testing exiting from the HBNB command interpreter."""

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


if __name__ == '__main__':
    unittest.main()
