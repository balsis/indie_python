class Person:
    def __init__(self, new_name, new_age):
        self.name = new_name  # здесь name - имя свойства
        self._age = new_age

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError('Имя должно быть непустой строкой')

    def delete_name(self):
        del self._name

    name = property(fget = get_name,
                    fset = set_name,
                    fdel = delete_name)  # свойство name