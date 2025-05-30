from abc import ABC, abstractmethod

class BaseScraper(ABC):
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    @abstractmethod
    def scrape(self):
        pass
