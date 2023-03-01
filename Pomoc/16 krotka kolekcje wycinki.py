krotka = (2, 4, 8, 16, 32, 64, 128, )
print(krotka)
print(krotka[6])
print(krotka[0])
#krotka[0]= 1  elementów krotki nie możemy zmieniać
print(krotka)

print('Elementow', krotka.count(2))
print('Index', krotka.index(64))


print('\nWycinki: ')
print(krotka[3:5])
print(krotka[0:7])
print(krotka[0:])
print(krotka[-4 :-2])
print(krotka[0:7:2])
print(krotka[:])
print(krotka[::-1])
print(krotka[::-2])


