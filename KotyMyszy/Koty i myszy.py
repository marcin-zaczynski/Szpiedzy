import random
import matplotlib
import matplotlib.pyplot as plt

class zwierze():
    def __init__(self,imie, kolor):
        self.imie = imie
        print(imie)
        self.kolor = kolor

class Kot(zwierze):
    def __init__(self, imie, ruch, kolor):
        super().__init__(imie,kolor)
        self.ruch = ruch
        self.x = []
        self.y = []

    def rusz(self):
        self.ruch[0] += random.randint(-5, 5)
        self.ruch[1] += random.randint(-5, 5)

        if self.ruch[0] >= 100:
            self.ruch[0] -= 5
        if self.ruch[1] >= 100:
            self.ruch[1] -= 5

        if self.ruch[0] <= 0:
            self.ruch[0] += 5
        if self.ruch[1] <= 0:
            self.ruch[1] += 5

        self.x.append(self.ruch[0])
        self.y.append(self.ruch[1])

class Mysz(zwierze):
    def __init__(self, imie, ruch, kolor):
        super().__init__(imie,kolor)
        self.ruch = ruch
        self.x = []
        self.y = []
    def rusz(self):
        self.ruch[0] += random.randint(-1, 1)
        self.ruch[1] += random.randint(-1, 1)

        if self.ruch[0] <= 0 :
            self.ruch[0] += 1
        if self.ruch[1] <=0:
            self.ruch[1] += 1
        if self.ruch[0] >= 100:
            self.ruch[0] -= 1
        if self.ruch[1] >= 100:
            self.ruch[1] -= 1
        self.x.append(self.ruch[0])
        self.y.append(self.ruch[1])

    def wroc_na_poczatek(self):
        self.ruch = [5, 5]

def wykres_krokow():

    for i in tablicaKotow:
        plt.plot(i.x, i.y, ":.", color=i.kolor, linewidth=1, alpha=1, label='kot')
    for i in tablicaMyszy:
        plt.plot(i.x, i.y, ":.", color=i.kolor, linewidth=1, alpha=1, label='mysz')
    plt.xlabel("lx")
    plt.ylabel("ly")
    plt.title("Ruchy kotów i myszy")
    plt.grid(True)
    plt.show()

tablicaKotow = [Kot('Przeciętniak1', [6, 6],'blue'), Kot('Przeciętniak2', [90, 100],'green'), Kot('Tip Top', [1, 1],'yellow')]
tablicaMyszy = [Mysz('Mysz1', [5, 5], 'purple' ),Mysz('Mysz2', [50, 50], 'pink')]

o = 0
while o <= 1000:
    o += 1
    for i in tablicaKotow:
        i.rusz()
    for i in tablicaMyszy:
        i.rusz()

    for i in tablicaKotow:
        for a in tablicaMyszy:
            if i.ruch == a.ruch:
                print('spotkanie', i.imie, 'z', a.imie)
                a.wroc_na_poczatek()

wykres_krokow()