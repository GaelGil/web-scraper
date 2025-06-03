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
            Function to add a field to our scraped item.

        get_field(self, key: str)
            Function to retrive the value of a feature in the scraped item

        get_item_values(self)
            Function to get the values of the scraped item
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

        This functions perfomes a simple insertion into the _data
        dictionary using a given key and value.

        Args:
            key: The feature/field of the item. Example 'price'
            value: The value of the feature/field of the item
                Example 20.

        Returns:
            None
        """
        self._data[key] = value

    def get_field(self, key: str) -> str:
        """Function to retrive the value of a feature in the scraped item

        Function that retrives a feature/field from the scraped item dictionary
        given a key. 

        Args:
            key: the feature we want to retrive from the scraped item dictionary

        Returns:
            str
        """
        return self._data[key]

    def get_item_values(self) -> list:
        """Function to get the values of the scraped item

        This functions returns only the values of the scraped item in the 
        dictionary

        Args:
            None

        Returns:
            list
        """
        return self._data.values()
