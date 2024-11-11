def print_results(lst):
    temp_list = sorted(lst, key = lambda x: x[0].upper(), reverse = True)
    [print(*i) for i in sorted(temp_list, key = lambda x: -x[1])]


marks = [('english', 100), ('Science', 100), ('maths', 100),
         ('Physics', 100), ('history', 100), ('Music', 100)]
print_results(marks)

