#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ Class to handle a State """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    def __init__(self, *args, **kwargs):
        """Constructor to a new instance of state"""
        super().__init__(self, *args, **kwargs)

    if models.storage_t != 'db':
        @property
        def citties(self):
            """Returns the list of City instances with
            state_id equals to the current State.id"""
            new_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    new_list.append(city)
            return new_list
