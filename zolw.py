from random import randint

from zwierze import Zwierze

SILA = 2
INICJATYWA = 1
KOLOR = (13, 61, 3)
PANCERZ = 5


class Zolw(Zwierze):

    def __init__(self, x, y, s):
        super().__init__(SILA, INICJATYWA, x, y)
        self.swiat = s
        self.kolor = KOLOR
        self.pancerz = PANCERZ

    def akcja(self):
        zolwRuszySie = randint(0, 100) < 25

        if zolwRuszySie:
            czyWspolrzedneOK = False
            noweWspolrzedne = (self.x, self.y)

            while not czyWspolrzedneOK:
                wspolrzedne = (self.x, self.y)
                noweWspolrzedne = self.losujKierunekRuchu(wspolrzedne)
                czyWspolrzedneOK = self.swiat.czyWspolrzednePoprawne(noweWspolrzedne)

            napotkany = self.swiat.organizmNaXY(noweWspolrzedne[0], noweWspolrzedne[1])
            self.prevX = self.x
            self.prevY = self.y
            self.x = noweWspolrzedne[0]
            self.y = noweWspolrzedne[1]
            if napotkany is None:
                self.wiek += 1
            else:
                self.kolizja(napotkany)
                if self.czyZyje:
                    self.wiek += 1

    def kolizja(self, napotkany):
        if type(napotkany) == type(self):
            self.x = self.prevX
            self.y = self.prevY
            self.swiat.dodajOrganizmWOtoczeniu(self)
        else:
            if napotkany.czyOdbilAtak(self):
                if self.czyZyje:
                    self.x = self.prevX
                    self.y = self.prevY
            else:
                napotkany.zabij()

    def czyOdbilAtak(self, atakujacy):
        if atakujacy.getSila() >= self.pancerz:
            return False
        else:
            return True
