#!/usr/bin/python3
""" State Module for HBNB project """
from hashlib import new
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """ Class to handle a State """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all")

    def __init__(self, *args, **kwargs):
        """Constructor to a new instance of state"""
        super().__init__(self, *args, **kwargs)

    @property
    def citties(self):
        """Returns the list of City instances with state_id equals to the current State.id"""
        new_list =[]
        all_cities = models.storage.all(City)
        for city in all_cities:
            if city.state_ide == self.id:
                new_list.append(city)
        return new_list
