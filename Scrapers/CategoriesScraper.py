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
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

class CategoriesScraper(BaseScraper):
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

    def scrape(self, url: str) -> list:
        """This function gets categories from a website

        Given a url and a xpath to categories on a website. This function
        goes to that page and gets categories to use to generate search 
        queries/urls. For example ebay has categories such as kitchen, clothes
        collectibles, electronics etc. We scrape that text from the webstite
        to use to generate search urls later.
    
        Args:
            url: The url of the page we want to visit
            xpath:  The xpath of the categories. 

        Returns: 
            list
        """
        self.get_url(url=url)
        try:
            self.wait_click(self.config['CATEGORIES_BUTTON'])
            categories_links = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, self.config['CATEGORIES'])))
        except NoSuchElementException: 
            self.log_message('i', 'Next button not found. Done finding links')
            return
        return [link.text for link in categories_links]
    
    def generate_urls(self, url: str, categories: list) -> list:
        """
        """
        urls = []
        for category in categories:
            if not category:
                continue
            urls.append(url % category)
        return urls
