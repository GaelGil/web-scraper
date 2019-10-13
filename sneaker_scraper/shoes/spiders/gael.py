base_url = 'https://stockx.com/sneakers/'
size_url = 'size-' 
page_url = '?page='
URLS = [base_url + size_url + str(i) + '?' + page_url + str(i) for i in range(1,25)]


def get_urls():
    new_url = [base_url + size_url + str(i) for i in range(5, 11)]
    #all possible urls we are scraping
    all_urls = []
    main = []
    for i in range(len(new_url)):
        main = [new_url[i] + page_url + str(x) for x in range(0,26)]
        all_urls.append(main)

    for x in range(len(all_urls)):
        for y in range(len(all_urls[x])):
            if (all_urls[x][y]) in main:
                pass
            elif (all_urls[x][y]) not in main:
                main.append(all_urls[x][y])

    return main

all_urls = get_urls()

for i in range(len(all_urls)):
    print(all_urls[i])


print(len(all_urls))