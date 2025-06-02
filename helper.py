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

def make_urls():
    urls = []
    for i in range(3):
        urls.append(f'https://www.goodreads.com/search?page=1&q={GENRES[i]}&qid=x02cPlELXg&tab=books')
        # urls.append(f'https://www.goodreads.com/search?page=2&q={GENRES[i]}&qid=jyOk4gd2oJ&search_type=books&tab=books&utf8=%E2%9C%93')
    return urls