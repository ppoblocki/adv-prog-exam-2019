"""Mlecz"""
from random import randint
from roslina import Roslina

KOLOR = (250, 255, 0)

class Mlecz(Roslina):
    """Klasa - Mlecz"""
    def __init__(self, x, y, s):
        super().__init__(0, 0, x, y)
        self.kolor = KOLOR
        self.swiat = s

    def akcja(self):
        for _ in range(0, 3):
            rozprzestrzenia_sie = randint(0, 100) < 20
            if rozprzestrzenia_sie:
                wspolrzedne_ok = False
                nowe_wspolrzedne = (self.x, self.y)
                while not wspolrzedne_ok:
                    wspolrzedne = (self.x, self.y)
                    nowe_wspolrzedne = self.losuj_kierunek_ruchu(wspolrzedne)
                    wspolrzedne_ok = self.swiat.wspolrzedne_poprawne(nowe_wspolrzedne)
                napotkany = self.swiat.organizmNaXY(nowe_wspolrzedne[0], nowe_wspolrzedne[1])
                x_poz, y_poz = nowe_wspolrzedne[0], nowe_wspolrzedne[1]
                if napotkany is None:
                    self.swiat.dodajGatunekRosliny(self, x_poz, y_poz)
                else:
                    napotkany.kolizja(self)
