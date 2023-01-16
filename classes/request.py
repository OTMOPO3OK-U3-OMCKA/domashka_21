class Request:
    FROM = None
    TO = None
    AMOUNT = None
    PRODUCT = None

    def __init__(self, ab: list, a: str):
        self.ab = self.hhh(ab)
        self.a = a
        self.FROM = self._get_ab(self.ab[0])
        self.TO = self._get_ab(self.ab[1])
        self.list_all = self.ret2()
        self.AMOUNT = self._get_int()
        self.PRODUCT = self._get_c()

    def ret(self):
        return [self.FROM, self.TO, self.PRODUCT, self.AMOUNT]

    def ret2(self) -> list:
        if None in [self.FROM, self.TO]:
            return []
        return self.TO.get_unique_items_count() + self.FROM.get_unique_items_count()

    def _get_ab(self, ab) -> object:
        for i in ab:
            if i in self.a:
                return ab[i]

    def _get_c(self) -> str:
        for i in self.list_all:
            if i in self.a:
                return i

    def _get_int(self) -> int:
        a = self.a.split(" ")
        for i in a:
            if i.isdigit():
                return int(i)

    def hhh(self, l: list):
        ww = [{}, {}]
        for i in l:
            for ii in range(2):
                ww[ii].update(i.p[ii])
        return ww
