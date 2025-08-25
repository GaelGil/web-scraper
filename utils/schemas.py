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


class Sneaker(BaseModel):
    """A Class to store the data we get from a product"""

    name: Optional[str] = None
    img: Optional[str] = None
    retail_price: Optional[str] = None
    display_price: Optional[str] = None
    release_data: Optional[str] = None
    description: Optional[str] = None
    style: Optional[str] = None
    price_range_year: Optional[str] = None


class ScrapeConfig(BaseModel):
    TITLE = "title"
    DESCRIPTION = "description"
    PRICE = "price"


class Config(BaseModel):
    """A Class to store the data we get from a product"""

    DRIVER_PATH: str
    HEADLESS: bool
    scrape_config: ScrapeConfig = ScrapeConfig
