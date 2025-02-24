
class PrettyPrint:

    def __str__(self):
        return f'{self.__class__.__name__}({", ".join([f"{i}={self.__dict__[i]}" for i in self.__dict__])})'


class Person(PrettyPrint):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


artem = Person('Artem', 'Egorov', 33)
ivan = Person('Ivan', 'Ivanov', 45)
print(artem)
print(ivan)