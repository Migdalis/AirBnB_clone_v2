#!/usr/bin/python3
""" Module that define unittests to models/user.py """
from tests.test_models.test_base_model import test_basemodel
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUserModel(unittest.TestCase):
    """Class to test the User class"""

    def test_inheritance(self):
        """Test class type"""
        inst_user = User()
        self.assertIsInstance(inst_user, User)
        self.assertIsInstance(inst_user, BaseModel)

    def test_attributes(self):
        "Test to verify if has atrributes of User"
        inst_user = User()
        self.assertTrue(hasattr(inst_user, "id"))
        self.assertTrue(hasattr(inst_user, "created_at"))
        self.assertTrue(hasattr(inst_user, "updated_at"))

        self.assertFalse(hasattr(inst_user, "first_name"))
        self.assertFalse(hasattr(inst_user, "last_name"))
        self.assertFalse(hasattr(inst_user, "email"))
        self.assertFalse(hasattr(inst_user, "password"))
        inst_user.first_name = "Maria"
        inst_user.last_name = "Lopez"
        inst_user.email = "emailmaria@gmail.com"
        inst_user.password = "123456"
        self.assertTrue(hasattr(inst_user, "first_name"))
        self.assertTrue(hasattr(inst_user, "last_name"))
        self.assertTrue(hasattr(inst_user, "email"))
        self.assertTrue(hasattr(inst_user, "password"))


class test_User(test_basemodel):
    """ Class to test the User class """

    def __init__(self, *args, **kwargs):
        """ Test a new instance User Class"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Test type first name"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Test type last name """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Test type email """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Test type password """
        new = self.value()
        self.assertEqual(type(new.password), str)
