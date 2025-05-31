from .BaseScraper import BaseScraper
from ScrapedItem import ScrapedItem
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import requests
import logging
import time

logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ProductScraper(BaseScraper):
    def iterate_urls(self, products) -> dict:
        data = {}
        i = 0
        for product in products: # for each link
            self.driver.set_url(product) # set url for each link
            item = self._xpaths.copy() # create a copy of each dictionary key (item) : value (elements)
            item = ScrapedItem()
            for key, xpath in self.config['product']['xpaths']: # for each item and dictionary
                elements = self.scrape_(key, xpath) # get the elements using xpath
                item.add_field(key, elements)
            data[i] = item # add each dictionary to the class variable `data`
            i+=1
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
            if key in self._multiple:
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
            next_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.config['next_button_xpath']))) # find next button
            next_button.click() # click on next button
            time.sleep(3) 
        except (NoSuchElementException, TimeoutException):
            logger.warning("Next button not found or not clickable")
            return False
        except Exception as e:
            logger.exception("Unexpected error while navigating to next page")
            return False
        return self.driver.current_url # return url of page we are on
    
    def handle_popup(self):
        time.sleep(5)  
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            popup = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal__content')]")))
            logger.info("Popup detected!")

            close_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'modal__close')]//button")))
            close_button.click()
            logger.info("Popup closed.")
        except TimeoutException:
            logger.info("Popup not detected or not visible, continuing...")