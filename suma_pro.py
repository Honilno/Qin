import random

from kostka import Kostka

kostka1 = Kostka.k6()
print("kostka1", kostka1)
suma_kostek1 = kostka1
while kostka1 == 6:
    kostka1 = Kostka.k6()
    print("kostka1",kostka1)
    suma_kostek1 = suma_kostek1 + kostka1
print ("suma_kostek1", suma_kostek1)

kostka2 = Kostka.k6()
print("kostka2", kostka2)
suma_kostek2 = kostka2
while kostka2 == 6:
    kostka2 = Kostka.k6()
    print("kostka2",kostka2)
    suma_kostek2 = suma_kostek2 + kostka2
print ("suma_kostek2", suma_kostek2)

suma_pro = suma_kostek1 - suma_kostek2
print ("suma_pro", suma_pro)

# alternatywnie do napisanego u gory kodu
suma_pro2 = Kostka.k6RO()-Kostka.k6RO()
print ("suma_pro2", suma_pro2)

# jeszcze inaczej
suma_pro2 = Kostka.k6PRO()
print (suma_pro2)