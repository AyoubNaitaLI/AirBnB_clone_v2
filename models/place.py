#!/usr/bin/python3
""" This is the place module """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ This is the place class """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", backref="place")
    
    @property
    def reviews(self):
        review = []
        from models import storage
        for obj in storage.all(Review):
            if obj.place_id == self.id:
                review.append(obj)
        return review
    """place_amenity = Table("place_amenity", Base.metadata,
            Column("place_id", String(60), ForeignKey("places.id"),
                   primary_key=True, nullable=False),
            Column("amenity_id", String(60), ForeignKey("amenities.id"),
                   primary_key=True, nullable=False)
    )
    amenities = relationship("Amenity", secondary=place_amenity,
                             backref="place", viewonly=False)
    @property
    def amenities(self):
        return Place.amenity_ids

    @amenities.setter
    def amenities(self, value):
        from models.amenity import Amenity
        if type(value) is Amenity:
            Place.amenity_ids.append(value.id)"""
