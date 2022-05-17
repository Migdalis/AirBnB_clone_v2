#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class to handle a amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor to a new instance of amenity"""
        super().__init__(self, *args, **kwargs)
