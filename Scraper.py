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

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import requests
import logging
import time
import csv

logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Scraper:
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
        self._urls = []
        self._links = []
        self._xpaths = {}
        self._multiple = {}
        self._data = {}
        self._next_button_path = ''
        self._link_xpath = ''
        self._categories = []
        logger.info("WebDriver initialized successfully")

    def set_url(self, url: str)  -> None:
        """Function to set the url that we will scrape.

        Function to set the url of the website that we want our scraper to visit.
        After its done we wait for 3 seconds. 

        Args:
            url: The url we want to scrape which is a string

        Returns:
            None
        """
        self._driver.get(url)
        time.sleep(3)

    def set_next_page_xpath(self, xpath: str) -> None:
        """This function sets the xpath for the next page button

        This functions sets the class variable next_button_xpath. Given a string
        we set the xpath for the next page button. For example on pages like amazon
        there are multiple pages of products. Often at the bottom there is a next
        page button. We will use this to click and check other pages.

        Args:
            xpath: A string containing the xpath to the next page button

        Returns: 
            None
        """
        self._next_button_path = xpath
    
    def set_xpaths(self, xpaths: dict) -> None:
        """This function sets the class variable xpaths.

        This functions sets the class variable xpaths. We are setting
        a dictionary where the element is a string a (key) and the xpath 
        is the value. This will be used to scrape each indiviual item of
        that data. For example if we want to scrape only the title then
        the dictionary would look like {'title': 'title_xpath'}.  If we
        already set xpaths we return and print a message.

        Args:
            xpath: A dictionary where the element is a string a (key) and
                the xpath is the value.

        Returns: 
            None
        """
        if self._xpaths:
            logger.warning('x_paths already set, add them instead')
            return 
        self._xpaths = xpaths

    def set_multiple(self, multiple: dict) -> None:
        """This function sets the class variable multiple.

        This functions sets the class variable multiple. The point of this
        is for when we have have elements that have multiple elements. For
        example a book or movie can have several authors/directors.
        Additionally it can also have several genres. During scraping our
        scraper check the `xpaths` dictionary and see if the key matches on
        in multiple. If we set multiple to be {'genres': 0} and our xpaths
        is {'genres': 'genres_xpath'} then our scraper will make sure to 
        handle that correctly.

        Args:
            multiple: A dictionary where the item is a string a (key) and
                value can be set to anything. 

        Returns: 
            None
        """
        if self._multiple:
            logger.warning('multiple already set, add to multiple instead using add_multiple')
            return
        self._multiple = multiple

    def set_urls(self, urls: list) -> None:
        """This function sets the class variable urls.

        This function sets the urls of the pages we want to scrape items from. For example
        if the page we want to scrape items has different types of items such as books and
        kitchen utensils on different pages then you can set the urls for those pages here.

        Args:
            multiple: A list containg urls of the websites we want to visit.

        Returns: 
            None
        """
        if self._urls:
            logger.warning('urls already set, add them instead with add_url')
            return
        self._urls = urls

    def set_link_xpath(self, xpath: str) -> None:
        """This sets the xpath for a link

        This sets the xpath for the link to a item on a page of items

        Args:
            xpath: The xpath to a link 

        Returns: 
            None
        """
        if self._link_xpath:
            logger.warning('link_xpath already set')
            return
        self._link_xpath = xpath
        logger.info(f'set {xpath}')

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
        if name in self._xpaths:
            logger.warning(f'{name} already in xpaths')
            return
        self._xpaths[name] = xpath
        logger.info(f'added {name}')
    
    def add_multiple(self, key: str, value: int=0) -> None:
        """This function adds a key and value to the xpath dictionary

        This function performs a simple insertion into a dictionary

        Args:
            name: A string representing the name of the element we want to scrape
            xpath: A string representing xpath to the element want want
                to scrape

        Returns: 
            None
        """
        if key in self._multiple:
            logger.warning(f'{key} already in multiple')
            return 
        self._multiple[key] = value
        logger.info(f'added {key}')
    
    def add_url(self, url: str) -> None:
        """This function adds url to our urls list

        This function performs a simple appending to a list.

        Args:
            url: A string representing the url we want to add

        Returns: 
            None
        """
        if url in self._urls:
            logger.warning(f'{url} is already in urls')
            return
        self._urls.append(url)
        logger.info(f'added {url}')

    def get_categories(self, url, categories_button, categories):
        """This function gets categories from a website

        Given a url and a xpath to categories on a website. This function
        goes to that page and gets categories to use to generate search 
        queries/urls. For example ebay has categories such as kitchen, clothes
        collectibles, electronics etc. We scrape that text from the webstite
        to use to generate search urls later.
    
        Args:
            url: The url of the page we want to visit
            xpath:  The xpath of the categories. 

        Returns: 
            None
        """
        self.set_url(url=url)
        try:
            browse_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, categories_button)))
            browse_button.click()
            categories_links = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//ul[contains(@class, 'genreList')]//li/a")))
        except NoSuchElementException: 
            logger.info('Next button not found. Done finding links')
            return
        self._categories = [link.text for link in categories_links]

    def generate_urls(self, base_url):
        """Function to generate search urls
        
        Args:
            base_url: the base url we want generate more urls of

        Returns: 
            None
        """
        pass

    def visit_urls(self, count: int=0, stop: int=5) -> None:
        """This function visits the pages of the urls we set.

        We have two arguments. One for counting and on for stoping.
        This function iterates our urls list. Each url will have 
        many pages since the idea is to have differnet url searches.
        We can choose to only scrape a couple of pages from each url.
        Thats what we use count and stop for. While we are not at
        our limit. We will go to the next page as long as there is
        a next page. We then get links from that page too. As an
        example if we have
        ['https://amazon/books', 'https://amazon/electronics'] then
        we will got each url, scrape item links, go to the other pages 
        of each url (ie https://amazon/books/p=2). until we are out
        stop. Then move to the next url and to the same.

        Args:
            count: a interger that we use to count
            stop: what page we stop at for each url.

        Returns: 
            None
        """
        for i in range(len(self._urls)): # iterate urls
            self.set_url(self._urls[i]) # set the url to scrape
            self.scrape_item_links() # scrape the items from the page
            while count != stop: # while we are not done
                new_url = self.next_page() # go to next page
                if not new_url: # if we reached all pages
                    continue 
                count += 1
                self.set_url(new_url) # set next page url
                self.scrape_item_links() # scrape the links to those items on that page
            count = 0 # set back to zero for each url

    def scrape_item_links(self) -> None:
        """This function scrapes links from a website

        This function scrapes links off of items listed on a website. As an example
        it can be used on the products page of amazon or any website where there
        are itmems listed. We scrape the links and then put them into the class
        list `links`.

        Args:
            None

        Returns: 
            None
        """
        try:
            links = self._driver.find_elements(By.XPATH, self.link_xpath)
            self._links.extend([link.get_attribute('href') for link in links])
            logger.info(f'Found links from {self._driver.current_url}')
        except NoSuchElementException:
            logger.warning('No item links found on the page')
        except Exception as e:
            logger.exception('Failed to scrape item links', e)
            
    def next_page(self) -> str:
        """This function sets the next page

        Using the xpath for the next page button we set earlier, this function tries to
        find the button. If we find it we click it. If we can't find it we return false.
        Otherwise we return the url of the page we are on after clicking the next page
        button.

        Args:
            None

        Returns: 
            str
        """
        try:
            next_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, self._next_button_path))) # find next button
            next_button.click() # click on next button
            time.sleep(3) 
        except (NoSuchElementException, TimeoutException):
            logger.warning("Next button not found or not clickable")
            return False
        except Exception as e:
            logger.exception("Unexpected error while navigating to next page")
            return False
        return self._driver.current_url # return url of page we are on

    def scrape_item(self, key: str, xpath: str) -> list:
        """Function to scrape data from items
        
        This functions scrapes data from a page. Given a key (name
        of the element we want to scrape) and a xpath to the element then we 
        scrape the data. Using the previously set dictionray of multiple, we
        check if we need to do multiple elements or just one. We also check
        for images. We then return the element we scraped. 

        Args:
            key: a sring that represents the name of the element we want to scrape
            xpath: a sring that represents the xpath of the element we want to 

        Returns:
            None
        """
        elements = ''
        try:
            if key in self.multiple:
                elements = self._driver.find_elements(By.XPATH, xpath)
                elements = [el.text.strip() for el in elements if el.text.strip()]
                elements = ' '.join(elements)
            else:
                element = self._driver.find_element(By.XPATH, xpath)
                if key == 'img':
                    img = element.get_attribute('src')
                    with open(f'{img}.png', 'wb') as f:
                        f.write(requests.get(img).content)
                    return img
                elements = element.text.strip()
        except Exception as e:
            logger.info('Error while scraping handling data', e)
        return elements
    
    def visit_items(self) -> None:
        """Function to visit each item from the links we scraped
        
        This functions uses the links we scraped to get individual information on 
        each of the items. For example if we previously scraped the products page
        on amazon. We would now have the links to each of the individual products.
        We set the url then using the xpaths we set earlier we will then scrape
        that data from each individual item. For example we have
        ['product1_link', 'product2_link', ... 'productn_link']. We will get all
        the data we want using the function scrape_item and the xpaths we set earlier.

        Args:
            None

        Returns:
            None
        """
        if not self._links:
            logger.info('There are no links to scrape')
            return
        i = 0
        for link in self._links: # for each link
            self.set_url(link) # set url for each link
            item = self._xpaths.copy() # create a copy of each dictionary key (item) : value (elements)
            for key, xpath in self._xpaths.items(): # for each item and dictionary
                elements = self.scrape_item(key, xpath) # get the elements using xpath
                item[key] = elements # set the value of the key to the elements
            self._data[i] = item # add each dictionary to the class variable `data`
            i+=1

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
        logger.info(f'Data written to {file_name}')

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
        formated_data = [list(self._xpaths.keys())]
        for value in self._data.values():
            formated_data.append(list(value.values()))        
        return formated_data

