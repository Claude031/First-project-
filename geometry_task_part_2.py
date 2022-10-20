import math


class Geometry:

    @classmethod
    def distance(cls, xa, ya, xb, yb):
        return f'distance between two points A = {xa, ya}, B = {xb, yb} is {math.sqrt((xb - xa)**2 + (yb - ya)**2)}'

    @classmethod
    def middle(cls, xa, ya, xb, yb):
        return f'Middle of bi-point (A,B) with coordinates {xa,ya} and {xb, yb} is point {(xa + xb) / 2, (ya + yb) / 2}'

    @classmethod
    def triangle_perimeter(cls, xa, ya, xb, yb, xc, yc):

        odcinek_AB = math.sqrt(((xb - xa) ** 2) + (yb - ya) ** 2)
        odcinek_BC = math.sqrt(((xc - xb)**2) + (yc - yb)**2)
        odcinek_CA = math.sqrt(((xa - xc)**2) + (ya - yc)**2)

        return f'the perimeter of triangle basing on points (A,B,C) with coordinates {xa,ya} , {xb, yb} and {xc,yc} is '\
               f'{odcinek_AB + odcinek_BC + odcinek_CA }'

    @classmethod
    def triangle_isosceles(cls, xa, ya, xb, yb, xc, yc):

        odcinek_AB = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
        odcinek_BC = math.sqrt((xc - xb) ** 2 + (yc - yb) ** 2)
        odcinek_CA = math.sqrt((xa - xc) ** 2 + (ya - yc) ** 2)
        odcinek_CB = math.sqrt((xb - xc) ** 2 + (yb - yc) ** 2)

        if odcinek_AB == odcinek_BC:
            return True
        elif odcinek_CA == odcinek_AB:
            return True
        elif odcinek_CA == odcinek_CB:
            return True
        elif odcinek_CA == odcinek_AB == odcinek_BC:
            return True
        else:
            return False


if __name__ == '__main__':

    geo = Geometry
    print(geo.distance(5,4,2,1))
    print(geo.middle(5,4,2,1))
    print(geo.triangle_perimeter(5,5,4,-1,5,4))
    print(geo.triangle_isosceles(0,1,1,0,0,0))
