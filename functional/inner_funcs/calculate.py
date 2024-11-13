def calculate(x, y, operation="a"):
    def addition(x, y):
        return (x + y)

    def subtraction(x, y):
        return (x - y)

    def division(x, y):
        return (x / y if y != 0 else "На ноль делить нельзя!")

    def multiplication(x, y):
        return (x * y)

    operations = {
        'a': addition(x, y),
        's': subtraction(x, y),
        'd': division(x, y),
        'm': multiplication(x, y)
    }

    print(operations.get(operation, "Ошибка. Данной операции не существует"))


calculate(10, 4, 's')
calculate(10, 0, 'd')
calculate(10, 4, 'w')
calculate(1, 2, 'a')
calculate(3, 1, 'd')
