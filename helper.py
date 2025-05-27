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

XPATHS = {
    'title': "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[1]/div[1]/h1",
    'author' : "//*[@id='__next']/div[2]/main/div[1]/div[2]/div[2]/div[2]/div[1]/h3/div/span[1]/a/span[1]",
    'rating': '//div[@class="RatingStatistics__rating"]',
    'raitings' : '//span[@data-testid="ratingsCount"]',
    'reviews' : '//span[@data-testid="reviewsCount"]',
    'overview' : '//div[@data-testid="description"]//span[@class="Formatted"]',
    'x': '//ul[@class="CollapsableList"]//span[@class="Button__labelItem"]',
    'pages' : '//p[@data-testid="pagesFormat"]',
    'publish_date' : '//p[@data-testid="publicationInfo"]',
    }


def get_genres():
    return GENRES


def get_xpaths():
    return XPATHS