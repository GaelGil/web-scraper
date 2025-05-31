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

class BaseScraper(ABC):
    """
    A class used to manage a webscraper

    Attributes:
        driver: The browser driver needed for webscraping
        urls: A list of urls to scrape for links
        x_paths: Will be used as a dictionary where the element is a string
            a (key) and the xpath is the value.
        multiple: A dictionary containing elements that might have more than 
            one elment to scrape
        data: A dictionary containing the data we scraped 
        links: A list containing links to individual items to scrape
        next_button_path: The xpath for the next page button
        link_xpath: the xpath for a link 

    Methods:
        __init__(self, driver_path: str, headless: bool)
            Initializes the instance to be ready for scraping

        set_url(self, url: str)
            Function to set the url that we will scrape

        set_next_page_xpath(self, xpath: str)
            This function sets the xpath for the next page button

        set_xpaths(self, xpaths: dict)
            This function sets the class variable xpaths

        set_multiple(self, multiple: dict)
            This function sets the class variable multiple

        set_urls(self, urls: list)
            This function sets the class variable urls

        set_link_xpath(self, xpath: str)
            This sets the xpath for a link
        
        add_xpath(self, name: str, xpath: str)
            This function adds a key and value to the xpath dictionary
        
        add_multiple(self, key: str, value: int=0)
            This function adds a key and value to the xpath dictionary
        
        add_url(self, url: str)
            This function adds url to our urls list

        visit_urls(self, count: int=0, stop: int=5)
            This function visits the pages of the urls we scraped

        scrape_item_links(self)
            This function scrapes links from a website

        next_page(self)
            This function sets the next page

        scrape_item(self, key, xpath)
            Function to scrape data from a item

        visit_items(self)
            Function to visit each item from the links we scraped

        to_csv(self, file_name: str, data: list)
            Function to write data to csv file
        
        format_data(self)
            Function to format data to be written to a csv file
    """
    def __init__(self, driver, config):
        """
        """
        self.driver = driver
        self.config = config

    def get_url(self, url: str) -> None:
        """
        """
        self.driver._driver.get(url)

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
