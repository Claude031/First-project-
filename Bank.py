from person import Person
class Bank:
    BANK_FEE = 0.05
    # lista kont


class BankAccount:

    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"{self.owner} {self.account_number} {self.balance}"

    @property
    def current_balance(self):
        return f"Current balance is: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return self.current_balance

    def withdraw(self, amount):
        if amount > self.balance:
            return f"No sufficient funds on the account. {self.current_balance}"
        self.balance -= amount
        return self.current_balance

    def bank_fees(self):
        self.balance *= 0.95
        return self.current_balance


if __name__ == '__main__':
    adas = Person("Adaś", "Miałczyński", 111111111)
    b = BankAccount(123, adas, 100)
    print(b.current_balance)
    print(b.deposit(500))
    print(b.withdraw(1000))
    print(b.withdraw(250))
    print(b.bank_fees())
