#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        if 'email' in kwargs:
            self.name = kwargs['email']
        if 'password' in kwargs:
            self.name = kwargs['password']
        if 'first_name' in kwargs:
            self.name = kwargs['first_name']
        if 'last_name' in kwargs:
            self.name = kwargs['last_name']
