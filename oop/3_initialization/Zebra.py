class Zebra:
    def __init__(self):
        self.a = "Полоска белая"
        self.b = "Полоска черная"

    def which_stripe(self):
        print(self.a)
        self.a, self.b = self.b, self.a


z1 = Zebra()
z1.which_stripe()  # печатает Полоска белая
z1.which_stripe()  # печатает Полоска черная
z1.which_stripe()  # печатает Полоска белая

z2 = Zebra()
z2.which_stripe()  # печатает Полоска белая
