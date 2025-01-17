import requests
import datetime as dt
import os

# ----------------------------------------------
os.environ["API_KEY"] = "67a8d10b0ad1458e4ac36d4c785f2bb5"
os.environ["api_id"] = "576a98eb"
os.environ["END"] = "https://trackapi.nutritionix.com/v2/natural/exercise"
os.environ["END2"] = "https://api.sheety.co/f3b135c316ef39a54c40b4fed743bce0/asfarWo/workouts"
os.environ["API_KEY_SHEET"] ="Basic YXNmYXJhZGRpZW46YTIwMDV0MjAwOA=="

end = os.environ.get("END")
API_KEY = os.environ.get("API_KEY")
API_ID = os.environ.get("api_id")

end2 = os.environ.get("END2")
sheet_key = os.environ.get("API_KEY_SHEET")

end2_2 = "https://api.sheety.co/f3b135c316ef39a54c40b4fed743bce0/asfarWo/workouts/3"
# ----------------------------------------------

now = dt.datetime.now()
now_date = now.strftime("%d/%m/%Y")
now_time = now.strftime("%X")

age = 19
height = 172
weight = 63
# ----------------------------------------------

param = {
    "query": input("apa olahraganya?"),
    "age": age,
    "height_cm": height,
    "weight_kg": weight,
}

secret = {
    "x-app-key": API_KEY,
    "x-app-id": API_ID
}

res = requests.post(end, headers=secret, json=param)
data = res.json()
obs = data["exercises"]
# ----------------------------------------------


for i in obs:
    sheet = {"workout" : {
        "date": now_date,
        "time": now_time,
        "exercise": i["name"].title(),
        "duration": i["duration_min"],
        "calories": i["nf_calories"],

    }}

    secret2 = {
        "Authorization": sheet_key
    }

    res2 = requests.put(end2_2, json=sheet, headers=secret2)

    print(sheet)

    print(res2.text)

