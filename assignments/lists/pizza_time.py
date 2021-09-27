TOPPING_NAME = 0
TOPPING_PRICE = 1

BASE_PRICE = 1500


def main():
    toppings = []
    PROMPT = "Would you like to add a topping(y/n)?: "
    while input(PROMPT).lower() != "n":
        add_topping(toppings)
    display_order(toppings)


def add_topping(toppings):
    topping_name = input("What topping would you like to add?: ")
    price_of_topping = int(input("What is the price of the topping?: "))
    toppings.append([topping_name, price_of_topping])


def display_order(toppings):
    pizza_price = BASE_PRICE + sum_of_toppings(toppings)
    topping_str = get_topping_str(toppings)
    if toppings:
        print(f"Pizza with {topping_str} | price: {pizza_price}")
    else:
        print(f"Pizza with no toppings | price: {BASE_PRICE}")


def sum_of_toppings(toppings):
    sum_of_toppings = 0
    for topping in toppings:
        sum_of_toppings += topping[TOPPING_PRICE]
    return sum_of_toppings


def get_topping_str(toppings):
    topping_str = ""
    for topping in toppings:
        topping_str += topping[TOPPING_NAME] + ", "
    return topping_str[:-2]


if __name__ == "__main__":
    main()
