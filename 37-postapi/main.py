import requests
import datetime as dt

now = dt.datetime.now().date()
now_upg = now.strftime("%Y%m%d")

USER = "asfaraddien"
TOKEN = "a2005t2008"
GRAPH = "graph1"
secret_bang ={
    "X-USER-TOKEN": TOKEN
}

url = "https://pixe.la/v1/users"
url2 = f"https://pixe.la/v1/users/{USER}/graphs"
url3 = f"https://pixe.la/v1/users/{USER}/graphs/{GRAPH}"
url4 = f"https://pixe.la/v1/users/{USER}/graphs/{GRAPH}/{now_upg}"

user_con ={
    "token":TOKEN,
    "username":USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# res = requests.post(url=url, json=user_con)
# print(res.text)


graph_con = {
    "id": GRAPH,
    "name":"Sepedaan",
    "unit":"km",
    "type":"float",
    "color":"sora",

}



# res2 = requests.post(url=url2, json=graph_con, headers=secret_bang)
# print(res2.text)

graph_con2 = {
    "date": now_upg,
    "quantity": "10.56",

}

# res3 = requests.post(url=url3,headers=secret_bang, json=graph_con2)
# print(res3.text)

graph_con3 = {
    "quantity": "10.56",

}

# res4 = requests.put(url=url4, headers=secret_bang, json=graph_con3)
# print(res4.text)

res5 = requests.delete(url=f"https://pixe.la/v1/users/{USER}/graphs/{GRAPH}/20240701", headers=secret_bang)
print(res5.text)
