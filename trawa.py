"""Trawa"""
from roslina import Roslina

KOLOR = (104, 244, 66)

class Trawa(Roslina):
    """Klasa - Trawa"""
    def __init__(self, x, y, s):
        super().__init__(0, 0, x, y)
        self.kolor = KOLOR
        self.swiat = s
