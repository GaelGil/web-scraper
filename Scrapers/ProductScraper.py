"""Class to scrape data from individual products

This class inherits from the BaseScraper class. This class is used to
scrape data from individual prodcuts. Below is a short example of how
it is used.

  Typical usage example:
    from DriverManager import DriverManager
    from ScraperSetUp import CONFIG
    from Scrapers.ProductsScraper import ProductsScraper

    products = ['product_link1', 'product_link2']
    driver_manager = DriverManager(CONFIG['DRIVER_PATH'], CONFIG['HEADLESS'])
    product_scraper = ProductScraper(driver=driver_manager, config=CONFIG_GOODREADS)
    data = product_scraper.iterate_urls(products)
    print(f'Data: {data}')

"""

from .BaseScraper import BaseScraper
from utils.schemas import BookItem
from selenium.common.exceptions import StaleElementReferenceException
import requests
from utils.models.Book import Sneaker


class ProductScraper(BaseScraper):
    """
    A class used to scrape products of a page

    Attributes:
        BaseScraper Attributes: ProductsScraper inherits from BaseScraper

    Methods:
        iterate_urls(self, products: list)
            Function to visit each item given a list of items

        scrape(self, key: str, xpath: str)
            Function to scrape data from a product
    """

    def save_to_db(self, item: BookItem) -> None:
        """Function to save data to a database
        Args:
            item: A ScrapedItem instance
        """
        self.log_message("i", f"Saving {item.title} to database ")
        if not item:
            return
        try:
            sneaker = Sneaker(
                name=item.name,
                img=item.img,
                retail_price=item.retail_price,
                display_price=item.display_price,
                release_data=item.release_data,
                description=item.description,
                style=item.style,
                price_range_year=item.price_range_year,
            )
            self.session.add(sneaker)
            self.log_message("i", f"Added {item.title} to session")
        except Exception as e:
            self.log_message("e", f"Failed to add {item.title}: {e}")

    def iterate_products(self, products: list) -> dict:
        """Function to visit each item given a list of items

        This functions takes in a list of products as its argument. We itterate
        through the products and set the url of each. Then using the config
        we set earlier we will then scrape that data from each individual item.
        For example we have  ['product1_link', 'product2_link', ... 'productn_link'].
        We will iterate the list and get data for each prodcut using the function
        `scrape`. We then return the data we got from each prodcut.
        Args:
            products: A list of products we want to scrape

        Returns:
            list
        """
        data: list = []
        for product in products:  # for each link
            current_item_dict: dict = {}
            self.get_url(product)  # set url for each link
            for key, xpath in self.config[
                "PRODUCT"
            ].items():  # for each item and dictionary
                # get the elements using xpath
                elements: list = self.scrape(key, xpath)
                # add the elements to the dictionary
                # as key is the name of the element we want and value is the elements
                current_item_dict[key] = elements
            item: BookItem = BookItem(
                **current_item_dict
            )  # create a scraped item instance
            self.log_message("i", f"ITEM: {item.model_dump()}")
            data.append(item)
            self.save_to_db(item)
        self.session.commit()  # commit the session
        return data

    def scrape(self, key: str, xpath: str) -> list:
        """Function to scrape data from a product

        This functions scrapes data from a page. Given a key (name
        of the element we want to scrape) and a xpath to the element we
        scrape the data. Using the config, we check if we need to do
        multiple elements or just one. We also check for images.
        We then return the element we scraped.

        Args:
            key: a sring that represents the name of the element we want to scrape
            xpath: a sring that represents the xpath of the element we want to

        Returns:
            list
        """
        elements = ""
        if key in self.config["MULTIPLE"]:
            elements = self.get_elements(xpath)
            texts = []
            for el in elements:
                try:
                    text = el.text.strip()
                    if text:
                        texts.append(text)
                except StaleElementReferenceException:
                    self.log_message(
                        "i", f"Skipped stale element while scraping key: {key}"
                    )
                    continue
            elements = " ".join(texts)
        elif key == "img":
            element = self.get_element(xpath)
            img = element.get_attribute("src")
            with open(f"./images/{img}.png", "wb") as f:
                f.write(requests.get(img).content)
            return img
        else:
            element = self.get_element(xpath)
            elements = element.text.strip()
        return elements
