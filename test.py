from utils.DriverManager import DriverManager
from scrapers.ProductsScaper import ProductsScraper

def main():
    driver = DriverManager(headless=True).get_driver()
    scraper = ProductsScraper(driver)

    try:
        scraper.navigate()
        scraper.scrape()
    finally:
        scraper.close()

if __name__ == "__main__":
    main()