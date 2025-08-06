from pydantic import BaseModel


class ScrapedItem(BaseModel):
    """A Class to store the data we get from a product"""

    title: str
    author: str
    raitings: int
    raiting: float
    reviews: int
    overview: str
    genres: str
    pages: int
    publish_date: str
