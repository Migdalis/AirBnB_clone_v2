#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'state_id' in kwargs:
            self.state_id = kwargs['state_id']
