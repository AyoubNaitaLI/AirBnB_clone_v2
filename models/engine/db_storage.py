#!/usr/bin/python3
""" This is the db_storage module """
from sqlalchemy import create_engine
import os


class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        """ Instantiation of engine """
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)
        env = os.getenv('HBNB_ENV')
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returning the objects """
        from models.user import User
        from models.state import State
        from models.city import City
        from models.review import Review
        from models.amenity import Amenity
        from models.place import Place
        if cls is not None:
            objs = {}
            for obj in self.__session.query(cls).all():
                objs[cls.__name__ + "." + obj.id] = obj
            return objs
        else:
            objs = {}
            for obj in self.__session.query(User, State, City, Amenity, Place,
                                            Review).all():
                objs[cls.__name__ + "." + str(obj.id)] = obj
            return objs

    def new(self, obj):
        """ Adding new objects """
        self.__session.add(obj)

    def save(self):
        """ Commiting changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete obj if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Create the tables in the database """
        from sqlalchemy.orm import sessionmaker, scoped_session
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.state import State
        from models.city import City
        from models.review import Review
        from models.amenity import Amenity
        from models.place import Place
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(expire_on_commit=True)
        Session = scoped_session(Session)
        Session.configure(bind=self.__engine)
        self.__session = Session()

    def close(self):
        """ Close method """
        self.__session.close()
