from abc import ABC, abstractmethod
from random import randint


class Organizm(ABC):

    def __init__(self, sila=0, inicjatywa=0, x=0, y=0):
        self.sila = sila
        self.inicjatywa = inicjatywa
        self.x = x
        self.y = y

        self.silaBazowa = self.sila
        self.prevX = self.x
        self.prevY = self.y
        self.wiek = 0
        self.czyZyje = True
        self.kolor = ()
        self.swiat = None

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self, napotkany):
        pass

    def rysuj(self):
        return self.kolor

    @abstractmethod
    def czyOdbilAtak(self, atakujacy):
        pass

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getPrevX(self):
        return self.prevX

    def getPrevY(self):
        return self.prevY

    def setSila(self, sila):
        self.sila = sila

    def getSila(self):
        return self.sila

    def getInicjatywa(self):
        return self.inicjatywa

    def getCzyZyje(self):
        return self.czyZyje

    def getKolor(self):
        return self.kolor

    def getWiek(self):
        return self.wiek

    def setWiek(self, wiek):
        self.wiek = wiek

    def setKolor(self, kolor):
        self.kolor = kolor

    def zabij(self):
        self.czyZyje = False
        self.sila = 0

    def losujKierunekRuchu(self, wspolrzedne, skok=1):
        kierunek = randint(0, 7)
        x = wspolrzedne[0]
        y = wspolrzedne[1]

        # Gora
        if kierunek == 0:
            y -= skok

        # Dol
        elif kierunek == 1:
            y += skok

        # Lewo
        elif kierunek == 2:
            x -= skok

        # Prawo
        elif kierunek == 3:
            x += skok

        # Lewy gorny
        elif kierunek == 4:
            x -= skok
            y -= skok

        # Prawy gorny
        elif kierunek == 5:
            x += skok
            y -= skok

        # Lewy dolny
        elif kierunek == 6:
            x -= skok
            y += skok

        # Prawy dolny
        elif kierunek == 7:
            x += skok
            y += skok

        return (x, y)

    def print_info(self):
        print(self.x)
        print(self.y)
        print(self.sila)
        if self.swiat is None:
            print("Brak referencji do swiata")
        else:
            print("Referencja do swiata poprawna!")
