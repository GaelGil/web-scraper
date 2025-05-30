from BaseScraper import BaseScraper
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
    def iterate_urls(self, count: int=0, stop: int=5) -> list:
        products = []
        for i in range(len(self.config)['URLS']):
            self.set_url(self.config['URLS'][i])
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