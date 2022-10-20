import math


class Geometry:

    @staticmethod
    def distance(a, b):
        xa, ya = a
        xb, yb = b
        return math.sqrt((xa - xb)**2 + (ya - yb)**2)

    @staticmethod
    def middle(a, b):
        middle_x = (a[0]+b[0])/2
        middle_y = (a[1]+b[1])/2
        return middle_x, middle_y

    @classmethod
    def triangle_perimeter(cls, a, b, c):
        return cls.distance(a, b) + cls.distance(b, c) + cls.distance(a, c)

    @classmethod
    def triangle_isoceles(cls, a, b, c):
        ab = cls.distance(a, b)
        bc = cls.distance(b, c)
        ac = cls.distance(a, c)
        return ab == bc or bc == ac or ab == ac


class Point:
    pass


class Triangle:
    pass


if __name__ == '__main__':
    a = (0, 0)
    b = (5, 5)
    c = (0, 5)
    print(Geometry.distance(a, b))
    print(Geometry.middle(a, b))
    print(Geometry.triangle_perimeter(a, b, c))
    print(Geometry.triangle_isoceles(a, b, c))