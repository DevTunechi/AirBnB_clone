#!/usr/bin/env python3
"""User Module Defines the user Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This defines User class.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
