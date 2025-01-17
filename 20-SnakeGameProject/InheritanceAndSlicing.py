class Animal:

    def __init__(self):
        self.mata = 2

    def nafas(self):
        print("tinggal nafas")


class Fish(Animal):
    """"belajar inheritance yaitu mengadopsi sifat sifat class lainnya"""

    def __init__(self):
        super().__init__()  # ini rumusnya ya! adopsi attribute maupun method

    def nafas(self):
        super().nafas()  # Manggil salah satu sifatnya
        print("bedanya ini di dalam air")

    def renang(self):
        print("tinggal renang!")


Fish().nafas()
print(Fish().mata)


alfabet = ["a", "b", "c", "d", "e", "f", "g"]
kord = ("a", 4, 0, "r")

print(alfabet[1:-2:2])
