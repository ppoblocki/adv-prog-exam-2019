import random
from random import randint

from zwierze import Zwierze

SILA = 4
INICJATYWA = 4
KOLOR = (252, 181, 118)


class Antylopa(Zwierze):

    def __init__(self, x, y, s):
        super().__init__(SILA, INICJATYWA, x, y)
        self.swiat = s
        self.kolor = KOLOR

    def akcja(self):
        czyWspolrzedneOK = False
        noweWspolrzedne = (self.x, self.y)

        while not czyWspolrzedneOK:
            wspolrzedne = (self.x, self.y)
            noweWspolrzedne = self.losujKierunekRuchu(wspolrzedne, skok=2)
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
            antylopaUcieknie = random.choice([True, False])
            if antylopaUcieknie and isinstance(self, Zwierze):
                '''
                A -> Antylopa
                [0][1][2]
                [3][A][4]
                [5][6][7]
                '''
                pola = []
                pola.append((self.x - 1, self.y - 1))
                pola.append((self.x - 1, self.y))
                pola.append((self.x - 1, self.y + 1))

                pola.append((self.x, self.y - 1))
                pola.append((self.x - 1, self.y + 1))

                pola.append((self.x + 1, self.y - 1))
                pola.append((self.x + 1, self.y))
                pola.append((self.x + 1, self.y + 1))

                mozliwePola = []  # lista pol dla antylopy do ucieczki
                for pole in pola:
                    if self.swiat.czyWspolrzednePoprawne(pole):
                        organizmXY = self.swiat.organizmNaXY(pole[0], pole[1])
                        if organizmXY is None:
                            mozliwePola.append(pole)

                if mozliwePola:
                    pole = mozliwePola[randint(0, len(mozliwePola) - 1)]
                    self.prevX = self.x
                    self.prevY = self.y
                    self.x = pole[0]
                    self.y = pole[1]
            else:
                if napotkany.czyOdbilAtak(self):
                    if self.czyZyje:
                        self.x = self.prevX
                        self.y = self.prevY
                    else:
                        napotkany.zabij()
