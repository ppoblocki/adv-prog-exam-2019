from random import randint

from zwierze import Zwierze

SILA = 3
INICJATYWA = 7
KOLOR = (255, 153, 0)


class Lis(Zwierze):

    def __init__(self, x, y, s):
        super().__init__(SILA, INICJATYWA, x, y)
        self.swiat = s
        self.kolor = KOLOR

    def akcja(self):
        '''
        L -> lis
        [0][1][2]
        [3][L][4]
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

        mozliwePola = []  # lista pol dla lisa
        for pole in pola:
            if self.swiat.czyWspolrzednePoprawne(pole):
                organizmXY = self.swiat.organizmNaXY(pole[0], pole[1])
                if organizmXY is None or organizmXY.getSila() <= self.sila:
                    mozliwePola.append(pole)

        if mozliwePola:
            pole = mozliwePola[randint(0, len(mozliwePola) - 1)]
            napotkany = self.swiat.organizmNaXY(pole[0], pole[1])
            self.prevX = self.x
            self.prevY = self.y
            self.x = pole[0]
            self.y = pole[1]
            if napotkany is None:
                self.wiek += 1
            else:
                self.kolizja(napotkany)
                if self.czyZyje:
                    self.wiek += 1
