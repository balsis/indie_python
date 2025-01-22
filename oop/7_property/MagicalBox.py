class MagicalBox:
    def __init__(self, contents=None):
        self._contents = contents

    @property
    def contents(self):
        print('getter')
        if self._contents == "rabbit":
            return "🐇 A magical rabbit!"
        else:
            return self._contents

    @contents.setter
    def contents(self, new_contents):
        print('setter')
        if new_contents == "wishes":
            print("🌟 Your wishes are granted!")
            self._contents = new_contents
        else:
            print("✨ The magic didn't work this time.")
            self._contents = new_contents


box = MagicalBox("rubies")
print(box.contents)
print()
box.contents = 'rubies2'
print()
print(box._contents)