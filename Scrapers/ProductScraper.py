"""Class to scrape data from individual products

This class inherits from the BaseScraper class. This class is used to
scrape data from individual prodcuts. Below is a short example of how
it is used.

  Typical usage example:
    from DriverManager import DriverManager
    from ScraperSetUp import CONFIG
    from Scrapers.ProductsScraper import ProductsScraper

    products = ['product_link1', 'product_link2']
    driver_manager = DriverManager(CONFIG['DRIVER_PATH'], CONFIG['HEADLESS'])
    product_scraper = ProductScraper(driver=driver_manager, config=CONFIG_GOODREADS)
    data = product_scraper.iterate_urls(products)
    print(f'Data: {data}')

"""

from .BaseScraper import BaseScraper
from ScrapedItem import ScrapedItem
from selenium.webdriver.common.by import By
import requests

class ProductScraper(BaseScraper):
    """
    A class used to scrape products of a page

    Attributes:
        BaseScraper Attributes: ProductsScraper inherits from BaseScraper

    Methods:
        iterate_urls(self, products: list)
            Function to visit each item given a list of items

        scrape(self, key: str, xpath: str)
            Function to scrape data from a product
    """

    def iterate_urls(self, products: list) -> dict:
        """Function to visit each item given a list of items
        
        This functions takes in a list of products as its argument. We itterate
        through the products and set the url of each. Then using the config
        we set earlier we will then scrape that data from each individual item.
        For example we have  ['product1_link', 'product2_link', ... 'productn_link'].
        We will iterate the list and get data for each prodcut using the function
        `scrape`. We then return the data we got from each prodcut.
        Args:
            products: A list of products we want to scrape

        Returns:
            list
        """
        data = []
        for product in products: # for each link
            self.get_url(product) # set url for each link
            item = ScrapedItem() # create a scraped item instance
            for key, xpath in self.config['PRODUCT'].items(): # for each item and dictionary
                elements = self.scrape(key, xpath) # get the elements using xpath
                item.add_field(key, elements) # insert the data collceted to scrapeditem
            data.append(item) # add item to list
        return data

    def scrape(self, key: str, xpath: str) -> list:
        """Function to scrape data from a product
        
        This functions scrapes data from a page. Given a key (name
        of the element we want to scrape) and a xpath to the element we
        scrape the data. Using the config, we check if we need to do
        multiple elements or just one. We also check for images.
        We then return the element we scraped. 

        Args:
            key: a sring that represents the name of the element we want to scrape
            xpath: a sring that represents the xpath of the element we want to 

        Returns:
            list
        """
        elements = ''
        if key in self.config['MULTIPLE']:
            elements = self.get_elements(xpath)
            texts = []
            for el in elements:
                try:
                    text = el.text.strip()
                    if text:
                        texts.append(text)
                except:
                    self.log_message('i', f'Skipped stale element while scraping key: {key}')
                    continue
            elements = ' '.join(texts)
        elif key == 'img':
            img = element.get_attribute('src')
            with open(f'./images/{img}.png', 'wb') as f:
                f.write(requests.get(img).content)    
            return img
        else:
            element = self.get_element(xpath)
            elements = element.text.strip()
        print()
        return elements

    