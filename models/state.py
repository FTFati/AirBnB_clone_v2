#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)

        cities = relationship("City",
                              backref="state",
                              cascade="all, delete-orphan"
                              )
    else:
        name = ""

        @property
        def cities(self):
                if STORAGE_TYPE != 'db':
                    var = models.storage.all()
                    lista = []
                    result = []
                    for key in var:
                        city = key.replace('.', ' ')
                        city = shlex.split(city)
                        if city[0] == 'City':
                            lista.append(var[key])
                    for elem in lista:
                        if elem.state_id == self.id:
                            result.append(elem)
                    return result
                else:
                    return [city for city in self.cities]
