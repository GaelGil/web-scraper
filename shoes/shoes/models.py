# from sqlalchemy import create_engine, Column, Table, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Integer, String
# from scrapy.utils.project import get_project_settings

# DeclarativeBase = declarative_base()

# def db_connect():
#     return create_engine(get_project_settings().get("CONNECTION_STRING"))

# def create_table(engine):
#     DeclarativeBase.metadata.create_all(engine)

# class SneakersDB(DeclarativeBase):
#     __tablename__ = "sneaker_table"

#     id = Column(Integer, primary_key=True)
#     shoe = Column('shoe', String())
#     price = Column('author', Integer())