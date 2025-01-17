import requests
from pprint import pprint

end = "https://api.sheety.co/f3b135c316ef39a54c40b4fed743bce0/flightDeals/prices/"

class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self):
        self.data = None


    def get(self):
        res = requests.get(url=end)
        print(res.text)
        self.data = res.json()

    def put(self):
        row_index = 2
        for i in range(len(self.data["prices"]) - 1):
            url2 = f"{end}/{row_index}"
            add_row = {"price": self.data["prices"][i]}
            res2 = requests.put(url2, json=add_row)
            row_index += 1
            print(res2.text)






