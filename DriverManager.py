"""Module to manage the web driver for a selenium web scraper

This python module is used to manage the web driver of a selenium web scraper.


"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

class DriverManager:
    """
    A class used to manage a webscraper

    Attributes:
        driver: The browser driver needed for webscraping

    Methods:
        __init__(self, driver_path: str, headless: bool)
            Initializes the instance to be ready for scraping

        get_driver(self)
            Function to get the driver

        quit_driver(self)
            Function to quit the driver
    """


    def __init__(self, driver_path: str, headless: bool) -> None:
        """Initializes the instance to be ready for scraping.

        Initializes the web driver witht eh firefox driver. Sets
        the headless option. Sets the pirvate variable _driver.

        Args: 
            driver_path: the path to the browser driver
            headless: bool to run browser in headless mode or not

        Returns:
            None
        """
        options = Options()
        options.headless = headless
        service = Service(driver_path)
        self._driver = webdriver.Firefox(service=service, options=options)

    def get_driver(self):
        """Function to get the web driver

        Args: 
            None

        Returns:
            None
        """
        return self._driver
    

    def quit_driver(self):
        """Function to quit the webd river

        Args: 
            None

        Returns:
            None
        """
        self._driver.quit()