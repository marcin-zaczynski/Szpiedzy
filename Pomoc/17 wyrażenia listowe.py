lista = list(range(10))


print(lista)

nowa = [i * 2 for i in lista]
nowa2 = [i + 2 for i in lista if i % 2 == 0]
print('Nowa: ', nowa)
print('Nowa2: ', nowa2)

# Formatowanie ciągów string

argumenty = ['Sebastian', 24]
tekst = 'Cześć mam na imię {imie} i mam {wiek} lat. {imie}'.format(imie = argumenty[0],wiek = argumenty[1])
print(tekst)
