#!/usr/bin/python3
"""
Unit tests for console using Mock module from python standard library
Checks console for capturing stdout into a StringIO object
"""

import os
import sys
from models import storage
from models.engine.file_storage import FileStorage
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class ConsoleTestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        with patch('builtins.input', return_value="quit"):
            console.HBNBCommand().cmdloop()
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_line(self, mock_stdout):
        with patch('builtins.input', return_value=""):
            console.HBNBCommand().cmdloop()
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command(self, mock_stdout):
        with patch('builtins.input', side_effect=["create BaseModel", "quit"]):
            console.HBNBCommand().cmdloop()
        self.assertIn("BaseModel", mock_stdout.getvalue())

    # Add more test methods for other commands

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_command(self, mock_stdout):
        with patch('builtins.input', side_effect=["create BaseModel", "show BaseModel 123", "quit"]):
            console.HBNBCommand().cmdloop()
        self.assertIn("123", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_command(self, mock_stdout):
        with patch('builtins.input', side_effect=["create BaseModel", "destroy BaseModel 123", "show BaseModel 123", "quit"]):
            console.HBNBCommand().cmdloop()
        self.assertIn("** no instance found **", mock_stdout.getvalue())

    # Add more test methods for other commands

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_command(self, mock_stdout):
        with patch('builtins.input', side_effect=["create BaseModel", "create User", "create State", "all", "quit"]):
            console.HBNBCommand().cmdloop()
        self.assertIn("BaseModel", mock_stdout.getvalue())
        self.assertIn("User", mock_stdout.getvalue())
        self.assertIn("State", mock_stdout.getvalue())

    # Add more test methods for other commands

if __name__ == '__main__':
    unittest.main()
