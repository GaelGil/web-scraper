from abc import ABC, abstractmethod
from selenium import webdriver

class BaseScraper(ABC):
    def __init__(self, driver):
        self._driver = driver 
    
    @abstractmethod
    def navigate(self):
        """Navigate to the target page."""
        pass
    
    @abstractmethod
    def scrape(self):
        """Perform scraping logic."""
        pass
    
    def close(self):
        self._driver.quit()