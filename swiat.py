import pygame
from random import randint, choice
from czlowiek import Czlowiek
from wilk import Wilk
from owca import Owca
from lis import Lis
from antylopa import Antylopa
from zolw import Zolw
from cyberowca import CyberOwca
from barszczsosnowskiego import BarszczSosnowskiego
from guarana import Guarana
from mlecz import Mlecz
from trawa import Trawa
from wilczejagody import WilczeJagody

# Kolory
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
blue = (0, 153, 255)
orange = (255, 153, 0)
gray = (183, 191, 187)
red = (255, 0, 0)

# Rozmiar kwadracika
pixel = 30

# Inicjalizacja okna
pygame.init()
pygame.display.set_caption("Patryk Pobłocki | 160273 | Programowanie obiektowe 2018 - Wirtualny swiat")
screen = pygame.display.set_mode((1280, 720))
screen.fill(white)
mouse = pygame.mouse.get_pos()


class Swiat:

    def __init__(self):
        self.wysokosc = 20
        self.szerokosc = 20
        self.max_liczba_organizmow = self.wysokosc * self.szerokosc
        self.numer_tury = 0
        self.organizmy = []
        self.czyCzlowiekGra = False
        self.lastKeyboardEvent = None
        self.nieWcisnietoStrzalki = False
        self.komunikatZapisu = 0
        self.komunikatOdczytu = 0
        self.brakPliku = 0

    def graj(self):
        # Obsluga zdarzen
        while True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # Zamykanie gry [X]
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)
                # Przyciski na dole okna (obsluga myszka)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 + 250 > mouse[0] > 50 and 650 + 50 > mouse[1] > 650:
                        if self.czyCzlowiekGra:
                            self.nieWcisnietoStrzalki = True
                        else:
                            self.wykonajTure()
                    if 350 + 250 > mouse[0] > 350 and 650 + 50 > mouse[1] > 650:
                        self.zapiszStanGry()

                    if 650 + 250 > mouse[0] > 650 and 650 + 50 > mouse[1] > 650:
                        self.wczytajStanGry()

                    if 800 + 250 > mouse[0] > 800 and 550 + 50 > mouse[1] > 550:
                        self.nowaGra()

                    if 950 + 250 > mouse[0] > 950 and 650 + 50 > mouse[1] > 650:
                        pygame.quit()
                        quit(0)
                # Klawisze strzalek + przyciski dolne
                if event.type == pygame.KEYDOWN:
                    # Klawisze strzalek
                    if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                        self.nieWcisnietoStrzalki = False
                        self.lastKeyboardEvent = event
                        self.wykonajTure()
                        self.lastKeyboardEvent = None
                    # Superzdolnosc czlowieka
                    if event.key == pygame.K_q:
                        if self.czyCzlowiekGra:
                            for organizm in self.organizmy:
                                if isinstance(organizm, Czlowiek):
                                    if organizm.get_cooldown() == 0:
                                        organizm.set_superzdolnosc(True)
                                        organizm.set_czas_trwania(0)
                                        organizm.set_cooldown(5)
                                        organizm.set_kolor(red)
                    # Nastepna tura
                    elif event.key == pygame.K_n:
                        if len(self.organizmy) < self.max_liczba_organizmow:
                            self.wykonajTure()
                    # Wyjscie [ESC]
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit(0)
                    # Zapisz gre [S]
                    elif event.key == pygame.K_s:
                        # self.zapiszStanGry()
                        self.nowaGra()
                    # Wczytaj gre [L]
                    elif event.key == pygame.K_l:
                        pass
            self.rysuj()

    def wykonajTure(self):

        if len(self.organizmy) < self.max_liczba_organizmow:
            if (self.czyCzlowiekGra and self.lastKeyboardEvent is not None) or not self.czyCzlowiekGra:
                # Sortowanie organizmow
                # TODO: sortowanie...

                organizmy_w_turze = len(self.organizmy)
                # Wykonanie tury dla zyjacych organizmow
                for i in range(0, organizmy_w_turze):
                    if self.organizmy[i].get_czy_zyje():
                        self.organizmy[i].akcja()

                # Usuwanie martwych organizmow
                pozostaleOrganizmy = []
                for organizm in self.organizmy:
                    if organizm.get_czy_zyje():
                        pozostaleOrganizmy.append(organizm)
                self.organizmy = pozostaleOrganizmy
                del pozostaleOrganizmy
                self.numer_tury += 1

    def zapiszStanGry(self):
        '''
        Format pliku: txt
        Zawartosc:

        <numer_tury>
        <nazwa_org> <x> <y> <sila> <wiek>
        <nazwa_org> <x> <y> <sila> <wiek>
        ...
        (opcjonalnie)
        superzdolnosc <status> <czas_trwania> <cooldown> <kolor>
        '''

        plik = open("wirtualny_swiat.txt", "w")
        plik.write(str(self.numer_tury) + "\n")

        indeks_czlowieka = -1
        for i, organizm in enumerate(self.organizmy):
            if isinstance(organizm, Czlowiek):
                indeks_czlowieka = i
            org = organizm.__class__.__name__ + " " \
                  + str(organizm.get_x()) + " " \
                  + str(organizm.get_y()) + " " \
                  + str(organizm.get_sila()) + " " \
                  + str(organizm.get_wiek()) + "\n"
            plik.write(org)

        if self.czyCzlowiekGra and indeks_czlowieka != -1:
            czlowiek = self.organizmy[indeks_czlowieka]
            ult = "superzdolnosc " \
                  + str(czlowiek.get_superzdolnosc()) + " " \
                  + str(czlowiek.get_czas_trwania()) + " " \
                  + str(czlowiek.get_cooldown())
            plik.write(ult)

        plik.close()
        self.komunikatZapisu = 500

    def wczytajStanGry(self):
        plik = open("wirtualny_swiat.txt", "r")
        if plik:
            for organizm in self.organizmy:
                del organizm
            del self.organizmy
            self.organizmy = []
            self.czyCzlowiekGra = False

            self.numer_tury = int(plik.readline())
            for linia in plik:
                dane = linia.split(' ')
                if dane[0] == 'superzdolnosc':
                    for organizm in self.organizmy:
                        if isinstance(organizm, Czlowiek):
                            self.czyCzlowiekGra = True
                            if dane[1] == 'True':
                                organizm.set_superzdolnosc(True)
                                organizm.set_kolor(red)
                            else:
                                organizm.set_superzdolnosc(False)
                                organizm.set_kolor(black)
                            organizm.set_czas_trwania(int(dane[2]))
                            organizm.set_cooldown(int(dane[3]))
                else:
                    nowy = dane[0] + "(%s, %s, self)" % (int(dane[1]), int(dane[2]))
                    exec("self.organizmy.append(%s)" % (nowy))
            self.komunikatOdczytu = 500
        else:
            self.brakPliku = 500

    def nowaGra(self):
        for organizm in self.organizmy:
            del organizm
        del self.organizmy
        self.__init__()
        pustePola = []
        for x in range(0, self.szerokosc):
            for y in range(0, self.wysokosc):
                pustePola.append((x, y))

        liczbaPustych = len(pustePola)
        zwierzeta = ['Wilk', 'Owca', 'Lis', 'Antylopa', 'Zolw', 'CyberOwca']
        rosliny = ['Trawa', 'Mlecz', 'Guarana', 'WilczeJagody', 'BarszczSosnowskiego']

        # Uzupelnianie swiata:
        # (1) Dodanie czlowieka
        czlowiek = choice([True, False])
        if czlowiek:
            pole = choice(pustePola)
            self.dodajOrganizm(Czlowiek(pole[0], pole[1], self))
            pustePola.remove(pole)
        # (2) Dodanie 2 x po 1 gatunku zwierzecia
        for i in range(0,2):
            for zwierze in zwierzeta:
                pole = choice(pustePola)
                z = zwierze + "(%s, %s, self)" % (pole[0], pole[1])
                exec("self.dodajOrganizm(%s)" % (z))
                pustePola.remove(pole)
        # (3) Dodanie po 1 gatunku rosliny
        for roslina in rosliny:
            pole = choice(pustePola)
            r = roslina + "(%s, %s, self)" % (pole[0], pole[1])
            exec("self.dodajOrganizm(%s)" % (r))
            pustePola.remove(pole)

    def rysuj(self):
        font = pygame.font.SysFont("Calibri", 30)
        # Czyszczenie ekranu
        screen.fill(white)
        # Rysowanie organizmow
        for organizm in self.organizmy:
            kolor = organizm.get_kolor()
            pygame.draw.rect(screen, kolor, pygame.Rect(
                50 + organizm.get_x() * pixel, 10 + organizm.get_y() * pixel, pixel, pixel))
            nazwa = organizm.__class__.__name__[0]
            screen.blit(font.render(nazwa, True, white), (50 + organizm.get_x() * pixel + 3, 10 + organizm.get_y() * pixel))


        pygame.draw.rect(screen, black, pygame.Rect(45, 5, 5, 610))
        pygame.draw.rect(screen, black, pygame.Rect(650, 5, 5, 610))

        pygame.draw.rect(screen, black, pygame.Rect(45, 5, 610, 5))
        pygame.draw.rect(screen, black, pygame.Rect(45, 610, 610, 5))
        # Rysowanie przyciskow
        pygame.draw.rect(screen, green, pygame.Rect(50, 650, 250, 50))  # Nastepna tura
        pygame.draw.rect(screen, gray, pygame.Rect(350, 650, 250, 50))  # Zapisz gre
        pygame.draw.rect(screen, orange, pygame.Rect(650, 650, 250, 50))  # Wczytaj gre
        pygame.draw.rect(screen, red, pygame.Rect(950, 650, 250, 50))  # Wyjście
        pygame.draw.rect(screen, blue, pygame.Rect(800, 550, 250, 50))  # Nowa gra

        # Etykiety przyciskow
        screen.blit(font.render("Następna tura [N]", True, black), (70, 660))
        screen.blit(font.render("Zapisz gre [S]", True, black), (400, 660))
        screen.blit(font.render("Wczytaj gre [L]", True, black), (690, 660))
        screen.blit(font.render("Zakończ [ESC]", True, black), (1000, 660))
        screen.blit(font.render("Nowa gra", True, black), (875, 560))
        # Rysowanie komunikatow
        screen.blit(font.render("Patryk Pobłocki | 160273", True, blue), (850, 10))

        screen.blit(font.render("Numer tury: %s" % (self.numer_tury), True, black), (850, 50))

        if len(self.organizmy) >= self.max_liczba_organizmow:
            screen.blit(font.render("Koniec gry", True, red), (850, 75))

        if self.czyCzlowiekGra and self.nieWcisnietoStrzalki:
            screen.blit(font.render("Wybierz kierunek człowieka", True, red), (850, 100))

        if self.komunikatZapisu > 0:
            screen.blit(font.render("Gra zapisana", True, green), (850, 150))
            self.komunikatZapisu -= 1

        if self.komunikatOdczytu > 0:
            screen.blit(font.render("Gra wczytana", True, orange), (850, 200))
            self.komunikatOdczytu -= 1

        if self.brakPliku > 0:
            screen.blit(font.render("Brak pliku: wirtualny_swiat.txt", True, red), (850, 250))
            self.brakPliku -= 1
        # print(mouse)

        # Renderowanie zmian
        pygame.display.flip()

    def czyWspolrzednePoprawne(self, wspolrzedne):
        poprawne = False

        if 0 <= wspolrzedne[0] < self.szerokosc:
            if 0 <= wspolrzedne[1] < self.wysokosc:
                poprawne = True
        return poprawne

    def dodajOrganizm(self, organizm):
        if isinstance(organizm, Czlowiek):
            self.czyCzlowiekGra = True
        self.organizmy.append(organizm)

    def dodajOrganizmWOtoczeniu(self, rodzic):
        danePoprawne = False
        proba = 0
        x = 0
        y = 0

        '''
        R -> rodzic
        [0][1][2]
        [3][R][4]
        [5][6][7]
        '''
        pola = []
        pola.append((rodzic.get_x() - 1, rodzic.get_y() - 1))
        pola.append((rodzic.get_x(), rodzic.get_y() - 1))
        pola.append((rodzic.get_x() + 1, rodzic.get_y() - 1))

        pola.append((rodzic.get_x() - 1, rodzic.get_y()))
        pola.append((rodzic.get_x() + 1, rodzic.get_y()))

        pola.append((rodzic.get_x() - 1, rodzic.get_y() + 1))
        pola.append((rodzic.get_x(), rodzic.get_y() + 1))
        pola.append((rodzic.get_x() + 1, rodzic.get_y() + 1))

        mozliwePola = []  # lista pustych pol dla nowego organizmu
        for pole in pola:
            if self.czyWspolrzednePoprawne(pole):
                if self.organizmNaXY(pole[0], pole[1]) is None:
                    mozliwePola.append(pole)

        if mozliwePola:
            pole = mozliwePola[randint(0, len(mozliwePola) - 1)]
            nowy = type(rodzic).__name__ + "(%s, %s, self)" % (pole[0], pole[1])
            exec("self.dodajOrganizm(%s)" % (nowy))


    def dodajGatunekRosliny(self, gatunek, x, y):
        if isinstance(gatunek, Trawa):
            self.organizmy.append(Trawa(x, y, self))
        elif isinstance(gatunek, Mlecz):
            self.organizmy.append(Mlecz(x, y, self))
        elif isinstance(gatunek, Guarana):
            self.organizmy.append(Guarana(x, y, self))
        elif isinstance(gatunek, WilczeJagody):
            self.organizmy.append(WilczeJagody(x, y, self))
        elif isinstance(gatunek, BarszczSosnowskiego):
            self.organizmy.append(BarszczSosnowskiego(x, y, self))

    def organizmNaXY(self, x, y):
        for organizm in self.organizmy:
            if (organizm.get_x(), organizm.get_y()) == (x, y):
                return organizm
        return None

    def getLastKeyboardEvent(self):
        return self.lastKeyboardEvent
