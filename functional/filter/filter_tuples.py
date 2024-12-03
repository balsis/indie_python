def filter_tuples(tuples):
    return tuple(filter(lambda x: x[0] * x[1] * x[2] == 60,numbers))

numbers = (
    (1, 2, 3), (1, 2, 30),
    (1, 20, 3), (15, 2, 3),
    (10, 2, 3), (10, 20, 30),
)
print(filter_tuples(numbers))
