class Square:
    def __init__(self, side=1):
        self.__side = side if side > 0 else 1
        
    def __str__(self):
        return "Side length: {}".format(self.__side)

    def __repr__(self):
        return "Square({})".format(self.__side)

    def __eq__(self, other):
        # you can either compare the areas or the sides, the sides is simpler so we go with that.
        # usually we cant access private members (that use the prefix __), but as we are inside a member method of the class that "other" is an instance of, it works.
        return self.__side == other.__side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return self.__side * 4