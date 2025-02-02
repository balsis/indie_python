class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_str(cls, value: str):
        day, month, year = map(int, (value.split('-')))
        return cls(day, month, year)


day_1 = Date.from_str('12-4-2024')
day_2 = Date.from_str('06-09-2022')
print(day_1.day, day_1.month, day_1.year)
print(day_2.day, day_2.month, day_2.year)
