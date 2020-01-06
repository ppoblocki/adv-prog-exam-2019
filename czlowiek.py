import pygame

from zwierze import Zwierze

SILA = 5
INICJATYWA = 4
KOLOR = (0, 0, 0)
ULT_KOLOR = (255, 0, 0)


class Czlowiek(Zwierze):

    def __init__(self, x, y, s):
        super().__init__(SILA, INICJATYWA, x, y)
        self.swiat = s
        self.kolor = KOLOR
        self.superzdolnoscON = False
        self.czasTrwania = 0
        self.cooldown = 0

    def akcja(self):
        x = self.x
        y = self.y
        key = self.swiat.getLastKeyboardEvent().key
        if key == pygame.K_UP:
            y -= 1
        elif key == pygame.K_DOWN:
            y += 1
        elif key == pygame.K_LEFT:
            x -= 1
        elif key == pygame.K_RIGHT:
            x += 1

        if self.swiat.czyWspolrzednePoprawne((x, y)):

            napotkany = self.swiat.organizmNaXY(x, y)

            self.prevX = self.x
            self.prevY = self.y

            self.x = x
            self.y = y

            if napotkany is None:
                self.wiek += 1

                if self.superzdolnoscON:
                    self.kolor = ULT_KOLOR
                    self.czasTrwania += 1
                    if self.czasTrwania > 5:
                        self.superzdolnoscON = False
                        self.kolor = KOLOR
                else:
                    if self.cooldown > 0:
                        self.cooldown -= 1
            else:
                self.kolizja(napotkany)

                if self.czyZyje:
                    self.wiek += 1

                    if self.superzdolnoscON:
                        self.kolor = ULT_KOLOR
                        self.czasTrwania += 1
                        if self.czasTrwania > 5:
                            self.superzdolnoscON = False
                            self.kolor = KOLOR
                    else:
                        if self.cooldown > 0:
                            self.cooldown -= 1
        else:
            pass

    def kolizja(self, napotkany):
        if napotkany.czyOdbilAtak(self):
            if self.superzdolnoscON:
                napotkany.setX(napotkany.getPrevX())
                napotkany.setY(napotkany.getPrevY())
            else:
                self.zabij()
        else:
            napotkany.zabij()

    def zabij(self):
        self.swiat.czyCzlowiekGra = False
        self.czyZyje = 0
        self.sila = 0

    def czyOdbilAtak(self, atakujacy):
        if self.superzdolnoscON and isinstance(atakujacy, Zwierze):
            return True
        else:
            if atakujacy.getSila() >= self.sila:
                return False
            else:
                atakujacy.zabij()
                return True

    def getSuperzdolnosc(self):
        return self.superzdolnoscON

    def setSuperzdolnosc(self, status):
        self.superzdolnoscON = status

    def getCzasTrwania(self):
        return self.czasTrwania

    def setCzasTrwania(self, czas):
        self.czasTrwania = czas

    def getCooldown(self):
        return self.cooldown

    def setCooldown(self, cooldown):
        self.cooldown = cooldown
