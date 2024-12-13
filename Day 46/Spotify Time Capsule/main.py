import os

import requests
import spotipy
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# music_date = input(
#     "Which year do you want to travel to? Type the date in this format: YYYY-MM-DD\n"
# )
# music_date = "2010-02-18"

# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
# }

# response = requests.get(
#     f"https://www.billboard.com/charts/hot-100/{music_date}/", headers=header
# )
# response.raise_for_status()
# website_html = response.text

# soup = BeautifulSoup(website_html, "html.parser")
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]

# for song in song_names:
#     print(song)


# Access environment variables as if they came from the actual environment
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")
SPOTIFY_ID = os.getenv("SPOTIFY_ID")
SPOTIFY_TOKEN = os.getenv("SPOTIFY_TOKEN")

# spotify_auth = spotipy.oauth2.SpotifyOAuth(
#     client_secret=SPOTIFY_SECRET,
#     client_id=SPOTIFY_ID,
#     scope="playlist-modify-private",
#     redirect_uri="http://example.com",
# )


sp = spotipy.Spotify(auth=SPOTIFY_TOKEN)
# user = sp.current_user()["id"]

# sp.search(2
