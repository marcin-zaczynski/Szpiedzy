import random
import json

with open("slowa.json", "r", encoding="utf-8") as file:
    slowa = json.load(file)
slowo = random.choice(slowa)

rozwiazanie = ['_','_','_','_','_']
podane=['pierwsze']
ilosc_prob = 0
for a in range(11):
    wyswietlenie = ' '.join(rozwiazanie)
    if podane[0] == slowo:
        print('Gratulacje!!! Udało się za', ilosc_prob,'razem')
        break
    if ilosc_prob == 10:
        print('Przegrałeś, odpowiedź to słowo', slowo, 'spróbuj ponownie')
        break
    print("Podaj słowo (zostało ci ", 10-ilosc_prob,'prób)')
    print(wyswietlenie)
    letter = input()
    podane[0]= letter
    for litera in letter:
        if litera in slowo:
            rozwiazanie[slowo.index(litera)]= litera
            x = slowo.index(litera)
            next = slowo[x+1:]
            if litera in str(next):
                rozwiazanie[next.index(litera) +(x+1)] = litera
    ilosc_prob += 1