#!/usr/bin/python3
"""Module that define unittests to models/amenity.py"""
from tests.test_models.test_base_model import test_basemodel
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenityModel(unittest.TestCase):
    """Class to test the Amenity class"""

    def test_inheritance(self):
        """Test class type"""
        inst_amenity = Amenity()
        self.assertIsInstance(inst_amenity, Amenity)
        self.assertIsInstance(inst_amenity, BaseModel)

    def test_attributes(self):
        "Test to verify if has atrributes"
        inst_amenity = Amenity()
        self.assertTrue(hasattr(inst_amenity, "id"))
        self.assertTrue(hasattr(inst_amenity, "created_at"))
        self.assertTrue(hasattr(inst_amenity, "updated_at"))

        self.assertFalse(hasattr(inst_amenity, "name"))
        inst_amenity.name = "California"
        self.assertTrue(hasattr(inst_amenity, "name"))

    def test_name2(self):
        """Test name type"""
        new = self.value()
        self.assertEqual(type(new.name), str)

class test_Amenity(test_basemodel):
    """ Class to test the Amenity class """

    def __init__(self, *args, **kwargs):
        """ Test a new instance Amenity Class"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Test type name """
        new = self.value()
        self.assertEqual(type(new.name), str)
