lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
lista2 = ['Marcin', 'Ela', 'Mateusz', 'Klaudia', 'Antek', 'Krzysztof', 'Paweł']
pusta = []
indexy = []

def dodawani_indexu(lista):
    if type(lista[0]) == str:
        a = 0
        for i in lista:
            if len(i) > 1:
                indexy.append(int((len(i)/2)) * ' '+str(a)+int(len(i)/2) *' ')
                a += 1
    else:
        a = 0
        for _ in lista:
            indexy.append(a)
            a += 1

def zmiana_miejsc(lista):
    lista2 = []
    print('lista:', lista)
    print('index:', indexy)
    index_listy1 = int(input('Proszę o podanie indexu listy który ma być zmieniony:'))
    index_listy2 = int(input('Proszę podać nr indexu listy na który ma być zamieniony:'))
    if len(lista) == 0:
        print('Lista jest pusta')

    for i in lista:
        lista2.append(i)
    try:
        lista2[index_listy1] = lista[index_listy2]
        lista2[index_listy2] = lista[index_listy1]
    except IndexError:
        print('Zły index listy')

    return lista2

def wybor_listy():
    print('Lista 1:', lista)
    print('Lista 2:', lista2)
    print('Proszę o wybór listy do modyfikowania')
    a = input()
    if a == '1':
        return lista
    elif a == '2':
        return lista2
    else:
        print('Zły wybór')




wybrana_lista = wybor_listy()

dodawani_indexu(wybrana_lista)
zmieniona_lista = zmiana_miejsc(wybrana_lista)

print('Nowa lista:', zmieniona_lista)

input()
