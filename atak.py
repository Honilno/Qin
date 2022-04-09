#PA - punkty akcji; WA - wartość ataku; WO - wartość obrony; RA - rezutlat ataku; U - uszkodzenia WB; - wielkość broni; WZ - wyparowanie zbroi

import random

from kostka import Kostka

gracz1PA = 9
gracz2PA = 9
gracz1WA = gracz1PA + 1
gracz2WO = gracz2PA + 3
gracz1WB = 2
gracz2WZ = 2

while (gracz1PA > 0) and (gracz2PA > 0):
    RA = gracz1WA - gracz2WO + Kostka.k6PRO()
    print("RA", RA)
    if RA >= 0:
        U = RA * gracz1WB - gracz2WZ
        print("U", U)
        if U < 1:
            gracz2PA = gracz2PA - 1
            print("rana lekka, PA -1")
        elif U < 2:
            gracz2PA = gracz2PA - 3
            print("rana średnia, PA -3")
        elif U < 4:
            gracz2PA = gracz2PA - 6
            print("rana ciężka, PA -6")
        else:
            gracz2PA = 0
            print("rana krytyczna, nie możesz dalej walczyć")
        print ("gracz2PA", gracz2PA)
