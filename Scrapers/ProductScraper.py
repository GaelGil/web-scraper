"""Class to scrape data from individual products

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

"""

from .BaseScraper import BaseScraper
from ScrapedItem import ScrapedItem
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import requests
import time

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

        next_page(self, next_page: bool)
            This function sets the next page

        handle_popup(self, popup: bool)
            This function handles a popup if it is detected
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
        # i = 0
        for product in products: # for each link
            self.get_url(product) # set url for each link
            item = ScrapedItem() # create a scraped item instance
            for key, xpath in self.config['PRODUCT']['xpaths'].items(): # for each item and dictionary
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
        try:
            if key in self.config['MULTIPLE']:
                elements = self.driver.find_elements(By.XPATH, xpath)
                elements = [el.text.strip() for el in elements if el.text.strip()]
                elements = ' '.join(elements)
            else:
                element = self.driver.find_element(By.XPATH, xpath)
                if key == 'img':
                    img = element.get_attribute('src')
                    with open(f'{img}.png', 'wb') as f:
                        f.write(requests.get(img).content)
                    return img
                elements = element.text.strip()
        except Exception as e:
            self.log_message('e', 'Error while scraping handling data')
        return elements
    
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
