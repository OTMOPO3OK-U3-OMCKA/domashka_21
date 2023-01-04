from classes.storage import Storage


class Store(Storage):
    def __init__(self):
        self.items = {'www': 16, 'mmm': 8, 'nnn': 11, 'ccc': 12, 'xxx': 6, 'kkk': 1}
        self.t = "на складе"
        self.f = "со склада"

