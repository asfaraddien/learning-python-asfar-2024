class User:
    # pertama : kita buat attributes
        # sama aja kayak gini:
        # user_1.id = "001"
        # user_1.username = "asfaraddien"
        # user_1.subscriber = 0
    # kedua : buat method

    def __init__(self, nomer_id, username):
        self.id = nomer_id
        self.username = username
        self.following = 0
        self.follower = 0  # ini default attribute


    def follow(self, followed):
        self.following += 1
        followed.follower += 1

user_1 = User("001", "asfaraddien")
user_2 = User("002", "masafa")

user_1.follow(user_2)   # ceritanya asfaraddien follow masafa

