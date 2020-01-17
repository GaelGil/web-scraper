# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from .models import SneakerDB, db_connect, create_table
brands = ['jordan', 'adidas', 'nike', 'vans', 'reebok', 'puma', 
            'dior', 'asics', 'balenciaga', 'chanel', 'converse',
             'gucci', 'vuitton', 'balance', 'prada', 'saucony', 
             'armour',]



class SneakersPipeline(object):
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
        sneakers.sneaker = str(item['sneaker_name'])
    
        #### check for the brand
        for i in range(len(brands)):
            brand = brands[i]
            current_sneaker = str(item['sneaker_name'])
            if brand in current_sneaker.lower():
                sneakers.brand = brand
            else:
                sneaker_brand = "other"


        #this converts '$219' into 219
        sneakers.price = int(item['sneaker_price'][0][1:])
        


        sneakers.date = str(item['release_date'])

        try:
            session.add(sneakers)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
