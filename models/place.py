#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
import models
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60), ForeignKey("amenities.id"),
                             primary_key=True, nullable=False)
                )

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity", viewonly=True)
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Constructor to a new instance of place"""
        super().__init__(self, *args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """Returns the list of Review instances with place_id equals to the current Place.id"""
            new_list =[]
            all_reviews = models.storage.all(Review)
            for rvw in all_reviews.values():
                if rvw.place_id == self.id:
                    new_list.append(rvw)
            return new_list

        @property
        def amenities(self):
            """Returns the list of Amenity instances linked to the Place"""
            new_list =[]
            all_amenities = models.storage.all(Amenity)
            for amnt in all_amenities.values():
                if amnt.id in self.amenity_ids:
                    new_list.append(amnt)
            return new_list

        @amenities.setter
        def amenities(self, amenity):
            """Setter method for add an Amenity.id"""
            if type(amenity) == Amenity:
                self.amenity_ids.append(amenity.id)
