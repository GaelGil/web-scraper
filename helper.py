GENRES = [
'Art',
'Biography',
'Business',
'Childrens',
'Classics',
'Comics',
'Cookbooks',
'Fantasy',
'Fiction',
'Graphic Novels',
'Historical Fiction',
'History',
'Horror',
'Memoir',
'Music',
'Mystery',
'Nonfiction',
'Poetry',
'Psychology',
'Romance',
'Science',
'Science Fiction',
'Self Help',
'Sports',
'Thriller',
'Travel',
'Young Adult',

]

# XPATHS = {
#     'title': "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[1]/div[1]/h1",
#     'author' : "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[2]/div[1]/h3/div/span[1]/a/span[1]",
#     'rating': '//div[@class="RatingStatistics__rating"]',
#     'raitings' : '//span[@data-testid="ratingsCount"]',
#     'reviews' : '//span[@data-testid="reviewsCount"]',
#     'overview' : '//div[@data-testid="description"]//span[@class="Formatted"]',
#     'genres': '//ul[@class="CollapsableList"]//span[@class="Button__labelItem"]',
#     'pages' : '//p[@data-testid="pagesFormat"]',
#     'publish_date' : '//p[@data-testid="publicationInfo"]',
#     }

XPATHS = {
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

# GENRES = [
#     'Nike',
#     'Jordan',
#     'adidas',
#     'Fear of God',
#     'New Balance',
#     'ASICS',
#     'Supreme',
#     'Pop Mart',
#     'UGG',
#     'Crocs',
#     'Yeezy',
#     'BAPE',
#     'Puma',
#     'Pokemon',
#     'Trending Brands',
#     'Louis Vuitton',
#     'Gucci',
#     'Travis Scott',
#     'Balenciaga',
#     'Converse',
#     'Saint Laurent',
#     'OFF-WHITE',
#     'Versace',
#     'Maison Mihara Yasuhiro',
#     'Vans',
#     'Birkenstock',
#     'Dior'
# ]



def make_urls():
    urls = []
    for i in range(1):
        # urls.append(f'https://www.goodreads.com/search?page=1&q={GENRES[i]}&qid=x02cPlELXg&tab=books')
        urls.append(f'https://www.goodreads.com/search?page=2&q={GENRES[i]}&qid=jyOk4gd2oJ&search_type=books&tab=books&utf8=%E2%9C%93')
    return urls