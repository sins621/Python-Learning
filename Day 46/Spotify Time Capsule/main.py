import os
import json

import requests
import spotipy
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")
SPOTIFY_ID = os.getenv("SPOTIFY_ID")
spotify_auth = spotipy.oauth2.SpotifyOAuth(
    client_secret=SPOTIFY_SECRET,
    client_id=SPOTIFY_ID,
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
)

spotify_token = spotify_auth.get_access_token()["access_token"]

music_date = input(
    "Which year do you want to travel to? Type the date in this format: YYYY-MM-DD\n"
)
music_date = "2010-02-18"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

response = requests.get(
    f"https://www.billboard.com/charts/hot-100/{music_date}/", headers=header
)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]


sp = spotipy.Spotify(auth=spotify_token)
user = sp.current_user()["id"]

music_year = music_date.split("-")[0]

for song in song_names:
    song_url = sp.search(
        q=f"track:{song} year:{music_year}", type="track", limit=1
    )
    track_url = song_url["tracks"]["items"][0]["external_urls"]["spotify"]
    # print(json.dumps(song_url, indent=2))
    print(track_url)
