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

        Function to set the url that we want our scraper to get. After its done
        we wait for 3 seconds. 

        Args:
            url: The url we want to scrape

        Returns:
            None
        """
        self.driver.get(url)
        time.sleep(3)

    def set_nextpage_xpath(self, xpath: str) -> None:
        self.next_button_path = xpath
    
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

    def set_multiple(self, multilple: list) -> None:
        self.multilple = multilple

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

    def scrape_links(self, link_xpath: str, count: int=0, stop: int = 5) -> None:
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
        if count == stop:
            print(f'Done getting links')
            return
        try:
            links = self.driver.find_elements(By.XPATH, link_xpath)
            self.links.extend([link.get_attribute('href') for link in links])
            print(f'Found links from {self.driver.current_url}')
            current_url = self.driver.current_url # get url of the current page
            new_url = self.next_page() # go to next page
            if new_url == current_url: # if on the same page
                print('No more pages to scrape')
                return
            else:
                count += 1
                self.set_url(new_url) 
                self.scrape_links(link_xpath, count, stop)
        except Exception as e:
            print('Error while scraping:', e)
 

    def next_page(self) -> str:
        next_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.next_button_path))) # find next button
        next_button.click() # click on next button
        time.sleep(3) 
        return self.driver.current_url 

    def handle_data(self, key, xpath) -> list:
        elements = None
        try:
            # print(f'multiple: {self.multilple}')
            # print(f'key: {key}')
            if key in self.multiple:
                # print(f'key: {key}')
                print('in multiple')
                elements = self.driver.find_elements(By.XPATH, xpath)
                elements = [el.text.strip() for el in elements if el.text.strip()]
                elements = ' '.join(elements)
            else:
                print('not in multiple')
                element = self.driver.find_element(By.XPATH, xpath)
                elements = element.text.strip()
        except Exception as e:
            print('Error while scraping handling data', e)
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


#TODO: fix next page function
#TODO: fix genres to get all genres

sc = Scraper(GECKODRIVER_PATH, headless=True)
sc.set_url('https://www.goodreads.com/search?page=1&q=horror&qid=x02cPlELXg&tab=books')
sc.set_nextpage_xpath('//a[@class="next_page" and @rel="next"]')
sc.scrape_links("//*[@id='bodycontainer']/div[3]/div[1]/div[2]/div[2]/table/tbody/tr/td[2]/a")
data_to_scrape = {
    'title': "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[1]/div[1]/h1",
    'author' : "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[2]/div[1]/h3/div/span[1]/a/span[1]",
    'rating': '//div[@class="RatingStatistics__rating"]',
    'raitings' : '//span[@data-testid="ratingsCount"]',
    'reviews' : '//span[@data-testid="reviewsCount"]',
    'overview' : '//div[@data-testid="description"]//span[@class="Formatted"]',
    'genres': '//ul[@class="CollapsableList"]//span[@class="Button__labelItem"]',
    'pages' : '//p[@data-testid="pagesFormat"]',
    'publish_date' : '//p[@data-testid="publicationInfo"]',
    }
sc.set_xpaths(data_to_scrape)
multiple = ['genres']
sc.set_multiple(multiple)
# print(sc.multilple)
# sc.scrape_items()
# sc.print_data()
# formated_data = sc.format_data()
# sc.to_csv('./data.csv', formated_data)