import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {}
for (index, value) in data.iterrows():
    data_dict[value["letter"]] = value.code
# ---------------------------------------------------------------- #
data_dict2 = pandas.DataFrame.to_dict(data, orient="records")
print(data_dict2)
print(data_dict)
# ---------------------------------------------------------------- #

def game():
    try:
        word = input("Masukan kata!: ").upper()
        answer = [data_dict[i] for i in word]
        print(answer)
    except KeyError:
        print("Maaf, kalau pakai yang niat dong!!")
    finally:
        game()

game()
