def decorator(func):
    def opakowanie():
        print('--------')
        func()
        print('--------')

    return opakowanie

def hello():
    print('Hello World!')
hello2 = decorator(hello)

hello2()
print()

@decorator
def witaj():
    print('Witaj Świecie')

witaj()

hello()
print()
print()


def dekorator(funkcja):
    print('...........')
    funkcja()
    print('...........')
    return dekorator

def tekst():
    print('Siemano Ludziska!!')

dekorator(tekst)
print()

tekst()
