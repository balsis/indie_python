def shift_letter(letter : str, shift: int):
    'Функция сдвигает символ letter на shift позиций'
    ind = ord(letter)
    a =  ind + shift
    if shift > 26:
        shift = shift % 26
    while a > 122:
        a = a - 26
    if a < 97:
        a = a + 26
    return chr(a)

print(shift_letter('a', 53))
assert shift_letter('b', 2) == 'd'
assert shift_letter('d', 1) == 'e'
assert shift_letter('z', 1) == 'a'
assert shift_letter('d', -2) == 'b'
assert shift_letter('d', 26) == 'd'
assert shift_letter('b', -3) == 'y'
assert shift_letter('z', 5) == 'e'
assert shift_letter('w', 28) == 'y'
assert shift_letter('w', -26) == 'w'
assert shift_letter('w', -27) == 'v'
assert shift_letter('a', 53) == 'b'