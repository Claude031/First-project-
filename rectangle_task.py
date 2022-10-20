import math

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def diagonal(self):
        return math.sqrt(self.length **2 + self.width**2)

    def display(self):
        return f'length:{self.length}, ' \
               f'width:{self.width}, '\
               f'perimeter: {self.perimeter()}, ' \
               f'area: {self.area()}, ' \
               f'diagonal: {self.diagonal()} '


class Cuboid(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.area() * self.height


if __name__ == '__main__':

    rec = Rectangle(3, 4)

    print(rec.perimeter())
    print(rec.area())
    print(rec.diagonal())
    print(rec.display())

    cub = Cuboid(10, 15, 5)

    print(cub.volume())

