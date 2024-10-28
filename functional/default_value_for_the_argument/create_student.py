def create_student(name, age, marks=[]):
    return {
        'name': name,
        'age': age,
        'marks': marks  # оценки
    }


def add_mark(student, mark):
    student['marks'].append(mark)


ivan = create_student('Ivan', 15)
anatoliy = create_student('Anatoliy', 16)

add_mark(ivan, 5)
add_mark(ivan, 5)
add_mark(anatoliy, 3)
print(add_mark(anatoliy, 4))