from typing import List


def count_leap_years(year1: int, year2: int) -> int:
    return len([year for year in range(year1, year2) if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0])



print(count_leap_years(2000, 2018))
print(count_leap_years(2015, 2020))
print(count_leap_years(1990, 2021))
print(count_leap_years(1890, 2021))
print(count_leap_years(2021, 2021))
