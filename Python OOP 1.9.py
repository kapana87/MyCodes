class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, hexcode):
        self._hexcode = hexcode
        self.r, self.g, self.b = [int(i, 16) for i in [self._hexcode[i: i + 2] for i in range(0, len(self._hexcode), 2)]]


color = Color('0000FF')

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)