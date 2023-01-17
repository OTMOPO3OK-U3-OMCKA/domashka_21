from classes.storage import Storage


class Shop(Storage):
    def __init__(self):
        self.capacity = 20
        self.items = {}
        self.limit = 5
        self.to_place = "в магазине"
        self.from_place = "из магазина"
        self.words_to_read = [{"из магазин": self, "c магазин": self},
                              {"в магазин": self}]

