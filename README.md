# web-scraper
## Description
This scraper was created using selenium. We scrape links off of items on a website. 
As an example it can be used on the products page of amazon or any website where there are itmems listed.
Once we have the links to each item or product. This way we can scrape data on each individual item. 
This class also has the functionality to write to a csv file if needed.

## How to use
###  Create virtual environment
~~~
python3 -m venv env
~~~

###  Activate virtual environment
~~~
source ./env/bin/activate
~~~

### Install libraries
~~~
pip install -r requirements.txt
~~~

### Set config
`ScraperSetUp.py`
~~~python
CONFIG_GOODREADS = {
    'PRODUCT': {
        'xpaths': {
            'title': "title_xpath",
            'description': 'description_xpath',
            'raitings' : 'raitings_xpath',
            'reviews' : 'reviews_xpath',
        }
    },
    'NEXT_PAGE_BUTTON_XPATH': {
        'xpath' : 'next_button_xpath'
    },
    'PRODUCTS': {
        'xpath': 'xpath_to_product_links'
    },
    'MULTIPLE': None,
    'URLS' : ['example.com'],
    'DRIVER_PATH': './drivers/geckodriver',
    'HEADLESS': True
}
 ~~~

 `main.py`

 ~~~python
from DriverManager import DriverManager
from ScraperSetUp import CONFIG_GOODREADS
from Scrapers.ProductScraper import ProductScraper
from Scrapers.ProductsScraper import ProductsScraper

driver_manager = DriverManager(CONFIG_GOODREADS['DRIVER_PATH'], CONFIG_GOODREADS['HEADLESS'])
products_scraper = ProductsScraper(driver=driver_manager, config=CONFIG_GOODREADS)
product_scraper = ProductScraper(driver=driver_manager, config=CONFIG_GOODREADS)
products = products_scraper.iterate_urls(stop=2, next_page=True, popup=True)
data = product_scraper.iterate_urls(products)
 ~~~


### Run
~~~
python3 Scraper.py
~~~
