base_url = 'https://stockx.com/sneakers/'
size_url = 'size-' 
page_url = '/page='
URLS = [base_url + size_url + str(i) + '?' + page_url + str(i) for i in range(1,25)]


def get_urls():
    new_url = [base_url + size_url + str(i) for i in range(1, 19)]
    #all possible urls we are scraping
    all_urls = []

    for i in range(len(new_url)):
        main = [new_url[i] + page_url + str(x) for x in range(0,26)]
        all_urls.append(main)
    return all_urls

all_urls = get_urls()
print(len(all_urls[0]))
