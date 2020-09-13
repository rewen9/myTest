from abc import ABC
from abc import abstractmethod


class Shape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        print('calc perim')

    def drag(self):
        print('Basic dragging')


from math import sqrt


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.c = c
        self.b = b

    def draw(self):
        print(f'Drawing triangle with sides= {self.a}')

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * 2)

    def perimeter(self):
        return self.a + self.b + self.c

    def drag(self):
        super().drag()
        print('triangle drag')



ex_triangle = Triangle(2,3,4)
print(ex_triangle.drag())