subject_marks = [('English', 88),
                 ('Science', 90),
                 ('Maths', 97),
                 ('Physics', 93),
                 ('History', 82)]

subject_marks = sorted(subject_marks, key=lambda x: x[1])
for i in subject_marks:
    print(*i, sep=' ')
