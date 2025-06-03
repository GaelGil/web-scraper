"""Class to scrape a website for the items displayed in it.

This class inherits from the BaseScraper class. This class is used to
scrape product links from a website. Below is a short example of how
it is used.

  Typical usage example:
    from DriverManager import DriverManager
    from ScraperSetUp import CONFIG
    from Scrapers.ProductsScraper import ProductsScraper

    driver_manager = DriverManager(CONFIG['DRIVER_PATH'], CONFIG['HEADLESS'])
    products_scraper = ProductsScraper(driver=driver_manager, config=CONFIG)
    products = products_scraper.iterate_urls(stop=2, next_page=True, popup=True)
    print(f'Products: {products}')
    
"""

from .BaseScraper import BaseScraper
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class ProductsScraper(BaseScraper):
    """
    A class used to scrape products of a page

    Attributes:
        BaseScraper Attributes: ProductsScraper inherits from BaseScraper

    Methods:
        iterate_urls(self, next_page: bool, popup: bool, count: int, stop: int):
            Function to visit websites and scrape links to products

        scrape(self)
            Function to scrape data links from a page

        next_page(self, next_page: bool)
            This function sets the next page

        handle_popup(self, popup: bool)
            This function handles a popup if it is detected
    """

    def iterate_urls(self, next_page: bool, popup: bool, count: int=1, stop: int=5) -> list:
        """Function to visit websites and scrape links to products
        
        Using the config set in the scraper. We itterate urls of pages
        that have products on their page. We handle popups if they appear.
        For each url we visit the next pages if there are any. In the end
        we retrun a list that looks like
        ['product1_link', 'product2_link', ... 'productn_link'].

        Args:
            next_page: A boolean to see if we need to check for next page
            popup: A boolean to see if we need to check for a popup
            count: A integer to keep track of how many pages we have
                visited per url (default=1)
            stop: A integer to let us know when to stop visitting pages for
                each url (default=5)

        Returns:
            list
        """
        products = []
        for i in range(len(self.config['URLS'])):
            self.get_url(self.config['URLS'][i])
            products.extend(self.scrape())
            while count != stop: # while we are not done
                self.handle_popup(popup)
                new_url = self.next_page(next_page) # go to next page
                self.handle_popup(popup)
                count += 1
                if not new_url: # if we reached all pages
                    continue 
                self.get_url(new_url) # set next page url
                self.scrape() # scrape the links to those items on that page
            count = 0 # set back to zero for each url
        return products

    def scrape(self) -> list:
        """Function to scrape data links from a page
        
        This functions scrapes the links/urls for all the products that appear in
        the page. 

        Args:
            None

        Returns:
            list
        """
        products = []
        try:
            self.wait_found(self.config['PRODUCTS'])
            links = self.driver.find_elements(By.XPATH, self.config['PRODUCTS'])
            products.extend([link.get_attribute('href') for link in links])
            self.log_message('i', f'Found links from {self.driver.current_url}')
        except NoSuchElementException:
            self.log_message('w', 'No item links found on the page')
        except Exception as e:
            self.log_message('e', 'Failed to scrape item links')
        return products

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
            self.wait_click(self.config['NEXT_PAGE_BUTTON_XPATH'])
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
