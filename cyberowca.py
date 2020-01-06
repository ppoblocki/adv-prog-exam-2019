from cmath import sqrt

from barszczsosnowskiego import BarszczSosnowskiego
from zwierze import Zwierze

SILA = 11
INICJATYWA = 4
KOLOR = (135, 135, 135)


class CyberOwca(Zwierze):

    def __init__(self, x, y, s):
        super().__init__(SILA, INICJATYWA, x, y)
        self.swiat = s
        self.kolor = KOLOR

    def akcja(self):

        wrog = []
        for organizm in self.swiat.organizmy:
            if isinstance(organizm, BarszczSosnowskiego):
                wrog.append((organizm.getX(), organizm.getY()))

        if len(wrog) > 0:
            odleglosci = []
            for w in wrog:
                odl = abs(sqrt((self.x - w[0]) ** 2 + (self.y - w[1]) ** 2))
                odleglosci.append(odl)
            najblizszy = min(odleglosci)
            index = odleglosci.index((najblizszy))

            najblizszy = wrog[index]
            self.prevX = self.x
            self.prevY = self.y

            x = self.x
            y = self.y

            if x < najblizszy[0]:
                x += 1
            elif x == najblizszy[0]:
                if y < najblizszy[1]:
                    y += 1
                elif y == najblizszy[1]:
                    pass
                elif y > najblizszy[1]:
                    y -= 1
            elif x > najblizszy[0]:
                x -= 1
            pass

            napotkany = self.swiat.organizmNaXY(x, y)
            self.prevX = self.x
            self.prevY = self.y
            self.x = x
            self.y = y
            if napotkany is None:
                self.wiek += 1
            else:
                # self.kolizja(napotkany)
                self.kolizja(napotkany)
                if self.czyZyje:
                    self.wiek += 1
        else:
            super().akcja()

    def kolizja(self, napotkany):
        if isinstance(napotkany, BarszczSosnowskiego):
            napotkany.zabij()
        else:
            super().kolizja(napotkany)
