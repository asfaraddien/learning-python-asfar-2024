def tambah(*args):
    result = 0
    for i in args:
        result += i
    print(result)

tambah(7, 9, 8)
###################################
class Car:
    def __init__(self, **kw):
        self.color = kw["color"]
        self.model = kw.get("model")  # if the argument is not given, then it ll return None
        self.type = kw.get("type")


