import sqlite3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy.dialects.sqlite
from sqlalchemy import create_engine, Column, Table
from sqlalchemy import Integer, String, Text


DeclarativeBase = declarative_base()

def db_connect():
    """
    start the database
    """
    return create_engine('sqlite:///database.db')

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class SneakerDB(DeclarativeBase):
    """
    create the table and somecolumns
    """
    __tablename__ = "sneaker_table"

    id = Column(Integer, primary_key=True)
    sneaker = Column('sneaker', Text())
    price = Column('price', Integer())
