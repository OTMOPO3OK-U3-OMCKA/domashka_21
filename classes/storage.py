class Storage():
    capacity = 100
    dd = None

    def __init__(self):
        self.items = {}
        self.t = "на объекте"

    def check_r(self, x, y):
        if self.items.get(x) is None:
            print(f"этого товара нет в наличии {self.t}")
            return False
        if type(y) is not int:
            print("количество товара введено неверно")
            return False
        if self.items.get(x) < y:
            print(f"Не хватает {self.t}, попробуйте заказать меньше")
            return False
        return True

    def check_a(self, x, y):
        if type(x) is not str:
            print("недопустимый товар")
            return False
        if type(y) is not int:
            print("количество товара введено неверно")
            return False
        if sum(self.items.values(), y) > self.capacity:
            print(f"{self.t} недостаточно места, попробуйте меньше")
            return False
        if self.dd is not None:
            if len(self.items.keys()) >= self.dd:
                print(f"{self.t} недостаточно места, попробуйте другой товар")
                return False
        return True

    def _add(self, x, y):
        if self.items.get(x) is None:
            self.items[x] = y
        else:
            self.items[x] += y

    def _remove(self, x, y):
        self.items[x] -= y
        if self.items.get(x) == 0:
            self.items.pop(x)
        print(f"нужное количество есть {self.t}")

    def get_free_space(self):
        c = self.capacity - sum(self.items.values())
        print(f"{self.t} {c} свободных мест")

    def get_items(self):
        if len(self.items) == 0:
            print(f"{self.t} нет товара")
        else:
            print(f"{self.t} хранится:")
            for i, v in self.items.items():
                print(f"{v} {i}")

    def get_unique_items_count(self):
        t = []
        for i in self.items.keys():
            t.append(i)
        return t

    def get_add_and_check(self, x, y):
        if self.check_a(x, y):
            self._add(x, y)

    def get_remove_and_check(self, x, y):
        if self.check_r(x, y):
            self._remove(x, y)