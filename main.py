from DriverManager import DriverManager
from ScraperSetUp import CONFIG_GOODREADS
from Scrapers.ProductScraper import ProductScraper
from Scrapers.ProductsScraper import ProductsScraper
from Scrapers.CategoriesScraper import CategoriesScraper
import csv

if __name__ == "__main__":
    # set the driver
    driver_manager = DriverManager(CONFIG_GOODREADS['DRIVER_PATH'], CONFIG_GOODREADS['HEADLESS'])

    # get categories
    categories_scraper = CategoriesScraper(driver=driver_manager, config=CONFIG_GOODREADS)
    categories = categories_scraper.scrape('https://www.goodreads.com/genres')
    # generate urls
    CONFIG_GOODREADS['URLS'] = categories_scraper.generate_urls('https://www.goodreads.com/search?page=1&q=%s&qid=x02cPlELXg&tab=books', categories)
    
    # get products from page
    products_scraper = ProductsScraper(driver=driver_manager, config=CONFIG_GOODREADS)
    products = products_scraper.iterate_urls(stop=1, next_page=True, handle_popup=True)

    # # scrape individual products data
    product_scraper = ProductScraper(driver=driver_manager, config=CONFIG_GOODREADS)
    data = product_scraper.iterate_urls(products)

    formated_data = []
    for value in data.values():
        formated_data.append(list(value.get_item_values()))  

    file_name = './data/good_reads.csv'
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(formated_data)
        print(f'Data written to {file_name}')

    # print(f'Products: {products}')
    # print(f'Data: {data}')
