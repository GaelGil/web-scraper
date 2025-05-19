from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.headless = True  

GECKODRIVER_PATH = "./drivers/geckodriver"

service = Service(GECKODRIVER_PATH)
driver = webdriver.Firefox(service=service, options=options)

url = "https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8"  
driver.get(url)

driver.get(url)

time.sleep(3)

try:
    articles = driver.find_elements(By.TAG_NAME, "h2")
    print("Found articles:")
    for article in articles:
        print("-", article.text)
except Exception as e:
    print("Error while scraping:", e)

driver.quit()
