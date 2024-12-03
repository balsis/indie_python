def get_info_marks(students, *marks):
    max_marks = list(map(max, zip(*marks)))
    return dict(zip(students,  max_marks))


math = [90, 76, 94]
history = [78, 79, 90]
students = ["Marie", "Michael", "Marge"]
print(get_info_marks(students,math, history))


