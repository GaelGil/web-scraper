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
from selenium.common.exceptions import NoSuchElementException, TimeoutException
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

        next_page(self, next_page: bool)
            This function sets the next page

        handle_popup(self, popup: bool)
            This function handles a popup if it is detected
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
            None
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


    def next_page(self, next_page: bool) -> str:
        """This function sets the next page

        Using the config, this function tries to find the next page button. If we
        find it we click it. If we can't find it we return false. If we do find it
        we return the url of the page we are on after clicking the next page button.

        Args:
            next_page: A boolean to see if we need to check for next page

        Returns: 
            str
        """
        if not next_page:
            return False
        try:
            self.wait_click(self.config['NEXT_PAGE_BUTTON_XPATH']['xpath'])
            time.sleep(3) 
        except (NoSuchElementException, TimeoutException):
            self.log_message('w', 'Next button not found or not clickable')
            return False
        except Exception as e:
            self.log_message('e', 'Unexpected error while navigating to next page')
            return False
        return self.driver.current_url # return url of page we are on
        
    def handle_popup(self, popup: bool):
        """This function handles a popup if it is detected

        Using the config, this function closes a popup if it appears on the page. 

        Args:
            popup: A boolean to see if we need to check for a popup

        Returns: 
            None
        """
        if not popup:
            return 
        time.sleep(5)  
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            popup = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal__content')]")))
            self.log_message('i', 'Popup detected!')
            close_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'modal__close')]//button")))
            close_button.click()
            self.log_message('i', 'Popup closed.')
        except TimeoutException:
            self.log_message('i', 'Popup not detected or not visible, continuing...')
