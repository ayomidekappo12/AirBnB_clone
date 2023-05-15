#!/usr/bin/python3
"""Tests for the BaseModel"""
import unittest
import pep8
from models.base_model import BaseModel


class TestBaseModelClass(unittest.TestCase):
    """BaseModel Class Test"""
    @classmethod
    def setUpClass(cls):
        cls.testobj = BaseModel()
        cls.testobj.name = "My_First_Model"
        cls.testobj.my_number = 89

    @classmethod
    def tearDownClass(cls):
        del cls.testobj

    def test_base_model_style(self):
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, 'Check code with pep8')

    def test_base_model_docstrings(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_base_model_init(self):
        self.assertTrue(isinstance(self.testobj, BaseModel))
        self.assertEqual(self.testobj.created_at, self.testobj.updated_at)

    def test_base_model_save(self):
        self.testobj.save()
        self.assertNotEqual(self.testobj.created_at, self.testobj.updated_at)

    def test_base_model_to_dict(self):
        testobj_dict = self.testobj.to_dict()
        self.assertIsInstance(testobj_dict['created_at'], str)
        self.assertIsInstance(testobj_dict['updated_at'], str)
        self.assertEqual(self.testobj.__class__.__name__, 'BaseModel')
