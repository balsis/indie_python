class Colour:
    def __init__(self, hex_code: str):
        if not isinstance(hex_code, str) or not hex_code.startswith("#") or len(hex_code) != 7:
            raise ValueError("Invalid HEX color format")

        self.hex_code = hex_code
        self._red = int(hex_code[1:3], 16)
        self._green = int(hex_code[3:5], 16)
        self._blue = int(hex_code[5:7], 16)

    @property
    def red(self):
        return self._red

    @property
    def green(self):
        return self._green

    @property
    def blue(self):
        return self._blue


colour = Colour("#ff0000")
print(colour.red)  # 255
print(colour.green)  # 0
print(colour.blue)  # 0
