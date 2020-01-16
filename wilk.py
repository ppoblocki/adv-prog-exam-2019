"""Wilk"""
from zwierze import Zwierze

SILA = 9
INICJATYWA = 5
KOLOR = (139, 115, 85)

class Wilk(Zwierze):
    """Klasa - Wilk"""
    def __init__(self, x, y, s):
        super().__init__(SILA, INICJATYWA, x, y)
        self.swiat = s
        self.kolor = KOLOR
