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
    page_number = 3
    start_urls = [
        'https://stockx.com/sneakers/release-date?years=2006&page=2',
    ]

    def parse(self, response):
        items = ShoesItem()
        all_shoes = response.css('div.iCgYKH')

        for shoe in all_shoes:
            show_name = shoe.css('.gMymmc::text').extract()
            shoe_price = shoe.css('.jwzdVc::text').extract()
            release_date =shoe.css('.fygSsx::text').extract()
            print(release_date[1])
                
            items['shoe'] = show_name
            items['price'] = shoe_price
            items['date'] = release_date[1]

            yield items
        # next_page = 'https://stockx.com/sneakers/release-date?years=2006&page=' + str(StockxSpider.page_number) + '/'
        # if StockxSpider.page_number <= 7:
        #     StockxSpider.page_number += 1
        #     for i in range(len(URLS)):
        #         yield scrapy.Request(URLS[i])


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