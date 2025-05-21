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

    Attributes:
        driver : The browser driver needed for webscraping

        links : None
            A list of links to scrape
        data : list
            The data we scraped

    Methods:
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

        Args:
            url: The url we want to scrape

        Returns:
            None
        """
        self.driver.get(url)
        time.sleep(3)

    def get_links(self, xpath: str) -> None:
        """This function gets book titles and their link

        Using the url set previously we scrape links of items on that website
        we then put those links into a list to be used for individual scraping.

        Args:
            xpath: The xpath to the link elemnts we want to scrape

        Returns: 
            None
        """
        try:
            links = self.driver.find_elements(By.XPATH, xpath)
            self.links = [link.get_attribute('href') for link in links]
            print('Found links')
        except Exception as e:
            print('Error while scraping:', e)

    def scrape_items(self, x_paths: dict) -> None:
        """Function to scrape items that we selected in get_links
        
        This functions uses the links we scraped to get individual information on 
        each of the items

        Args:
            x_paths: A dictionary containing the key as the item we want to scrape
            and the value being the xpath of that item

        Returns:
            None
        """
        if not self.links:
            print('There are no links to scrape')
            return
        for link in self.links:
            self.set_url(link)
            item = []
            for key, xpath in x_paths.items():
                # print(f'Key: {key}, Value: {xpath}')
                try:
                    if key in ['author', 'tags']:
                        elements = self.driver.find_elements(By.XPATH, xpath)
                        elements = [el.text.strip() for el in elements if el.text.strip()]
                        print(elements)
                        item.append(elements)
                    else:
                        element = self.driver.find_element(By.XPATH, xpath)
                        elements = element.text.strip()
                        item.append(elements)

                except Exception as e:
                    print('Error while scraping:', e)
            self.data.append(item)

    def print_data(self) -> None:
        """Function to scrape items that we selected in get_links
        
        This functions uses the links we scraped to get individual information on 
        each of the items

        Args:
            x_paths: A dictionary containing the key as the item we want to scrape
            and the value being the xpath of that item

        Returns:
            None
        """
        print(self.data)
        return


    def to_csv(self) -> None:
        """Function to write data to csv
        
        This functions uses the links we scraped to get individual information on 
        each of the items

        Args:
            x_paths: A dictionary containing the key as the item we want to scrape
            and the value being the xpath of that item

        Returns:
            None
        """
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