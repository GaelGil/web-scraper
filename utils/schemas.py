from pydantic import BaseModel
from typing import Optional


class ScrapedItem(BaseModel):
    """A Class to store the data we get from a product"""

    title: Optional[str] = None
    author: Optional[str] = None
    ratings: Optional[str] = None
    rating: Optional[str] = None
    reviews: Optional[str] = None
    overview: Optional[str] = None
    genres: Optional[str] = None
    pages: Optional[str] = None
    publish_date: Optional[str] = None


class EventItem(BaseModel):
    """A Class to store the data we get from a product"""

    name = Optional[str] = None
    date = Optional[str] = None
    time = Optional[str] = None
    description = Optional[str] = None
    location = Optional[str] = None
    address = Optional[str] = None
    runtime = Optional[str] = None
    price = Optional[str] = None
