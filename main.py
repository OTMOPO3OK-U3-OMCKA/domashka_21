from classes.shop import Shop
from classes.store import Store
from classes.request import Request

sh = Shop()
st = Store()
ab = [{"из склад": st, "со склад": st, "из магазин": sh, "c магазин": sh},
      {"в склад": st, "на склад": st, "в магазин": sh}]
# переменная < ab > содержит адресации откуда и куда для поиска в строке,
# в случае добавления других пунктов назначения и отправки(то есть создание др классов: ларёк, гипермаркет, рынок и др)
# нужно добавить в словари переменной теги поиска пунктов. Пример: rn = Rinok()
# ab = [{"из склад": st, "со склад": st, "из магазин": sh, "c магазин": sh},     + "с рынка": rn, "из рынка": rn
#       {"в склад": st, "на склад": st, "в магазин": sh}]                        + "на рынок": rn, "в рынок": rn

s = None
while s != "выход":
    s = input("Курьер: ")
    rr = Request(ab, s)
    if None in rr.ret():
        print("заказ не принят")
    elif rr.FROM.check_r(rr.PRODUCT, rr.AMOUNT) is False:
        pass
    elif rr.TO.check_a(rr.PRODUCT, rr.AMOUNT) is False:
        pass
    else:
        rr.FROM.get_remove_and_check(rr.PRODUCT, rr.AMOUNT)
        rr.TO.get_add_and_check(rr.PRODUCT, rr.AMOUNT)
        print(f"Курьер забрал {rr.AMOUNT} {rr.PRODUCT} {rr.FROM.f}")
        print(f"Курьер везет {rr.AMOUNT} {rr.PRODUCT} {rr.FROM.f} {rr.TO.t[:-1]}")
        print(f"Курьер доставил {rr.AMOUNT} {rr.PRODUCT} {rr.TO.t[:-1]}")
        rr.FROM.get_items()
        rr.TO.get_items()
        rr.FROM.get_free_space()
        rr.TO.get_free_space()
