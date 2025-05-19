import time
import requests
from bs4 import BeautifulSoup

class Scraper:
    """
    A class used for webscraping

    Attributes
    ----------
    spotify_client : list
        The spotify client

    Methods
    -------
    set_url(self, query:str, limit:int)
        Searches spotify for playlists.

    get_query(self, playlist_ids:str, popularity:int, popular:bool):
        Get a list of tracks for the new playlist.

    get_header(self, playlist_name:str, for_user:str)
        Gets popular or unpopular songs and adds them to a list

    set_urls(self, playlist_name:str)
        Creates a spotify playlists.
    
    set_link_tag(self, playlist_id:str)
        Add songs in a list to a spotify playlists.

    set_tags(self, playlist_id:str)
        Add songs in a list to a spotify playlists.

    set_links(self, playlist_id:str)
        Add songs in a list to a spotify playlists.
    """

    url = ''
    urls = ''
    headers = ''
    query = ''
    link_tag = ''
    tags = ''
    
    def __init__(self):
        """
        This function will call the class function `auth_spotify` and create a list for later use.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

    def set_url(self, url):
        self.url = url

    def set_query(self, query):
        self.query = query
    
    def set_header(self, header):
        self.headers = header
    
    def set_urls(self, urls):
        self.urls = urls
    
    def set_link_tag(self, link_tag):
        self.link_tag = link_tag
    
    def set_tags(self, tags):
        self.tags = tags

    def get_links(self):
        try:
            response = requests.get(self.url+self.query, headers=self.headers)
            response.raise_for_status()
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                book_links = [selector['href'] for selector in soup.select(self.link_tag)]
                return book_links
        except requests.RequestException as e:
            print(f"Request failed: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return
        
    def get_data_from_link(self, data):
        return data

    def print_data(self, data):
        if data:
            for idx, title in enumerate(data, start=1):
                print(f"{idx}. {title}")        
        else: 
            print("nothing")



url = f'https://www.barnesandnoble.com/s/'
header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
sc = Scraper()
sc.set_url(url)
sc.set_header(header)
sc.set_query("travel")
sc.set_link_tag('.product-shelf-title a')
for _ in range(3):  # Making 3 requests as an example
    data = sc.get_links()
    sc.print_data(data)
    time.sleep(2)
