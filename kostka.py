import random

class Kostka:
    @staticmethod
    def k6():
        return random.randint(1, 6)

    @staticmethod
    def k6RO():
        kostka1 = Kostka.k6()
        suma_kostek = kostka1
        while kostka1 == 6:
            kostka1 = Kostka.k6()
            suma_kostek = suma_kostek + kostka1

        return suma_kostek

    @staticmethod
    def k6PRO():
        return Kostka.k6RO()-Kostka.k6RO()
