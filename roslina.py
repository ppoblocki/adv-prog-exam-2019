from random import randint

from organizm import Organizm
from zwierze import Zwierze


class Roslina(Organizm):

    def __init__(self, sila=0, inicjatywa=0, x=0, y=0):
        super().__init__(sila, inicjatywa, x, y)

    def akcja(self):
        czyRozprzestrzeniaSie = randint(0, 100) < 20

        if czyRozprzestrzeniaSie:
            czyWspolrzedneOK = False
            noweWspolrzedne = (self.x, self.y)

            while not czyWspolrzedneOK:
                wspolrzedne = (self.x, self.y)
                noweWspolrzedne = self.losujKierunekRuchu(wspolrzedne)
                czyWspolrzedneOK = self.swiat.czyWspolrzednePoprawne(noweWspolrzedne)

            napotkany = self.swiat.organizmNaXY(noweWspolrzedne[0], noweWspolrzedne[1])
            x, y = noweWspolrzedne[0], noweWspolrzedne[1]
            if napotkany is None:
                self.swiat.dodajGatunekRosliny(self, x, y)
            else:
                napotkany.kolizja(self)

    def kolizja(self, napotkany):
        if isinstance(napotkany, Zwierze):
            self.zabij()

    def czyOdbilAtak(self, atakujacy):
        return False
