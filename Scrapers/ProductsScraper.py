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
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

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
    """
    def iterate_urls(self, next_page, popup, count: int=1, stop: int=5) -> list:
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
        for i in range(len(self.config['URLS'])):
            self.get_url(self.config['URLS'][i])
            products.extend(self.scrape())
            while count != stop: # while we are not done
                self.handle_popup(popup)
                new_url = self.next_page(next_page) # go to next page
                self.handle_popup(popup)
                count += 1
                if not new_url: # if we reached all pages
                    continue 
                self.get_url(new_url) # set next page url
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
            self.wait_found(self.config['PRODUCTS']['xpath'])
            links = self.driver.find_elements(By.XPATH, self.config['PRODUCTS']['xpath'])
            products.extend([link.get_attribute('href') for link in links])
            self.log_message('i', f'Found links from {self.driver.current_url}')
        except NoSuchElementException:
            self.log_message('w', 'No item links found on the page')
        except Exception as e:
            self.log_message('e', 'Failed to scrape item links')
        return products
    

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
            self.log_message('w', 'Unexpected error while navigating to next page"')
            return False
        return self.driver.current_url # return url of page we are on
    
    def handle_popup(self, popup: bool) -> None:
        """Initializes the instance to be ready for scraping.

        Initializes the Scraper instance with broswer driver and
        headless mode (optional)

        Args: 
            driver_path: the path to the browser driver
            headless: bool to run browser in headless mode or not

        Returns:
            None
        """
        if not popup:
            return 
        time.sleep(5)  
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            popup = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal__content')]")))
            self.log_message('i', 'popup detected')
            close_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'modal__close')]//button")))
            close_button.click()
            self.log_message('i', 'popup closed')
        except TimeoutException:
            self.log_message('i', 'opup not detected or not visible, continuing...')
