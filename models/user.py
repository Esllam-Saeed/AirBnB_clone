#!/usr/bin/python3
""" This module contains the definition for the 'User' Class """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class Definition for User Class, Subclass of BaseModel """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
