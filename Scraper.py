"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time  

GECKODRIVER_PATH = "./drivers/geckodriver"

class Scraper:
    """
    A class used to manage a webscraper

    Attributes
    ----------
    driver : None
        The browser driver
    links : None
        A list of links to scrape
    data : list
        The data we scraped

    Methods
    -------
    set_url(self, url:str)
        Set the url to scrape.

    scrape_links(self, playlist_ids:str, popularity:int, popular:bool):
        Get a list of tracks for the new playlist.

    scrape_items(self, playlist_ids:str, popularity:int, popular:bool):
        Get a list of tracks for the new playlist.

    scrape_item(self, playlist_ids:str, popularity:int, popular:bool):
        Get a list of tracks for the new playlist.

    to_csv(self)
        Write the data that we scraped to a csv
    
    """
    driver = None
    links = None
    data = []
    def __init__(self) -> None:
        """Initializes the instance to be ready for scraping.

        Initializes the Scraper instance to set the options and driver
        on the selenium scraper.

        Args: 
            None

        Returns:
            None
        """
        options = Options()
        options.headless = True 
        service = Service(GECKODRIVER_PATH)
        self.driver = webdriver.Firefox(service=service, options=options)

    def set_url(self, url: str)  -> None:
        """Function to set the url that we will scrape.

        Parameters
        ----------
        url : str
            The url we want to scrape

        Returns:
            None
        """
        self.driver.get(url)
        time.sleep(3)

    def get_links(self, xpath: str) -> None:
        """
        This function gets book titles and their link

        Parameters
        ----------
        xpath : str
            The xpath to the link elemnts we want to scrape

        Returns:
            None
        """
        try:
            links = self.driver.find_elements(By.XPATH, xpath)
            self.links = [link.get_attribute('href') for link in links]
            print('Found links')
        except Exception as e:
            print('Error while scraping:', e)

    def scrape_items(self, to_scrape: dict) -> None:
        """Function to scrape items that we selected in 
        This function passes the links to another function called scrape_item where
        all the data proccessing will be handeld.

        Args:
            to_scrape: A dictionary containing the 

        Returns:
            None
        """
        if not self.links:
            print('There are no links to scrape')
            return
        print(self.links)
        for link in self.links:
            self.set_url(link)
            item = []
            for key, value in to_scrape.items():
                print(f'Key: {key}, Value: {value}')
                try:
                    key = self.driver.find_elements(By.XPATH, value)
                    item.append(key)
                except Exception as e:
                    print('Error while scraping:', e)
            self.data.append(item)

    def print_data(self) -> None:
        print(self.data)
        return


sc = Scraper()
sc.set_url('https://www.barnesandnoble.com/s/education')
sc.get_links("//div[@class='product-shelf-title product-info-title pt-xs']/a")
data_to_scrape = {
    'title': "//h1[@class='pdp-header-title']",
    'publish_date' : "//table[@class='plain centered']//tr[th='Publication date:']/td",
    'author' : "//span[@id='key-contributors']/a",
    'tags' : "//div[@class='related-sub-text pt-xxs']/a",
    'pages' : "//table[@class='plain centered']//tr[th='Pages:']/td",
    'publisher' : "//table[@class='plain centered']//tr[th='Publisher:']/td//span",
    'isbn' : "//table[@class='plain centered']//tr[th='ISBN-13:']/td",
    'overview' : "//div[contains(@class, 'overview-cntnt')]"
    }
sc.scrape_items(data_to_scrape)
sc.print_data()