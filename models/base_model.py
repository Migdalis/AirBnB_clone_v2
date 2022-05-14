#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        print("ID {}".format(self.id))
        new_dict = self.create_dict_params(args)
        if new_dict:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)
            print("Dict class 1 {}".format(self.__dict__))
        else:
            storage.new(self)
            print("Dict class 2 {}".format(self.__dict__))

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def create_dict_params(self, *args):
        print("In dic {}".format(type(args)))
        dict_params = dict((x, y) for x, y in args[1:])
        """for arg in args:
            key = arg.split('=')[0]
            value = arg.split('=')[1]
            if isinstance(value, str) and '\"' in value:
                value = value.replace('_', ' ')
                value = value.replace('\"', '')
                dict_params[key.replace('\'', '')] = value"""
        print("Type: {}".format(dict_params))
        return dict_params
