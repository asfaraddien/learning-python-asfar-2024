# absolut file path    --> /user/document/project/main.py
# relative file path   --> ./ (di directory ini ke...)
#                      --> ../ (sebelum directory ini ke...)



# Buka File, baca, tutup manual
file = open('../../../Desktop/text.txt')
content = file.read()
# print(content)
file.close()

# Sama, tapi buka otomatis, sekalian nambah tulisan
with open('../../../text.txt', mode="a") as file:  # a: append r: read-only w: dihapus semua, ganti baru
    file.write("Bermanfaat")

# Buat file baru, sekalian nulis isinya
with open("textbaru.txt", mode="w") as baru:
    baru.write("gile enak")
