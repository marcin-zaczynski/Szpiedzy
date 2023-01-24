import random
class Kot:
    def __init__(self, imie, ulubionaZabawka, nielubianaZabawka):
        self.imie = imie
        self.ulubionaZabawka = ulubionaZabawka
        self.nielubianaZabawka = nielubianaZabawka


    def przywitajsie(self):
        print('Cześć, jestem', self.imie)

    def ulubionazabawka(self):
        print('Moją ulubioną zabawką jest', self.ulubionaZabawka)

    def napotkanazabawka(self,zabawki):
        while True:
            zabawka = zabawki[random.randint(0,len(zabawki)-1)]
            a = random.randint(0,11)
            if zabawka != self.ulubionaZabawka and zabawka != self.nielubianaZabawka:
                if a > 7:
                    print(self.imie, 'lubi zabawke', zabawka)
                    break
                else:
                    print('Nie polubiłem zabawki', zabawka)
                    break

    def nielubzabawki(self):
        print('Nie lubie zabawki', self.nielubianaZabawka)

zabawki = ['mysz','kość', 'piórko', 'kłębek', 'kartonik', 'drapak', 'laser']
def wybor(zabawki):
    zabawka = zabawki[random.randint(0, len(zabawki))]
    return zabawka

kot1 = Kot('TipTop', zabawki[0], zabawki[1])
kot2 = Kot('Mruczek',zabawki[2], zabawki[3])
kot1.przywitajsie()
kot1.napotkanazabawka(zabawki)
kot1.ulubionazabawka()
kot1.nielubzabawki()
kot2.przywitajsie()
kot2.napotkanazabawka(zabawki)
kot2.ulubionazabawka()
kot2.nielubzabawki()
