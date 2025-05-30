from scrapers.BaseScraper import BaseScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ProductsScraper(BaseScraper):
    def navigate(self):
        self._driver.get("https://www.google.com")
    
    def scrape(self):
        search_box = self._driver.find_element("name", "q")
        search_box.send_keys("OpenAI")
        search_box.submit()

    def navigate(self):
        """Navigate to Google homepage."""
        self._driver.get("https://www.google.com")
        time.sleep(1)

        # Accept cookies if the popup appears
        try:
            agree_button = self._driver.find_element(By.XPATH, "//button[contains(text(),'I agree') or contains(text(),'Accept all')]")
            agree_button.click()
            time.sleep(1)
        except:
            pass  # no popup

    def scrape(self):
        """Search for 'OpenAI' and print the titles of the first few results."""
        search_box = self._driver.find_element(By.NAME, "q")
        search_box.send_keys("OpenAI")
        search_box.send_keys(Keys.RETURN)

        time.sleep(2)  # Wait for results to load

        # Get search result titles
        results = self._driver.find_elements(By.XPATH, "//h3")
        print("Top search results for 'OpenAI':\n")

        count = 0
        for result in results:
            title = result.text.strip()
            if title:
                count += 1
                print(f"{count}. {title}")
            if count == 5:
                break