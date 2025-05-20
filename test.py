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

    scrape_links(self, playlist_ids:str, popularity:int, popular:bool):
        Get a list of tracks for the new playlist.

    scrape_items(self, playlist_ids:str, popularity:int, popular:bool):
        Get a list of tracks for the new playlist.

    scrape_item(self, playlist_ids:str, popularity:int, popular:bool):
        Get a list of tracks for the new playlist.
    
    """
    driver = None
    links = None
    data = []
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
            print(links)
            for link in self.links:
                print(link.get_attribute('href'))
            print('Found links')
        except Exception as e:
            print('Error while scraping:', e)

    def scrape_items(self, to_scrape):
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
        if not self.links:
            print('There are no links to scrape')
            return
        print(self.links)
        for link in self.links:
            self.set_url(link)
            item = []
            for key, value in to_scrape.items():
                print(f'Key: {key}, Value: {value}')
            #     try:
            #         key = self.driver.find_elements(By.XPATH, value)
            #         item.append(key)
            #     except Exception as e:
            #         print('Error while scraping:', e)
            # self.data.append(item)

    def print_data(self):
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