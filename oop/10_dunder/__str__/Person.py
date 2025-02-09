class Person:
    def __init__(self, name, surname, gender="male"):
        self.name = name
        self.surname = surname
        self.gender = gender

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if value not in ['male', 'female']:
            print('Не знаю, что вы имели в виду? Пусть это будет мальчик!')
            self._gender = 'male'
        else:
            self._gender = value

    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        else:
            return f'Гражданка {self.surname} {self.name}'

p1 = Person('Chuck', 'Norris')
print(p1) # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2) # печатает "Гражданка Kunis Mila"
p3 = Person('Оби-Ван', 'Кеноби', True)# печатает "Не знаю, что вы имели в виду? Пусть это будет мальчик!"
print(p3) # печатает "Гражданин Кеноби Оби-Ван"