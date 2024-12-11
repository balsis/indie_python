def my_recursive_func(value):
    if len(value) <= 3:
        print(value)
        my_recursive_func(value + '*')


my_recursive_func('*')
