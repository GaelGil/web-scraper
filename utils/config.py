from schemas import ScraperConfig, Product, Url

DRIVER_PATH = "./drivers/geckodriver"
HEADLESS = True

GOODREADS: ScraperConfig = ScraperConfig(
    products=[
        Product(
            xpath='//*[@id="__next"]/div[2]/main/div[1]/div[2]/div[2]/div[1]/div[1]/h1',
            name="title",
        ),
        Product(
            xpath='//*[@id="__next"]/div[2]/main/div[1]/div[2]/div[2]/div[2]/div[1]/h3/div/span[1]/a/span[1]',
            name="author",
        ),
        Product(
            xpath='//div[@class="RatingStatistics__rating"]',
            name="rating",
        ),
        Product(
            xpath='//span[@data-testid="ratingsCount"]',
            name="ratings",
        ),
        Product(
            xpath='//span[@data-testid="reviewsCount"]',
            name="reviews",
        ),
        Product(
            xpath='//div[@data-testid="description"]//span[@class="Formatted"]',
            name="overview",
        ),
        Product(
            xpath='//div[@data-testid="genresList"]//span[@class="Button__labelItem"]',
            name="genres",
        ),
        Product(
            xpath='//p[@data-testid="pagesFormat"]',
            name="pages",
        ),
        Product(
            xpath='//p[@data-testid="publicationInfo"]',
            name="publish_date",
        ),
    ],
    products_xpath='//*[@id="bodycontainer"]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr/td[2]/a',
    urls=[
        Url(url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=Art"),
        Url(url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=Biography"),
        Url(url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=Classics"),
        Url(url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=Comics"),
        Url(url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=Cookbooks"),
        Url(url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=Drama"),
        Url(url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=Fantasy"),
        Url(url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=Fiction"),
        Url(url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=Graphic+Novels"),
        Url(url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=History"),
        Url(url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=Horror"),
        Url(url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=Mystery"),
        Url(url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=Nonfiction"),
        Url(url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=Poetry"),
        Url(url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=Romance"),
        Url(url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=Science"),
        Url(
            url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=Science+Fiction"
        ),
        Url(url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=Thriller"),
        Url(url="https://www.goodreads.com/search?utf8=%E2%9C%93&query=Young+Adult"),
    ],
    next_page_button_xpath='//a[@class="next_page" and @rel="next"]',
    multiple={"genres": 0},
    categories_button='//span[text()="Browse ▾"]',
    categories='//ul[contains(@class, "genreList")]//li/a',
    popup='//button[@class="gr-iconButton"][.//img[@alt="Dismiss"]]',
    close_popup_button='//button[@class="gr-iconButton"][.//img[@alt="Dismiss"]]',
)

STOCKX: ScraperConfig = ScraperConfig(
    products=[
        Product(
            xpath="name",
            name='//h1[@data-component="primary-product-title"]',
        ),
        Product(
            xpath="img",
            name='//div[@id="three-sixty-image"]//img[@data-image-type="360"]',
        ),
        Product(
            xpath="retail_price",
            name='//div[@class="RatingStatistics__rating"]',
        ),
        Product(
            xpath="display_price",
            name='//h2[@data-testid="trade-box-buy-amount"]',
        ),
        Product(
            xpath="release_data",
            name='//div[@data-component="product-trait"][.//span[text()="Release Date"]]//p',
        ),
        Product(
            xpath="description",
            name='//div[@data-component="ProductDescription" and @data-testid="product-description"]/p',
        ),
        Product(
            xpath="style",
            name='//div[@data-component="product-trait"][.//span[text()="Style"]]/p',
        ),
        Product(
            xpath="price_range_year",
            name='//div[@data-component="product-trait"][.//span[text()="Price Range"]]//p',
        ),
    ],
    products_xpath='//a[@data-testid="productTile-ProductSwitcherLink"]/@href',
    urls=[
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
