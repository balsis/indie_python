def get_info_marks(students, *marks):
    max_mark = list(map(max, zip(*marks)))
    min_mark = list(map(min, zip(*marks)))
    dct = {}
    for i in range(len(students)):
        dct[students[i]] = {"best": max_mark[i], "worst": min_mark[i]}
    return dct



math = [90, 76, 94]
history = [78, 79, 90]
students = ["Marie", "Michael", "Marge"]
print(get_info_marks(students, math, history))


