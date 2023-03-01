zmienna = 1
zmienna2 = 'Abc'

lista = [1,2,'c','d','e']

print(lista)
print(lista[4])
lista[2] = 3
print(lista)
tekst = 'Hello World'
print(tekst[2])
print(lista + ['f','g'])
print(lista * 3)
print('Ilość elementów', len(lista))
lista.append('f') #dołanczanie na końcu
print(lista)
lista.append(['g','h'])
print(lista)
print(lista[6][0])
lista.insert(3, 3)#dołancza gdzie chcemy
print(lista)
print('Ilość:', lista.count('e')) #count liczenie
print('index:', lista.index('f')) #na którym miejscu dany index
lista.remove('f')     # remove usówanie
print(lista)

lista2 = [1,20,35,-5,0]
print('min:',min(lista2))  #minimalna liczba
print('max', max(lista2))   #maksymalna liczba
lista2.sort()              #sortuje
print(lista2)
lista2.reverse()      #odwrócenie
print(lista2)
lista2.clear()
print(lista2)