#!/usr/bin/python3
"""Tests for the BaseModel"""
import unittest
import pep8
from models.user import User


class TestUserClass(unittest.TestCase):
    """User Class Test"""
    @classmethod
    def setUpClass(cls):
        cls.testobj = User()

    @classmethod
    def tearDownClass(cls):
        del cls.testobj
    
    def test_base_model_style(self):
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, 'Check code with pep8')

    def test_base_model_docstrings(self):
        self.assertIsNotNone(User.__doc__)

    def test_user_properties(self):
        assert hasattr(self.testobj, 'email'), 'object lacks email property'
        assert hasattr(self.testobj, 'password'), 'object lacks password property'
        assert hasattr(self.testobj, 'first_name'), 'object lacks first_name property'
        assert hasattr(self.testobj, 'last_name'), 'object lacks last_name property'
