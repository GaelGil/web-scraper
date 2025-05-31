from .BaseScraper import BaseScraper
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import logging
import time

logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ProductsScraper(BaseScraper):
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
    def iterate_urls(self, count: int=0, stop: int=5) -> list:
        """Initializes the instance to be ready for scraping.

        Initializes the Scraper instance with broswer driver and
        headless mode (optional)

        Args: 
            driver_path: the path to the browser driver
            headless: bool to run browser in headless mode or not

        Returns:
            None
        """
        products = []
        print(self.config['URLS'])
        for i in range(len(self.config['URLS'])):
            self.get_url(self.config['URLS'][i])
            products.extend(self.scrape())
            while count != stop: # while we are not done
                self.handle_popup()
                new_url = self.next_page() # go to next page
                self.handle_popup()
                if not new_url: # if we reached all pages
                    continue 
                count += 1
                self.set_url(new_url) # set next page url
                self.scrape() # scrape the links to those items on that page
            count = 0 # set back to zero for each url
        return products


    def scrape(self):
        """Initializes the instance to be ready for scraping.

        Initializes the Scraper instance with broswer driver and
        headless mode (optional)

        Args: 
            driver_path: the path to the browser driver
            headless: bool to run browser in headless mode or not

        Returns:
            None
        """
        products = []
        try:
            links = self.driver.find_elements(By.XPATH, self.config['PRODUCTS']['xpath'])
            products.extend([link.get_attribute('href') for link in links])
            logger.info(f'Found links from {self.driver.current_url}')
        except NoSuchElementException:
            logger.warning('No item links found on the page')
        except Exception as e:
            logger.exception('Failed to scrape item links', e)
        return products
    

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
            next_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.config['NEXT_PAGE_BUTTON_XPATH']))) # find next button
            next_button.click() # click on next button
            time.sleep(3) 
        except (NoSuchElementException, TimeoutException):
            logger.warning("Next button not found or not clickable")
            return False
        except Exception as e:
            logger.exception("Unexpected error while navigating to next page")
            return False
        return self.driver.current_url # return url of page we are on
    
    def handle_popup(self) -> None:
        """Initializes the instance to be ready for scraping.

        Initializes the Scraper instance with broswer driver and
        headless mode (optional)

        Args: 
            driver_path: the path to the browser driver
            headless: bool to run browser in headless mode or not

        Returns:
            None
        """
        time.sleep(5)  
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            popup = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal__content')]")))
            logger.info("Popup detected!")

            close_button = WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'modal__close')]//button")))
            close_button.click()
            logger.info("Popup closed.")
        except TimeoutException:
            logger.info("Popup not detected or not visible, continuing...")