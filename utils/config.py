from .schemas import ScraperConfig, ToScrape, Url

DRIVER_PATH = "./drivers/geckodriver"
HEADLESS = True

GOODREADS: ScraperConfig = ScraperConfig(
    product_info=[
        ToScrape(
            xpath='//*[@id="__next"]/div[2]/main/div[1]/div[2]/div[2]/div[1]/div[1]/h1',
            name="title",
        ),
        ToScrape(
            xpath='//*[@id="__next"]/div[2]/main/div[1]/div[2]/div[2]/div[2]/div[1]/h3/div/span[1]/a/span[1]',
            name="author",
        ),
        ToScrape(
            xpath='//div[@class="RatingStatistics__rating"]',
            name="rating",
        ),
        ToScrape(
            xpath='//span[@data-testid="ratingsCount"]',
            name="ratings",
        ),
        ToScrape(
            xpath='//span[@data-testid="reviewsCount"]',
            name="reviews",
        ),
        ToScrape(
            xpath='//div[@data-testid="description"]//span[@class="Formatted"]',
            name="overview",
        ),
        ToScrape(
            xpath='//div[@data-testid="genresList"]//span[@class="Button__labelItem"]',
            name="genres",
        ),
        ToScrape(
            xpath='//p[@data-testid="pagesFormat"]',
            name="pages",
        ),
        ToScrape(
            xpath='//p[@data-testid="publicationInfo"]',
            name="publish_date",
        ),
    ],
    products_url_xpath='//*[@id="bodycontainer"]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr/td[2]/a',
    urls_to_scrape=[
        # Url(url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Art"),
        # Url(
        #     url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Biography"
        # ),
        # Url(
        #     url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Classics"
        # ),
        # Url(url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Comics"),
        # Url(
        #     url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Cookbooks"
        # ),
        # Url(url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Drama"),
        # Url(url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Fantasy"),
        # Url(url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Fiction"),
        # Url(
        #     url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Graphic+Novels"
        # ),
        # Url(url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=History"),
        # Url(url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Horror"),
        # Url(url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Mystery"),
        Url(
            url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Nonfiction"
        ),
        Url(url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Poetry"),
        Url(url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Romance"),
        Url(url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Science"),
        Url(
            url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Science+Fiction"
        ),
        Url(
            url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Thriller"
        ),
        Url(
            url="https://www.goodreads.com/search?page=4&utf8=%E2%9C%93&query=Young+Adult"
        ),
    ],
    next_page_button_xpath='//a[@class="next_page" and @rel="next"]',
    multiple={"genres": 0},
    categories_button='//span[text()="Browse ▾"]',
    categories='//ul[contains(@class, "genreList")]//li/a',
    popup='//button[@class="gr-iconButton"][.//img[@alt="Dismiss"]]',
    close_popup_button='//button[@class="gr-iconButton"][.//img[@alt="Dismiss"]]',
)

STOCKX: ScraperConfig = ScraperConfig(
    product_info=[
        ToScrape(
            xpath="name",
            name='//h1[@data-component="primary-product-title"]',
        ),
        ToScrape(
            xpath="img",
            name='//div[@id="three-sixty-image"]//img[@data-image-type="360"]',
        ),
        ToScrape(
            xpath="retail_price",
            name='//div[@class="RatingStatistics__rating"]',
        ),
        ToScrape(
            xpath="display_price",
            name='//h2[@data-testid="trade-box-buy-amount"]',
        ),
        ToScrape(
            xpath="release_data",
            name='//div[@data-component="product-trait"][.//span[text()="Release Date"]]//p',
        ),
        ToScrape(
            xpath="description",
            name='//div[@data-component="ProductDescription" and @data-testid="product-description"]/p',
        ),
        ToScrape(
            xpath="style",
            name='//div[@data-component="product-trait"][.//span[text()="Style"]]/p',
        ),
        ToScrape(
            xpath="price_range_year",
            name='//div[@data-component="product-trait"][.//span[text()="Price Range"]]//p',
        ),
    ],
    products_url_xpath='//a[@data-testid="productTile-ProductSwitcherLink"]/@href',
    urls_to_scrape=[
        Url(url="https://stockx.com/search?s==adidas&category=sneakers"),
        Url(url="https://stockx.com/search?s==Air+Jordan&category=sneakers"),
        Url(url="https://stockx.com/search?s==ASICS&category=sneakers"),
        Url(url="https://stockx.com/search?s==New Balance&category=sneakers"),
        Url(url="https://stockx.com/search?s==Nike&category=sneakers"),
        Url(url="https://stockx.com/search?s==Louis+Vuitton&category=sneakers"),
        Url(url="https://stockx.com/search?s==Yeezy&category=converse"),
    ],
    next_page_button_xpath='//a[@aria-label="Next"]',
    multiple={},
    categories_button="",
    categories="",
    popup="",
    close_popup_button="",
)
