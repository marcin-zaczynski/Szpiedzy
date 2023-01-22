import time

t1 = time.time()
class Zwierzeta:
    listaZwierzat = []
    def __init__(self, imie, wiek, gatunek ):
        self.imie = imie
        self.wiek = str(wiek)
        self.gatunek = gatunek


    def przedstaw(self):
        return 'Cześć mam na imię '+ self.imie + ' mam '+ self.wiek +' lat. ' + 'Jestem z garunku ' + self.gatunek + '.'

    def domoweZoo(self):
        return self.listaZwierzat.append(self)

class Psy(Zwierzeta):
    def glos(self):
        return self.imie + ' szczeka'

class Wąż(Zwierzeta):
    def glos(self):
        return self.imie + ' syczy'

class Chomik(Zwierzeta):
    def glos(self):
        return self.imie + ' pipipi'

pierwsze = Wąż('Snake', 18, 'wąż')
drugie = Psy('Cirii', 4, 'pies')
trzecie = Chomik('Herkules', 2, 'chomik')
pierwsze.domoweZoo()
drugie.domoweZoo()
trzecie.domoweZoo()
print(trzecie.glos())
print(drugie.glos())

for i in Zwierzeta.listaZwierzat:
    print(i.przedstaw())
t2 = time.time()

czas = t2-t1
print('Czas działania programu:', czas)

