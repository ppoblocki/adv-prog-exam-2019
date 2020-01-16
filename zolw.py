"""Zolw"""
from random import randint
from zwierze import Zwierze

SILA = 2
INICJATYWA = 1
KOLOR = (13, 61, 3)
PANCERZ = 5

class Zolw(Zwierze):
    """Klasa - Zolw"""
    def __init__(self, x, y, s):
        super().__init__(SILA, INICJATYWA, x, y)
        self.swiat = s
        self.kolor = KOLOR
        self.pancerz = PANCERZ

    def akcja(self):
        zolw_ruszy_sie = randint(0, 100) < 25
        if zolw_ruszy_sie:
            wspolrzedne_ok = False
            nowe_wspolrzedne = (self.x, self.y)
            while not wspolrzedne_ok:
                wspolrzedne = (self.x, self.y)
                nowe_wspolrzedne = self.losuj_kierunek_ruchu(wspolrzedne)
                wspolrzedne_ok = self.swiat.czyWspolrzednePoprawne(nowe_wspolrzedne)
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
            if napotkany.odbil_atak(self):
                if self.czy_zyje:
                    self.x = self.prevX
                    self.y = self.prevY
            else:
                napotkany.zabij()

    def odbil_atak(self, atakujacy):
        if atakujacy.get_sila() >= self.pancerz:
            result = False
        else:
            result = True
        return result
