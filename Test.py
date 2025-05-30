from DriverManager import DriverManager
from ScraperSetUp import CONFIG
from Scrapers.BaseScraper import BaseScraper
from Scrapers.BookScraper import BookScraper

def run_scraper(scraper_class, config):
    driver_manager = DriverManager()
    scraper = scraper_class(driver_manager.get_driver(), config)
    results = scraper.scrape()
    driver_manager.quit_driver()
    return results

if __name__ == "__main__":
    product_data = run_scraper(ProductScraper, CONFIG['product'])
    news_data = run_scraper(NewsScraper, CONFIG['news'])

    print("Products:", product_data)
    print("News:", news_data)
