# -*- coding: utf-8 -*-
import scrapy
from ..items import ShoesItem
# BredItem

class BredSpiderSpider(scrapy.Spider):
    name = 'bred_spider'
    page_number = 2
    start_urls = [
        'https://stockx.com/sneakers/release-date?years=2012,2013&page=1',
        ]

    def parse(self, response):
        # selects a sneaker container div
        sneakers = response.css('.browse-tile')
        for sneaker in sneakers:
            # selects the name of the sneaker, price, and release date
            sneaker_name = sneaker.css('.hbRDwP , .hbRDwP div').css('::text').extract()
            sneaker_price = sneaker.css('.cziEBO::text').extract()
            sneaker_release_date = sneaker.css('.change::text').extract()



            items = ShoesItem()
            items['sneaker_name'] = sneaker_name
            items['sneaker_price'] = sneaker_price
            items['release_date'] = sneaker_release_date

            yield items

        next_page = 'https://stockx.com/sneakers/release-date?years=2012,2013&page='  + str(BredSpiderSpider.page_number) + ''
        if BredSpiderSpider.page_number <= 25:
            BredSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)


