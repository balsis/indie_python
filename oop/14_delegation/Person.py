# Напишите определение классов Person и Employee
class Person:
    def __init__(self, name, passport):
        self.name = name
        self.passport = passport

    def display(self):
        print(f'{self.name}: {self.passport}')


class Employee(Person):
    def __init__(self, name, passport, salary, department):
        super().__init__(name, passport)
        self.salary = salary
        self.department = department

# Ниже располагается код для проверки

assert issubclass(Employee, Person)

emp = Person("just human", 123456)
emp.display()
assert emp.__dict__ == {'name': 'just human', 'passport': 123456}

emp2 = Employee("Geek2", 534432, 321321, 'Roga & Koputa')
emp2.display()
assert emp2.__dict__ == {'salary': 321321, 'department': 'Roga & Koputa',
                         'name': 'Geek2', 'passport': 534432}
