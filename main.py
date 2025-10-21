#!/usr/bin/env python3

from kostka import Kostka
from lod import Lod 


if __name__ == '__main__':
    k = Kostka(10)
    lodicka = Lod("Randomacka lod", 100, 80, 50, k)
    clun = Lod("C(l)unik", 40, 20, 30, k)

    lodicka.utoc(clun)
    print(clun.vypis_zpravu())
