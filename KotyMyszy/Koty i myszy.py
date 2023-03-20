import random
import matplotlib
import matplotlib.pyplot as plt

class zwierze:
    def __init__(self,imie):
        self.imie = imie
        print(imie)
class Kot(zwierze):
    def __init__(self, imie, ruch):
        super().__init__(imie)
        self.ruch = ruch



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


class Mysz(zwierze):
    def __init__(self, imie, ruch):
        super().__init__(imie)
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

def dodanie_do_wspolrzednych(ktory):
    if ktory == kot1:
        lxk1.append(kot1.ruch[0])
        lyk1.append(kot1.ruch[1])
    elif ktory == kot2:
        lxk2.append(kot2.ruch[0])
        lyk2.append(kot2.ruch[1])
    elif ktory == kot3:
        lxk3.append(kot3.ruch[0])
        lyk3.append(kot3.ruch[1])

    else:
        print('Błąd')

def wykres_krokow():
    plt.plot(lxk1, lyk1, ":.", color="blue", linewidth=1, alpha=1, label='kot')
    plt.plot(lxk2, lyk2, ":.", color="green", linewidth=1, alpha=1, label='kot')
    plt.plot(mysz1.x, mysz1.y, ":.", color="yellow", linewidth=1, alpha=1, label='mysz')
    plt.plot(mysz2.x, mysz2.y, ":.", color="purple", linewidth=1, alpha=1, label='mysz')
    plt.plot(lxk3,lyk3, ':.',color='pink',linewidth=1,alpha=1, label='kot')
    plt.xlabel("lx")
    plt.ylabel("ly")
    plt.title("Ruchy kotów i myszy")
    plt.grid(True)
    plt.show()


kot1 = Kot('Przeciętniak1', [6, 6])
kot2 = Kot('Przeciętniak2', [90, 100])
kot3 = Kot('Tip Top', [1, 1])
mysz1 = Mysz('Mysz1', [5, 5])
mysz2 = Mysz('Mysz2', [50, 50])
tablicaMyszy = [mysz1, mysz2]

lxk1 = []
lyk1 = []
lxk2 = []
lyk2 = []
lxk3 = []
lyk3 = []

o = 0
while o <= 1000:
    o += 1
    kot1.rusz()
    dodanie_do_wspolrzednych(kot1)
    kot2.rusz()
    dodanie_do_wspolrzednych(kot2)
    kot3.rusz()
    dodanie_do_wspolrzednych(kot3)

    for i in tablicaMyszy:
        i.rusz()

    for i in tablicaMyszy:
        if i.ruch == kot1.ruch:
            i.wroc_na_poczatek()
            print('spotkanie', kot1.imie, ' z ', i.imie)
        if i.ruch == kot2.ruch:
            i.wroc_na_poczatek()
            print('spotkanie', kot2.imie, ' z ', i.imie)
        if i.ruch == kot3.ruch:
            i.wroc_na_poczatek()
            print('spotkanie', kot3.imie, ' z ', i.imie)

wykres_krokow()