"""Cyber-owca"""
from cmath import sqrt
from barszczsosnowskiego import BarszczSosnowskiego
from zwierze import Zwierze

SILA = 11
INICJATYWA = 4
KOLOR = (135, 135, 135)

class CyberOwca(Zwierze):
    """Klasa - Cyber-owca"""
    def __init__(self, x, y, s):
        super().__init__(SILA, INICJATYWA, x, y)
        self.swiat = s
        self.kolor = KOLOR

    def akcja(self):
        wrogowie = []
        for organizm in self.swiat.organizmy:
            if isinstance(organizm, BarszczSosnowskiego):
                wrogowie.append((organizm.get_x(), organizm.get_y()))

        if len(wrogowie) > 0:
            odleglosci = []
            for wrog in wrogowie:
                odl = abs(sqrt((self.x - wrog[0]) ** 2 + (self.y - wrog[1]) ** 2))
                odleglosci.append(odl)
            najblizszy = min(odleglosci)
            index = odleglosci.index((najblizszy))

            najblizszy = wrogowie[index]
            self.prevX = self.x
            self.prevY = self.y

            x_poz = self.x
            y_poz = self.y

            if x_poz < najblizszy[0]:
                x_poz += 1
            elif x_poz == najblizszy[0]:
                if y_poz < najblizszy[1]:
                    y_poz += 1
                elif y_poz == najblizszy[1]:
                    pass
                elif y_poz > najblizszy[1]:
                    y_poz -= 1
            elif x_poz > najblizszy[0]:
                x_poz -= 1

            napotkany = self.swiat.organizmNaXY(x_poz, y_poz)
            self.prevX = self.x
            self.prevY = self.y
            self.x = x_poz
            self.y = y_poz
            if napotkany is None:
                self.wiek += 1
            else:
                self.kolizja(napotkany)
                if self.czy_zyje:
                    self.wiek += 1
        else:
            super().akcja()

    def kolizja(self, napotkany):
        if isinstance(napotkany, BarszczSosnowskiego):
            napotkany.zabij()
        else:
            super().kolizja(napotkany)
