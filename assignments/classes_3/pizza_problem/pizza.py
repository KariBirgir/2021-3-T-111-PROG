from topping import Topping

class Pizza:
    def __init__(self, name="Unnamed", size="large", toppings=None):
        self.__name = name
        self.__price_dict = {"small" : 800, "medium":1200, "large":1500}
        if size in self.__price_dict:
            self.__size = size
        else:
            raise ValueError("Invalid size of pizza")
        # You should call the function, incase the function validates each topping in the list in the future, although in this problem, it does not matter
        self.__toppings = []
        if toppings is not None:
            self.add_toppings(toppings)
    
    def __str__(self):
        pizza_str = f"{self.__size.capitalize()} {self.__name} pizza with "
        if self.__toppings:
            pizza_str += ", ".join([str(topping) for topping in self.__toppings])
        else:
            pizza_str += "nothing"
        return pizza_str

    def add_topping(self, topping):
        self.__toppings.append(topping)
    
    def add_toppings(self, toppings):
        for topping in toppings:
            self.add_topping(topping)

    def get_price(self):
        price = self.__price_dict[self.__size]
        for topping in self.__toppings:
            price += topping.get_price()
        return price