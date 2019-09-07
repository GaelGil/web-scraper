import scrapy
from ..items import ShoesItem
# from scrapy.spiders import Spider

class StockxSpider(scrapy.Spider):
    name = 'stockx_shoes'
    # allowed_domains = ]
    start_urls = [
        'https://stockx.com/sneakers'
    ]

    def parse(self, response):
        items = ShoesItem()
        all_shoes = response.css('div.iCgYKH')

        for shoe in all_shoes:
            show_name = shoe.css('.gMymmc::text').extract()
            shoe_price = shoe.css('.jwzdVc::text').extract()
            
            items['shoe'] = show_name
            items['price'] = shoe_price

            yield items


class GoatSpider(scrapy.Spider):
    name = 'goat_shoes'
    start_urls = [
        'https://www.goat.com/sneakers'
    ]

    def parse(self, response):
        items = ShoesItem()
        all_shoes = response.css('div.kufmhh')
        for shoe in all_shoes:
            goat_name = shoe.css('.truncate::text').extract()
            goat_price = shoe.css('.gBogxQ::text').extract()

            items['shoe'] = goat_name
            items['price'] = goat_price

            yield items