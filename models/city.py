#!/usr/bin/python
""" City class, inherits from BaseModel """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class, inherits from BaseModel """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ City initializer """
        super().__init__(*args, **kwargs)
