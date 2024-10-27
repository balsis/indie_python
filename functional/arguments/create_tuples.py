def create_tuples(lst1, lst2):
    return [(i, j) for i, j in zip(lst1, lst2)]


print(create_tuples([1, 2, 3, 4], [5, 6, 7, 8]))
