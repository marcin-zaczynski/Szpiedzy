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

    for kot in tablicaKotow:
        plt.plot(kot.x, kot.y, ":.", color=kot.kolor, linewidth=1, alpha=1, label='kot')
    for mysz in tablicaMyszy:
        plt.plot(mysz.x, mysz.y, ":.", color=mysz.kolor, linewidth=1, alpha=1, label='mysz')
    plt.xlabel("lx")
    plt.ylabel("ly")
    plt.title("Ruchy kotów i myszy")
    plt.grid(True)
    plt.show()

tablicaKotow = [Kot('Przeciętniak1', [6, 6],'blue'), Kot('Przeciętniak2', [90, 100],'green'), Kot('Tip Top', [1, 1],'yellow')]
tablicaMyszy = [Mysz('Mysz1', [5, 5], 'purple' ),Mysz('Mysz2', [50, 50], 'pink'), Mysz('Jery',[90, 90], 'orange')]

o = 0
while o <= 1000:
    o += 1
    for kot in tablicaKotow:
        kot.rusz()
    for mysz in tablicaMyszy:
        mysz.rusz()

    for kot in tablicaKotow:
        for mysz in tablicaMyszy:
            if kot.ruch == mysz.ruch:
                print('spotkanie', kot.imie, 'z', mysz.imie)
                mysz.wroc_na_poczatek()

wykres_krokow()