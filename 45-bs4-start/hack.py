from bs4 import BeautifulSoup
from pprint import pprint
import requests
import lxml
import time


def begin():
    order = {}
    for tu in range(10, 11):
        time.sleep(1)
        res = requests.get(f"https://news.ycombinator.com/news?p={tu}")
        data = res.text

        soup = BeautifulSoup(data, features="lxml")
        all_news = soup.find_all(class_="titleline")
        all_news2 = [i.find("a") for i in all_news]
        news = {i.get_text(): i.get("href") for i in all_news2}
        print(f"Jumlah link: {len(news)}")

        news_score = soup.select(selector=".score")
        news_score2 = [int(i.get_text().split()[0]) for i in news_score]
        print(f"Jumlah skor: {len(news_score2)}")

        if len(news) == len(news_score2):
            num = 0
            for (key, value) in news.items():
                order[key] = {"link": value, "point": news_score2[num]}
                num += 1
            print(f"Jumlah data: {len(order)}\n")

        else:
            print(f"Jumlah data: {len(order)}")
            print(f"Tidak sama. halaman: {tu}\n")



    max_ = {}
    max_po = 0
    for (key, value) in order.items():
        if max_po < value["point"]:
            max_po = value["point"]
            max_ = {key: value}
    print(max_)


begin()
while True:
    time.sleep(30)
    begin()
