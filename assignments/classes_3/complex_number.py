class ComplexNumber:
    def __init__(self, real_part=0, complex_part=0):
        self.real_part = real_part
        self.complex_part = complex_part

    def __str__(self):
        number_str = ""
        prefix = ""
        if self.real_part != 0:
            number_str += str(self.real_part)
            prefix = '-' if self.complex_part < 0 else "+"
        number_str += f"{prefix}{abs(self.complex_part)}i" if self.real_part != 0 else f"{self.complex_part}i"
        return number_str

    def __add__(self, other):
        return ComplexNumber(self.real_part + other.real_part, self.complex_part + other.complex_part)

    def __sub__(self, other):
        return ComplexNumber(self.real_part - other.real_part, self.complex_part - other.complex_part)
    
    def __mul__(self, other):
        return ComplexNumber(self.real_part*other.real_part - self.complex_part*other.complex_part,
                             self.real_part*other.complex_part + self.complex_part*other.real_part)
