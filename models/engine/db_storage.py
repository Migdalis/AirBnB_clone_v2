#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone using sqlAlchemy"""
from sqlalchemy import create_engine
import models
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Class to manage storage of models in database"""
    __engine = None
    __session = None
    
    classes = {
               'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

    def __init__(self):
        """Initialize __engine with the Environment variables"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')
        ), pool_pre_ping=True)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return a dictionary of all objects depending of the class name """
        new_dict = {}
        if cls is None:
            for clss in DBStorage.classes:
                all_objs = self.__session.query(DBStorage[clss].all())
                for obj in all_objs:
                    key = obj.to_dict()['__class__'] + '.' + obj.id
                    new_dict[key] = obj
        else:
            all_objs = self.__session.query(cls).all()
            for obj in all_objs:
                    key = obj.to_dict()['__class__'] + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()
