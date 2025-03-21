class CustomButton:
    def __init__(self, text, **kwargs):
        self.text = text
        for key, value in kwargs.items():
            setattr(self, key, value)

    def config(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def click(self):
        try:
            self.command()
        except AttributeError:
            print("Кнопка не настроена")
        except TypeError:
            print("Кнопка сломалась")


def func():
    print('Оно живое')


btn = CustomButton(text = "Hello", bd = 20, bg = '#ffaaaa')

print(btn.text)
btn.click()  # Кнопка не настроена
btn.config(command = func)
btn.click()  # Оно живое

def func2():
    print('Оно суперживое')

btn2 = CustomButton(text="Hello2", bd=20, bg='#ffaaaa')
btn2.click()  # Кнопка не настроена
btn2.config(command=func2)
btn2.click()  # Оно суперживое
btn2.config(command='hello')
btn2.click()  # Кнопка сломалась
btn2.config(command=lambda: print(123))
btn2.click()  # 123
del btn2.command
btn2.click()  # 123
