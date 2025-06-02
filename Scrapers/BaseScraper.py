"""Program to scrape a website and the items displayed in it.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:
    sc = Scraper(driver=driver_path, headless=True)
    sc.set_next_page_xpath(xpath=next_button_xpath)
    sc.set_xpaths(xpaths)
    sc.set_multiple(multiple)
    sc.set_urls(urls)
    sc.set_link_xpath(link_xpath)
    sc.visit_urls(stop=5) # only go to 5 pages per each url
    sc.visit_items() # visit items scraped
    formated_data = sc.format_data() # format the data
    sc.to_csv('./data.csv', formated_data) # write data to csv
"""

from abc import ABC, abstractmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BaseScraper(ABC):
    """
    A class that will be inherrited by other webscraper
    classes

    Attributes:
        driver: The browser driver needed for webscraping
        config: a dictionary representing with important info
            for the scraper 

    Methods:
        __init__(self, driver_path: str, headless: bool)
            Initializes the instance to be ready for scraping

        set_url(self, url: str)
            Function to set the url that we will scrape

        set_next_page_xpath(self, xpath: str)
            This function sets the xpath for the next page button

        set_xpaths(self, xpaths: dict)
            This function sets the class variable xpaths
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


    def wait(self, xpath: str, time: int=15) -> None:
        """
        """
        wait = WebDriverWait(self.driver, time)
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))


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
