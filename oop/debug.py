class CountDown:
    value = 10

    def decrement(self):
        self.value = CountDown.value - 1


counter = CountDown()
counter.decrement()
counter.decrement()
counter.decrement()

print(CountDown.value)
print(counter.value)