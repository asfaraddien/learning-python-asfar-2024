import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import time

url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
url2 = "https://www.google.com/finance/quote/USD-IDR?hl=en"

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7"
}

def find():
    res = requests.get(url, headers=head)
    data = res.text

    sup = BeautifulSoup(data, features="lxml")
    price = float(f"{sup.find(name="span", class_="a-price-whole").get_text()}{sup.find(name="span", class_="a-price-fraction").get_text()}")
    print(price)

def find2():
    res = requests.get(url2, headers=head)
    data = res.text

    sup = BeautifulSoup(data, features="lxml")
    price = sup.find(name="div", class_="YMlKec fxKbKc").get_text()
    lev = sup.find(name="div", class_="JwB6zf").get_text()
    new = float(price.replace(",", "_"))
    print(f"{new} | {lev}")

# find()
# while True:
#     time.sleep(3)
#     find()

find2()
while True:
    time.sleep(2)
    find2()
