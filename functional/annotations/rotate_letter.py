def rotate_letter(letter:str, shift: int) -> str:
    "Функция сдвигает символ letter на shift позиций"
    if shift > 26:
        shift %=  26
    letters = 'abcdefghijklmnopqrstuvwxyz'
    index = letters.index(letter) + shift
    if index> 26:
        index %= 26
    return letters[index]


# rotate_letter('b', 2)=> 'd'
# rotate_letter('d', 1) => 'e'
# rotate_letter('z', 1) => 'a'
# rotate_letter('d', -2) => 'b'
# rotate_letter('d', 26) => 'd'
# rotate_letter('b', -3) => 'y'

print(rotate_letter('a', 3))
print(rotate_letter('d', -2))
print(rotate_letter('w', -26))
print(rotate_letter('w', -27))
print(rotate_letter('a', 53))
print(rotate_letter('z', 5))
