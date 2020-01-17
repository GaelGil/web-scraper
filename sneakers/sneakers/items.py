# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SneakersItem(scrapy.Item):
    sneaker_name = scrapy.Field()
    sneaker_last_sale = scrapy.Field()
    pass


# this isn't used anymore
# class BredItem(scrapy.Item):
#     chart = scrapy.Field()
#     td = scrapy.Field()
#     pass


class ShoesItem(scrapy.Item):
    sneaker_name = scrapy.Field()
    sneaker_price = scrapy.Field()
    release_date = scrapy.Field()



