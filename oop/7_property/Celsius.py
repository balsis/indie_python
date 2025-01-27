class Celsius:
    def __init__(self, temp):
        self.temperature = temp

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError
        else:
            self._temperature = value

    def to_fahrenheit(self):
        return (self._temperature * 9 / 5) + 32


# Ниже код для проверки методов класса Celsius

celsius = Celsius(25)
assert celsius.temperature == 25
assert celsius.to_fahrenheit() == 77.0

celsius.temperature = 30
assert celsius.temperature == 30
assert celsius.to_fahrenheit() == 86.0

print('Good')
