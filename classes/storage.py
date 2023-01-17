class Storage():
    capacity = 100
    limit = None

    def __init__(self):
        self.items = {}
        self.to_place = "на объекте"
        self.from_place = "с объекта"
        self.words_to_read = [{}, {}]

    def check_availability_prod(self, product, count):
        if self.items.get(product) is None:
            print(f"этого товара нет в наличии {self.to_place}")
            return False
        if type(count) is not int:
            print("количество товара введено неверно")
            return False
        if self.items.get(product) < count:
            print(f"Не хватает {self.to_place}, попробуйте заказать меньше")
            return False
        return True

    def checking_entry_product(self, product, count):
        if type(product) is not str:
            print("недопустимый товар")
            return False
        if type(count) is not int:
            print("количество товара введено неверно")
            return False
        if sum(self.items.values(), count) > self.capacity:
            print(f"{self.to_place} недостаточно места, попробуйте меньше")
            return False
        if self.limit is not None:
            if len(self.items.keys()) >= self.limit:
                print(f"{self.to_place} недостаточно места, попробуйте другой товар")
                return False
        return True

    def _add(self, product, count):
        if self.items.get(product) is None:
            self.items[product] = count
        else:
            self.items[product] += count

    def _remove(self, product, count):
        self.items[product] -= count
        if self.items.get(product) == 0:
            self.items.pop(product)
        print(f"нужное количество есть {self.to_place}")

    def get_free_space(self):
        c = self.capacity - sum(self.items.values())
        print(f"{self.to_place} {c} свободных мест")

    def get_items(self):
        if len(self.items) == 0:
            print(f"{self.to_place} нет товара")
        else:
            print(f"{self.to_place} хранится:")
            for i, v in self.items.items():
                print(f"{v} {i}")

    def get_unique_items_count(self):
        product_list = []
        for i in self.items.keys():
            product_list.append(i)
        return product_list

    def get_add_and_check(self, product, count):
        if self.checking_entry_product(product, count):
            self._add(product, count)

    def get_remove_and_check(self, product, count):
        if self.check_availability_prod(product, count):
            self._remove(product, count)