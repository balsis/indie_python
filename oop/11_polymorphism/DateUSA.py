class DateEurope:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def format(self):
        return f'{self.day:02}/{self.month:02}/{self.year:04}'

    def isoformat(self):
        return f'{self.year:04}-{self.month:02}-{self.day:02}'


class DateUSA:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def format(self):
        return f'{self.month:02}/{self.day:02}/{self.year:04}'

    def isoformat(self):
        return f'{self.year:04}-{self.month:02}-{self.day:02}'


d = DateEurope(5, 12, 2001)
print(d.format())
print(d.isoformat())


d = DateUSA(1, 5, 890)
print(d.format())
print(d.isoformat())