#!/usr/bin/python3
"""Module that define unittests to models/base_model.py"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
from time import sleep


class test_basemodel(unittest.TestCase):
    """Class to test base model """

    def __init__(self, *args, **kwargs):
        """Test to constructor """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def test_default(self):
        """Test new instances default """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ Test new instances with kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test types in dictionary """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test string """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ Test convert to dictionary"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ Test kwargs is none """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ Test kwargs have just a key"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ Test new instance id """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ Test format date created """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ Test format date updated """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

class TestBaseModel(unittest.TestCase):
    """Class to test the BaseModel class"""

    def test_id(self):
        """Test the id attribute"""
        inst_one = BaseModel()
        inst_two = BaseModel()
        self.assertIsInstance(inst_one, BaseModel)
        self.assertTrue(hasattr(inst_one, "id"))
        self.assertNotEqual(inst_one.id, inst_two.id)
        self.assertIsInstance(inst_one.id, str)
        inst_one = BaseModel(132)
        self.assertNotEqual(inst_one.id, 132)
        inst_one = BaseModel("Hello")
        self.assertNotEqual(inst_one.id, "Hello")
        inst_one = BaseModel([0, "h", 3])
        self.assertNotEqual(inst_one.id, [0, "h", 3])

    def test_create_at(self):
        """Test the create_at attribute"""
        inst = BaseModel()
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertIsInstance(inst.created_at, datetime)
        self.assertNotEqual(inst.created_at, datetime.now())

    def test_updated_at(self):
        """Test the updated_at attribute"""
        inst = BaseModel()
        self.assertTrue(hasattr(inst, "updated_at"))
        self.assertIsInstance(inst.updated_at, datetime)
        before_time_created = inst.created_at
        before_time_updated = inst.updated_at
        inst.save()
        self.assertNotEqual(before_time_updated, inst.updated_at)
        self.assertEqual(before_time_created, inst.created_at)

    def test_strclasname(self):
        """Test class name"""
        inst = BaseModel()
        self.assertEqual('[BaseModel]' in str(inst), True)

    def test_strint(self):
        """Test __string__"""
        inst = BaseModel()
        result = "[{}] ({}) {}".format(inst.__class__.__name__,
                                       inst.id, inst.__dict__)
        self.assertEqual(result, str(inst))

    def test_to_dict(self):
        """Test the values of dictionary method"""
        inst = BaseModel()
        dict_inst = inst.to_dict()
        self.assertTrue(dict, type(dict_inst))
        self.assertIn("id", dict_inst)
        self.assertIn("created_at", dict_inst)
        self.assertIn("updated_at", dict_inst)
        self.assertIn("__class__", dict_inst)
        self.assertEqual(str, type(dict_inst["created_at"]))
        self.assertEqual(str, type(dict_inst["updated_at"]))

    def test_save(self):
        """Test to save method"""
        inst = BaseModel()
        sleep(0.5)
        date_now = datetime.now()
        inst.save()
        diference = inst.updated_at - date_now
        self.assertTrue(abs(diference.total_seconds()) < 0.01)
