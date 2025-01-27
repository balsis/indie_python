class Notebook:
    def __init__(self, lst):
        self._notes = lst

    @property
    def notes_list(self):
        for i in range(len(self._notes)):
            print(f'{i+1}.{self._notes[i]}')


note = Notebook(list(range(10, 20)))
note.notes_list
try:
    note.notes_list = [3, 4, 3] # при попытке сохранить новое значение должна быть ошибка
except AttributeError:
    pass