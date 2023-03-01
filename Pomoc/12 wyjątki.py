x = 12
y = 3

try:
    lista = [3]
    print(lista[0])
    print(x + '!')
    print(x / y)
    print('Linijka po operacji')
except (ZeroDivisionError, TypeError,):
    print('Dzielenie przez zero, lub błąd typów danych')
except:
    print('Każdy inny wyjątek (błąd)')
finally:
    print('FINALLY: Wykonam się i tak')

print('Dalsze instrukcje...')
