class Vector2D:
    def __init__(self, x=0, y=0):
        self.vector = [x, y]

    def __str__(self):
        return f"|{self.vector[0]}|\n|{self.vector[1]}|\n"

    def add(self, other):
        for i in range(len(self.vector)):
            self.vector[i] += other.vector[i]

    def subtract(self, other):
        for i in range(len(self.vector)):
            self.vector[i] -= other.vector[i]

    def scale(self, scalar):
        self.vector = [i * scalar for i in self.vector]
