from .BaseScraper import BaseScraper
from ..ScrapedItem import ScrapedItem

class BookScraper(BaseScraper):
    def scrape(self):
        self.driver.get(self.config['url'])
        items = self.driver.find_elements_by_xpath(self.config['xpaths']['item'])

        results = []
        for item in items:
            title = item.find_element_by_xpath(self.config['xpaths']['title']).text
            link = item.find_element_by_xpath(self.config['xpaths']['link']).get_attribute('href')
            results.append(ScrapedItem(title, link, 'News').to_dict())
        return results
