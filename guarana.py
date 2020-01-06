from roslina import Roslina
from zwierze import Zwierze

KOLOR = (244, 92, 66)


class Guarana(Roslina):

    def __init__(self, x, y, s):
        super().__init__(0, 0, x, y)
        self.kolor = KOLOR
        self.swiat = s

    def kolizja(self, napotkany):
        if isinstance(napotkany, Zwierze):
            napotkany.setSila(napotkany.getSila() + 3)
            self.zabij()

    def czyOdbilAtak(self, atakujacy):
        if isinstance(atakujacy, Zwierze):
            atakujacy.setSila(atakujacy.getSila() + 3)
        return False
