#!/usr/bin/python3
"""Tests for the BaseModel"""
import unittest
import os
import pep8
from models.base_model import BaseModel
from models.user import User


class TestUserClass(unittest.TestCase):
    """User Class Test"""
    @classmethod
    def setUpClass(cls):
        cls.testuser = User()
        cls.testuser.email = "akinayomide@alx.com"
        cls.testuser.password = "password"
        cls.testuser.first_name = "Akin"
        cls.testuser.last_name = "Ayomide"

    @classmethod
    def tearDownClass(cls):
        del cls.testuser
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass
  
    def test_user_style(self):
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, 'Check code with pep8')

    def test_user_is_subclass(self):
        self.assertTrue(issubclass(self.testuser.__class__, BaseModel))

    def test_user_docstrings(self):
        self.assertIsNotNone(User.__doc__)

    def test_user_properties(self):
        proplist = ['id', 'created_at', 'email', 'password', 'first_name', 'last_name']
        for property in proplist:
            self.assertTrue(property in self.testuser.__dict__, f"{property} is not a property")

    def test_user_properties_str(self):
        self.assertEqual(type(self.testuser.email), str, "email must be str")
        self.assertEqual(type(self.testuser.password), str, "password must be str")
        self.assertEqual(type(self.testuser.first_name), str, "first_name must be str")
        self.assertEqual(type(self.testuser.last_name), str, "last_name must be str")

    def test_user_save(self):
        self.testuser.save()
        self.assertNotEqual(self.testuser.created_at, self.testuser.updated_at)
