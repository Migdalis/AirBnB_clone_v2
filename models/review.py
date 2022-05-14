#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        if 'place_id' in kwargs:
            self.name = kwargs['place_id']
        if 'user_id' in kwargs:
            self.name = kwargs['user_id']
        if 'text' in kwargs:
            self.name = kwargs['text']
