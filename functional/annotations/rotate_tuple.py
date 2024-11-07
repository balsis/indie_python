from __future__ import annotations

from typing import Tuple, Any


def rotate(tpl: tuple[int | float, ...], shift: int = 1) -> tuple[int | float, ...]:
    "Функция выполняет циклический сдвиг кортежа на shift позиций вправо (shift>0) или влево (shift<0)"
    shift = shift % len(tpl)
    if shift == 0:  # Если сдвиг равен 0, возвращаем оригинальный список
        return tpl
    return tuple(tpl[-shift:] + tpl[:len(tpl) - shift])


print(rotate((1, 2, 3, 4, 5, 6, 7), 2))
