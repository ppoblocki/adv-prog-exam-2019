from organizm import Organizm

class Zwierze(Organizm):

    def __init__(self, sila=0, inicjatywa=0, x=0, y=0):
        super().__init__(sila, inicjatywa, x, y)

    def akcja(self):
        czyWspolrzedneOK = False
        noweWspolrzedne = (self.x, self.y)

        while not czyWspolrzedneOK:
            wspolrzedne = (self.x, self.y)
            noweWspolrzedne = self.losuj_kierunek_ruchu(wspolrzedne)
            czyWspolrzedneOK = self.swiat.czyWspolrzednePoprawne(noweWspolrzedne)

        napotkany = self.swiat.organizmNaXY(noweWspolrzedne[0], noweWspolrzedne[1])
        self.prevX = self.x
        self.prevY = self.y
        self.x = noweWspolrzedne[0]
        self.y = noweWspolrzedne[1]
        if napotkany is None:
            self.wiek += 1
        else:
            # self.kolizja(napotkany)
            self.kolizja(napotkany)
            if self.czy_zyje:
                self.wiek += 1

    def kolizja(self, napotkany):
        if type(napotkany) == type(self):
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
        if atakujacy.get_sila() >= self.sila:
            return False
        else:
            return True
