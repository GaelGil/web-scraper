from utils.DriverManager import DriverManager
from utils.config import GOODREADS, DRIVER_PATH, HEADLESS
from Scrapers.ProductScraper import ProductScraper
from Scrapers.ProductsScraper import ProductsScraper
from utils.db_connection import Database

if __name__ == "__main__":
    # set the driver
    driver_manager = DriverManager(DRIVER_PATH, HEADLESS)
    driver = driver_manager.get_driver()
    # start the database
    db = Database()
    db.init_db()
    with db.session_scope() as session:
        # get links to products from page
        products_scraper = ProductsScraper(driver=driver, config=GOODREADS)
        products = products_scraper.iterate_urls(
            stop=3, next_page=True, handle_popup=True
        )
        # scrape individual products data
        product_scraper = ProductScraper(
            driver=driver, config=GOODREADS, session=session
        )
        # get the raw data
        data = product_scraper.iterate_products(products)
        print(f"DATALENGTH: {len(data)}")
        # print(f"DATA: {data}")
