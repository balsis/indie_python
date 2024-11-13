def count_strings(*args):
    return len([i for i in args if isinstance(i, str)])


print(count_strings(1, 2, 'hello', True, 't'))
print(count_strings('1', '2', 'hello', True, 't'))
print(count_strings())
