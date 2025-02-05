class File:
    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        print(f'Файл {self.name} восстановлен из корзины')
        self.in_trash = False

    def remove(self):
        print(f'Файл {self.name} был удален')
        self.is_deleted = True

    def read(self):
        if self.is_deleted:
            print(f'ErrorReadFileDeleted({self.name})')
        elif self.in_trash:
            print(f'ErrorReadFileTrashed({self.name})')
        else:
            print(f'Прочитали все содержимое файла {self.name}')

    def write(self, content):
        if self.is_deleted:
            print(f'ErrorWriteFileDeleted({self.name})')
        elif self.in_trash:
            print(f'ErrorWriteFileTrashed({self.name})')
        else:
            print(f'Записали значение {content} в файл {self.name}')

f1 = File('puppies.jpg')
assert f1.name == 'puppies.jpg'
assert f1.in_trash is False
assert f1.is_deleted is False

f1.read()  # Прочитали все содержимое файла puppies.jpg
f1.remove()  # Файл puppies.jpg был удален
assert f1.is_deleted is True
f1.read()  # ErrorReadFileDeleted(puppies.jpg)

passwords = File('pass.txt')
assert passwords.name == 'pass.txt'
assert passwords.in_trash is False
assert passwords.is_deleted is False

f3 = File('xxx.doc')

assert f3.__dict__ == {'name': 'xxx.doc', 'in_trash': False, 'is_deleted': False}
f3.read()
f3.remove()
assert f3.is_deleted is True
f3.read()
f3.in_trash = True
f3.is_deleted = False
f3.read()
f3.write('hello')
f3.restore_from_trash()
assert f3.in_trash is False
f3.write('hello')  # Записали значение «hello» в файл cat.jpg

f2 = File('cat.jpg')
f2.write('hello')  # Записали значение «hello» в файл cat.jpg
f2.write([1, 2, 3])  # Записали значение «hello» в файл cat.jpg
f2.remove()  # Файл cat.jpg был удален
f2.write('world')  # ErrorWriteFileDeleted(cat.jpg)
print('Ok')