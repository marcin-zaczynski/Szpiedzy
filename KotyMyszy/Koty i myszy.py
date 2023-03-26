import random
import matplotlib
import matplotlib.pyplot as plt
from tkinter import*

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
        self.punkt_x = []
        self.punkt_y = []
    def rusz(self):
        self.punkt_kota.x += random.randint(-5, 5)
        self.punkt_kota.y += random.randint(-5, 5)

        if self.punkt_kota.x >= 100:
            self.punkt_kota.x = 99
        if self.punkt_kota.y >= 100:
            self.punkt_kota.y = 99

        if self.punkt_kota.x <= 0:
            self.punkt_kota.x = 1
        if self.punkt_kota.y <= 0:
            self.punkt_kota.y = 1

        self.historia_kota.append(self.punkt_kota)
        self.punkt_x.append(self.punkt_kota.x)
        self.punkt_y.append(self.punkt_kota.y)


class Mysz(zwierze):
    def __init__(self, imie, poczatek, kolor):
        super().__init__(imie,kolor)
        self.poczatek = poczatek
        self.historia_myszy = []
        self.punkt_myszy = Punkt(self.poczatek[0],self.poczatek[1])
        self.punkt_x = []
        self.punkt_y = []

    def rusz(self):
        self.punkt_myszy.x += random.randint(-1, 1)
        self.punkt_myszy.y += random.randint(-1, 1)

        if self.punkt_myszy.x <= 0 :
            self.punkt_myszy.x = 1
        if self.punkt_myszy.y <=0:
            self.punkt_myszy.y = 1
        if self.punkt_myszy.x >= 100:
            self.punkt_myszy.x = 99
        if self.punkt_myszy.y >= 100:
            self.punkt_myszy.y = 99

        self.historia_myszy.append(self.punkt_myszy)
        self.punkt_x.append(self.punkt_myszy.x)
        self.punkt_y.append(self.punkt_myszy.y)

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
        #for punkt in mysz.historia_myszy:
        #    punkt_x.append(punkt.x)
        #    punkt_y.append(punkt.y)
        #plt.plot(punkt_x,punkt_y, ":.", color=mysz.kolor, linewidth=1, alpha=1, label='mysz')
        plt.plot(mysz.punkt_x, mysz.punkt_y, ":.", color=mysz.kolor, linewidth=1, alpha=1, label='mysz')
    for kot in tablicaKotow:
        #punkt_x = []
        #punkt_y = []
        #for polozenie in kot.historia_kota:
        #    punkt_x.append(polozenie.x)
        #    punkt_y.append(polozenie.y)
        #plt.plot(punkt_x, punkt_y, ":.", color=kot.kolor, linewidth=1, alpha=1, label='kot')
        plt.plot(kot.punkt_x, kot.punkt_y, ":.", color=kot.kolor, linewidth=1, alpha=1, label='kot')
    plt.xlabel("lx")
    plt.ylabel("ly")
    plt.title("Ruchy kotów i myszy")
    plt.grid(True)
    plt.show()
Punkt.kot = (6,6)
tablicaKotow = [Kot('Przeciętniak1',(6,6),'blue'), Kot('Przeciętniak2',(90, 1000),'green'), Kot('Tip Top',(1, 1),'yellow')]
tablicaMyszy = [Mysz('Mysz1', [5, 5], 'purple' ),Mysz('Mysz2', [50, 50], 'pink'), Mysz('Jery',[90, 90], 'orange')]

o = 0
def krok():

    for kot in tablicaKotow:
        kot.rusz()
    for mysz in tablicaMyszy:
        mysz.rusz()

    for kot in tablicaKotow:
        for mysz in tablicaMyszy:
            if kot.historia_kota == mysz.historia_myszy:
                print('spotkanie', kot.imie, 'z', mysz.imie)
                mysz.wroc_na_poczatek()
                print(mysz.imie)
    wykres_krokow()
class kroki:
    def __init__(self):
        self.okno_przycisku = Tk()
        self.okno_przycisku.geometry('140x100')
        self.okno_przycisku.title('Kroki')
        nazwa = Label(self.okno_przycisku, text='Zrób po jednym kroku')
        nazwa.grid(column=0,row=0)
        self.przycisk_krok = Button(self.okno_przycisku, text="Zrób krok ", command= krok)
        self.przycisk_krok.grid(row=1, column=0)
        self.okno_przycisku.mainloop()

jeden_krok =kroki()
