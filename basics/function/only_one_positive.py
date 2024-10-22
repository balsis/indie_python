def only_one_positive(*args):
    count = 0
    lst = [i for i in args if i > 0]
    print('True') if len(lst) == 1 else print('False')

assert only_one_positive(1, 2) is False
assert only_one_positive(-1, 0, -3, 5, -3) is True
assert only_one_positive() is False