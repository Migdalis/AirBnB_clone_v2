#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref



class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey('states.id'))

    def __init__(self, *args, **kwargs):
        """Constructor to a new instance of city"""
        super().__init__(self, *args, **kwargs)
