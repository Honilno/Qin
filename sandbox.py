import random

from kostka import Kostka

kostka1 = Kostka.k6()
print (kostka1)
suma_kostek = kostka1
while kostka1 == 6:
    kostka1 = Kostka.k6()
    print(kostka1)
    suma_kostek = suma_kostek + kostka1
print (suma_kostek)

print ("rzut otwarty")
rzut = Kostka.k6RO()
print (rzut)








