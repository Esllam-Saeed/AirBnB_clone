#!/usr/bin/python3
""" This module contains the definition for the 'Review' Class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Definition for Review Class, Subclass of BaseModel """

    place_id = ""
    user_id = ""
    text = ""
