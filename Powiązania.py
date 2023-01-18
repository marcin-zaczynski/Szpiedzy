import sys
import json


with open('szpiedzy.json','r') as file:
    osoby = json.load(file)


with open('kontakty.json','r') as file:
    kontakty = json.load(file)

def dodajOsobe(imie, nazwisko):
    a = len(osoby)+1
    osoby[a] = imie, nazwisko
    with open('szpiedzy.json', 'w') as file:
        json.dump(osoby, file)

def powiazania(nr1, nr2):
    a = int(nr1)
    b = int(nr2)
    kontakty[a] = b
    with open('kontakty.json','w') as file:
        json.dump(kontakty, file)


def powiazaneKontakty(kontakt):
    for i in kontakty.keys():
        print(kontakty[kontakt])

        #print('nr', kontakt,'jest powiązany z', kontakty[kontakt])

def logowanie():
    while True:
        login = 'login'
        haslo = 'haslo'
        podlogin = input('Podaj login:')
        podhaslo = input('Podaj hasło:')
        if podlogin == login and podhaslo == haslo:
            print('Dostęp uznany')
            break

        else:
            print('Zły login lub hasło, spróbuj ponownie')


def wykonuj():
    while True:
        print("""
            1 - wyświetl sieć kontaktów
            2 - dodaj osobę
            3 - dodaj powiązanie pomiędzy kontaktami
            4 - wyświetl powiązania
            9 - zamknij \n
        """)
        x = input('Podaj nr:')
        if x == '1':
            a = 1
            for i in osoby.values():
                print(str(a)+':'+str(i))
                a+=1


        elif x == '2':
            a = input('Podaj imię: ')
            b = input('Podaj nazwisko: ')
            dodajOsobe(a, b)
            continue

        elif x == '3':
            a = input('nr pierwszej osoby')
            b = input('nr drugiej osoby')
            powiazania(a,b)
            continue

        elif x == '4':
            print(kontakty)
            continue


        elif x == '9':
            sys.exit()

        else:
            print('Błędna cyfra')
            continue


logowanie()
wykonuj()