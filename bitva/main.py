#!/usr/bin/env python3

from kostka import Kostka 
from lod import Lod 

class Sektor:
    """
    Správa souboje dvou lodí
    """

    def __init__(self, lod_1, lod_2, kostka):
        self._lod_1 = lod_1
        self._lod_2 = lod_2
        self._kostka = kostka

    def souboj(self):
        print("Vitej v randomackem sektoru!")
        print("======================")
        print()
        print(f"Dnes se utkaji lode {self._lod_1} a {self._lod_2}.")
        print("Zahajit souboj...")
        input()

        self._lod_1.utoc(self._lod_2)
        self._vypis_zpravu(self._lod_1.vypis_zpravu())
        self._vypis_zpravu(self._lod_2.vypis_zpravu())
        self._lod_2.utoc(self._lod_1)
        self._vypis_zpravu(self._lod_2.vypis_zpravu())
        self._vypis_zpravu(self._lod_1.vypis_zpravu())


    def _vypis_zpravu(self, zprava):
        print(zprava)

if __name__ == '__main__':
    k = Kostka(10)
    lodicka = Lod("Randomacka lod", 100, 80, 50, k)
    clun = Lod("C(l)unik", 40, 20, 30, k)
    orion = Sektor(lodicka, clun, k)

    orion.souboj()
