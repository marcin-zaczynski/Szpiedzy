słownik = {1: 'Poniedziałek', 2: 'Wtorek', 7: 'Niedziela'}#słownik składa się z par wartości klucz, wartość

print(słownik[1])
print(słownik[7])
słownik[3] = 'Środa'
słownik[4] = False
słownik[5] = 5
print(słownik)
słownik['a'] = 1
print(słownik['a'])
print(słownik)

#print(słownik[8])
print(słownik.get(8, 'Inny dzień')) #opcjonalny parametr jeśli nie znajdzie indeksu
print('\nPętla')

for l in słownik: #literuje po kluczach
    print(l)

for l in słownik.values(): #literuje po wartościach
    print(l)

print('\n....')
print(słownik.pop(1)) #usówa indeksy
print(słownik)