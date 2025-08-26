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
uv venv
```

### Activate virtual environment

```
source .venv/bin/activate
```

### Install libraries

```
uv sync
```

### Database Setup

I set up a local Postgres database to save my data so I created a `.env` file

```sh
DATABASE_URL=postgresql://postgres:password@localhost:5432/webscraper
```

Once set up make sure to run migrations or create them if not initialized.

### Set config

`ScraperSetUp.py`

```python
GOODREADS: ScraperConfig = ScraperConfig(
    product_info=[
        ToScrape(
            xpath='//*[@id="__next"]/div[2]/main/div[1]/div[2]/div[2]/div[1]/div[1]/h1',
            name="title",
        ),
        ToScrape(
            xpath='//*[@id="__next"]/div[2]/main/div[1]/div[2]/div[2]/div[2]/div[1]/h3/div/span[1]/a/span[1]',
            name="author",
        ),
    ],
    products_url_xpath='//*[@id="bodycontainer"]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr/td[2]/a',
    urls_to_scrape=[
        Url(url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Art"),
        Url(
            url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Biography"
        ),
        Url(
            url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Classics"
        ),
        Url(url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Comics"),
    ],
    next_page_button_xpath='//a[@class="next_page" and @rel="next"]',
    multiple={"genres": 0},
    categories_button='//span[text()="Browse ▾"]',
    categories='//ul[contains(@class, "genreList")]//li/a',
    popup='//button[@class="gr-iconButton"][.//img[@alt="Dismiss"]]',
    close_popup_button='//button[@class="gr-iconButton"][.//img[@alt="Dismiss"]]',
)
```

`main.py`

```python
from DriverManager import DriverManager
from ScraperSetUp import CONFIG
from Scrapers.ProductScraper import ProductScraper
from Scrapers.ProductsScraper import ProductsScraper
from Scrapers.CategoriesScraper import CategoriesScraper

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
        # stop after 3 pages
        # next pages are available to go to them
        # there is a popup so we handle it
        products = products_scraper.iterate_urls(
            stop=3, next_page=True, handle_popup=True
        )
        # scrape individual products data
        product_scraper = ProductScraper(
            driver=driver, config=GOODREADS, session=session
        )
        # get the raw data
        data = product_scraper.iterate_products(products)

        print(f"DATA: {data}")


```

### Run

```
python3 main.py
```
