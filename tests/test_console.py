#!/usr/bin/python3
"""Unittest for console.py"""
import unittest
import sys
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """Test cases for HBNBCommand class"""

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()
        self.saved_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        """Tear down test environment"""
        sys.stdout = self.saved_stdout

    def test_create(self):
        """Test create command"""
        self.assertFalse('BaseModel' in storage.all())
        self.console.onecmd("create BaseModel")
        self.assertTrue('BaseModel' in storage.all())

    def test_show(self):
        """Test show command"""
        self.console.onecmd("create BaseModel")
        obj_id = list(storage.all().keys())[0].split('.')[1]
        self.console.onecmd("show BaseModel {}".format(obj_id))
        self.assertTrue('[BaseModel]' in sys.stdout.getvalue())

    def test_destroy(self):
        """Test destroy command"""
        self.console.onecmd("create BaseModel")
        obj_id = list(storage.all().keys())[0].split('.')[1]
        self.assertTrue('BaseModel' in storage.all())
        self.console.onecmd("destroy BaseModel {}".format(obj_id))
        self.assertFalse('BaseModel' in storage.all())

    def test_all(self):
        """Test all command"""
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create BaseModel")
        self.console.onecmd("all BaseModel")
        self.assertIn('[BaseModel]', sys.stdout.getvalue())
        self.assertIn('2', sys.stdout.getvalue())

    def test_update(self):
        """Test update command"""
        self.console.onecmd("create BaseModel")
        obj_id = list(storage.all().keys())[0].split('.')[1]
        self.console.onecmd("update BaseModel {} first_name 'John'".format(obj_id))
        self.assertEqual(BaseModel.first_name, 'John')

    def test_emptyline(self):
        """Test emptyline method"""
        self.assertIsNone(self.console.onecmd(""))

    def test_quit(self):
        """Test quit command"""
        self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test EOF signal"""
        self.assertTrue(self.console.onecmd("EOF"))

    def test_invalid_command(self):
        """Test invalid command"""
        self.assertFalse(self.console.onecmd("invalidcommand"))

if __name__ == "__main__":
    unittest.main()
