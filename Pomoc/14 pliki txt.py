plik = open('G:\\Mój dysk\\Programowanie\\Pliki\\test.txt', 'a')
if plik.writable:#czy jest otwarty do zapisu
    ile = plik.write(input('Wprowadź tekst:') + '\n') #liczy znaki
    print('Zapisano ' + str(ile) + ' znaków')
# 'w' otwiera zawsze czysty plik
# 'a' otwiera z zawartością i dodaje na koniec pliku
# 'r' otwiera plik tylko do odczytu

plik.close()
plik = open('G:\\Mój dysk\\Programowanie\\Pliki\\test.txt','r')
if plik.readable():
    print('Zawartość pliku')
    # tekst = plik.read() # wyświetla cały tekst
    # tekst = plik.readlines() #tworzy listę z każdej linijki
    # print(tekst)
    # for l in tekst:
        #print(l)     wyświetla listę każdą w nowej linijce
    for l in plik:
        print(l)

