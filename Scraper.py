"""Program to scrape a website and the items displayed in it.

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
    sc.set_xpaths(xpaths)
    sc.scrape_items(data_to_scrape)
    formated_data = sc.format_data()
    c.to_csv('example.csv', formated_data)
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
        driver: The browser driver needed for webscraping
        links: Will be used as a list of links to scrape
        x_paths: Will be used as a dictionary where the element is a string a (key) and
            the xpath is the value.
        data: A list containing the data we scraped 

    Methods:
        set_url(self, url:str)
            Set the url to scrape.

        scrape_links(self, xpath: str)
            This function scrapes links from a website

        set_xpaths(self, xpaths: dict)
            This function sets the xpaths for items we want to scrape
        
        add_xpath(self, name: str, xpath: str)
            This function adds a key and value to the xpath dictionary

        scrape_items(self, multiple: list)
            Function to scrape data from the links we got in scrape_links

        print_data(self)
            Function to print class variable `data`

        to_csv(self, file_name: str, data: list)
            Function to write data to csv

        format_data(self)
            Function to format data to be written to a csv file
    
    """
    driver = None
    links = []
    xpaths = {}
    multiple = []
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

        Function to set the url that we want our scraper to get. After its done
        we wait for 3 seconds. 

        Args:
            url: The url we want to scrape

        Returns:
            None
        """
        self.driver.get(url)
        time.sleep(3)

    def scrape_links(self, xpath: str) -> None:
        """This function scrapes links from a website

        Using the url we set previously, we scrape links off of items on that website. 
        As an example it can be used on the products page of amazon or any website where
        there are itmems listed. We scrape the links and then put them into the class
        list `links`.

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

    def set_xpaths(self, xpaths: dict) -> None:
        """This function sets the xpaths for items we want to scrape

        This functions sets the class variable xpaths. We are setting
        a dictionary where the element is a string a (key) and the xpath 
        is the value. This will be used to scrape each indiviual items
        data. If we already set xpaths we return and print a message.

        Args:
            xpath: A dictionary where the element is a string a (key) and
                the xpath is the value.

        Returns: 
            None
        """
        if self.xpaths:
            print('x_paths already set, add them instead')
            return 
        self.xpaths = xpaths

    def add_xpath(self, name: str, xpath: str) -> None:
        """This function adds a key and value to the xpath dictionary

        This function performs a simple insertion into a dictionary

        Args:
            name: A string representing the name of the element we want to scrape
            xpath: A string representing xpath to the element want want
                to scrape

        Returns: 
            None
        """
        self.xpaths[name] = xpath
        print(f'added {name}')

    def set_multiple(self, multilple: list) -> None:
        self.multilple = multilple


    def handle_data(self, key, xpath) -> list:
        elements = None
        try:
            if key in self.multiple:
                elements = self.driver.find_elements(By.XPATH, xpath)
                elements = [el.text.strip() for el in elements if el.text.strip()]
                elements = ' '.join(elements)
            else:
                element = self.driver.find_element(By.XPATH, xpath)
                elements = element.text.strip()
        except Exception as e:
            print('Error while scraping:', e)
        return elements
    
    def scrape_items(self) -> None:
        """Function to scrape data from the links we got in scrape_links
        
        This functions uses the links we scraped to get individual information on 
        each of the items. For example if we previously scraped the products page
        on amazon. We would now have the links to each of the individual products.
        This function will go to each product (link) and scrape data from their page using
        the xpaths set in the function `set_xpaths`. 

        Args:
            None

        Returns:
            None
        """
        if not self.links:
            print('There are no links to scrape')
            return
        i = 0
        for link in self.links: # for each link
            self.set_url(link) # set url for each link
            item = self.xpaths.copy() # create a copy of each dictionary key (item) : value (elements)
            for key, xpath in self.xpaths.items(): # for each item and dictionary
                elements = self.handle_data(key, xpath) # get the elements using xpath
                item[key] = elements # set the value of the key to the elements
            self.data[i] = item # add each dictionary to the class variable `data`
            i+=1
            if i == 1:
                return

    def print_data(self) -> None:
        """Function to print class variable `data`

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
        formated into list. Use the function `format_data` first.

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

    def format_data(self) -> list:
        """Function to format data to be written to a csv file

        This function formats the data we scraped into a list that will be able to
        be written to csv. 
        Ex: [[col1, col2, col3], [1, 2, 3], [4, 5, 6]]. 
        We then return this list to be written to csv.

        Args:
            None

        Returns:
            list
        """
        formated_data = [list(self.xpaths.keys())]
        for value in self.data.values():
            formated_data.append(list(value.values()))        
        return formated_data

#TODO: add next page functionality
#TODO: review set multiple funtionality and remove if not used


sc = Scraper()
sc.set_url('https://www.goodreads.com/shelf/show/horror')
sc.scrape_links("//*[@id='bodycontainer']/div[3]/div[1]/div[2]/div[3]/div[8]/div[1]/a[2]")
data_to_scrape = {
    'title': "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[1]/div[1]/h1",
    'author' : "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[2]/div[1]/h3/div/span[1]/a/span[1]",
    'rating': "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[2]/div[2]/a/div[1]/div",
    'raitings' : "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[2]/div[2]/a/div[2]/div/span[1]",
    'reviews' : "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[2]/div[2]/a/div[2]/div/span[2]",
    'overview' : "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[1]/div/div/span",
    'genres': "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[2]/div[5]/ul",
    'pages' : "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[2]/div[6]/div/span[1]/span/div/p[1]",
    'publish_date' : "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[2]/div[6]/div/span[1]/span/div/p[2]",
    }
sc.set_xpaths(data_to_scrape)
multiple = ['author', 'overview', 'genres']
sc.set_multiple(multilple)
sc.scrape_items()
formated_data = sc.format_data()
sc.to_csv('./data.csv', formated_data)