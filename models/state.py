#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """ Cities getter """
        from models import storage
        from models.city import City
        obj_list = storage.all(City)
        cities = []
        for key in obj_list.keys():
            if obj_list[key].state_id == self.id:
                cities.append(obj_list[key])
        return cities
