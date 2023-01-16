from classes.shop import Shop
from classes.store import Store
from classes.request import Request

sh = Shop()
st = Store()
ll = [sh, st]


s = None
while s != "выход":
    s = input("Курьер: ")
    request = Request(ll, s)
    if None in request.ret():
        print("заказ не принят")
    elif request.FROM.check_r(request.PRODUCT, request.AMOUNT) is False:
        pass
    elif request.TO.check_a(request.PRODUCT, request.AMOUNT) is False:
        pass
    else:
        request.FROM.get_remove_and_check(request.PRODUCT, request.AMOUNT)
        request.TO.get_add_and_check(request.PRODUCT, request.AMOUNT)
        print(f"Курьер забрал {request.AMOUNT} {request.PRODUCT} {request.FROM.f}")
        print(f"Курьер везет {request.AMOUNT} {request.PRODUCT} {request.FROM.f} {request.TO.t[:-1]}")
        print(f"Курьер доставил {request.AMOUNT} {request.PRODUCT} {request.TO.t[:-1]}")
        request.FROM.get_items()
        request.TO.get_items()
        request.FROM.get_free_space()
        request.TO.get_free_space()
