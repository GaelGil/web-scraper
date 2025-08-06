from utils.DriverManager import DriverManager
from utils.ScraperSetUp import FUN_CHEAP
from Scrapers.ProductScraper import ProductScraper
from Scrapers.ProductsScraper import ProductsScraper
from utils.db_connection import SessionLocal
from utils.init_db import init_db

import csv

if __name__ == "__main__":
    # set the driver
    driver_manager = DriverManager(FUN_CHEAP["DRIVER_PATH"], FUN_CHEAP["HEADLESS"])

    # get products from page
    products_scraper = ProductsScraper(driver=driver_manager, config=FUN_CHEAP)
    products = products_scraper.iterate_urls(stop=3, next_page=True, handle_popup=True)
    init_db()
    session = SessionLocal()

    # # scrape individual products data
    product_scraper = ProductScraper(
        driver=driver_manager, config=FUN_CHEAP, session=session
    )
    data = product_scraper.iterate_urls(products)

    formated_data = [list(FUN_CHEAP["PRODUCT"].keys())]
    for item in data:
        formated_data.append(list(item.get_item_values()))

    file_name = "./data/fun_cheap.csv"
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(formated_data)
        print(f"Data written to {file_name}")
