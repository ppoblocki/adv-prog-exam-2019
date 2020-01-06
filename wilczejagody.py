from roslina import Roslina
from zwierze import Zwierze

KOLOR = (47, 1, 96)


class WilczeJagody(Roslina):

    def __init__(self, x, y, s):
        super().__init__(0, 0, x, y)
        self.kolor = KOLOR
        self.swiat = s

    def kolizja(self, napotkany):
        if isinstance(napotkany, Zwierze):
            napotkany.zabij()

    def czyOdbilAtak(self, atakujacy):
        if isinstance(atakujacy, Zwierze):
            atakujacy.zabij()
        return True
