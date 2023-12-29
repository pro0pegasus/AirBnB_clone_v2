#!/usr/bin/python3
"""
Define State class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state

    Attributes:
        name (str): name of state

    """
    name = ""
