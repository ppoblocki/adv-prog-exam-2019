"""Zwierze"""
from organizm import Organizm

class Zwierze(Organizm):
    """Klasa - Zwierze"""
    def __init__(self, sila=0, inicjatywa=0, x=0, y=0):
        super().__init__(sila, inicjatywa, x, y)

    def akcja(self):
        wspolrzedne_ok = False
        nowe_wspolrzedne = (self.x, self.y)

        while not wspolrzedne_ok:
            wspolrzedne = (self.x, self.y)
            nowe_wspolrzedne = self.losuj_kierunek_ruchu(wspolrzedne)
            wspolrzedne_ok = self.swiat.wspolrzedne_poprawne(nowe_wspolrzedne)

        napotkany_przeciwnik = self.swiat.organizmNaXY(nowe_wspolrzedne[0], nowe_wspolrzedne[1])
        self.prevX = self.x
        self.prevY = self.y
        self.x = nowe_wspolrzedne[0]
        self.y = nowe_wspolrzedne[1]
        if napotkany_przeciwnik is None:
            self.wiek += 1
        else:
            # self.kolizja(napotkany_przeciwnik)n
            self.kolizja(napotkany_przeciwnik)
            if self.czy_zyje:
                self.wiek += 1

    def kolizja(self, napotkany_przeciwnik):
        print(self)
        if isinstance(self, napotkany_przeciwnik.__class__):
            self.x = self.prevX
            self.y = self.prevY
            self.swiat.dodajOrganizmWOtoczeniu(self)
        else:
            if napotkany_przeciwnik.odbil_atak(self):
                if self.czy_zyje:
                    self.x = self.prevX
                    self.y = self.prevY
            else:
                napotkany_przeciwnik.zabij()

    def odbil_atak(self, atakujacy):
        return bool(atakujacy.get_sila() >= self.sila)
