# PA - punkty akcji;
# WA - wartość ataku;
# WO - wartość obrony;
# RA - rezutlat ataku;
# U - uszkodzenia;
# WB - wielkość broni;
# WZ - wyparowanie zbroi
# OT - obrona tarczy
#math.ceil to zaokrąglanie w górę
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
        print("rana krytyczna, gracz", gracz_id,   "nie może dalej walczyć")
    return nowegracz_pa



def funkcja_ataku(atakujacyWA, obroncaWO, atakujacy_id, atakujacyWB, obroncaWZ, obroncaPA, obronca_id):
    RA = atakujacyWA - obroncaWO + Kostka.k6PRO()
    print ("atak", atakujacy_id, "gracza")
    print("RA", RA)
    if RA >= 0:
        U = RA * atakujacyWB - obroncaWZ
        print("U", U)
        obroncaPA = nowegraczpa(obroncaPA, U, obronca_id)
    return obroncaPA

gracz1PA = 10
gracz2PA = 10

gracz1WB = 2
gracz2WB = 2
gracz1WZ = 2
gracz2WZ = 2
gracz1OT = 2
gracz2OT = 3
U = 0


while (gracz1PA > 0) and (gracz2PA > 0):
    gracz1WA = math.ceil(gracz1PA / 2)
    gracz2WA = math.ceil(gracz2PA / 2)
    gracz2WO = gracz2PA - gracz2WA + gracz2OT
    gracz1WO = gracz1PA - gracz1WA + gracz1OT
    print ("gracz1WA", gracz1WA,
           "gracz2WA", gracz2WA,
           "gracz1WO", gracz1WO,
           "gracz2WO", gracz2WO,)


    #atak 1 gracza
    gracz2PA = funkcja_ataku(gracz1WA, gracz2WO, 1, gracz1WB, gracz2WZ, gracz2PA, 2)
    print("gracz2PA", gracz2PA)

    #atak 2 gracza
    gracz1PA = funkcja_ataku(gracz2WA, gracz1WO, 2, gracz2WB, gracz1WZ, gracz1PA, 1)
    print("gracz1PA", gracz1PA)



