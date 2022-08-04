#!/usr/bin/python
""" Review class, inherits from BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class, inherits from BaseModel """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Review initializer """
        super().__init__(*args, **kwargs)
