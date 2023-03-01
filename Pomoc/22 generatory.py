def gen():
    i = 0
    while i < 5:
        yield i              # yield zwraca wynik bez przerywania pętli
        i += 1

for i in gen():
    print(i)

print(list(gen()))

def parzyste(x):
    i = 0
    while i <= x:
        if i % 2 == 0:
            yield i
        i += 1

for i in parzyste(25):
    print(i)

print(list(parzyste(30)))