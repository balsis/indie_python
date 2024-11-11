def get_sort_lines(lst):
    return sorted(lst, key = lambda x: (abs(x[1]-x[0]), x[0], x[1]))


lines = [(5, 6), (5, 4), (1, 0), (0, -1), (1, 2), (2, 1)]
print(get_sort_lines(lines))