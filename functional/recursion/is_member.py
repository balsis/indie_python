def is_member2(value, lst):
    return value in lst


def is_member(value, lst):
    if len(lst) == 1:
        return value in lst
    elif lst[0] == value:
        return True
    else:
        return is_member(value, lst[1:])

assert is_member("e", ['a', 'e', 'i', 'o', 'u']) is True
assert is_member(10, [1, 23, 3, 43, 10, 35]) is True
assert is_member('might', ['or', 'maybe', 'this']) is False
print('Проверки пройдены, вы - молодец!')