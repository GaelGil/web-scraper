import time
import requests
from bs4 import BeautifulSoup

class Scraper:
    """
    A class used to communicate with the Spotify api.

    Attributes
    ----------
    spotify_client : list
        The spotify client

    Methods
    -------
    search_spotify_playlist(self, query:str, limit:int)
        Searches spotify for playlists.

    get_tracks_for_new_playlist(self, playlist_ids:str, popularity:int, popular:bool):
        Get a list of tracks for the new playlist.

    get_popular_tracks(self, playlist_name:str, for_user:str)
        Gets popular or unpopular songs and adds them to a list

    create_spotify_playlist(self, playlist_name:str)
        Creates a spotify playlists.
    
    add_tracks_to_playlist(self, playlist_id:str)
        Add songs in a list to a spotify playlists.
    """

    URL = f'https://www.barnesandnoble.com/s/'
    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

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
        self.spotify_client = self.auth_spotify()



def get_data(search_query):
    try:
        response = requests.get(URL+search_query, headers=HEADERS)
        response.raise_for_status()

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            book_titles = [title.text.strip() for title in soup.select('.product-shelf-title a')]
            return book_titles

    except requests.RequestException as e:
        print(f"Request failed: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None

search_query = 'cool'

for _ in range(3):  # Making 3 requests as an example
    barnes_and_noble_data = get_data(search_query)

    if barnes_and_noble_data:
        # print(barnes_and_noble_data)
        for idx, title in enumerate(barnes_and_noble_data, start=1):
            print(f"{idx}. {title}")

    else: 
        print("nothing")
    # Add a delay of 2 seconds between requests
    time.sleep(2)

