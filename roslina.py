"""Roslina"""
from random import randint
from organizm import Organizm
from zwierze import Zwierze

class Roslina(Organizm):
    """Klasa - Roslina"""
    def __init__(self, sila=0, inicjatywa=0, x=0, y=0):
        super().__init__(sila, inicjatywa, x, y)

    def akcja(self):
        rozprzestrzenia_sie = randint(0, 100) < 20
        if rozprzestrzenia_sie:
            wspolrzedne_ok = False
            nowe_wspolrzedne = (self.x, self.y)
            while not wspolrzedne_ok:
                wspolrzedne = (self.x, self.y)
                nowe_wspolrzedne = self.losuj_kierunek_ruchu(wspolrzedne)
                wspolrzedne_ok = self.swiat.czyWspolrzednePoprawne(nowe_wspolrzedne)
            napotkany = self.swiat.organizmNaXY(nowe_wspolrzedne[0], nowe_wspolrzedne[1])
            x_poz, y_poz = nowe_wspolrzedne[0], nowe_wspolrzedne[1]
            if napotkany is None:
                self.swiat.dodajGatunekRosliny(self, x_poz, y_poz)
            else:
                napotkany.kolizja(self)

    def kolizja(self, napotkany):
        """kolizja()"""
        if isinstance(napotkany, Zwierze):
            self.zabij()

    def odbil_atak(self, atakujacy):
        """odbil_atak()"""
        return False
