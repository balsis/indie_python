def print_results(lst):
    [print(*i) for i in sorted(lst, key = lambda x: (-x[1], x[0].upper()))]


marks = [('English', 88), ('Science', 90), ('Maths', 88),
         ('Physics', 93), ('History', 78), ('French', 78),
         ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
print_results(marks)

print("_" * 20)

marks = [('english', 100), ('Science', 100), ('maths', 100),
         ('Physics', 100), ('history', 100), ('Music', 100)]
print_results(marks)