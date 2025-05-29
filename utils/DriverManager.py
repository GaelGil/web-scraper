from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class DriverManager:
    def __init__(self, headless=True):
        self.headless = headless

    def get_driver(self):
        options = Options()
        if self.headless:
            options.add_argument("--headless")
        return webdriver.Firefox(options=options)
