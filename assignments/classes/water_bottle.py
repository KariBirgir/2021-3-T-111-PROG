class WaterBottle:
    def __init__(self, max_capacity=2):
        self.max_capacity = max_capacity
        self.volume = 0

    def __str__(self):
        return f"{self.volume:.1f}L"

    def fill(self):
        self.volume = self.max_capacity

    def drink(self, amount):
        if amount <= 0:
            return
        if amount > self.volume:
            self.volume = 0
        else:
            self.volume -= amount
