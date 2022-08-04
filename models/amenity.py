#!/usr/bin/python
""" Amenity class, inherits from BaseModel """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class, inherits from BaseModel """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Amenity initializer"""
        super().__init__(*args, **kwargs)
