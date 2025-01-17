from random import randint

letter = [1, 2, 3]
new = [i + 2 for i in letter]

letter2 = [i for i in range(5)]

letter3 = [i for i in range(5) if i != 3]
############################################
list1 = ["Asfar", "Hamdan", "Harun"]
dict1 = {name: randint(1, 100) for name in list1}

dict2 = {name: nilai - 10 for (name, nilai) in dict1.items()}
############################################
dict3 = {
    "name": ["Asfar", "Hamdan", "Harun"],
    "nilai": [100, 90, 80]
}

import pandas
data = pandas.DataFrame(dict3)
for (index, row) in data.iterrows():
    if index == 2:
        print(row.nilai)

