#!/usr/bin/python3
"""a new Class in my Module"""
from models.base_model import BaseModel

class Review(BaseModel):
    """The Client Opinion"""
    place_id = ""
    user_id = ""
    text = ""
