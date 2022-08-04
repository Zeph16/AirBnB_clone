#!/usr/bin/python3
""" User class, inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class, inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ User initializer """
        super().__init__(*args, **kwargs)
