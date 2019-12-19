import scrapy
from ..items import ShoesItem
from scrapy.http import Request

#The base url has the main url we scrape from
#URLS is a list with the same url but with pages
#1-25 so we can scrape  those pages
# base_url = 'https://stockx.com/sneakers?page='
# URLS = [base_url + str(i) for i in range(1, 25)]



class StockxSpider(scrapy.Spider):
    name = 'stockx'
    page_number = 2
    start_urls = [
        'https://stockx.com/sneakers/release-date?page=1&years=2018',
        'https://stockx.com/sneakers/release-date?page=2&years=2018',
        'https://stockx.com/sneakers/release-date?page=3&years=2018',
        'https://stockx.com/sneakers/release-date?page=4&years=2018',
        'https://stockx.com/sneakers/release-date?page=5&years=2018',
        'https://stockx.com/sneakers/release-date?page=6&years=2018',
        'https://stockx.com/sneakers/release-date?page=7&years=2018',
        'https://stockx.com/sneakers/release-date?page=8&years=2018',
        'https://stockx.com/sneakers/release-date?page=9&years=2018',
        'https://stockx.com/sneakers/release-date?page=10&years=2018',
        'https://stockx.com/sneakers/release-date?page=11&years=2018',
        'https://stockx.com/sneakers/release-date?page=12&years=2018',
        # 'https://stockx.com/sneakers/release-date?page=13&years=2018',
        # 'https://stockx.com/sneakers/release-date?page=14&years=2018',
        # 'https://stockx.com/sneakers/release-date?page=15&years=2018',
        # 'https://stockx.com/sneakers/release-date?page=16&years=2018',
        # 'https://stockx.com/sneakers/release-date?page=17&years=2018',
        # 'https://stockx.com/sneakers/release-date?page=18&years=2018',
        # 'https://stockx.com/sneakers/release-date?page=19&years=2018',
        # 'https://stockx.com/sneakers/release-date?page=20&years=2018',
        # 'https://stockx.com/sneakers/release-date?page=21&years=2018',
        # 'https://stockx.com/sneakers/release-date?page=22&years=2018',
        # 'https://stockx.com/sneakers/release-date?page=23&years=2018',
        # 'https://stockx.com/sneakers/release-date?page=24&years=2018',
        # 'https://stockx.com/sneakers/release-date?page=25&years=2018',
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
        # next_page = 'https://stockx.com/sneakers/release-date?page=' + str(StockxSpider.page_number) + ''
        # years = '&years=2012,2013'
        # if StockxSpider.page_number <= 25:
        #     StockxSpider.page_number += 1
        #     for i in range(len(URLS)):
        #         page_url  = str(URLS[i])
        #         new_url = page_url + years
        #         yield scrapy.Request(new_url)


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