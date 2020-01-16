"""Guarana"""
from roslina import Roslina
from zwierze import Zwierze

KOLOR = (244, 92, 66)

class Guarana(Roslina):
    """Klasa - Guarana"""
    def __init__(self, x, y, s):
        super().__init__(0, 0, x, y)
        self.kolor = KOLOR
        self.swiat = s

    def kolizja(self, napotkany):
        if isinstance(napotkany, Zwierze):
            napotkany.set_sila(napotkany.get_sila() + 3)
            self.zabij()

    def odbil_atak(self, atakujacy):
        if isinstance(atakujacy, Zwierze):
            atakujacy.set_sila(atakujacy.get_sila() + 3)
        return False
