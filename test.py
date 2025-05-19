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
    driver : 
        The browser driver

    Methods
    -------
    set_url(self, query:str, limit:int)
        Searches spotify for playlists.

    scrape(self, playlist_ids:str, popularity:int, popular:bool):
        Get a list of tracks for the new playlist.
    """
    driver = None
    links = None
    def __init__(self):
        """
        This function will call the class function `auth_spotify` and create a list for later use.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        options = Options()
        options.headless = True 
        service = Service(GECKODRIVER_PATH)
        self.driver = webdriver.Firefox(service=service, options=options)

    def set_url(self, url):
        """
        Function to set the url that we will scrape.

        Parameters
        ----------
        url : str
            The url we want to scrape
        Returns
        -------
        None
        """
        self.driver.get(url)
        time.sleep(3)

    def get_links(self, xpath):
        """
        This function gets book titles and their link

        Parameters
        ----------
        xpath : str
            The xpath to the link elemnts we want to scrape

        Returns
        -------
        None
        """
        try:
            self.links = self.driver.find_elements(By.XPATH, xpath)
            print("Found links")
        except Exception as e:
            print("Error while scraping:", e)

        # self.driver.quit()

    def scrape_item(self, link):
        try:
            self.links = self.driver.find_elements(By.XPATH, xpath)
            # title = 
            # publish_date = 
            # author = 
            # tags = 
            # pages = 
            # publisher
            # overview
            print("Found links")
        except Exception as e:
            print("Error while scraping:", e)


    def scrape_items(self):
        """
        This function passes the links to another function called scrape_item where
        all the data proccessing will be handeld.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        for link in self.links:
            self.scrape_item(link)

sc = Scraper()
sc.set_url('https://www.barnesandnoble.com/s/education')
sc.get_links("//div[@class='product-shelf-title product-info-title pt-xs']/a")
sc.scrape_items()