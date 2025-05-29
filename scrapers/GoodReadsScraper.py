from scrapers.BaseScraper import BaseScraper

class GoodReadsScraper(BaseScraper):
    def navigate(self):
        self._driver.get("https://www.google.com")
    
    def scrape(self):
        search_box = self._driver.find_element("name", "q")
        search_box.send_keys("OpenAI")
        search_box.submit()
