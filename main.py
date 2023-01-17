from classes.shop import Shop
from classes.store import Store
from classes.request import Request

shoper_class = Shop()
store_class = Store()
list_classes = [shoper_class, store_class]


user_input = None
while user_input != "выход":
    user_input = input("Курьер: ")
    request = Request(list_classes, user_input)
    if None in request.get_full_attributes():
        print("заказ не принят")
    elif request.FROM.check_availability_prod(request.PRODUCT, request.AMOUNT) is False:
        pass
    elif request.TO.checking_entry_product(request.PRODUCT, request.AMOUNT) is False:
        pass
    else:
        request.FROM.get_remove_and_check(request.PRODUCT, request.AMOUNT)
        request.TO.get_add_and_check(request.PRODUCT, request.AMOUNT)
        print(f"Курьер забрал {request.AMOUNT} {request.PRODUCT} {request.FROM.from_place}")
        print(f"Курьер везет {request.AMOUNT} {request.PRODUCT} {request.FROM.from_place} {request.TO.to_place[:-1]}")
        print(f"Курьер доставил {request.AMOUNT} {request.PRODUCT} {request.TO.to_place[:-1]}")
        request.FROM.get_items()
        request.TO.get_items()
        request.FROM.get_free_space()
        request.TO.get_free_space()
