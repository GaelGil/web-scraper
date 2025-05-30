from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class DriverManager:
    def __init__(self, driver_path: str, headless: bool=True) -> None:
        """
        """
        options = Options()
        options.headless = headless
        service = Service(driver_path)
        self._driver = webdriver.Firefox(service=service, options=options)

    def get_driver(self):
        options = Options()
        if self.headless:
            options.add_argument("--headless")
        return webdriver.Firefox(options=options)
