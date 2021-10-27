class BackpackItem:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def __repr__(self):
        return f"BackpackItem({self.name}, {self.size})"
