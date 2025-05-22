"""Proram to scrape a website and the items displayed in it.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:
    sc = Scraper()
    sc.set_url('example_url')
    sc.get_links("xpath_for_links")
    xpaths = {
    'title': "title_xpath]",
    }
    sc.scrape_items(data_to_scrape)
"""


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import csv

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
    x_paths = None
    data = {}

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

    def set_xpaths(self, x_paths: dict) -> None:
        """This function gets book titles and their link

        Using the url set previously we scrape links of items on that website
        we then put those links into a list to be used for individual scraping.

        Args:
            xpath: The xpath to the link elemnts we want to scrape

        Returns: 
            None
        """
        if self.x_paths:
            print('x_paths already set, add them instead')
            return 
        self.x_paths = x_paths

    def add_xpath(self, name: str, x_path: str) -> None:
        """This function gets book titles and their link

        Using the url set previously we scrape links of items on that website
        we then put those links into a list to be used for individual scraping.

        Args:
            xpath: The xpath to the link elemnts we want to scrape

        Returns: 
            None
        """
        self.x_paths[name] = xpath
        print(f'added {name}')
    

    def scrape_items(self, x_paths: dict, multiple: list) -> None:
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
        i = 0
        for link in self.links:
            self.set_url(link)
            item = x_paths.copy()
            for key, xpath in x_paths.items():
                try:
                    if key in multiple:
                        elements = self.driver.find_elements(By.XPATH, xpath)
                        elements = [el.text.strip() for el in elements if el.text.strip()]
                        elements = ' '.join(elements)
                    else:
                        element = self.driver.find_element(By.XPATH, xpath)
                        elements = element.text.strip()
                    item[key] = elements
                except Exception as e:
                    print('Error while scraping:', e)
            self.data[i] = item
            i+=1
            # if i == 1:
        return

    def print_data(self) -> None:
        """print data

        Args:
            None

        Returns:
            None
        """
        print(self.data.values())
        return

    def to_csv(self, file_name: str, data: list) -> None:
        """Function to write data to csv
        
        This function writes the data we scraped to csv. Must be first
        formated into list

        Args:
            file_name: The name of the csv file we are going to create 

            data: The formated data that we are going to write to a csv file

        Returns:
            None
        """
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f'Data written to {file_name}')

    def format_data(self, x_paths: dict) -> list:
        """Function to format data to be written to a csv file

        This function formats the data we scraped into a list that will be able to
        be written to csv. 
        Ex: [[col1, col2, col3], [1, 2, 3], [4, 5, 6]]

        Args:
            cols: A list of columns for the csv file

        Returns:
            None
        """
        formated_data = self.format_data([list(x_paths.keys())])
        for value in self.data.values():
            cols.append(list(value.values()))        
        return cols



# TODO: switch to scraping goodreads instead
sc = Scraper()
sc.set_url('https://www.barnesandnoble.com/s/education')
# TODO: set_x_path functions/add xpath
sc.get_links("//div[@class='product-shelf-title product-info-title pt-xs']/a")
data_to_scrape = {
    'title': "/html/body/main/div[3]/div[2]/section/div[2]/div/div[3]/div[1]/header/div/h1",
    'publish_date' : "//table[@class='plain centered']//tr[th='Publication date:']/td",
    'author' : "//span[@id='key-contributors']/a",
    'pages' : "//table[@class='plain centered']//tr[th='Pages:']/td",
    'publisher' : "//table[@class='plain centered']//tr[th='Publisher:']/td//span",
    'isbn' : "//table[@class='plain centered']//tr[th='ISBN-13:']/td",
    'overview' : "//div[contains(@class, 'overview-cntnt')]"
    }
multiple = ['author']
sc.scrape_items(data_to_scrape, multiple)
# sc.print_data()
sc.to_csv('./data.csv', data_to_scrape)