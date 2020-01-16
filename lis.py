"""Lis"""
from random import randint
from zwierze import Zwierze

SILA = 3
INICJATYWA = 7
KOLOR = (255, 153, 0)

class Lis(Zwierze):
    """Klasa - Lis"""
    def __init__(self, x, y, s):
        super().__init__(SILA, INICJATYWA, x, y)
        self.swiat = s
        self.kolor = KOLOR

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

        mozliwe_pola = []  # lista pol dla lisa
        for pole in pola:
            if self.swiat.czyWspolrzednePoprawne(pole):
                organizm_x_y = self.swiat.organizmNaXY(pole[0], pole[1])
                if organizm_x_y is None or organizm_x_y.get_sila() <= self.sila:
                    mozliwe_pola.append(pole)

        if mozliwe_pola:
            pole = mozliwe_pola[randint(0, len(mozliwe_pola) - 1)]
            napotkany = self.swiat.organizmNaXY(pole[0], pole[1])
            self.prevX = self.x
            self.prevY = self.y
            self.x = pole[0]
            self.y = pole[1]
            if napotkany is None:
                self.wiek += 1
            else:
                self.kolizja(napotkany)
                if self.czy_zyje:
                    self.wiek += 1
