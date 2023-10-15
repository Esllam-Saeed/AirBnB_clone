#!/usr/bin/python3
""" This module contains the definition for the 'City' Class """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class Definition for City Class, Subclass of BaseModel """

    state_id = ""
    name = ""
