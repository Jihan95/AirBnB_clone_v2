#!/usr/bin/python3
"""
State class, a subclass of BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.engine import file_storage
from models.city import City
import os
storage = os.environ.get("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """
    A subclass of BaseModel class

    Public class attribute:
    name (str): state name
    """

    __tablename__ = 'states'
    if storage == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all,delete", backref="state")
    else:
        name = ""

    @property
    def cities(self):
        """cities property"""
        from models import storage
        list_of_cities = []
        allcities = storage.all(City)
        for city in allcities.values():
            if city.state_id == self.id:
                list_of_cities.append(city)
        return list_of_cities
