def filter_collection(f, collection):
    if isinstance(collection, list):
        return [i for i in collection if f(i)]
    elif isinstance(collection, tuple):
        return tuple([i for i in collection if f(i)])
    else:
        return "".join([i for i in collection if f(i)])


def is_even(num):
    return num % 2 == 0

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_numbers = filter_collection(is_even, numbers)
print(even_numbers)