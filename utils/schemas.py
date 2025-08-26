from pydantic import BaseModel
from typing import Optional


class BookItem(BaseModel):
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


class SneakerItem(BaseModel):
    """A Class to store the data we get from a product"""

    name: Optional[str] = None
    img: Optional[str] = None
    retail_price: Optional[str] = None
    display_price: Optional[str] = None
    release_data: Optional[str] = None
    description: Optional[str] = None
    style: Optional[str] = None
    price_range_year: Optional[str] = None


class ToScrape(BaseModel):
    """A class for the name of the product info and the xpath"""

    name: Optional[str] = None
    xpath: Optional[str] = None


class Url(BaseModel):
    """A class for the url"""

    url: Optional[str] = None


class ScraperConfig(BaseModel):
    """A class for the config"""

    product_info: list[ToScrape]
    products_url_xpath: Optional[str]
    urls_to_scrape: list[Url]
    next_page_button_xpath: Optional[str]
    multiple: dict
    categories_button: Optional[str]
    categories: Optional[str]
    popup: Optional[str]
    close_popup_button: Optional[str]
