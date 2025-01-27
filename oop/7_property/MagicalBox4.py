class MagicalBox:
    def __init__(self, contents=None):
        print(f'запустился __init__. установим self.contents (свойство)')
        self.contents = contents
        # print(f'__init__ установил значение {self.contents=}')

    @property
    def contents(self):
        print('запускаем геттер contents')
        if self._contents == "rabbit":
            print('да, self._contents == "rabbit"')
            return "🐇 A magical rabbit!"
        else:
            print('нет, self._contents != "rabbit"')
            return self._contents

    @contents.setter
    def contents(self, new_contents):
        print(f'запускаем setter contents. кстати, {new_contents=}')
        if new_contents == "wishes":
            print("🌟 Your wishes are granted!")
            self._contents = new_contents
        else:
            print("✨ The magic didn't work this time.")
            self._contents = new_contents

print('сейчас создадим экземпляр класса')
box = MagicalBox("rabbit")
print('сейчас обратимся к box.contents')
print(box.contents)