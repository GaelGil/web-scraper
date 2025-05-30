from DriverManager import DriverManager
from ScraperSetUp import CONFIG
from Scrapers.ProductScraper import ProductScraper
from Scrapers.ProductsScraper import ProductsScraper



if __name__ == "__main__":
    driver_manager = DriverManager()
    products_scraper = ProductsScraper(driver=driver_manager, config=CONFIG)
    product_scraper = ProductScraper(driver=driver_manager, config=CONFIG)
    products = products_scraper.iterate_urls()
    data = products_scraper.iterate_urls(products)


    print("Products:", products)
    print("data", )
