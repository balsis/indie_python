class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name


class Father:
    def __init__(self, father_name):
        self.father_name = father_name


class Child(Mother, Father):
    def __init__(self, child_name, mother_name, father_name):
        super().__init__(mother_name)
        Father.father_name = father_name
        self.child_name = child_name

    def introduce(self):
        return f"Меня зовут {self.child_name}. Моя мама - {self.mother_name}, мой папа - {self.father_name}"


child = Child("Анна", "Мария", "Иван")
print(child.introduce())