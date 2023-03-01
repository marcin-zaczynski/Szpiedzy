a = 'Parzyste' if 10 % 2 == 0 else 'Nieparzyste'
print(a)

for i in range(10):
    if i > 5 :
        continue
else:
    print('Koniec5555')

try:
    a = 5/0
except ZeroDivisionError:
    print('Błąd')
else:
    print('Koniec')
finally:
    print('Zawsze')