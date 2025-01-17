from pprint import pprint
import requests



class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def __init__(self):
        self.API_KEY = "MaQIeEElTuSMIZqbiX5bbAzso4nAGPb3"
        self.API_SECRET = "NSbjoQZ13qq4XtRp"
        self.TOKEN = self.token_new()

    def token_new(self):
        token_end = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.API_KEY,
            'client_secret': self.API_SECRET
        }
        res = requests.post(url=token_end,data=body,headers=header)
        print(res.json()['access_token'])
        print(res.json()['expires_in'])
        return res.json()['access_token']


    def code(self, city):
        code_end = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        header = {
            "Authorization": f"Bearer {self.TOKEN}"
        }

        param = {
            "keyword": city
        }
        res2 = requests.get(code_end, params=param, headers=header)
        print(res2.text)
        return res2.json()["data"][0]["iataCode"]

