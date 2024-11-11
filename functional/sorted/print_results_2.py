def print_results(lst):
    [print(*i) for i in sorted(lst, key = lambda x: x[1], reverse=True)]


marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93), ('History', 82)]
print_results(marks)
