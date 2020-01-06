from random import randint

from roslina import Roslina

KOLOR = (250, 255, 0)


class Mlecz(Roslina):

    def __init__(self, x, y, s):
        super().__init__(0, 0, x, y)
        self.kolor = KOLOR
        self.swiat = s

    def akcja(self):
        for i in range(0, 3):
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
