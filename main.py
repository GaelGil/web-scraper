from DriverManager import DriverManager
from ScraperSetUp import CONFIG_GOODREADS
from Scrapers.ProductScraper import ProductScraper
from Scrapers.ProductsScraper import ProductsScraper
from helper import make_urls

#TODO: add good comments to all classes
#TODO: add start stop system
#TODO: updated readme again

if __name__ == "__main__":
    CONFIG_GOODREADS['URLS'] = make_urls()
    driver_manager = DriverManager(CONFIG_GOODREADS['DRIVER_PATH'], CONFIG_GOODREADS['HEADLESS'])
    products_scraper = ProductsScraper(driver=driver_manager, config=CONFIG_GOODREADS)
    product_scraper = ProductScraper(driver=driver_manager, config=CONFIG_GOODREADS)
    products = products_scraper.iterate_urls(stop=2, next_page=True, popup=True)
    data = product_scraper.iterate_urls(products)

    print("Products:", products)
    print("data", )
