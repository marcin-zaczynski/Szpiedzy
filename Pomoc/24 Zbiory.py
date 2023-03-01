liczby1 = {0, 1, 2, 4}

slowa = set(['a', 'b', 'c'])   #zbiór wartości unikalne

print(liczby1)
print(slowa)

liczby1.add(5)
print(liczby1)

liczby1.add(5)
print(liczby1)

liczby1.remove(0)
print(liczby1)

print(1 in liczby1)
print('a' in liczby1)


liczby1 = {0, 1, 2, 4}
liczby2 = {3, 4, 5, 6}
print(liczby1 | liczby2)   # | suma zbiorów
print(liczby1 & liczby2)   # & wartość powtarzające się
print(liczby1 - liczby2)   # - różnica pierwszy od drugiego
print(liczby1 ^ liczby2)   # ^ pozostałe które się nie powtarzają
