class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# Ниже расположен код для проверок, его не нужно удалять
modelX = Vehicle(200, 18000)
assert modelX.max_speed == 200
assert modelX.mileage == 18000
assert modelX.__dict__ == {'max_speed': 200, 'mileage': 18000}

audi = Vehicle(240, 5)
assert audi.__dict__ == {'max_speed': 240, 'mileage': 5}
print('Good')
