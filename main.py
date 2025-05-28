from Scraper import Scraper
from helper import XPATHS, make_urls

GECKODRIVER_PATH = "./drivers/geckodriver"
NEXT_PAGE_BUTTON_XPATH = '//a[@class="next_page" and @rel="next"]'
LINK_XPATH = "//*[@id='bodycontainer']/div[3]/div[1]/div[2]/div[2]/table/tbody/tr/td[2]/a"
MULTIPLE = {'genres' : 0}


sc = Scraper(GECKODRIVER_PATH, headless=True)
sc.set_next_page_xpath(NEXT_PAGE_BUTTON_XPATH)
sc.set_xpaths(XPATHS)
sc.set_multiple(MULTIPLE)
sc.set_urls(make_urls())
sc.set_link_xpath(LINK_XPATH)
sc.visit_urls(stop=5)
sc.visit_items()
formated_data = sc.format_data()
sc.to_csv('./data.csv', formated_data)
