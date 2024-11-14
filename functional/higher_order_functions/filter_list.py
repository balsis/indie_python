def filter_list(f, lst):
    return [i for i in lst if f(i)]


def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_list(is_even, numbers) # берем только четные
print(even_numbers)