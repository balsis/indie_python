class Employee:
    def __init__(self, name, base_pay, bonus):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus

    def get_pay(self):
        return self.base_pay + self.bonus


class SalesEmployee(Employee):
    def __init__(self, name, base_pay, bonus, sales_incentive):
        super().__init__(name, base_pay, bonus)
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return super().get_pay() + self.sales_incentive


jack = Employee('Jack', 5000, 1000)
assert jack.name == 'Jack'
assert jack.base_pay == 5000
assert jack.bonus == 1000
assert jack.get_pay() == 6000

john = SalesEmployee('John', 5000, 1000, 2000)
assert john.name == 'John'
assert john.base_pay == 5000
assert john.bonus == 1000
assert john.sales_incentive == 2000
assert john.get_pay() == 8000

print('Good')
