"""Antylopa"""
import random
from random import randint

from zwierze import Zwierze

SILA = 4
INICJATYWA = 4
KOLOR = (252, 181, 118)

class Antylopa(Zwierze):
    """Klasa - Antylopa"""
    def __init__(self, x, y, s):
        super().__init__(SILA, INICJATYWA, x, y)
        self.swiat = s
        self.kolor = KOLOR

    def akcja(self):
        czy_wspolrzedne_ok = False
        nowe_wspolrzedne = (self.x, self.y)

        while not czy_wspolrzedne_ok:
            wspolrzedne = (self.x, self.y)
            nowe_wspolrzedne = self.losuj_kierunek_ruchu(wspolrzedne, skok=2)
            czy_wspolrzedne_ok = self.swiat.czyWspolrzednePoprawne(nowe_wspolrzedne)

        napotkany = self.swiat.organizmNaXY(nowe_wspolrzedne[0], nowe_wspolrzedne[1])
        self.prevX = self.x
        self.prevY = self.y
        self.x = nowe_wspolrzedne[0]
        self.y = nowe_wspolrzedne[1]
        if napotkany is None:
            self.wiek += 1
        else:
            self.kolizja(napotkany)
            if self.czy_zyje:
                self.wiek += 1

    def kolizja(self, napotkany):
        if isinstance(self, type(napotkany)):
            self.x = self.prevX
            self.y = self.prevY
            self.swiat.dodajOrganizmWOtoczeniu(self)
        else:
            antylopa_ucieknie = random.choice([True, False])
            if antylopa_ucieknie and isinstance(self, Zwierze):
                pola = []
                pola.append((self.x - 1, self.y - 1))
                pola.append((self.x - 1, self.y))
                pola.append((self.x - 1, self.y + 1))

                pola.append((self.x, self.y - 1))
                pola.append((self.x - 1, self.y + 1))

                pola.append((self.x + 1, self.y - 1))
                pola.append((self.x + 1, self.y))
                pola.append((self.x + 1, self.y + 1))

                mozliwe_pola = []  # lista pol dla antylopy do ucieczki
                for pole in pola:
                    if self.swiat.czyWspolrzednePoprawne(pole):
                        organizm_x_y = self.swiat.organizmNaXY(pole[0], pole[1])
                        if organizm_x_y is None:
                            mozliwe_pola.append(pole)

                if mozliwe_pola:
                    pole = mozliwe_pola[randint(0, len(mozliwe_pola) - 1)]
                    self.prevX = self.x
                    self.prevY = self.y
                    self.x = pole[0]
                    self.y = pole[1]
            else:
                if napotkany.odbil_atak(self):
                    if self.czy_zyje:
                        self.x = self.prevX
                        self.y = self.prevY
                    else:
                        napotkany.zabij()
