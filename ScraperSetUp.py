CONFIG = {
    'product': {
        'url': 'https://example.com/products',
        'xpaths': {
            'item': '//div[@class="product"]',
            'title': './/h2/text()',
            'link': './/a/@href',
        }
    },
    'news': {
        'url': 'https://example.com/news',
        'xpaths': {
            'item': '//div[@class="news-item"]',
            'title': './/h3/text()',
            'link': './/a/@href',
        }
    }
}