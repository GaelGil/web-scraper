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
    'genres': '//ul[@class="CollapsableList"]//span[@class="Button__labelItem"]',
    'pages' : '//p[@data-testid="pagesFormat"]',
    'publish_date' : '//p[@data-testid="publicationInfo"]',
    }

NEXT_PAGE_BUTTON_XPATH = '//a[@class="next_page" and @rel="next"]'

LINKS_XPATH = "//*[@id='bodycontainer']/div[3]/div[1]/div[2]/div[2]/table/tbody/tr/td[2]/a"

MULTIPLE = {'genres' : 0}

def make_urls():
    urls = []
    for i in range(len(GENRES)//3):
        urls.append(f'https://www.goodreads.com/search?page=1&q={GENRES[i]}&qid=x02cPlELXg&tab=books')
    return urls