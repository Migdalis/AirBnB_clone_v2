#!/usr/bin/python3
"""Module that define unittests to models/city.py"""
from tests.test_models.test_base_model import test_basemodel
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCityModel(unittest.TestCase):
    """Class to test the City class"""

    def test_inheritance(self):
        """Test class type"""
        inst_city = City()
        self.assertIsInstance(inst_city, City)
        self.assertIsInstance(inst_city, BaseModel)

    def test_attributes(self):
        "Test to verify if has atrributes"
        inst_city = City()
        self.assertTrue(hasattr(inst_city, "id"))
        self.assertTrue(hasattr(inst_city, "created_at"))
        self.assertTrue(hasattr(inst_city, "updated_at"))

        self.assertFalse(hasattr(inst_city, "state_id"))
        self.assertFalse(hasattr(inst_city, "name"))
        inst_city.state_id = "675"
        inst_city.name = "California"
        self.assertTrue(hasattr(inst_city, "state_id"))
        self.assertTrue(hasattr(inst_city, "name"))


class test_City(test_basemodel):
    """ Class to test the City Class"""

    def __init__(self, *args, **kwargs):
        """ Test a new instance City Class"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Test type state id"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ Test type name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
