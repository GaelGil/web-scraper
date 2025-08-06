"""Module to manage the web driver for a selenium web scraper

This python module is used to manage the web driver of a selenium web scraper.
It has a class variable _driver that is initlaized once the class instance is
created. To initialize we give the path to the firefox geckodriver and bool
to set the option to run the browser in headless mode or not.

  Typical usage example:
    driver_manager = DriverManager('path_to_driver', True)
    driver_manager.get_driver()
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


    def __init__(self, driver_path: str, headless: bool=True) -> None:
        """Initializes the instance to be ready for scraping.

        Initializes the web driver witht eh firefox driver. Sets
        the headless option. Sets the pirvate variable _driver.

        Args: 
            driver_path: the path to the browser driver
            headless: bool to run browser in headless mode or not
                Set to true by default.

        Returns:
            None
        """
        options = Options()
        options.headless = headless
        service = Service(driver_path)
        self._driver: webdriver = webdriver.Firefox(service=service, options=options)

    def get_driver(self) -> webdriver:
        """Function to get the web driver

        Args: 
            None

        Returns:
            None
        """
        return self._driver
    

    def quit_driver(self) -> None:
        """Function to quit the webd river

        Args: 
            None

        Returns:
            None
        """
        self._driver.quit()