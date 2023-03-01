class Test:
    def __del__(self):
        print('Bye Class')

obj = Test()
obj2 = obj
lista = [obj2]
del obj
del obj2
del lista

print('Koniec')