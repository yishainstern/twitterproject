
class convertcolor:

    def rgb(self, triplet):
        if not len(triplet) == 6:
            return -10, -10, -10
        a1 = self.HEXDEC[triplet[0:2]]
        a2 = self.HEXDEC[triplet[2:4]]
        a3 = self.HEXDEC[triplet[4:6]]
        return a1, a2, a3

    def triplet(self, rgb):
        return format(rgb[0] << 16 | rgb[1] << 8 | rgb[2], '06'+self.LOWERCASE)

    def __init__(self):
        self.NUMERALS = "0123456789abcdefABCDEF"
        self.HEXDEC = {v: int(v, 16) for v in (x + y for x in self.NUMERALS for y in self.NUMERALS)}
        self.LOWERCASE = 'x'
        self.UPPERCASE = 'X'
