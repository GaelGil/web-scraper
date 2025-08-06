from utils.DriverManager import DriverManager
from utils.ScraperSetUp import CONFIG_GOODREADS
from Scrapers.ProductScraper import ProductScraper
from Scrapers.ProductsScraper import ProductsScraper
from utils.db_connection import SessionLocal
from utils.init_db import init_db

import csv

if __name__ == "__main__":
    # set the driver
    driver_manager = DriverManager(
        CONFIG_GOODREADS["DRIVER_PATH"], CONFIG_GOODREADS["HEADLESS"]
    )
    # start the database
    init_db()
    session = SessionLocal()

    # get products from page
    products_scraper = ProductsScraper(driver=driver_manager, config=CONFIG_GOODREADS)
    products = products_scraper.iterate_urls(stop=3, next_page=True, handle_popup=True)

    # # scrape individual products data
    product_scraper = ProductScraper(
        driver=driver_manager, config=CONFIG_GOODREADS, session=session
    )
    # get the raw data
    data = product_scraper.iterate_urls(products)

    formated_data = [list(CONFIG_GOODREADS["PRODUCT"].keys())]
    for item in data:
        formated_data.append(list(item.get_item_values()))

    file_name = "./data/fun_cheap.csv"
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(formated_data)
        print(f"Data written to {file_name}")
