""""CARA PERTAMA"""
# with open("weather_data.csv") as data:
#     data_list = data.readlines()
#     print(data_list)


""""CARA KEDUA"""
# import csv
# with open("weather_data.csv") as data:
#     data_list = csv.reader(data)
#     temperature = []
#     for i in data_list:
#         if i[1] != "temp":
#             temperature.append(int(i[1]))
#     print(temperature)


""""CARA KETIGA"""
import pandas

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].tolist()
# print(data)
# monday = data[data.day == "Monday"]
# temp_mon = monday.temp[0]
# temp_mon_f = temp_mon * 9/5 + 32
# print(temp_mon_f)

"""""get a column"""""
# temp1 = data["temp"]
# temp = data.temp


"""""get a row"""""
# row = data[data.day == "monday"]


"""""get a mean"""""
# mean = data["temp"].mean()
# max = data["temp"].max()
# print(max)
"""""get a mean2"""""
# temp_mean = sum(temp_list) / len(temp_list)
# print(temp_mean)

"""""play with row"""""
data2 = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data2[data2["Primary Fur Color"] == "Gray"])
cinnamon = len(data2[data2["Primary Fur Color"] == "Cinnamon"])
black = len(data2[data2["Primary Fur Color"] == "Black"])

new_tab = {
    "color": ["gray", "cinnamon", "black"],
    "count": [gray, cinnamon, black],
}

new = pandas.DataFrame(new_tab)
new.to_csv("squirrel_count.csv")
