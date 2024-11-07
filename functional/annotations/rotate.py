from __future__ import annotations


def rotate(lst: list[int | float], shift: int = 1) -> list[int | float]:
    "Функция выполняет циклический сдвиг списка на shift позиций вправо(shift>0) или влево(shift<0)"
    shift = shift % len(lst)
    if shift == 0:  # Если сдвиг равен 0, возвращаем оригинальный список
        return lst
    return lst[-shift:] + lst[:len(lst) - shift]


print(rotate([1, 2, 3, 4, 5, 6], 2))
print(rotate([1, 2, 3, 4, 5, 6], -3))
print(rotate([1, 2, 3, 4, 5, 6, 7], 21))
