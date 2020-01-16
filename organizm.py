"""Organizm"""
from abc import ABC, abstractmethod
from random import randint

class Organizm(ABC):
    """Klasa - Organizm"""
    def __init__(self, sila=0, inicjatywa=0, x=0, y=0):
        self.sila = sila
        self.inicjatywa = inicjatywa
        self.x = x
        self.y = y
        self.sila_bazowa = self.sila
        self.prev_x = self.x
        self.prev_y = self.y
        self.wiek = 0
        self.czy_zyje = True
        self.kolor = ()
        self.swiat = None

    @abstractmethod
    def akcja(self):
        """akcja()"""

    @abstractmethod
    def kolizja(self, napotkany):
        """kolizja()"""

    def rysuj(self):
        """rysuj()"""
        return self.kolor

    @abstractmethod
    def odbil_atak(self, atakujacy):
        """odbil_atak()"""

    def get_x(self):
        """get_x()"""
        return self.x

    def set_x(self, x):
        """set_x()"""
        self.x = x

    def get_y(self):
        """get_y()"""
        return self.y

    def set_y(self, y):
        """set_y()"""
        self.y = y

    def get_prev_x(self):
        """get_prev_x()"""
        return self.prev_x

    def get_prev_y(self):
        """get_prev_y()"""
        return self.prev_y

    def set_sila(self, sila):
        """set_sila()"""
        self.sila = sila

    def get_sila(self):
        """get_sila()"""
        return self.sila

    def get_inicjatywa(self):
        """get_inicjatywa()"""
        return self.inicjatywa

    def get_czy_zyje(self):
        """get_czy_zyje()"""
        return self.czy_zyje

    def get_kolor(self):
        """get_kolor()"""
        return self.kolor

    def get_wiek(self):
        """get_wiek()"""
        return self.wiek

    def set_wiek(self, wiek):
        """set_wiek()"""
        self.wiek = wiek

    def set_kolor(self, kolor):
        """set_kolor()"""
        self.kolor = kolor

    def zabij(self):
        """zabij()"""
        self.czy_zyje = False
        self.sila = 0

    def losuj_kierunek_ruchu(self, wspolrzedne, skok=1):
        """losuj_kierunek_ruchu()"""
        kierunek = randint(0, 7)
        x_poz = wspolrzedne[0]
        y_poz = wspolrzedne[1]
        if kierunek == 0:
            y_poz -= skok
        elif kierunek == 1:
            y_poz += skok
        elif kierunek == 2:
            x_poz -= skok
        elif kierunek == 3:
            x_poz += skok
        elif kierunek == 4:
            x_poz -= skok
            y_poz -= skok
        elif kierunek == 5:
            x_poz += skok
            y_poz -= skok
        elif kierunek == 6:
            x_poz -= skok
            y_poz += skok
        elif kierunek == 7:
            x_poz += skok
            y_poz += skok
        return (x_poz, y_poz)

    def print_info(self):
        """print_info()"""
        print(self.x)
        print(self.y)
        print(self.sila)
        if self.swiat is None:
            print("Brak referencji do swiata.")
        else:
            print("Referencja do swiata poprawna!")
