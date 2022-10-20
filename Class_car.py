class Car:

    def __init__(self, brand, model, colour='red', year=2022):
        self._brand = brand
        self.model = model
        self.colour = colour
        self.year = year

    def show_details(self):
        return f"{self._brand} {self.model} {self.colour} {self.year}"

    def honk(self):
        return 'tekst'

if __name__ == '__main__':

    a = Car('mercedes', 'model')
    b = Car('seat', 'ibiza', 'green', 2019)

    print(a.show_details())
    print(b.show_details())
    b.year = 1990
    print(a.show_details())
    print(b.show_details())

