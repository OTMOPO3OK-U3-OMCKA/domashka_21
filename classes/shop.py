from classes.storage import Storage


class Shop(Storage):
    def __init__(self):
        self.capacity = 20
        self.items = {}
        self.dd = 5
        self.t = "в магазине"
        self.f = "из магазина"

