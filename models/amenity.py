#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        if 'name' in kwargs:
            self.name = kwargs['name']
