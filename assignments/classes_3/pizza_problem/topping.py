class Topping:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __str__(self):
        return self.__name

    def get_price(self):
        return self.__price
