from sqlalchemy import Column, Integer, Text
from utils.db_connection import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=True)
    date = Column(Text, nullable=True)
    time = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    location = Column(Text, nullable=True)
    address = Column(Text, nullable=True)
    runtime = Column(Text, nullable=True)
    price = Column(Text, nullable=True)
