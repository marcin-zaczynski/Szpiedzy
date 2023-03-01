print(', '.join(['a', 'b', 'c' ])) # Połącz
print('Witaj Świecie'.replace('Witaj', 'Cześć'))  #zastąp
print('To jest zdanie'.startswith('To')) #rozpoczyna się od zwraca True of False
print('To jest zdanie'.endswith('.')) # kończy się zwraca True or False
print('j' in 'To jest zdanie') #czy j znajduje się w zdaniu( liście)
print('To jest zdanie'.upper()) #duże litery
print('To jest zdanie'.lower()) # małe litery

print('-----------')
lista = [10, 20, 25, 30, 35, 40 ]
if all([i % 2 == 0 for i in lista]): # wszystkie parzyste
    print('Wszystkie parzyste')

if any([i % 2 ==0 for i in lista]):
    print('Chociaż jedena parzysta')
else:
    print('Wszystkie nieparzyste')

for i in enumerate(lista): #tworzy numeracje do listy
    print(i)

for i in enumerate(lista):
    print(i[0] + 1, '-', i[1])


