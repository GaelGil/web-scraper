import scrapy
from ..items import ShoesItem
from scrapy.http import Request

#The base url has the main url we scrape from
#URLS is a list with the same url but with pages
#1-25 so we can scrape  those pages
base_url = 'https://stockx.com/sneakers?page='
URLS = [base_url + str(i) for i in range(1, 25)]

class StockxSpider(scrapy.Spider):
    name = 'stockx'
    page_number = 2
    start_urls = [
        'https://stockx.com/sneakers',
    ]
    for i in range(len(URLS)):
        start_urls.append(URLS[i])  

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