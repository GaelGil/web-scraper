from DriverManager import DriverManager
from ScraperSetUp import CONFIG
from Scrapers.ProductScraper import ProductScraper
from Scrapers.ProductsScraper import ProductsScraper
from helper import make_urls

#TODO: add good comments to all classes
#TODO: add start stop system
#TODO: updated readme again

if __name__ == "__main__":
    CONFIG['URLS'] = make_urls()
    driver_manager = DriverManager(CONFIG['DRIVER_PATH'], CONFIG['HEADLESS'])
    products_scraper = ProductsScraper(driver=driver_manager, config=CONFIG)
    product_scraper = ProductScraper(driver=driver_manager, config=CONFIG)
    products = products_scraper.iterate_urls()
    data = product_scraper.iterate_urls(products)

    print("Products:", products)
    print("data", )
