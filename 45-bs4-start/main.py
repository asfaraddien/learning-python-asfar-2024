import bs4 as bs
import lxml

with open("website.html", "r", encoding="utf-8") as data:
    contents = data.read()

soup = bs.BeautifulSoup(contents, "html.parser")
# print(soup.title.string)

all_anchor = soup.find_all(name="a", )
# print(all_anchor)

all_anchor_link = []
for i in all_anchor:
    all_anchor_link.append(i.get("href"))
# print(all_anchor_link)

paragraph = soup.find(name="p", id="test")
# print(paragraph.get_text())

head = soup.find(name="h3", class_="heading")
# print(head)

#sekarang milihnya pakai selector

anch = soup.select_one("p a")
print(anch)