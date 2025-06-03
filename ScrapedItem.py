"""Class that represents a scraped item

This python module is used to represent a item that we scrape and its data.
It has a class variable _data that is a dictionary. We can add to it, 
retrive a field and return the dictionaries values. This is used when scraping
a item such as a product on amazons page. We can store the name, price,
description etc. 

  Typical usage example:
    item1 = ScrapedItem()
    item1['title'] = 'A title'
    item1['price'] = 10

    item2 = ScrapedItem()
    item1['title'] = 'The title'
    item1['price'] = 20

"""

class ScrapedItem:
    """
    A class used to represent a item and its features.

    Attributes:
        _data: A dictionary to hold the items features. Each key is
            a feature and the value being the items actual feature. 
            Example {'product_name': 'name'}

    Methods:
        __init__(self)
            Initializes the instance

        add_field(key: str, value: str)

    """

    def __init__(self) -> None:
        """Initializes the instance to be ready for scraping.

        Initializes the Scraper instance to set the options and driver
        on the selenium scraper. 

        Args: 
            None

        Returns:
            None
        """
        self._data = {}


    def add_field(self, key: str, value: str)  -> None:
        """Function to add a field to our scraped item.

        This 

        Args:
            url: The url we want to scrape which is a string

        Returns:
            None
        """
        self._data[key] = value

    def get_field(self, key: str) -> None:
        """Function to set the url that we will scrape.

        Function to set the url of the website that we want our scraper to visit.
        After its done we wait for 3 seconds. 

        Args:
            url: The url we want to scrape which is a string

        Returns:
            None
        """
        return self._data[key]
    

    def get_item_values(self) -> None:
        """Function to set the url that we will scrape.

        Function to set the url of the website that we want our scraper to visit.
        After its done we wait for 3 seconds. 

        Args:
            url: The url we want to scrape which is a string

        Returns:
            None
        """
        return self._data.values()
