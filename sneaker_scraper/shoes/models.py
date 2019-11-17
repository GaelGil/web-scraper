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
    return create_engine('sqlite:///main_sneakers.db')

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class SneakerDB(DeclarativeBase):
    """
    create the table and columns for 
    sneaker, price, brand
    """
    __tablename__ = "year2008_and_09"

    id = Column(Integer, primary_key=True)
    sneaker = Column('sneaker', Text(200))
    price = Column('price', Text(200))
    brand = Column('brand', Text(200))
    date = Column('date', Text(200))
