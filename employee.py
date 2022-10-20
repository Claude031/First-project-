class Employee:

    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def show_details(self):
        return f'Employee name: {self.name} {self.surname} and salary is {self.salary} '


class Developer(Employee):

    def __init__(self, name, surname, salary, language):
        super().__init__(name, surname, salary)
        self.language = language

    def show_details(self):
        return super().show_details() + f'Language:{self.language}'


class MyManager(Employee):

    def __init__(self, name, surname, salary, team):
        super().__init__(name, surname, salary)
        self.team = team

    def show_details(self):
        return super().show_details() + f'Team:{self.team}'


if __name__ == '__main__':

    emp = Employee('Anna', 'Koto', 100)
    print(emp.show_details())

    emp_developer = Developer(emp.name, emp.surname, emp.salary, 'Python')
    print(emp_developer.show_details())

    my_man = MyManager(emp.name, emp.surname, emp.salary, 'it')
    print(my_man.show_details())