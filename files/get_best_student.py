def get_best_student(filename):
    file = open(filename)
    text = file.readlines()
    best_student, max_score = None, 0
    for i in text:
        student, score = i.split(":")
        if int(score) >= max_score:
            max_score = int(score)
            best_student = student

    surname, name = best_student.split()
    best_student = name + " " + surname
    return best_student


print(get_best_student("students.txt"))
