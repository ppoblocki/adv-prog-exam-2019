"""Czlowiek"""
import pygame
from zwierze import Zwierze

SILA = 5
INICJATYWA = 4
KOLOR = (0, 0, 0)
ULT_KOLOR = (255, 0, 0)

class Czlowiek(Zwierze):
    """Klasa - Czlowiek"""
    def __init__(self, x, y, s):
        super().__init__(SILA, INICJATYWA, x, y)
        self.swiat = s
        self.kolor = KOLOR
        self.superzdolnosc_wlaczona = False
        self.czas_trwania = 0
        self.cooldown = 0

    def akcja(self):
        x_poz = self.x
        y_poz = self.y
        key = self.swiat.getLastKeyboardEvent().key
        if key == pygame.K_UP:
            y_poz -= 1
        elif key == pygame.K_DOWN:
            y_poz += 1
        elif key == pygame.K_LEFT:
            x_poz -= 1
        elif key == pygame.K_RIGHT:
            x_poz += 1

        if self.swiat.czyWspolrzednePoprawne((x_poz, y_poz)):
            napotkany = self.swiat.organizmNaXY(x_poz, y_poz)
            self.prevX = self.x
            self.prevY = self.y
            self.x = x_poz
            self.y = y_poz
            if napotkany is None:
                self.wiek += 1
                if self.superzdolnosc_wlaczona:
                    self.kolor = ULT_KOLOR
                    self.czas_trwania += 1
                    if self.czas_trwania > 5:
                        self.superzdolnosc_wlaczona = False
                        self.kolor = KOLOR
                else:
                    if self.cooldown > 0:
                        self.cooldown -= 1
            else:
                self.kolizja(napotkany)
                if self.czyZyje:
                    self.wiek += 1
                    if self.superzdolnosc_wlaczona:
                        self.kolor = ULT_KOLOR
                        self.czas_trwania += 1
                        if self.czas_trwania > 5:
                            self.superzdolnosc_wlaczona = False
                            self.kolor = KOLOR
                    else:
                        if self.cooldown > 0:
                            self.cooldown -= 1
        else:
            pass

    def kolizja(self, napotkany):
        if napotkany.odbil_atak(self):
            if self.superzdolnosc_wlaczona:
                napotkany.set_x(napotkany.get_prev_x())
                napotkany.set_y(napotkany.get_prev_y())
            else:
                self.zabij()
        else:
            napotkany.zabij()

    def zabij(self):
        self.swiat.czyCzlowiekGra = False
        self.czyZyje = 0
        self.sila = 0

    def odbil_atak(self, atakujacy):
        if self.superzdolnosc_wlaczona and isinstance(atakujacy, Zwierze):
            result = True
        else:
            if atakujacy.get_sila() >= self.sila:
                result = False
            else:
                atakujacy.zabij()
                result = True
        return result

    def get_superzdolnosc(self):
        """Pobiera status superzdolnosci."""
        return self.superzdolnosc_wlaczona

    def set_superzdolnosc(self, status):
        """Ustawia status superzdolnosci"""
        self.superzdolnosc_wlaczona = status

    def get_czas_trwania(self):
        """Pobiera czas trwania superzdolnosci"""
        return self.czas_trwania

    def set_czas_trwania(self, czas):
        """Ustawia czas trwania superzdolnosci"""
        self.czas_trwania = czas

    def get_cooldown(self):
        """Pobiera czas odnowienia superzdolnosci"""
        return self.cooldown

    def set_cooldown(self, cooldown):
        """Ustawia czas odnowienia superdolnosci"""
        self.cooldown = cooldown
