# web-scraper

## Description

This scraper was created using selenium. We scrape links off of items on a website.
As an example it can be used on the products page of amazon or any website where there are items listed.
Once we have the links to each item or product. This way we can scrape data on each individual item.
This class also has the functionality to write to a csv file if needed.

<!-- psql postgres -->
<!--  -->

## How to use

### Create virtual environment

```
python3 -m venv env
```

### Activate virtual environment

```
source ./env/bin/activate
```

### Install libraries

```
pip install -r requirements.txt
```

### Set config

`ScraperSetUp.py`

```python
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
```

`main.py`

```python
from DriverManager import DriverManager
from ScraperSetUp import CONFIG
from Scrapers.ProductScraper import ProductScraper
from Scrapers.ProductsScraper import ProductsScraper
from Scrapers.CategoriesScraper import CategoriesScraper

# set the driver
driver_manager = DriverManager(CONFIG_GOODREADS['DRIVER_PATH'], CONFIG_GOODREAD ['HEADLESS'])

# get categories
categories_scraper = CategoriesScraper(driver=driver_manager, config=CONFIG_GOODREADS)
categories = categories_scraper.scrape('https://www.goodreads.com/genres')

# generate urls
CONFIG_GOODREADS['URLS'] = categories_scraper.generate_urls('https://www.goodreads.com/search?page=99&q=%s&qid=x02cPlELXg&tab=books', categories)

# get products from page
products_scraper = ProductsScraper(driver=driver_manager, config=CONFIG_GOODREADS)
products = products_scraper.iterate_urls(stop=1000, next_page=True, handle_popup=True)

# scrape individual products data
product_scraper = ProductScraper(driver=driver_manager, config=CONFIG_GOODREADS)
data = product_scraper.iterate_urls(products)

print(f'Products: {products}')
print(f'Data: {data}')

```

### Run

```
python3 main.py
```
