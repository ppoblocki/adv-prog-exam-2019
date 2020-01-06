from zwierze import Zwierze

SILA = 4
INICJATYWA = 4
KOLOR = (231, 232, 229)


class Owca(Zwierze):

    def __init__(self, x, y, s):
        super().__init__(SILA, INICJATYWA, x, y)
        self.swiat = s
        self.kolor = KOLOR
