#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ Class to handle a State """
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor to a new instance of state"""
        super().__init__(self, *args, **kwargs)
