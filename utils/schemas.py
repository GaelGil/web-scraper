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


class Product(BaseModel):
    """A Class to store the data we get from a product"""

    name: Optional[str] = None
    xpath: Optional[str] = None


class Url(BaseModel):
    """A Class to store the data we get from a product"""

    url: Optional[str] = None


class GoodReads(BaseModel):
    products: list[Product]
    products_xpath: Optional[str]
    urls: list[Url]
    next_page_button_xpath: Optional[str]
    multiple: dict
    categories_button: Optional[str]
    categories: Optional[str]
    popup: Optional[str]
    close_popup_button: Optional[str]


class StockX(BaseModel):
    products: list[Product]
    products_xpath: Optional[str]
    urls: list[Url]
    next_page_button_xpath: Optional[str]
    multiple: dict
    categories_button: Optional[str]
    categories: Optional[str]
    popup: Optional[str]
    close_popup_button: Optional[str]
