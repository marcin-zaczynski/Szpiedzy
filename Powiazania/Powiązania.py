import sys
import json

try:
    with open('osoby.json','r') as file:
        osoby = json.load(file)

except FileNotFoundError:
    osoby = {}
    with open('osoby.json', 'w') as file:
        json.dump(osoby, file)

try:
    with open('kontakty.json','r') as file:
        kontakty = json.load(file)

except FileNotFoundError:
    kontakty = {}
    with open('kontakty.json','w') as file:
        json.dump(kontakty, file)


def dodajOsobe(imie, nazwisko):
    a = len(osoby)+1
    osoby[a] = imie, nazwisko
    with open('osoby.json', 'w') as file:
        json.dump(osoby, file)


def powiazania(nr1, nr2):
    a = int(nr1)
    b = int(nr2)
    print()
    try:
        kontakty[a] = kontakty[a],b
    except KeyError:
        kontakty[a] = b

    try:
        kontakty[b] = kontakty[b], a
    except KeyError:
        kontakty[b] = a

    with open('kontakty.json','w') as file:
        json.dump(kontakty, file)


def powiazaneKontakty(kontakt):
    try:
        c = kontakty[kontakt]
        print('Powiązania dla kontaktu:', osoby[kontakt])
        try:
            for i in c:
                i = str(i)
                if osoby[i] == 'osoba usunięta':
                    print()
                else:
                    print(osoby[i])
        except TypeError:
            b = str(c)
            if osoby[b] == 'osoba usunięta':
                print()
            else:
                print(osoby[b])
    except KeyError:
        print('Brak powiązań, lub źle wpisany numer')


def usunOsobe(nrOsoby):
    osoby[nrOsoby] = 'osoba usunięta'
    with open('osoby.json', 'w') as file:
        json.dump(osoby, file)
    kontakty.pop(nrOsoby)
    with open('kontakty.json','w') as file:
        json.dump(kontakty, file)


def logowanie():
    while True:
        __login = 'login'
        __haslo = 'haslo'
        podlogin = input('Podaj login:')
        podhaslo = input('Podaj hasło:')
        if podlogin == __login and podhaslo == __haslo:
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
            4 - wyświetl powiązane osoby z kontaktem
            5 - usuń osobę
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
            a = input('Podaj nr osoby do wyświetlenia kontaktów')
            powiazaneKontakty(a)

        elif x == '5':
            a = input('Podaj nr osoby do usunięcia')
            usunOsobe(a)

        elif x == '9':
            sys.exit()

        else:
            print('Błędna cyfra')
            continue


#logowanie()
wykonuj()
