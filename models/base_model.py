#!/usr/bin/python3
"""Defines the BaseModel class."""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    from sqlalchemy import Column, String, Date
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(Date, nullable=False, default=datetime.utcnow())
    updated_at = Column(Date, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            if 'id' not in kwargs.keys():
                kwargs['id'] = str(uuid.uuid4())
            if 'updated_at' in kwargs.keys():
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
            else:
                kwargs['updated_at'] = datetime.utcnow().isoformat()
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
            if 'created_at' in kwargs.keys():
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
            else:
                kwargs['created_at'] = datetime.utcnow().isoformat()
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
            if '__class__' in kwargs.keys():
                del kwargs['__class__']
            self.__dict__.update(kwargs)


    def save(self):
        """Update updated_at with the current datetime."""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        d = self.__dict__.copy()
        d.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """ Deleting instance from storage """
        from models import storage
        storage.delete(self)
