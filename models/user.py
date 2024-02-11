#!/usr/bin/python3
"""A USER Module"""
from models.base_model import BaseModel


class User(BaseModel):
    """The User Needed Attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
