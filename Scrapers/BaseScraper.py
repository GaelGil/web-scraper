"""This is an abstract class that represents a base web scraper

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:
    
"""

from abc import ABC, abstractmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import logging


logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BaseScraper(ABC):
    """
    A class that will be inherrited by other webscraper
    classes

    Attributes:
        driver: the browser driver needed for webscraping
        config: a dictionary that holds info for our webscraper

    Methods:
        __init__(self, driver_path: str, headless: bool)
            Initializes the instance to be ready for scraping

        get_url(self, url: str)
            Function to set the url that we will scrape
    """
    def __init__(self, driver, config):
        """
        """
        self.driver = driver.get_driver()
        self.config = config

    def get_url(self, url: str) -> None:
        """
        """
        self.driver.get(url)

    def wait_click(self, xpath: str, time: int=15) -> None:
        """
        """
        try:
            button = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable((By.XPATH, xpath))) 
            button.click()
        except NoSuchElementException:
            self.log_message('w', 'NoSuchElementException element not found')

    def wait_found(self, xpath: str, time: int=15) -> None:
        """
        """
        try:
            wait = WebDriverWait(self.driver, time)
            wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except NoSuchElementException:
            self.log_message('w', 'NoSuchElementException element not found')

    def log_message(self, log_type: str, message: str='') -> None:
        """
        """
        if log_type == 'e':
            logger.exception(message)
        elif log_type == 'w':
            logger.warning(message)
        else:
            logger.info(message)

    @abstractmethod
    def scrape(self):
        """
        """
        pass

    @abstractmethod
    def next_page(self):
        """
        """
        pass

    @abstractmethod
    def handle_popup(self):
        """
        """
        pass
