from sqlalchemy import Column, Integer, Text
from utils.db_connection import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=True)
    author = Column(Text, nullable=True)
    rating = Column(Text, nullable=True)
    ratings = Column(Text, nullable=True)
    reviews = Column(Text, nullable=True)
    overview = Column(Text, nullable=True)
    genres = Column(Text, nullable=True)
    pages = Column(Text, nullable=True)
    publish_date = Column(Text, nullable=True)
