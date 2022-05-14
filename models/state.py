#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""

    def __init__(self, *args, **kwargs):
        print("Name args {}".format(args))
        print("Name kwargs {}".format(kwargs))
        super().__init__(self, args)
        print("Aqui {}".format(self.id))
        print("Name {}".format(kwargs))
        if kwargs:
            self.name = kwargs['name']
            print("In State: {}".format(self.name))

