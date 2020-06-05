from abc import ABC
from math import sqrt, e


class Function(ABC):
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def calculate(self):
        raise NotImplementedError


class Type1(Function):

    def calculate(self):
        return self.x ** 2 + sqrt(3 * (self.y ** 3))


class Type2(Function):

    def calculate(self):
        return (3 * self.x ** 2) * (self.z ** (1. / 3)) + e ** (sqrt(4 * self.y))


option = input("Enter the type of calculation (1 or 2) you'd like to perform: ")
if option == "1":
    x, y = input("Enter x y: ").split()
    val = Type1(float(x), float(y))
    print(val.calculate())

elif option == "2":
    x, y, z = input("Enter x y z: ").split()
    val = Type2(float(x), float(y), float(z))
    print(val.calculate())

else:
    raise ValueError
