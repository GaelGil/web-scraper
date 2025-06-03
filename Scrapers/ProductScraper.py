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

from .BaseScraper import BaseScraper
from ScrapedItem import ScrapedItem
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import requests
import time

class ProductScraper(BaseScraper):
    """
    A class used to scrape products from a web page

    Attributes:
        None

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
    """
    def iterate_urls(self, products: list) -> dict:
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
        data = []
        # i = 0
        for product in products: # for each link
            self.get_url(product) # set url for each link
            item = ScrapedItem()
            for key, xpath in self.config['PRODUCT']['xpaths'].items(): # for each item and dictionary
                elements = self.scrape(key, xpath) # get the elements using xpath
                item.add_field(key, elements)
            data.append(item)
        return data

    def scrape(self, key: str, xpath: str) -> list:
        """Function to scrape data from products
        
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
            if key in self.config['MULTIPLE']:
                elements = self.driver.find_elements(By.XPATH, xpath)
                elements = [el.text.strip() for el in elements if el.text.strip()]
                elements = ' '.join(elements)
            else:
                element = self.driver.find_element(By.XPATH, xpath)
                if key == 'img':
                    img = element.get_attribute('src')
                    with open(f'{img}.png', 'wb') as f:
                        f.write(requests.get(img).content)
                    return img
                elements = element.text.strip()
        except Exception as e:
            self.log_message('e', 'Error while scraping handling data')
        return elements
    
    def next_page(self, next_page: bool) -> str:
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
        if not next_page:
            return False
        try:
            self.wait_click(self.config['NEXT_PAGE_BUTTON_XPATH']['xpath'])
            time.sleep(3) 
        except (NoSuchElementException, TimeoutException):
            self.log_message('w', 'Next button not found or not clickable')
            return False
        except Exception as e:
            self.log_message('e', 'Unexpected error while navigating to next page')
            return False
        return self.driver.current_url # return url of page we are on
        
    def handle_popup(self):
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
        time.sleep(5)  
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            popup = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal__content')]")))
            self.log_message('i', 'Popup detected!')
            close_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'modal__close')]//button")))
            close_button.click()
            self.log_message('i', 'Popup closed.')
        except TimeoutException:
            self.log_message('i', 'Popup not detected or not visible, continuing...')
