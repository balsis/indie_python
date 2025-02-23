class NewInt(int):
    def repeat(self, n=2):
        return int(str(self) * n)

    def to_bin(self):
        return int(bin(self)[2:])


c2 = NewInt(31)
assert c2.repeat() == 3131
assert c2.repeat(4) == 31313131
assert NewInt(16).to_bin() == 10000
assert NewInt(14).to_bin() == 1110