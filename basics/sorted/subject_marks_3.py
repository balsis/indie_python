subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
                 ('Physics', 93), ('History', 78), ('French', 78),
                 ('Art', 78), ('Chemistry', 88), ('Programming', 91)]

subject_marks = sorted(subject_marks, key=lambda x: (-x[1], x[0]))
for i in subject_marks:
    print(*i, sep=' ')