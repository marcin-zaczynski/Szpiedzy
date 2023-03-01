class Czlowiek :
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedtawSie(self, powitanie = 'Cześć'):
        return powitanie + ', mam na imię '+ self.imie + ' lat ' + str(self.wiek) +'.'

obiekt = Czlowiek('Sebastian', 24)
print(obiekt.imie)
print(obiekt.przedtawSie())
print(obiekt.przedtawSie('Witam'))

#print('Podaj swoje imię')
#x = input()
#print('Podaj swój wiek')
#y = input()
#obiekt2 = Czlowiek(x, y)
#print('Wpisz swoje powitanie')
#print((obiekt2.przedtawSie(input())))

print()
print()
#inny przykład
class osoba:

    def __init__(self, imie, wiek, plec):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def przywitaj(self):
        print('Cześć. Mam na imię', self.imie)

    def ruszaj(self):
        if self.plec == 'kobieta':
            print('Ruszyłam w drogę')
        else:
            print('Ruszyłem w drogę')

    def mysl(self):
            if self.wiek < 2:
                print('Dopiero się uczę')
            else:
                print('Nie ma problemu')

mike = osoba('Mike', 18, 'mężczyzna')

print('Obiekt -',mike.imie,mike.wiek, mike.plec,'\n')

mike.przywitaj()
mike.ruszaj()
mike.mysl()


# Ćwiczenie

class ksiazki:

    def __init__(self, tytul, iloscStron, autor, dataWydania, wlasciciel):
        self.tytul = tytul
        self.iloscStron = iloscStron
        self.autor = autor
        self.dataWydania = dataWydania
        self.wlasciciel = wlasciciel

    def informacje(self):
        return 'Książka ', self.tytul, 'ilość stron: ', self.iloscStron,'autor: ', self.autor,'Data wydania: ',self.dataWydania, 'Właścicielem: ',self.wlasciciel

    def zmianaWlasciciela(self):
        if self.wlasciciel != 'Marcin':
            return 'Książka', self.tytul, ' zmiana właściciela na:', self.wlasciciel

k1 = ksiazki('Wiedźmin','285', 'Andrzej Sapkowski', '1986', 'Adam')
k2 = ksiazki("Tańczący z wilkami", 500,  "Blake Michael", 1988, "Analityk")
k3 = ksiazki("Forrest Gump", 500,  "Winston Groom", 1986, "Analityk")

print(k1.informacje())
print(k2.informacje())
print(k3.informacje())
print(k1.zmianaWlasciciela())
listaKsiazek = list(k1.informacje())+ list(k2.informacje())+ list(k3.informacje())
print('lista' , listaKsiazek)

for i in listaKsiazek:
    print(i)



