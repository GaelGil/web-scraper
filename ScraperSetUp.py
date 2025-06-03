CONFIG_GOODREADS = {
    'PRODUCT': {

            'title': "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[1]/div[1]/h1",
            'author' : "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[2]/div[1]/h3/div/span[1]/a/span[1]",
            'rating': '//div[@class="RatingStatistics__rating"]',
            'raitings' : '//span[@data-testid="ratingsCount"]',
            'reviews' : '//span[@data-testid="reviewsCount"]',
            'overview' : '//div[@data-testid="description"]//span[@class="Formatted"]',
            'genres': '//ul[@class="CollapsableList"]//span[@class="Button__labelItem"]',
            'pages' : '//p[@data-testid="pagesFormat"]',
            'publish_date' : '//p[@data-testid="publicationInfo"]',
    },
    'NEXT_PAGE_BUTTON_XPATH': '//a[@class="next_page" and @rel="next"]',
    'PRODUCTS':  '//*[@id="bodycontainer"]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr/td[2]/a',
    'MULTIPLE': {'genres' : 0},
    'URLS' : [],
    'DRIVER_PATH': './drivers/geckodriver',
    'HEADLESS': True,
    'CATEGORIES_BUTTON' : '//span[text()="Browse ▾"]',
    'CATEGORIES' : '//ul[contains(@class, "genreList")]//li/a'
}


CONFIG_SNAKERS = {
    'PRODUCT': {
        'xpaths': {
            'title': "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[1]/div[1]/h1",
            'author' : "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[2]/div[1]/h3/div/span[1]/a/span[1]",
            'rating': '//div[@class="RatingStatistics__rating"]',
            'raitings' : '//span[@data-testid="ratingsCount"]',
            'reviews' : '//span[@data-testid="reviewsCount"]',
            'overview' : '//div[@data-testid="description"]//span[@class="Formatted"]',
            'genres': '//ul[@class="CollapsableList"]//span[@class="Button__labelItem"]',
            'pages' : '//p[@data-testid="pagesFormat"]',
            'publish_date' : '//p[@data-testid="publicationInfo"]',
        }
    },
    'NEXT_PAGE_BUTTON_XPATH': {
        'xpath' : '//a[@class="next_page" and @rel="next"]'
    },
    'PRODUCTS': {
        'xpath': '//*[@id="bodycontainer"]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr/td[2]/a'
    },
    'MULTIPLE': {'genres' : 0},
    'URLS' : [],
    'DRIVER_PATH': './drivers/geckodriver',
    'HEADLESS': True
}