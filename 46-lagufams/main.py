from pprint import pprint
import requests
from bs4 import BeautifulSoup
import lxml
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
client = os.environ.get("CLIENT_ID")
sec = os.environ.get("CLIENT_SEC")
red = "https://example.com/"
scope = "playlist-modify-private"
id_ = '31ol4wjeeyt3godrb5rtpsiufieq'
play_id = "2G9iedNBkOFfvlB5GZlecM"

date = "2020-06-25"  #input("Tanggal: (YYYY-MM-DD)")
url = f"https://www.billboard.com/charts/hot-100/{date}/"

res = requests.get(url)
data = res.text
scrapper = BeautifulSoup(data, features="lxml")
songsbf = scrapper.select("ul li ul li h3")
songs = [i.get_text().strip() for i in songsbf]
print(songs)

acc = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client, client_secret=sec, redirect_uri=red, scope=scope))
print(acc.current_user())

def make_play():
    new = acc.user_playlist_create(id_, "100 Songs", description="hmmm HARAM!", public=False)
    return new["id"]

def add(song):
    acc.playlist_add_items(play_id, song)



song_list = []
for song in songs:
    job = acc.search(limit=1, q=f"track:{song} year:{date.split(sep="-")[0]}", type="track")
    song_list.append(job["tracks"]["items"][0]["uri"])
pprint(song_list)
add(song_list)





