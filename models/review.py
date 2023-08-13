#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review with the following atrr"""

    place_id = ""
    user_id = ""
    text = ""
