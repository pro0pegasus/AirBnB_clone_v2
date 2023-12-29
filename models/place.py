#!/usr/bin/python3
"""
Mod for Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Inherit from BaseModel class

     Attributes:
        city_id (str): City id
        user_id (str): Usr id
        name (str): name of place.
        description (str): descr of place
        number_rooms (int): numb of rooms of  place
        number_bathrooms (int): numb of bathrooms of  place
        max_guest (int): max numb of guests of  place
        price_by_night (int): price by night of  place
        latitude (float): latitude of  place
        longitude (float): longitude of  place
        amenity_ids (list): list of Amenty ids

    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
