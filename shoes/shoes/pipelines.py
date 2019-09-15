# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import sqlalchemy
from sqlalchemy import Table, Column, Text, String, MetaData, create_engine, Integer
from sqlalchemy.orm import sessionmaker


# class ShoesPipeline(object):
#     def __init__(self):
#         engine = create_engine('sqlite:///test_db.db')
#         session = sessionmaker(bind=engine)()
        
#         shoe_name = Column(String, primary_key=True)
#         shoe_price = Column(Integer)


#this one works
class ShoesPipeline(object):
    def __init__(self):
        self.create_conncetion()
        self.create_table()
    
    def create_conncetion(self):
        self.conn = sqlite3.connect('shoes.db')
        self.curr =  self.conn.cursor()

    def create_table(self): 
        self.curr.execute("""DROP TABLE IF EXISTS shoes_table""")
        self.curr.execute("""create table shoes_table (
                        name text,
                        price text
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)

        # print("PipeLine" + item['shoe'][0])
        return item

    def store_db(self, item):
        self.curr.execute("""insert into shoes_table values (?, ?)""",(
            item['shoe'][0],
            item['price'][0]
        ))
        self.conn.commit()

