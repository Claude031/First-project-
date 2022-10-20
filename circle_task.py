import math


class Circle:

    def __init__(self, a, b, r):
        self.center = (a, b)
        self.radius = r

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def test_belongs(self, x, y):

        if ((x - self.center[0])**2) + (y - self.center[1])**2 == self.radius**2:
            return f'Point {x, y} is belongs to the circle C {self.center[0], self.center[1]}'

        if ((x - self.center[0])**2) + (y - self.center[1])**2 != self.radius**2:
            return f'Point {x, y} is not belongs to the circle C {self.center[0], self.center[1]}'

if __name__ == '__main__':

    circ = Circle(5, 4, 5)

    print(circ.area())
    print(circ.perimeter())
    print(circ.test_belongs(4,2))





