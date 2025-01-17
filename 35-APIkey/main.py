import requests
import os

# api_key = "26f2940b2b5039ac32213dcd7b3f1ca6"
# API = "https://api.openweathermap.org/data/2.5/forecast"
# my_lng = 106.669708
# my_lat = -6.227181
#
# lng = 107.770
# lat = -6.692
# parameter = {
#     "lat": lat,
#     "lon": lng,
#     "appid": api_key,
#     "cnt": 4
#
# }
#
# res = requests.get(API, params=parameter)
# res.raise_for_status()
#
# data = res.json()["list"]
#
# is_it_rain = [data[i]["weather"][0]["id"] for i in range(len(data))]
# print(data)
# print(is_it_rain)
#
#
# for i in is_it_rain:
#     if i < 700:
#         print("Hujan coy!")

print(os.environ.get("API_KEY"))
