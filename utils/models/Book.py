from sqlalchemy import Column, Integer, String
from utils.db_connection import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=True)
    author = Column(String(80), nullable=True)
    rating = Column(String(80), nullable=True)
    raitings = Column(String(80), nullable=True)
    reviews = Column(String(80), nullable=True)
    overview = Column(String(80), nullable=True)
    genres = Column(String(80), nullable=True)
    pages = Column(String(80), nullable=True)
    publish_date = Column(String(80), nullable=True)
