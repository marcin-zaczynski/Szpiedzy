from random import randint

los = randint(1,10)
odp = -1
i = 0
print(' Zgadnij liczbę z przedziału od 1 do 10')

while odp != los:
    i += 1
    odp = int(input(' Podaj liczbę:  '))
    if odp > los:
        print('Podaj mniejszą liczbę')
        if odp >= 11:
            print('Liczba miała być od 1 do 10')
    elif odp < los:
        print('Podaj większą liczbę')
print('Brawo odgadłeś za',i,'razem')