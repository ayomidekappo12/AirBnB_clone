#!/usr/bin/python3
"""
this module creates a Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    class for managing review objects
    """
    place_id = ""
    user_id = ""
    text = ""