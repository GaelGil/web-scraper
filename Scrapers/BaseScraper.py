"""This is an abstract class that represents a base web scraper

This abstract class is the base web scraper. Other site specific class
scrapers should inherit from this class. This class handles all the logging.
The webdriver and the config

  Typical usage example:
  from .BaseScraper import BaseScraper

  class SiteSpecificScraper(BaseScraper)

  scraper = SiteSpecificScraper(config, driver)
    
"""

from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
import logging
import time

logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BaseScraper(ABC):
    """
    A abstract class that will be inherrited by other webscraper
    classes.

    Attributes:
        driver: the browser driver needed for webscraping
        config: a dictionary that holds info for our webscraper

    Methods:
        __init__(self, driver, config)
            Initializes the instance to be ready for scraping

        get_url(self, url: str)
            Function to set the url that we will scrape

        wait_click(self, xpath: str, time: int=15)
            This function waits for a element to be clickable then clicks it

        wait_found(self, xpath: str, time: int=15)
            This function waits for a element to be located

        log_message(self,log_type: str, message: str)
            Function to log a message

        get_element(self, xpath: str)
            Function to get a element

        get_elements(self, xpath: str)
            Function to get elements

        current_url(self)
            Function to get the current url 

        scrape(self)
            Abstract method to be implemented by other scraper classes

        next_page(self, next_page: bool)
            Abstract method to be implemented by other scraper classes

        handle_popup(self: handle_popup: bool)
            Abstract method to be implemented by other scraper classes
    """
    def __init__(self, driver, config) -> None:
        """This function initaliazes the class

        Args:
            driver: The web driver used for scraping
            config: important information for the webscraper

        Returns:
            None
        """
        self.driver: webdriver = driver.get_driver()
        self.config: dict = config

    def get_url(self, url: str) -> None:
        """This function sets the url we are going to scrape

        Args:
            url: The url that we want to scrape from

        Returns:
            None
        """
        try:
            self.driver.get(url)
        except TimeoutException:
            self.log_message('e', f"Timeout while trying to load: {url}")

    def wait_click(self, xpath: str, time: int=15) -> None:
        """This function waits for a element to be clickable then clicks it

        Args:
            xpath: The xpath to the element we want to click
            time: The time we wait until we look for it
            
        Returns:
            None
        """
        try:
            button = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable((By.XPATH, xpath))) 
            button.click()
        except NoSuchElementException:
            self.log_message('w', 'NoSuchElementException element not found')

    def wait_found(self, xpath: str, time: int=15) -> None:
        """This function waits for a element to be located

        Args:
            xpath: The xpath to the element we want to locate
            time: The time we wait until we look for it
            
        Returns:
            None
        """
        try:
            wait = WebDriverWait(self.driver, time)
            wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except NoSuchElementException:
            self.log_message('w', 'NoSuchElementException element not found')

    def log_message(self, log_type: str, message: str='') -> None:
        """Function to log a message
        Args:
            log_type: A string to represent the type of message we
                want to log
            message: The message we want to log. Set to an empty string 
                by default
            
        Returns:
            None
        """
        if log_type == 'e':
            logger.exception(message)
        elif log_type == 'w':
            logger.warning(message)
        else:
            logger.info(message)
    
    def get_element(self, xpath: str) -> None:
        """Function to get a element
        Args:
            xpath: The xpath of the element we want
            
        Returns:
            str
        """
        try:
            return self.driver.find_element(By.XPATH, xpath)
        except TimeoutException:
            self.log_message('e', f'Timeout Exception {e}')
        except NoSuchElementException:
            self.log_message('e', f'No such element Exception {e}')
        except StaleElementReferenceException:
            self.log_message('e', f'Stale element exception{e}')
        except Exception as e:
            self.log_message('e', f'Exception {e}')
        return None

    def get_elements(self, xpath: str) -> list:
        """Function to get elements
        Args:
            xpath: The xpath of the elements we want
            
        Returns:
            str
        """
        try:
            return self.driver.find_elements(By.XPATH, xpath)
        except TimeoutException:
            self.log_message('e', f'Timeout Exception {e}')
        except NoSuchElementException:
            self.log_message('e', f'No such element Exception {e}')
        except StaleElementReferenceException:
            self.log_message('e', f'Stale element exception{e}')
        except Exception as e:
            self.log_message('e', f'Exception {e}')
        return []

    def current_url(self) -> str:
        """Function to get the current url 
        Args:
            None

        Returns:
            str
        """
        return self.driver.current_url
    
    def next_page(self, next_page: bool) -> str:
        """This function sets the next page

        Using the config, this function tries to find the next page button. If we
        find it we click it. If we can't find it we return. If we do find it
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
        except NoSuchElementException:
            self.log_message('e', 'Next button not found or not clickable')
            return 
        except TimeoutException:
            self.log_message('e', 'Time out exception')
            return 
        except Exception as e:
            self.log_message('e', f'Unexpected error while navigating to next page {e}')
            return 
        return self.current_url() # return url of page we are on
        
    def handle_popup(self, handle_popup: bool) -> None:
        """This function handles a popup if it is detected

        Using the config, this function closes a popup if it appears on the page. 

        Args:
            popup: A boolean to see if we need to check for a popup

        Returns: 
            None
        """
        if not handle_popup:
            return 
        time.sleep(5)  
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            popup_close = self.driver.find_element(By.XPATH, self.config['POPUP'])
            self.driver.execute_script("arguments[0].click();", popup_close)
            time.sleep(1)
            self.log_message('i', 'PopUp Detect attempting to close')
        except NoSuchElementException:
            self.log_message('e', f'No such element: {NoSuchElementException}')

    @abstractmethod
    def scrape(self):
        """Abstract method to be implemented by other scraper classes
        """
        pass
