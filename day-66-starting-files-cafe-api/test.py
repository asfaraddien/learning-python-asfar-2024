class Test:
    def __init__(self):
        self.attribute1 = "hello world"
        self.attribute2 = 5
    def __repr__(self):
        return f"ini test yang namany"

test_o = Test()
print(getattr(test_o, "attribute1"))
print("Asfar Addien".capitalize())

