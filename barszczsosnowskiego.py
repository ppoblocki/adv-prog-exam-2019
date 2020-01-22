"""Barszcz Sosnowskiego"""
from roslina import Roslina
from zwierze import Zwierze

SILA = 10
KOLOR = (196, 255, 196)

class BarszczSosnowskiego(Roslina):
    """Klasa - Barszcz Sosnowskiego"""
    def __init__(self, x, y, s):
        super().__init__(0, 0, x, y)
        self.kolor = KOLOR
        self.swiat = s

    def akcja(self):
        pola = []
        pola.append((self.x - 1, self.y - 1))
        pola.append((self.x - 1, self.y))
        pola.append((self.x - 1, self.y + 1))

        pola.append((self.x, self.y - 1))
        pola.append((self.x - 1, self.y + 1))

        pola.append((self.x + 1, self.y - 1))
        pola.append((self.x + 1, self.y))
        pola.append((self.x + 1, self.y + 1))

        poprawne_pola = []
        for pole in pola:
            if self.swiat.wspolrzedne_poprawne(pole):
                poprawne_pola.append(pole)

        for pole in poprawne_pola:
            organizm = self.swiat.organizmNaXY(pole[0], pole[1])
            if isinstance(organizm, Zwierze) and not type(organizm).__name__ == 'CyberOwca':
                organizm.zabij()
        super().akcja()

    def kolizja(self, napotkany):
        if isinstance(napotkany, Zwierze):
            napotkany.zabij()

    def odbil_atak(self, atakujacy):
        return True
