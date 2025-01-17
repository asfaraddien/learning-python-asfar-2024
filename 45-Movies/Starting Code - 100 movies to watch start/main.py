import requests
from bs4 import BeautifulSoup
import lxml
import pandas

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

res = requests.get(URL)
data = res.text
soup = BeautifulSoup(data, features="lxml")
moviesbef = soup.find_all(name="h3", class_="title")
movies = [i.get_text() for i in moviesbef]
movies.reverse()
print(movies)

with open("movies.txt", 'w', encoding="utf-8") as de:
    for i in movies:
        tex = f"{i}\n"
        de.write(tex)