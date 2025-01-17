#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch


wish = DataManager()
search = FlightSearch()

# wish.get()
# pprint(wish.data)
# flight_list = wish.data["prices"]
flight_list = [{'city': 'Paris', 'iataCode': 'PAR', 'id': 2, 'lowestPrice': 54},
 {'city': 'Frankfurt', 'iataCode': 'FRA', 'id': 3, 'lowestPrice': 42},
 {'city': 'Tokyo', 'iataCode': 'TYO', 'id': 4, 'lowestPrice': 485},
 {'city': 'Hong Kong', 'iataCode': 'HKG', 'id': 5, 'lowestPrice': 551},
 {'city': 'Istanbul', 'iataCode': 'IST', 'id': 6, 'lowestPrice': 95},
 {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'id': 7, 'lowestPrice': 414},
 {'city': 'New York', 'iataCode': 'NYC', 'id': 8, 'lowestPrice': 240},
 {'city': 'San Francisco', 'iataCode': 'SFO', 'id': 9, 'lowestPrice': 260},
 {'city': 'Dublin', 'iataCode': 'DBN', 'id': 10, 'lowestPrice': 378}]

for i in flight_list:
    if i["iataCode"] == "":
        chosen = i["city"]
        chosen = search.code(chosen)
        i["iataCode"] = chosen


pprint(flight_list)
wish.data = {"prices": flight_list}
wish.put()

# search.token_new()





