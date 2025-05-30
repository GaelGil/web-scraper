"""Program to scrape a website and the items displayed in it.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

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

        set_driver(self)
            Function to get the driver

        quit_driver(self)
            Function to quit the driver
    """


    def __init__(self, driver_path: str, headless: bool) -> None:
        """Initializes the instance to be ready for scraping.

        Initializes the Scraper instance with broswer driver and
        headless mode (optional)

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
        """Function to get the driver
        
        """
        return self._driver

    def quit_driver(self):
        """Function to quit the driver
        """
        self._driver.quit()