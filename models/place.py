#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        if 'city_id' in kwargs:
            self.name = kwargs['city_id']
        if 'user_id' in kwargs:
            self.name = kwargs['user_id']
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'description' in kwargs:
            self.name = kwargs['description']
        if 'number_rooms' in kwargs:
            self.name = kwargs['number_rooms']
        if 'number_bathrooms' in kwargs:
            self.name = kwargs['number_bathrooms']
        if 'max_guest' in kwargs:
            self.name = kwargs['max_guest']
        if 'price_by_night' in kwargs:
            self.name = kwargs['price_by_night']
        if 'latitude' in kwargs:
            self.name = kwargs['latitude']
        if 'longitude' in kwargs:
            self.name = kwargs['longitude']
        if 'amenity_ids' in kwargs:
            self.name = kwargs['amenity_ids']