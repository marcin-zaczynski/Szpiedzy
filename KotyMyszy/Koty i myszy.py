import random
import matplotlib
import matplotlib.pyplot as plt


pozycjak1 = [6, 6]
pozycjak2 = [90, 100]
pozycjaMyszy1 = [5, 5]
pozycjaMyszy2 = [50, 50]

class zwierze:
    def __init__(self, imie):
        self.imie = imie
        print(imie)

    def ruchKota(self, ruch):
        self.ruch = ruch

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

    def ruchMyszy(self, ruchM):
        self.ruchM = ruchM

        self.ruchM[0] += random.randint(-1, 1)
        self.ruchM[1] += random.randint(-1, 1)


        if self.ruchM[0] <= 0 :
            self.ruchM[0] += 1
        if self.ruchM[1] <=0:
            self.ruchM[1] += 1
        if self.ruchM[0] >= 100:
            self.ruchM[0] -= 1
        if self.ruchM[1] >= 100:
            self.ruchM[1] -= 1

def dodanie_do_wspolrzednych(ktory):
    if ktory == kot1:
        lxk1.append(pozycjak1[0])
        lyk1.append(pozycjak1[1])
    elif ktory == kot2:
        lxk2.append(pozycjak2[0])
        lyk2.append(pozycjak2[1])
    elif ktory == mysz1:
        lxm1.append(pozycjaMyszy1[0])
        lym1.append(pozycjaMyszy1[1])
    elif ktory == mysz2:
        lxm2.append(pozycjaMyszy2[0])
        lym2.append(pozycjaMyszy2[1])
    else:
        print('Błąd')

def wykres_krokow():
    plt.plot(lxk1, lyk1, ":.", color="blue", linewidth=1, alpha=1, label='kot')
    plt.plot(lxk2, lyk2, ":.", color="green", linewidth=1, alpha=1, label='mysz')
    plt.plot(lxm1, lym1, ":.", color="yellow", linewidth=1, alpha=1, label='mysz')
    plt.plot(lxm2, lym2, ":.", color="purple", linewidth=1, alpha=1, label='mysz')
    plt.xlabel("lx")
    plt.ylabel("ly")
    plt.title("Ruchy kotów i myszy")
    plt.grid(True)
    plt.show()


kot1 = zwierze('Przeciętniak1')
kot2 = zwierze('Przeciętniak2')
mysz1 = zwierze('Mysz1')
mysz2 = zwierze('Mysz2')

lxk1 = []
lyk1 = []
lxk2 = []
lyk2 = []
lxm1 = []
lym1 = []
lxm2 = []
lym2 = []
kot1_spotkanie = 0
o = 0
while o <= 500:
    o += 1
    kot1.ruchKota(pozycjak1)
    dodanie_do_wspolrzednych(kot1)
    kot2.ruchKota(pozycjak2)
    dodanie_do_wspolrzednych(kot2)
    mysz1.ruchMyszy(pozycjaMyszy1)
    dodanie_do_wspolrzednych(mysz1)
    mysz2.ruchMyszy(pozycjaMyszy2)
    dodanie_do_wspolrzednych(mysz2)
    if pozycjak1 == pozycjaMyszy1:
        print('spotkanie kota 1 z myszą 1')
        pozycjaMyszy1 = [5, 5]
    elif pozycjak1 == pozycjaMyszy2:
        pozycjaMyszy2 = [50, 50]
        print('spotkanie kota 1 z myszą 2')
    elif pozycjak2 == pozycjaMyszy1:
        pozycjaMyszy1 = [5, 5]
        print('spotkanie kota 2 z myszą 1')
    elif pozycjak2 == pozycjaMyszy2:
        pozycjaMyszy2 = [50, 50]
        print('spotkanie kota 2 z myszą 2')
wykres_krokow()


