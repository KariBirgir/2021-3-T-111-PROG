from backpack_item import BackpackItem

class Backpack:
    def __init__(self, max_capacity = 10):
        self.max_capacity = max_capacity
        self.current_capacity = 0
        self.__contents = []

    def add(self, item: BackpackItem):
        if self.current_capacity + item.size > self.max_capacity:
            print("Maximum capacity would be exceeded!")
        else:
            self.__contents.append(item)
            self.current_capacity += item.size

    def __repr__(self):
        return f"Backpack({self.current_capacity}/{self.max_capacity})"
    
    def __str__(self):
        return f"{repr(self)}: {self.__contents}"
