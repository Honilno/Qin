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
    RA_1 = gracz1WA - gracz2WO + Kostka.k6PRO()
    print ("atak 1 gracza")
    print("RA_1", RA_1)
    if RA_1 >= 0:
        U = RA_1 * gracz1WB - gracz2WZ
        print("U", U)
        gracz2PA = nowegraczpa(gracz2PA, U, 2)
        print("gracz2PA", gracz2PA)

    #atak 2 gracza
    if gracz2PA > 0:
        RA_2 = gracz2WA - gracz1WO + Kostka.k6PRO()
        print("atak 2 gracza")
        print("RA_2", RA_2)
        if RA_2 >= 0:
            U = RA_2 * gracz2WB - gracz1WZ
            print("U", U)
            gracz1PA = nowegraczpa(gracz1PA, U, 1)
            print("gracz1PA", gracz1PA)

