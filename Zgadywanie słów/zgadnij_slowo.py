import random
import json

with open("slowa.json", "r", encoding="utf-8") as file:
    slowa = json.load(file)

slowo = random.choice(slowa)
#print(slowo)

rozwiazanie = ['_','_','_','_','_']
ilosc = 0
for a in range(10):
    y = ''.join(rozwiazanie)
    wyswietlenie = ' '.join(rozwiazanie)
    if str(y) == slowo:
        print('Gratulacje!!! Udało się za', ilosc,'razem')
        break
    print("Podaj słowo (zostało ci ", 10-ilosc,'prób)')
    print(wyswietlenie)
    letter = input()
    for litera in letter:
        if litera in slowo:
            rozwiazanie[slowo.index(litera)]= litera
            x = slowo.index(litera)
            next = slowo[x+1:]
            if litera in str(next):
                rozwiazanie[next.index(litera) +(x+1)] = litera
    ilosc += 1