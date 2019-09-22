# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from .models import SneakerDB, db_connect, create_table



class ShoesPipeline(object):
    def __init__(self):
        """
        starts database connection and creates table, 
        as well as session
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        """
        session = self.Session()
        sneakers = SneakerDB()

        # name of the shoe
        sneakers.sneaker = str(item['shoe'])

        #this converts '$219' into 219
        sneakers.price = int(item['price'][0][1:])
        
        #Gets brand of shoe by getting first word of name.
        #This will always work becuase the brand is always
        #the first word in the name of the shoe
        brand = str(item['shoe'][0])
        brand = brand.partition(' ')[0]
        sneakers.brand = brand

        try:
            session.add(sneakers)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item




#this one works
# class ShoesPipeline(object):
#     def __init__(self):
#         self.create_conncetion()
#         self.create_table()
    
#     def create_conncetion(self):
#         self.conn = sqlite3.connect('shoes.db')
#         self.curr =  self.conn.cursor()

#     def create_table(self): 
#         self.curr.execute("""DROP TABLE IF EXISTS shoes_table""")
#         self.curr.execute("""create table shoes_table (
#                         name text,
#                         price text
#                         )""")

#     def process_item(self, item, spider):
#         self.store_db(item)

#         # print("PipeLine" + item['shoe'][0])
#         return item

#     def store_db(self, item):
#         self.curr.execute("""insert into shoes_table values (?, ?)""",(
#             item['shoe'][0],
#             item['price'][0]
#         ))
#         self.conn.commit()

