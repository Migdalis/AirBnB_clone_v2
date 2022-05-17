#!/usr/bin/python3
"""Module that define unittests to models/place.py"""
from tests.test_models.test_base_model import test_basemodel
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlaceModel(unittest.TestCase):
    """Class to test the Place class"""

    def test_inheritance(self):
        """Test class type"""
        inst_place = Place()
        self.assertIsInstance(inst_place, Place)
        self.assertIsInstance(inst_place, BaseModel)

    def test_attributes(self):
        "Test to verify if has atrributes"
        inst_place = Place()
        self.assertTrue(hasattr(inst_place, "id"))
        self.assertTrue(hasattr(inst_place, "created_at"))
        self.assertTrue(hasattr(inst_place, "updated_at"))

        self.assertFalse(hasattr(inst_place, "city_id"))
        self.assertFalse(hasattr(inst_place, "name"))
        inst_place.city_id = "564"
        inst_place.name = "California"
        self.assertTrue(hasattr(inst_place, "city_id"))
        self.assertTrue(hasattr(inst_place, "name"))


class test_Place(test_basemodel):
    """ Class to test the Place class """

    def __init__(self, *args, **kwargs):
        """ Test new instance Place"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Test type city id"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Test type user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ Test type name """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ Test type description"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Test type number rooms """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Test type number bathrooms """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Test type max guest """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Test type price by night """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Test type latitude """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ Test type  longitude """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ Test type amenity ids """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
