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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from helper import XPATHS, make_urls
import time
import csv

GECKODRIVER_PATH = "./drivers/geckodriver"
NEXT_PAGE_BUTTON_XPATH = '//a[@class="next_page" and @rel="next"]'
LINKS_XPATH = "//*[@id='bodycontainer']/div[3]/div[1]/div[2]/div[2]/table/tbody/tr/td[2]/a"
MULTIPLE = {'genres' : 0}

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
    urls = []
    links = []
    xpaths = {}
    multiple = {}
    data = {}
    next_button_path = ''

    def __init__(self, driver_path: str, headless: bool) -> None:
        """Initializes the instance to be ready for scraping.

        Initializes the Scraper instance to set the options and driver
        on the selenium scraper. 

        Args: 
            driver_path: the path to the browser driver
            headless: bool for headless option

        Returns:
            None
        """
        options = Options()
        options.headless = headless
        service = Service(driver_path)
        self.driver = webdriver.Firefox(service=service, options=options)

    def set_url(self, url: str)  -> None:
        """Function to set the url that we will scrape.

        Function to set the url that we want our scraper to visit. After its done
        we wait for 3 seconds. 

        Args:
            url: The url we want to scrape which is a string

        Returns:
            None
        """
        self.driver.get(url)
        time.sleep(3)

    def set_next_page_xpath(self, xpath: str) -> None:
        """This function sets the xpath for the next page button

        This functions sets the class variable next_button_xpath. Given a string
        we set the xpath for the next page button. For example on pages like amazon
        there are multiple pages of products. Often at the bottom there is a next
        page button. That is the use case for this. 

        Args:
            xpath: A string containing the xpath to the next page button

        Returns: 
            None
        """
        self.next_button_path = xpath
    
    def set_xpaths(self, xpaths: dict) -> None:
        """This function sets the class variable xpaths for items we want to scrape

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

    def set_multiple(self, multiple: dict) -> None:
        """This function sets the class variable multiple.

        This functions sets the class variable multiple. The point of this
        is for when we have have elements that have multiple elements. For example
        a book or movie can have several authors/directors. Additionally it can also 
        have several genres. The use case for this would be if to add these to the
        multiple dictionary. Later while scraping our scraper will look out for them
        to scrape them correctly. We use a dictionary for faster look up.

        Args:
            multiple: A dictionary where the item is a string a (key) and
                value can be set to anything. 

        Returns: 
            None
        """
        if self.multiple:
            print('multiple already set, add to multiple instead')
            return
        self.multiple = multiple

    def add_xpath(self, name: str, xpath: str) -> None:
        """This function adds a key and value to the xpath dictionary

        This function performs a simple insertion into the class variable xpaths.
        If it already exists we ignore it and return a message. If not we add it.

        Args:
            name: A string representing the name of the element we want to scrape
            xpath: A string representing xpath to the element want want
                to scrape

        Returns: 
            None
        """
        if name in self.xpaths:
            print(f'{name} already in xpaths')
            return
        self.xpaths[name] = xpath
        print(f'added {name}')
    
    def add_multiple(self, key: str, value: int=0):
        """This function adds a key and value to the xpath dictionary

        This function performs a simple insertion into a dictionary

        Args:
            name: A string representing the name of the element we want to scrape
            xpath: A string representing xpath to the element want want
                to scrape

        Returns: 
            None
        """
        if key in self.multiple:
            print(f'{key} already in multiple')
            return 
        self.multiple[key] = value
        print(f'added {key}')

    def set_urls(self, url: str):
        """This function sets the class variable multiple.

        This functions sets the class variable multiple. The point of this
        is for when we have have elements that have multiple elements. For example
        a book or movie can have several authors/directors. Additionally it can also 
        have several genres. The use case for this would be if to add these to the
        multiple dictionary. Later while scraping our scraper will look out for them
        to scrape them correctly. We use a dictionary for faster look up.

        Args:
            multiple: A dictionary where the item is a string a (key) and
                value can be set to anything. 

        Returns: 
            None
        """
        self.urls = url

    def iterate_urls(self, link_xpath: str, count: int=0, stop: int=5):
        """This function sets the class variable multiple.

        This functions sets the class variable multiple. The point of this
        is for when we have have elements that have multiple elements. For example
        a book or movie can have several authors/directors. Additionally it can also 
        have several genres. The use case for this would be if to add these to the
        multiple dictionary. Later while scraping our scraper will look out for them
        to scrape them correctly. We use a dictionary for faster look up.

        Args:
            multiple: A dictionary where the item is a string a (key) and
                value can be set to anything. 

        Returns: 
            None
        """
        for i in range(len(self.urls)): # iterate urls
            self.set_url(self.urls[i]) # set the url to scrape
            self.scrape_item_links(link_xpath) # scrape the items from the page
            while count != stop: # while we are not done
                new_url = self.next_page() # go to next page
                if type(new_url) is bool: # if we reached all pages
                    continue 
                count += 1
                self.set_url(new_url) # set next page url
                self.scrape_item_links(link_xpath) # scrape the links to those items on that page
            count = 0

    def scrape_item_links(self, link_xpath: str) -> None:
        """This function scrapes links from a website

        This function scrapes links off of items on the url we previously provided at `set_url`
        As an example it can be used on the products page of amazon or any website where
        there are itmems listed. We scrape the links and then put them into the class
        list `links`.

        Args:
            link_xpath: The xpath to the link elements we want to scrape.

        Returns: 
            None
        """
        try:
            links = self.driver.find_elements(By.XPATH, link_xpath)
            self.links.extend([link.get_attribute('href') for link in links])
            print(f'Found links from {self.driver.current_url}')
        except Exception as e:
            print('Error while scraping:', e)
            
    def next_page(self) -> str:
        """This function scrapes links from a website

        This function scrapes links off of items on the url we previously provided at `set_url`
        As an example it can be used on the products page of amazon or any website where
        there are itmems listed. We scrape the links and then put them into the class
        list `links`.

        Args:
            link_xpath: The xpath to the link elements we want to scrape.

        Returns: 
            None
        """
        try:
            next_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.next_button_path))) # find next button
            next_button.click() # click on next button
            time.sleep(3) 
        except NoSuchElementException: # if we cant find the next page button throw exception
            print('Next button not found. Done finding links')
            return True # return True
        return self.driver.current_url # return url of page we are on

    def scrape_item(self, key, xpath) -> list:
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
        elements = ''
        try:
            if key in self.multiple:
                elements = self.driver.find_elements(By.XPATH, xpath)
                elements = [el.text.strip() for el in elements if el.text.strip()]
                elements = ' '.join(elements)
            else:
                element = self.driver.find_element(By.XPATH, xpath)
                elements = element.text.strip()
        except Exception as e:
            print('Error while scraping handling data', e)
        return elements
    
    def iterate_items(self) -> None:
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
                elements = self.scrape_item(key, xpath) # get the elements using xpath
                item[key] = elements # set the value of the key to the elements
            self.data[i] = item # add each dictionary to the class variable `data`
            i+=1

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

sc = Scraper(GECKODRIVER_PATH, headless=True)
sc.set_next_page_xpath(NEXT_PAGE_BUTTON_XPATH)
sc.set_xpaths(XPATHS)
sc.set_multiple(MULTIPLE)
sc.set_urls(make_urls())
sc.iterate_urls(LINKS_XPATH)
sc.iterate_items()
formated_data = sc.format_data()
sc.to_csv('./data.csv', formated_data)
