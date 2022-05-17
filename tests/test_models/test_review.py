#!/usr/bin/python3
""" Module that define unittests to models/review.py """
from tests.test_models.test_base_model import test_basemodel
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReviewModel(unittest.TestCase):
    """Class to test the Review class"""

    def test_inheritance(self):
        """Test class type"""
        inst_rev = Review()
        self.assertIsInstance(inst_rev, Review)
        self.assertIsInstance(inst_rev, BaseModel)

    def test_attributes(self):
        "Test to verify if has atrributes"
        inst_rev = Review()
        self.assertTrue(hasattr(inst_rev, "id"))
        self.assertTrue(hasattr(inst_rev, "created_at"))
        self.assertTrue(hasattr(inst_rev, "updated_at"))

        self.assertFalse(hasattr(inst_rev, "place_id"))
        self.assertFalse(hasattr(inst_rev, "user_id"))
        inst_rev.place_id = "564"
        inst_rev.user_id = "786"
        self.assertTrue(hasattr(inst_rev, "place_id"))
        self.assertTrue(hasattr(inst_rev, "user_id"))


class test_review(test_basemodel):
    """ Class to test the Review class """

    def __init__(self, *args, **kwargs):
        """ Test new instance review """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Test type place id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Test type user id """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Test type text """
        new = self.value()
        self.assertEqual(type(new.text), str)
