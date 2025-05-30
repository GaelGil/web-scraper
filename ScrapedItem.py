"""class the represents a scraped item


"""

class ScrapedItem:
    """
    A class used to manage a webscraper

    Attributes:
        _data: 

    Methods:
        __init__(self, driver_path: str, headless: bool)
            Initializes the instance to be ready for scraping

    """


    def __init__(self) -> None:
        """Initializes the instance to be ready for scraping.

        Initializes the Scraper instance to set the options and driver
        on the selenium scraper. 

        Args: 
            driver_path: the path to the browser driver
            headless: bool for headless option

        Returns:
            None
        """
        self._data = {}


    def add_field(self, key: str, value: str)  -> None:
        """Function to set the url that we will scrape.

        Function to set the url of the website that we want our scraper to visit.
        After its done we wait for 3 seconds. 

        Args:
            url: The url we want to scrape which is a string

        Returns:
            None
        """
        self._data[key] = value


    def get_field(self, key: str) -> None:
        return self._data[key]
    

    def get_item_values(self) -> None:
        return self._data.values()
        # pass