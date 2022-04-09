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
        print("rana lekka, gracz", gracz_id, "PA -1")
    elif U < 2:
        nowegracz_pa = nowegracz_pa - 3
        print("rana średnia, gracz", gracz_id, "PA -3")
    elif U < 4:
        nowegracz_pa = nowegracz_pa - 6
        print("rana ciężka, gracz", gracz_id, "PA -6")
    else:
        nowegracz_pa = 0
        print("rana krytyczna, gracz", gracz_id, "nie może dalej walczyć")
    return nowegracz_pa


def funkcja_ataku(atakujacyWA, obroncaWO, atakujacy_id, atakujacyWB, obroncaWZ, obroncaPA, obronca_id):
    RA = atakujacyWA - obroncaWO + Kostka.k6PRO()
    print("atak", atakujacy_id, "gracza")
    print("RA", RA)
    if RA >= 0:
        U = RA * atakujacyWB - obroncaWZ
        print("U", U)
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
    print("tura", tura_id,)
    print("gracz1WA", turagracz1WA,
          "gracz2WA", turagracz2WA,
          "gracz1WO", turagracz1WO,
          "gracz2WO", turagracz2WO, )

    # atak 1 gracza
    turagracz2PA = funkcja_ataku(turagracz1WA, turagracz2WO, 1, turagracz1WB, turagracz2WZ, turagracz2PA, 2)
    print("gracz2PA", turagracz2PA)

    # atak 2 gracza
    turagracz1PA = funkcja_ataku(turagracz2WA, turagracz1WO, 2, turagracz2WB, turagracz1WZ, turagracz1PA, 1)
    print("gracz1PA", turagracz1PA)


    return (turagracz1PA, turagracz2PA)


gracz1PA = 10
gracz2PA = 10

gracz1WB = 2
gracz2WB = 2
gracz1WZ = 2
gracz2WZ = 2
gracz1OT = 2
gracz2OT = 3
U = 0
AG1 = 0.8
AG2 = 0.3

tura_id = 1
while (gracz1PA > 0) and (gracz2PA > 0):
    result = tura(gracz1PA, gracz2PA, gracz2OT, gracz1OT, gracz1WB, gracz2WZ, gracz2WB, gracz1WZ, tura_id, AG1, AG2)
    tura_id += 1
    gracz1PA = result[0]
    gracz2PA = result[1]
