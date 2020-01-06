from organizm import Organizm


class Zwierze(Organizm):

    def __init__(self, sila=0, inicjatywa=0, x=0, y=0):
        super().__init__(sila, inicjatywa, x, y)

    def akcja(self):
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
            # self.kolizja(napotkany)
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
        if atakujacy.getSila() >= self.sila:
            return False
        else:
            return True
