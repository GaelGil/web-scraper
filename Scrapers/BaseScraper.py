from abc import ABC, abstractmethod

class BaseScraper(ABC):
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def set_url(self, url: str) -> None:
        self.driver.get(url)

    @abstractmethod
    def scrape(self):
        pass

    @abstractmethod
    def next_page(self):
        pass

    @abstractmethod
    def handle_popup(self):
        pass
