class Request:
    FROM = None
    TO = None
    AMOUNT = None
    PRODUCT = None

    def __init__(self, list_classes: list, user_input: str):
        self.combined_list_with_data = self.get_list_for_reading_the_places_of_sending_and_receiving(list_classes)
        self.str_user_input = user_input
        self.FROM = self._get_object_for_navigation_to_end_from(self.combined_list_with_data[0])
        self.TO = self._get_object_for_navigation_to_end_from(self.combined_list_with_data[1])
        self.list_all = self.get_full_products_to_end_from_ojects()
        self.AMOUNT = self._get_int()
        self.PRODUCT = self._get_product_in_str_from_lists_objects()

    def get_full_attributes(self):
        return [self.FROM, self.TO, self.PRODUCT, self.AMOUNT]

    def get_full_products_to_end_from_ojects(self) -> list:
        if None in [self.FROM, self.TO]:
            return []
        return self.TO.get_unique_items_count() + self.FROM.get_unique_items_count()

    def _get_object_for_navigation_to_end_from(self, ab) -> object:
        for i in ab:
            if i in self.str_user_input:
                return ab[i]

    def _get_product_in_str_from_lists_objects(self) -> str:
        for i in self.list_all:
            if i in self.str_user_input:
                return i

    def _get_int(self) -> int:
        a = self.str_user_input.split(" ")
        for i in a:
            if i.isdigit():
                return int(i)

    def get_list_for_reading_the_places_of_sending_and_receiving(self, places_of_sending_and_receiving: list):
        list_for_reading_the_places_of_sending_and_receiving = [{}, {}]
        for i in places_of_sending_and_receiving:
            for ii in range(2):
                list_for_reading_the_places_of_sending_and_receiving[ii].update(i.words_to_read[ii])
        return list_for_reading_the_places_of_sending_and_receiving
