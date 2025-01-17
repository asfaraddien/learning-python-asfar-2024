import requests


class Post:
    def __init__(self):
        url = "https://api.npoint.io/c790b4d5cab58020d391"
        res = requests.get(url)
        self.data = res.json()
        self.title = None
        self.subtitle = None
        self.content = None

    def milih(self, num):
        for i in self.data:
            if i["id"] == num:
                self.title = i["title"]
                self.subtitle = i["subtitle"]
                self.content = i["body"]



