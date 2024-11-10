is_leap = lambda year: (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(is_leap(1900))
print(is_leap.__name__)