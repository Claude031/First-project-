class Calculator:

    def add(self, a, b):
        return a + b

    def substract(self, a, b):
        return a - b

    def divide(self, a, b):
        return a / b

    def multiply(self, a, b):
        return a * b


if __name__ == '__main__':
    calculator = Calculator()
    print(calculator.add(2, 7))
    print(calculator.substract(10, 5))
    print(calculator.multiply(2, 30))
    print(calculator.divide(99, 30))