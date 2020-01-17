# -*- coding: utf-8 -*-
import scrapy
from ..items import SneakersItem
SneakersItem


class SneakerSpiderSpider(scrapy.Spider):
    name = 'sneaker'
    page_number = 2
    start_urls = [
        # 'https://stockx.com/sneakers/last-sale',
        'https://stockx.com/sneakers/last-sale?years=2019&page=1'
        ]

    def parse(self, response):
        sneakers = response.css('.browse-tile')
        for sneaker in sneakers:
            sneaker_name = sneaker.css('.hbRDwP , .hbRDwP div').css('::text').extract()
            sneaker_last_sale = sneaker.css('.change::text').extract()


            items = SneakersItem()
            items['sneaker_name'] = sneaker_name
            items['sneaker_last_sale'] = sneaker_last_sale

            yield items

        next_page = 'https://stockx.com/sneakers/last-sale?years=2019&page=' + str(SneakerSpiderSpider.page_number) + ''
        if SneakerSpiderSpider.page_number <= 25:
            SneakerSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)