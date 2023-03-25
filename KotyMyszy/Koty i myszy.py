import random
import matplotlib
import matplotlib.pyplot as plt

class zwierze():
    def __init__(self,imie, kolor):
        self.imie = imie
        print(imie)
        self.kolor = kolor

class Kot(zwierze):
    def __init__(self, imie, poczatek, kolor):
        super().__init__(imie,kolor)
        self.poczatek = poczatek
        self.historia_kota = []
        self.punkt_kota = Punkt(poczatek[0],poczatek[1])
    def rusz(self):
        self.punkt_kota.x += random.randint(-5, 5)
        self.punkt_kota.y += random.randint(-5, 5)

        if self.punkt_kota.x >= 100:
            self.punkt_kota.x -= 5
        if self.punkt_kota.y >= 100:
            self.punkt_kota.y -= 5

        if self.punkt_kota.x <= 0:
            self.punkt_kota.x += 5
        if self.punkt_kota.y <= 0:
            self.punkt_kota.y += 5

        self.historia_kota.append(self.punkt_kota)



class Mysz(zwierze):
    def __init__(self, imie, poczatek, kolor):
        super().__init__(imie,kolor)
        self.poczatek = poczatek
        self.historia_myszy = []
        self.punkt_myszy = Punkt(self.poczatek[0],self.poczatek[1])

    def rusz(self):
        self.punkt_myszy.x += random.randint(-1, 1)
        self.punkt_myszy.y += random.randint(-1, 1)

        if self.punkt_myszy.x <= 0 :
            self.punkt_myszy.x += 1
        if self.punkt_myszy.y <=0:
            self.punkt_myszy.y += 1
        if self.punkt_myszy.x >= 100:
            self.punkt_myszy.x -= 1
        if self.punkt_myszy.y >= 100:
            self.punkt_myszy.y -= 1

        self.historia_myszy.append(self.punkt_myszy)

    def wroc_na_poczatek(self):
        self.ruch = [5, 5]

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def wykres_krokow():
    for mysz in tablicaMyszy:
        punkt_x = []
        punkt_y = []
        for polozenie in mysz.historia_myszy:
            punkt_x.append(polozenie.x)
            punkt_y.append((polozenie.y))
        plt.plot(punkt_x,punkt_y, ":.", color=mysz.kolor, linewidth=1, alpha=1, label='mysz')
    for kot in tablicaKotow:
        punkt_x = []
        punkt_y = []
        for polozenie in kot.historia_kota:
            punkt_x.append(polozenie.x)
            punkt_y.append((polozenie.y))

        plt.plot(punkt_x, punkt_y, ":.", color=kot.kolor, linewidth=1, alpha=1, label='kot')
    plt.xlabel("lx")
    plt.ylabel("ly")
    plt.title("Ruchy kotów i myszy")
    plt.grid(True)
    plt.show()
Punkt.kot = (6,6)
tablicaKotow = [Kot('Przeciętniak1',(6,6),'blue'), Kot('Przeciętniak2',(90, 1000),'green'), Kot('Tip Top',(1, 1),'yellow')]
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
            if kot.historia_kota == mysz.historia_myszy:
                print('spotkanie', kot.imie, 'z', mysz.imie)
                mysz.wroc_na_poczatek()

wykres_krokow()