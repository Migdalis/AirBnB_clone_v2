#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """Constructor to a new instance of review"""
        super().__init__(self, *args, **kwargs)
