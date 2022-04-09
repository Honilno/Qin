# PA - punkty akcji;
# WA - wartość ataku;
# WO - wartość obrony;
# RA - rezutlat ataku;
# U - uszkodzenia;
# WB - wielkość broni;
# WZ - wyparowanie zbroi
# OT - obrona tarczy
# AG- agresywność
# math.ceil to zaokrąglanie w górę
import random
import math

from kostka import Kostka


def nowegraczpa(graczpa, U, gracz_id):
    nowegracz_pa = graczpa
    if U < 1:
        nowegracz_pa = nowegracz_pa - 1

    elif U < 2:
        nowegracz_pa = nowegracz_pa - 3

    elif U < 4:
        nowegracz_pa = nowegracz_pa - 6

    else:
        nowegracz_pa = 0

    return nowegracz_pa


def funkcja_ataku(atakujacyWA, obroncaWO, atakujacy_id, atakujacyWB, obroncaWZ, obroncaPA, obronca_id):
    RA = atakujacyWA - obroncaWO + Kostka.k6PRO()

    if RA >= 0:
        U = RA * atakujacyWB - obroncaWZ

        obroncaPA = nowegraczpa(obroncaPA, U, obronca_id)
    return obroncaPA


def tura(turagracz1PA,
         turagracz2PA,
         turagracz2OT,
         turagracz1OT,
         turagracz1WB,
         turagracz2WZ,
         turagracz2WB,
         turagracz1WZ,
         tura_id,
         turaAG1,
         turaAG2):
    turagracz1WA = math.ceil(turagracz1PA * turaAG1)
    turagracz2WA = math.ceil(turagracz2PA * turaAG2)
    turagracz2WO = turagracz2PA - turagracz2WA + turagracz2OT
    turagracz1WO = turagracz1PA - turagracz1WA + turagracz1OT


    # atak 1 gracza
    turagracz2PA = funkcja_ataku(turagracz1WA, turagracz2WO, 1, turagracz1WB, turagracz2WZ, turagracz2PA, 2)

    # atak 2 gracza
    turagracz1PA = funkcja_ataku(turagracz2WA, turagracz1WO, 2, turagracz2WB, turagracz1WZ, turagracz1PA, 1)
    return turagracz1PA, turagracz2PA


def walka (walkagracz1PA,
         walkagracz2PA,
         walkagracz2OT,
         walkagracz1OT,
         walkagracz1WB,
         walkagracz2WZ,
         walkagracz2WB,
         walkagracz1WZ,
         walkaAG1,
         walkaAG2):

    tura_id = 1
    while (walkagracz1PA > 0) and (walkagracz2PA > 0):
        result = tura(walkagracz1PA, walkagracz2PA, walkagracz2OT, walkagracz1OT, walkagracz1WB, walkagracz2WZ,
                      walkagracz2WB, walkagracz1WZ, tura_id, walkaAG1, walkaAG2)
        tura_id += 1
        walkagracz1PA = result[0]
        walkagracz2PA = result[1]
    return walkagracz1PA, walkagracz2PA, tura_id


gracz1PA = 10
gracz2PA = 10

gracz1WB = 2
gracz2WB = 2
gracz1WZ = 2
gracz2WZ = 2
gracz1OT = 2
gracz2OT = 3
# U = 0 nie jest tu potrzebne
AG1 = 0.8
AG2 = 0.3

wynik_walki = walka(gracz1PA, gracz2PA, gracz2OT, gracz1OT, gracz1WB, gracz2WZ, gracz2WB, gracz1WZ, AG1, AG2)
print ("wynik walki", wynik_walki)

