def find_keys(**kwargs):
    temp_list = [k for k, v in kwargs.items() if isinstance(v, (list, tuple))]
    return sorted(temp_list, key = lambda x: x.upper())


print(find_keys(marks=[4, 5], name='Ashle', surname='Brown', age=20, Also=(1, 2)))
print(find_keys(t=[4, 5], w=[5, 3], A=(3, 2), a={2, 3}, b=[4]))
print(find_keys(marks=[4, 5], ashle=[5], surname='Brown', age=20, Also=(1, 2)))
print(find_keys(At=[4], awaited=(3,), aDobe=[5]))
